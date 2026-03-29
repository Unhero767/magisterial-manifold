import json
import os

class MasterWeaver:
    """
    Predictive Intelligence Layer.
    Scans the topological ledger and recommends harmonic interventions.
    """
    def __init__(self, vault_path="src/data/vault.json"):
        self.vault_path = vault_path

    def weave_diagnostics(self):
        if not os.path.exists(self.vault_path):
            return "\n[!] THE LOOM IS EMPTY. Manifest sectors to begin weaving."

        with open(self.vault_path, "r") as f:
            manifold = json.load(f)

        print("\n... Analyzing Vault Topology ...\n")
        recommendations = []
        rec_count = 1

        for sector_name, data in manifold.items():
            c_a = data["consistency_a"]
            neighbors = data["neighbors"]

            # 1. Detect Ex◦ Proximity (The Burn Risk)
            if c_a < 0.40:
                recommendations.append(
                    f"{rec_count}. [ STABILIZE ]: Sector {sector_name} is nearing critical logic decay (◦A = {c_a:.2f}).\n"
                    f"   Recommendation: Manifest a Jovian Anchor tied to 'CORE_DOGMA' to restore coherence."
                )
                rec_count += 1

            # 2. Detect Harmonic Resonance (Safe Expansion)
            elif c_a >= 0.90:
                recommendations.append(
                    f"{rec_count}. [ EXPAND ]: Sector {sector_name} has high harmonic resonance (◦A = {c_a:.2f}).\n"
                    f"   Recommendation: Safe to manifest high-entropy entities (W_l up to 0.60)."
                )
                rec_count += 1

            # 3. Detect Topological Isolation
            if not neighbors and sector_name != "CORE":
                recommendations.append(
                    f"{rec_count}. [ LINK ]: {sector_name} is logically isolated.\n"
                    f"   Recommendation: Link to a stable sector to establish a shared narrative boundary."
                )
                rec_count += 1

        if not recommendations:
            return "[ WEAVER ADVISORY ]: The Manifold is in perfect equilibrium. Maintain current vectors."
        
        header = f"[ WEAVER ADVISORY: {len(recommendations)} Optimal Paths Detected ]"
        return header + "\n" + "\n".join(recommendations)

if __name__ == "__main__":
    weaver = MasterWeaver()
    print(weaver.weave_diagnostics())
