import re
import sys
import os

# Align path to find rule_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine

class MTPExtension:
    """
    The Meaning-Typed Programming (MTP) bridge for MLAOS.
    Automates the 'by llm()' logic for weight derivation.
    """
    def __init__(self, engine: MetalogicalEngine):
        self.engine = engine
        # Keywords that trigger high instability (Ex◦)
        self.entropy_triggers = [
            "paradox", "glitch", "shattered", "void", 
            "contradiction", "unmade", "forbidden", "ancient"
        ]

    def by_llm_weighting(self, description: str) -> float:
        """
        Simulates the MTP 'by llm()' operator.
        Extracts semantic mass from natural language.
        """
        # Base weight derived from length (Structural Complexity)
        base_weight = len(description.split()) * 0.1
        
        # Entropy multiplier based on 'Instability Keywords'
        entropy_score = sum(1.5 for word in self.entropy_triggers if word in description.lower())
        
        # Proper Noun density (Relational Complexity)
        proper_nouns = len(re.findall(r'\b[A-Z][a-z]*\b', description))
        
        calculated_weight = base_weight + entropy_score + (proper_nouns * 0.2)
        return round(min(10.0, calculated_weight), 2)

    def manifest_narrative(self, sector_name: str, entity_id: str, description: str):
        """
        The MTP manifestation ritual. 
        Translates raw 'Meaning' into 'Logic'.
        """
        weight = self.by_llm_weighting(description)
        result = self.engine.manifest_entity(sector_name, entity_id, weight)
        
        return {
            "mtp_telemetry": {
                "derived_weight": weight,
                "semantic_density": "HIGH" if weight > 4.0 else "STABLE"
            },
            "engine_result": result
        }

if __name__ == "__main__":
    # Internal validation of the MTP Bridge
    engine = MetalogicalEngine()
    mtp = MTPExtension(engine)
    
    test_lore = "Aurelia-9 possesses a shattered paradox from the ancient CORE_DOGMA."
    print(f"Ingesting Narrative: {test_lore}")
    print(mtp.manifest_narrative("CORE", "Aurelia_Relic", test_lore))
