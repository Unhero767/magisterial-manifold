import sys, os, random
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine, ManifoldSector
from mtp_extension import MTPExtension
from lore_vault import LoreVault
from master_weaver import MasterWeaver
from aletheic_matrix import AletheicMatrix
from mission_vault import MissionVault

def clear(): os.system('clear')

def main():
    engine, mtp, vault = MetalogicalEngine(), MTPExtension(MetalogicalEngine()), LoreVault()
    weaver, oracle, m_vault = MasterWeaver(), AletheicMatrix(), MissionVault()
    
    saved_state = vault.load_manifold()
    if saved_state:
        for name, d in saved_state.items():
            s = ManifoldSector(name, d["consistency_a"], d["instability_ex"])
            s.tethers, s.entities, s.neighbors = set(d["tethers"]), d["entities"], d["neighbors"]
            engine.sectors[name] = s
            
    current_sector = "CORE"
    
    while True:
        clear()
        sector = engine.sectors.get(current_sector)
        print(f"=== MLAOS ARCHITECT INTERFACE (MISSION-ACTIVE) ===")
        print(f"SECTOR: {current_sector} | ◦A: {round(sector.consistency_a, 4)} | Ex◦: {round(sector.instability_ex, 4)}")
        print("-" * 55)
        print("COMMANDS: manifest | anchor | link | sector | weave | query")
        print("          missions | run-mission [id] | quit")
        
        try:
            line = input("\n[MTP_INPUT]> ").strip().split(' ', 2)
            if not line: continue
            cmd = line[0].lower()
            
            if cmd == "quit": break
            elif cmd == "missions":
                missions = m_vault.load_all()
                for mid, m in missions.items():
                    print(f"- {mid}: {m['objective']['primary']} (Threat: {m['objective']['threat_level']})")
            elif cmd == "run-mission":
                mid = line[1]
                m = m_vault.load_all().get(mid)
                if not m: print("[!] Mission not found."); continue
                
                target = engine.sectors.get(m['sector'])
                print(f"\n--- INITIATING {mid} ---")
                print(f"Target Sector: {m['sector']} (◦A: {target.consistency_a})")
                
                if target.consistency_a < m['constraints']['min_consistency_a']:
                    print(f"[!] ABORT: Sector instability too high for {m['protagonist']}.")
                else:
                    roll = random.random()
                    print(f"Resonance Check: {round(roll, 2)} vs {m['success_probability']['final_resonance']}")
                    if roll <= m['success_probability']['final_resonance']:
                        print(f"[ SUCCESS ]: {m['protagonist']} extracted {len(m['loot_table'])} fragments.")
                        for item in m['loot_table']: print(f"  > Received: {item['id']} ({item['utility']})")
                    else:
                        print(f"[ FAILURE ]: {m['failure_protocol']} engaged.")
            
            elif cmd == "weave": print(weaver.weave_diagnostics())
            elif cmd == "query": print(oracle.interrogate(" ".join(line[1:])))
            elif cmd == "manifest":
                eid, desc = line[1], line[2]
                res = mtp.manifest_narrative(current_sector, eid, desc)
                print(f"\n[RESULT]: {res.get('engine_result', {}).get('status', 'STABILIZED')}")
            
            vault.save_manifold(engine.sectors)
            input("\nPress Enter...")
        except Exception as e:
            print(f"\n[!] Error: {e}"); input("\nPress Enter...")

if __name__ == "__main__": main()
