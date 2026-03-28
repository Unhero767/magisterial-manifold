import sys
import os
from rule_engine import MetalogicalEngine

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    engine = MetalogicalEngine()
    current_sector = "CORE"
    
    while True:
        clear()
        sector = engine.sectors.get(current_sector)
        print(f"=== MLAOS ARCHITECT INTERFACE ===")
        print(f"ACTIVE SECTOR: {current_sector}")
        print(f"CONSISTENCY (◦A): {round(sector.consistency_a, 3)}")
        print(f"INSTABILITY (Ex◦): {round(sector.instability_ex, 3)}")
        tethers_list = ', '.join(sector.tethers) if sector.tethers else 'NONE'
        print(f"TETHERS: {tethers_list}")
        print("-" * 34)
        print("COMMANDS: manifest [id] [weight] | anchor [id] | sector [name] | quit")
        
        try:
            line = input("\n[LOGIC_INPUT]> ").strip().split()
            if not line: continue
            cmd = line[0].lower()
            
            if cmd == "quit": break
            elif cmd == "sector":
                current_sector = line[1].upper()
                if current_sector not in engine.sectors:
                    from rule_engine import ManifoldSector
                    engine.sectors[current_sector] = ManifoldSector(current_sector)
            elif cmd == "manifest":
                eid, w = line[1], float(line[2])
                print(f"\n{engine.manifest_entity(current_sector, eid, w)}")
                input("\nPress Enter...")
            elif cmd == "anchor":
                tid = line[1]
                print(f"\n{engine.apply_jovian_anchor(current_sector, tid)}")
                input("\nPress Enter...")
        except Exception as e:
            print(f"\n[!] Error: {e}")
            input("\nPress Enter...")

if __name__ == "__main__":
    main()
