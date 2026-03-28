import math
from dataclasses import dataclass, field
from typing import Dict, Set, Any

@dataclass
class ManifoldSector:
    name: str
    consistency_a: float = 1.0
    instability_ex: float = 0.0
    tethers: Set[str] = field(default_factory=set)
    entities: Dict[str, float] = field(default_factory=dict)

class MetalogicalEngine:
    def __init__(self, burn_threshold: float = 0.60):
        self.sectors: Dict[str, ManifoldSector] = {"CORE": ManifoldSector("CORE")}
        self.burn_threshold = burn_threshold

    def manifest_entity(self, sector_name: str, entity_id: str, weight: float) -> Dict[str, Any]:
        if sector_name not in self.sectors:
            self.sectors[sector_name] = ManifoldSector(sector_name)
        
        sector = self.sectors[sector_name]
        effective_weight = weight / (1.0 + (len(sector.tethers) * 0.5))
        sector.consistency_a -= (effective_weight * 0.05)
        
        instability_spike = effective_weight * (0.1 / max(0.1, sector.consistency_a))
        sector.instability_ex = min(1.0, sector.instability_ex + instability_spike)
        
        sector.entities[entity_id] = weight

        if sector.consistency_a < self.burn_threshold:
            return self._trigger_burn(sector)

        return {
            "status": "STABILIZED",
            "telemetry": {"◦A": round(sector.consistency_a, 3), "Ex◦": round(sector.instability_ex, 3)},
            "entities_count": len(sector.entities)
        }

    def apply_jovian_anchor(self, sector_name: str, tether_id: str):
        if sector_name in self.sectors:
            s = self.sectors[sector_name]
            s.tethers.add(tether_id)
            s.consistency_a = min(1.0, s.consistency_a + 0.20)
            s.instability_ex = max(0.0, s.instability_ex - 0.25)
            return f"[ ◦A RESTORED ] Sector {sector_name} anchored by {tether_id}."

    def _trigger_burn(self, sector: ManifoldSector):
        sector.consistency_a = 0.0
        sector.instability_ex = 1.0
        return {"status": "METALOGICAL_BURN", "msg": f"Ex◦ Event in {sector.name}"}
