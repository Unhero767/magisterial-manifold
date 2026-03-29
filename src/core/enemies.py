import random

class KMS_Sentinel:
    def __init__(self):
        self.name = "K_M_Synthetica Sentinel"
        self.integrity = 50  # HP equivalent
        self.entropy_output = 0.12  # Base damage to ◦A

    def entropy_attack(self, protagonist, sector):
        """
        Forces an immediate Ex◦ Check.
        If the sector is already unstable, the damage multiplies.
        """
        print(f"\n[ ! WARNING ! ]: {self.name} is initiating 'ENTROPY_ATTACK'...")
        
        # Calculate the 'Burn Factor'
        # Formula: Base Damage * (1 + Sector Instability)
        burn_factor = self.entropy_output * (1 + sector.instability_ex)
        
        print(f"  Target: {protagonist}")
        print(f"  Metalogical Pressure: {round(burn_factor, 4)}")
        
        # Apply damage to the sector's Consistency
        sector.consistency_a = max(0.0, sector.consistency_a - burn_factor)
        sector.instability_ex = min(1.0, sector.instability_ex + (burn_factor * 0.8))
        
        # The Ex◦ Check: If Instability exceeds 0.50, Aurelia-9 suffers 'System Glitch'
        if sector.instability_ex > 0.50:
            return "[ SYSTEM_GLITCH ]: Aurelia-9's code is de-syncing. Discard 1 Logic Fragment."
        
        return "[ SHIELD_HELD ]: Integrity remains within Sovereign limits."

