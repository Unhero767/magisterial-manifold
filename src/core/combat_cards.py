import random

class CombatCard:
    def __init__(self, name, cost, type):
        self.name = name
        self.cost = cost  # Cost in 'Cycles' or 'Memory'
        self.type = type

    def execute(self, sector, engine):
        pass

class LogicFragmentCard(CombatCard):
    def __init__(self):
        super().__init__("LOGIC_FRAGMENT_01", cost=2, type="RESTORATION")
        self.description = "Expends a Primordial string to restore 0.05 ◦A."

    def execute(self, sector, engine):
        """
        Performs a 'Structural Repair' ritual.
        Increases consistency (◦A) and dampens instability (Ex◦).
        """
        print(f"\n[ EXECUTING {self.name} ]")
        
        # Immutable Fact: Restore 0.05 Consistency
        old_a = sector.consistency_a
        sector.consistency_a = min(1.0, sector.consistency_a + 0.05)
        
        # Bonus: Reduce instability by a factor of the repair
        old_ex = sector.instability_ex
        sector.instability_ex = max(0.0, sector.instability_ex - 0.02)
        
        print(f"  ◦A: {round(old_a, 4)} -> {round(sector.consistency_a, 4)}")
        print(f"  Ex◦: {round(old_ex, 4)} -> {round(sector.instability_ex, 4)}")
        return "[CALM_RESTORED]: The Logic Storm recedes."

class LogicStorm:
    """An environmental encounter that drains ◦A every turn."""
    def __init__(self, intensity=0.03):
        self.intensity = intensity

    def erode(self, sector):
        sector.consistency_a -= self.intensity
        sector.instability_ex += (self.intensity * 0.5)
        print(f"\n[ LOGIC STORM ACTIVE ]: Sector {sector.name} is fraying...")
