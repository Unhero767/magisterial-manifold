import time
import os
import sys
from combat_cards import LogicFragmentCard
from enemies import KMS_Sentinel

def clear(): os.system('clear')

def start_storm(sector, engine):
    hack_progress = 0
    storm_intensity = 0.04
    fragment_card = LogicFragmentCard()
    sentinel = KMS_Sentinel()
    sentinel_triggered = False
    
    print(f"!!! LOGIC STORM DETECTED IN {sector.name} !!!")
    print("Hacking K_M_Synthetica Sub-Vault... Security levels rising.")
    time.sleep(1.5)

    while hack_progress < 100:
        clear()
        # 1. Environmental Erosion
        sector.consistency_a -= storm_intensity
        sector.instability_ex += (storm_intensity * 0.5)
        hack_progress += 5
        
        # 2. [ INTERCEPTION CHECK ]
        # Triggered if Consistency falls below the 0.85 threshold
        if sector.consistency_a < 0.85 and not sentinel_triggered:
            print(f"\n[ ! ] SECURITY BREACH DETECTED: {sentinel.name} HAS ARRIVED.")
            print(sentinel.entropy_attack("Aurelia-9", sector))
            sentinel_triggered = True  
            time.sleep(2)

        # 3. Display Telemetry
        print(f"=== [ SECTOR: {sector.name} ] ===")
        print(f"Consistency (◦A): {round(sector.consistency_a, 4)}")
        print(f"Instability (Ex◦): {round(sector.instability_ex, 4)}")
        print(f"Vault Hack: {hack_progress}% [{'=' * (hack_progress // 5)}{' ' * (20 - (hack_progress // 5))}]")
        print("-" * 40)
        
        # 4. Critical Failure Check
        if sector.consistency_a <= 0:
            print("\n[ CRITICAL COLLAPSE ]: Sector has dissolved into the Glitch-Wastes.")
            return False

        # 5. Agent Intervention
        print("COMMANDS: play fragment | wait")
        action = input("[ACTION]> ").strip().lower()
        
        if action == "play fragment":
            print(fragment_card.execute(sector, engine))
            time.sleep(1)
        
        time.sleep(0.5)

    print("\n[ SUCCESS ]: Vault Decrypted. Aurelia-9 extracts the data.")
    return True

if __name__ == "__main__":
    from rule_engine import ManifoldSector, MetalogicalEngine
    engine = MetalogicalEngine()
    veil = ManifoldSector("NEON_VEIL", 0.90, 0.10)
    start_storm(veil, engine)
