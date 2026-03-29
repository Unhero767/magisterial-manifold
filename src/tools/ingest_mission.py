import sys
import os

# Ensure the core logic is reachable
sys.path.append(os.path.join(os.getcwd(), 'src/core'))
from mission_vault import MissionVault

protocol = {
  "mission_id": "MP_01_SILICON_EYE",
  "sector": "NEON_VEIL",
  "protagonist": "AURELIA_9",
  "objective": {
    "primary": "Infiltrate K_M_Synthetica Sub-Vault 04",
    "secondary": "Extract 'Primordial Algorithm' fragment residue",
    "threat_level": "BETA (High-Entropy)"
  },
  "constraints": {
    "min_consistency_a": 0.85,
    "max_instability_ex": 0.40
  },
  "success_probability": {"base": 0.72, "final_resonance": 0.77},
  "loot_table": [
    {"id": "LOGIC_FRAGMENT_01", "type": "MTP_DATA", "utility": "+0.05 ◦A restoration"},
    {"id": "ASH_SHARD", "type": "ENTROPY_FUEL", "utility": "Localized Ex◦ burst"}
  ],
  "failure_protocol": "QUARANTINE_SECTOR_04"
}

mv = MissionVault()
print(mv.anchor_mission(protocol))
