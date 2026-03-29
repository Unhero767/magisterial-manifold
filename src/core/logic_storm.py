import time
import os
import sys
from combat_cards import LogicFragmentCard

def clear(): os.system('clear')

def start_storm(sector, engine):
    hack_progress = 0
    storm_intensity = 0.04
    fragment_card = LogicFragmentCard()
    
    print(f"!!! LOGIC STORM DETECTED IN {sector.name} !!!")
    print("Hacking K_M_Synthetica Sub-Vault... Hold the line.")
    time.sleep(2)

    while hack_progress < 100:
        clear()
        # 1. Environmental Erosion
        sector.consistency_a -= storm_intensity
        sector.instability_ex += (storm_intensity * 0.5)
        hack_progress += 5
        
        # 2. Display Telemetry
        print(f"=== [ SECTOR: {sector.name} ] ===")
        print(f"Consistency (◦A): {round(sector.consistency_a, 4)} [{'#' * int(sector.consistency_a * 20)}{'-' * (20 - int(sector.consistency_a * 20))}]")
        print(f"Instability (Ex◦): {round(sector.instability_ex, 4)}")
        print(f"Vault Hack: {hack_progress}% [{'=' * (hack_progress // 5)}{' ' * (20 - (hack_progress // 5))}]")
        print("-" * 40)
        
        # 3. Critical Failure Check
        if sector.consistency_a <= 0:
            print("\n[ CRITICAL COLLAPSE ]: The Neon Veil has dissolved into the Glitch-Wastes.")
            return False

        # 4. Agent Intervention (Non-blocking check)
        print("COMMANDS: play fragment | wait")
        action = input("[ACTION]> ").strip().lower()
        
        if action == "play fragment":
            print(fragment_card.execute(sector, engine))
            time.sleep(1)
        elif action == "wait":
            print("Holding position...")
        
        time.sleep(0.5)

    print("\n[ SUCCESS ]: Vault Sub-sector 04 decrypted. Aurelia-9 extracts the data.")
    return True

if __name__ == "__main__":
    from rule_engine import ManifoldSector, MetalogicalEngine
    engine = MetalogicalEngine()
    veil = ManifoldSector("NEON_VEIL", 0.90, 0.10)
    start_storm(veil, engine)
