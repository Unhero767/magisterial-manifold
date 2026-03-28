import random
import sys
import os

# Align path to find rule_engine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine

def run_stress_test(iterations=100):
    engine = MetalogicalEngine(burn_threshold=0.60)
    sector_name = "STRESS_CHAMBER"
    
    print(f"--- INITIATING METALOGICAL STRESS-TEST ---")
    print(f"Target Sector: {sector_name}")
    print(f"Burn Threshold: {engine.burn_threshold}\n")

    for i in range(1, iterations + 1):
        entity_id = f"Anomaly_{i:03d}"
        # Random weight between 0.5 (minor detail) and 5.0 (core paradigm shift)
        weight = round(random.uniform(0.5, 5.0), 2)
        
        result = engine.manifest_entity(sector_name, entity_id, weight)
        
        if result["status"] == "METALOGICAL_BURN":
            print(f"\n[!] CRITICAL FAILURE at Iteration {i}")
            print(f"    Cause: {entity_id} (Weight: {weight})")
            print(f"    Final State: {result['msg']}")
            return i
        
        telemetry = result["telemetry"]
        print(f"[{i:03d}] Manifested {entity_id} | Weight: {weight} | ◦A: {telemetry['◦A']} | Ex◦: {telemetry['Ex◦']}")

    print("\n[✓] TEST COMPLETE: Sector maintained stability through all iterations.")
    return iterations

if __name__ == "__main__":
    run_stress_test()
