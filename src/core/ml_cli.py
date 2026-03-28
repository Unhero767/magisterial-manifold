import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from rule_engine import MetalogicalEngine, ManifoldSector
from mtp_extension import MTPExtension

def clear(): os.system('clear')

def main():
    engine = MetalogicalEngine()
    mtp = MTPExtension(engine)
    current_sector = "CORE"
    
    while True:
        clear()
        sector = engine.sectors.get(current_sector)
        print(f"=== MLAOS ARCHITECT INTERFACE (MTP-ENABLED) ===")
        print(f"SECTOR: {current_sector} | ◦A: {round(sector.consistency_a, 3)} | Ex◦: {round(sector.instability_ex, 3)}")
        print("-" * 48)
        print("COMMANDS: manifest [id] [description] | anchor [id] | quit")
        
        try:
            line = input("\n[MTP_INPUT]> ").strip().split(' ', 2)
            if not line: continue
            cmd = line[0].lower()
            
            if cmd == "quit": break
            elif cmd == "manifest":
                eid, desc = line[1], line[2]
                res = mtp.manifest_narrative(current_sector, eid, desc)
                print(f"\n[MTP WEIGHT]: {res['mtp_telemetry']['derived_weight']}")
                print(f"[RESULT]: {res['engine_result']}")
                input("\nPress Enter...")
            elif cmd == "anchor":
                print(f"\n{engine.apply_jovian_anchor(current_sector, line[1])}")
                input("\nPress Enter...")
        except Exception as e:
            print(f"\n[!] Error: {e}")
            input("\nPress Enter...")

if __name__ == "__main__": main()
