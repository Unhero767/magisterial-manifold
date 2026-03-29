import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine, ManifoldSector
from mtp_extension import MTPExtension
from lore_vault import LoreVault
from master_weaver import MasterWeaver

def clear(): os.system('clear')

def main():
    engine = MetalogicalEngine()
    mtp = MTPExtension(engine)
    vault = LoreVault()
    weaver = MasterWeaver()
    
    # Attempt to load existing manifold state
    saved_state = vault.load_manifold()
    if saved_state:
        for name, d in saved_state.items():
            s = ManifoldSector(name, d["consistency_a"], d["instability_ex"])
            s.tethers = set(d["tethers"])
            s.entities = d["entities"]
            s.neighbors = d["neighbors"]
            engine.sectors[name] = s
            
    current_sector = "CORE"
    
    while True:
        clear()
        sector = engine.sectors.get(current_sector)
        print(f"=== MLAOS ARCHITECT INTERFACE (WEAVER-LINKED) ===")
        print(f"SECTOR: {current_sector} | ◦A: {round(sector.consistency_a, 4)} | Ex◦: {round(sector.instability_ex, 4)}")
        print(f"NEIGHBORS: {', '.join(sector.neighbors) if sector.neighbors else 'NONE'}")
        print("-" * 55)
        print("COMMANDS: manifest [id] [desc] | anchor [id] | link [s1] [s2] | sector [name] | weave | quit")
        
        try:
            line = input("\n[MTP_INPUT]> ").strip().split(' ', 2)
            if not line: continue
            cmd = line[0].lower()
            
            if cmd == "quit": break
            elif cmd == "sector":
                current_sector = line[1].upper()
                if current_sector not in engine.sectors:
                    engine.sectors[current_sector] = ManifoldSector(current_sector)
            elif cmd == "link":
                if len(line) < 3:
                    print("\n[!] Usage: link [sector1] [sector2]")
                else:
                    s1, s2 = line[1].upper(), line[2].upper()
                    engine.define_topology(s1, s2)
                    print(f"\n[ ✓ ] TOPOLOGY SYNCED: {s1} <--> {s2}")
            elif cmd == "manifest":
                if len(line) < 3:
                    print("\n[!] Usage: manifest [id] [description]")
                else:
                    eid, desc = line[1], line[2]
                    res = mtp.manifest_narrative(current_sector, eid, desc)
                    
                    telemetry = res.get('mtp_telemetry', {})
                    print(f"\n[MTP INDEX (I)]: {telemetry.get('I_divergence', 'N/A')}")
                    
                    if "Ex◦" in telemetry.get('status', ''):
                        print(f"[ ! QUARANTINE ! ]: {telemetry.get('msg')}")
                    else:
                        print(f"[RESULT]: {res.get('engine_result', {}).get('status', 'UNKNOWN')}")
            elif cmd == "anchor":
                if len(line) < 2:
                    print("\n[!] Usage: anchor [id]")
                else:
                    print(f"\n{engine.apply_jovian_anchor(current_sector, line[1])}")
            elif cmd == "weave":
                print(weaver.weave_diagnostics())
            
            # AUTOMATIC PERSISTENCE
            vault.save_manifold(engine.sectors)
            input("\nPress Enter...")
            
        except Exception as e:
            print(f"\n[!] Systemic Anomaly: {e}")
            input("\nPress Enter...")

if __name__ == "__main__": main()
