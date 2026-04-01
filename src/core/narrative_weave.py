"""
src/core/narrative_weave.py
The Weaving Core of the Spire.
Synthesizing R_eff and Archetypes into story transitions.
"""

class NarrativeWeave:
    def __init__(self, neo4j_driver=None):
        self.driver = neo4j_driver

    def calculate_transition_probability(self, r_eff, edge_weight):
        """
        Uses the Restorative κ to determine if a transition is stable.
        If R_eff exceeds the edge_weight, the 'grain' breaks.
        """
        # A delta of 0.0 indicates perfect alignment with the grain.
        return max(0.0, 1.0 - abs(r_eff - edge_weight))

    def weave_next_moment(self, current_v0, active_archetype):
        """
        Queries the Loom for the next potential narrative vector.
        """
        # Calculate the effective resonance against the mythic constant
        r_eff = current_v0 * active_archetype.effective_kappa
        
        print(f"--- [WEAVE] Resonance {r_eff:.2f} interacting with {active_archetype.name} ---")
        
        # In a strange universe, this return manifests the next 'Event' node.
        return {"r_eff": r_eff, "status": "NEO4J_QUERY_PENDING"}
