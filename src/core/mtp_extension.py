import re
import sys
import os
from typing import List, Dict, Any

# Align path to find rule_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine

class MTPExtension:
    """
    Formalizes the Semantic Ingestion Sequence using MTP principles.
    Enforces Sovereign Truths and calculates the Index of Divergence (I).
    """
    def __init__(self, engine: MetalogicalEngine, sovereign_truths: List[str] = None):
        self.engine = engine
        self.logic_threshold = 0.85
        
        # The immutable axioms of the Manifold
        self.sovereign_truths = sovereign_truths or [
            "The CORE_DOGMA remains absolute.",
            "Metalogical Burn is irreversible without Jovian Anchors.",
            "Consistency (◦A) must precede expansion."
        ]
        
        # Mathematical Constants for the I formula
        self.W_t = 0.15  # Weight of defined structural thresholds
        self.beta = 0.05 # Contextual buffer (simulating Walker spatial memory)

    def _calculate_semantic_proximity(self, narrative: str) -> float:
        """
        Simulates the LLM high-dimensional latent space calculation (W_l).
        Measures cosine similarity divergence from Sovereign Truths.
        """
        divergence = 0.10
        narrative_lower = narrative.lower()
        
        # Simulated divergence triggers against Sovereign Truths
        anomalies = ["paradox", "shattered", "void", "unmade", "forbidden", "glitch", "infinite"]
        for word in anomalies:
            if word in narrative_lower:
                divergence += 0.25 # High divergence penalty
                
        return min(1.0, divergence)

    def by_llm_weighting(self, narrative: str) -> float:
        """
        Derives the logic_weight using the exact Index of Divergence formula:
        I = (W_t * T) + (W_l * N_trig) - Beta
        """
        # T: Number of structural thresholds crossed (e.g., length complexity)
        word_count = len(narrative.split())
        T = 1 if word_count > 10 else 0
        if word_count > 30: T = 2

        # W_l: Dynamically derived semantic proximity
        W_l = self._calculate_semantic_proximity(narrative)

        # N_trig: Conditional triggers engaged (capitalized entities/concepts)
        proper_nouns = re.findall(r'\b[A-Z][A-Za-z0-9_]*\b', narrative)
        N_trig = len(proper_nouns) * 0.5
        if N_trig == 0: N_trig = 0.5 # Minimum trigger baseline

        # I: Index of Divergence
        I = (self.W_t * T) + (W_l * N_trig) - self.beta
        
        return round(max(0.0, I), 3)

    def manifest_narrative(self, sector_name: str, entity_id: str, description: str) -> Dict[str, Any]:
        """
        The execution phase of the Semantic Ingestion Sequence.
        Includes an automatic Ex◦ Quarantine Protocol.
        """
        index_I = self.by_llm_weighting(description)
        
        # The Ex◦ Anomaly Detection
        if index_I > self.logic_threshold:
            return {
                "mtp_telemetry": {
                    "I_divergence": index_I,
                    "status": "Ex◦ ANOMALY DETECTED: QUARANTINED",
                    "msg": f"Narrative rejected. Index {index_I} exceeds {self.logic_threshold} threshold."
                },
                "engine_result": {"status": "BLOCKED_BY_BRIDGE"}
            }

        # If mathematically stable, pass to the Walker/Engine for topological manifestation
        result = self.engine.manifest_entity(sector_name, entity_id, index_I)
        
        return {
            "mtp_telemetry": {
                "I_divergence": index_I,
                "status": "SEMANTIC_INGESTION_SAFE"
            },
            "engine_result": result
        }

if __name__ == "__main__":
    # Internal Validation Sequence
    engine = MetalogicalEngine()
    mtp = MTPExtension(engine)
    
    print("Testing Safe Logic...")
    print(mtp.manifest_narrative("CORE", "Test_01", "A standard Magisterial node."))
    
    print("\nTesting Ex◦ Anomaly...")
    print(mtp.manifest_narrative("GLITCH_WASTES", "Paradox_01", "An infinite shattered paradox of forbidden CORE_DOGMA."))
