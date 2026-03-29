import random

class CombatCard:
    def __init__(self, name, cost, card_type):
        self.name = name
        self.cost = cost
        self.type = card_type

    def execute(self, sector, **kwargs):
        pass

class LogicFragmentCard(CombatCard):
    def __init__(self):
        super().__init__("LOGIC_FRAGMENT_01", cost=2, card_type="RESTORATION")
        self.description = "Expends a Primordial string to restore +0.05 ◦A and purge -0.02 Ex◦."

    def execute(self, sector, **kwargs):
        print(f"\n[ EXECUTING {self.name} ]")
        old_a = sector.consistency_a
        sector.consistency_a = min(1.0, sector.consistency_a + 0.05)
        old_ex = sector.instability_ex
        sector.instability_ex = max(0.0, sector.instability_ex - 0.02)
        print(f"  ◦A: {round(old_a, 4)} -> {round(sector.consistency_a, 4)}")
        print(f"  Ex◦: {round(old_ex, 4)} -> {round(sector.instability_ex, 4)}")
        return "[ CALM_RESTORED ]: The Logic Storm recedes."

class AshShardCard(CombatCard):
    def __init__(self):
        super().__init__("ASH_SHARD", cost=1, card_type="ENTROPY_WEAPON")
        self.description = "Weaponizes pure Ex◦. Deals 40 Integrity damage but spikes Sector Instability by +0.15."

    def execute(self, sector, **kwargs):
        target = kwargs.get('target')
        print(f"\n[ EXECUTING {self.name} ]")
        print("  > Aurelia-9 crushes the shard, releasing a localized Metalogical Burn.")
        
        if target:
            target.integrity -= 40
            print(f"  > {target.name} takes 40 Entropy Damage. (Integrity: {max(0, target.integrity)})")
        
        old_ex = sector.instability_ex
        sector.instability_ex = min(1.0, sector.instability_ex + 0.15)
        print(f"  > Sector {sector.name} Ex◦: {round(old_ex, 4)} -> {round(sector.instability_ex, 4)}")
        
        if sector.instability_ex >= 0.50:
            print("  [ ! ] WARNING: Entropy threshold breached. Glitch-Waste cascade imminent.")
            
        return "[ BURN_APPLIED ]: The target's architecture is melting."

class LogicStorm:
    def __init__(self, intensity=0.03):
        self.intensity = intensity

    def erode(self, sector):
        sector.consistency_a -= self.intensity
        sector.instability_ex += (self.intensity * 0.5)
        print(f"\n[ LOGIC STORM ACTIVE ]: Sector {sector.name} is fraying...")
