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
        print(f"=== MLAOS ARCHITECT INTERFACE (TOPOLOGY-AWARE) ===")
        print(f"SECTOR: {current_sector} | ◦A: {round(sector.consistency_a, 4)} | Ex◦: {round(sector.instability_ex, 4)}")
        print(f"NEIGHBORS: {', '.join(sector.neighbors) if sector.neighbors else 'NONE'}")
        print("-" * 52)
        print("COMMANDS: manifest [id] [desc] | anchor [id] | link [s1] [s2] | sector [name] | quit")
        
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
                s1, s2 = line[1].upper(), line[2].upper()
                engine.define_topology(s1, s2)
                print(f"\n[ ✓ ] TOPOLOGY SYNCED: {s1} <--> {s2}")
                input("\nPress Enter...")
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

# --- Magisterial Color Mapping ---
PROTOCOL_COLORS = {
    "Luminous_Static": CYAN if HAS_COLOR else "",
    "Standard_Dogma": Fore.GREEN if HAS_COLOR else "",
    "Purge": RED if HAS_COLOR else "",
    "Lore_Sync": Fore.MAGENTA if HAS_COLOR else "",
    "Alert": Fore.YELLOW if HAS_COLOR else ""
}

def ritual_log(protocol, message):
    """Logs a message with the associated protocol color."""
    color = PROTOCOL_COLORS.get(protocol, "")
    prefix = f"[{protocol.upper()}]"
    magisterial_print(f"{prefix} {message}", color)

# --- Magisterial Color Mapping ---
PROTOCOL_COLORS = {
    "Luminous_Static": CYAN if HAS_COLOR else "",
    "Standard_Dogma": (Fore.GREEN if HAS_COLOR else ""),
    "Purge": (RED if HAS_COLOR else ""),
    "Lore_Sync": (Fore.MAGENTA if HAS_COLOR else ""),
    "Alert": (Fore.YELLOW if HAS_COLOR else "")
}

def ritual_log(protocol, message):
    """Logs a message with the associated protocol color."""
    color = PROTOCOL_COLORS.get(protocol, "")
    prefix = f"[{protocol.upper()}]"
    magisterial_print(f"{prefix} {message}", color)
