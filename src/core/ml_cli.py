#!/usr/bin/env python3
import argparse
import sys
import json
import os
from pathlib import Path

STATE_FILE = Path("src/data/reality_state.json")

def fossilize_state(payload):
    """Writes the current reality state to the L1 Memory Spine (JSON)."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(payload, f, indent=4)
        print(f"[ + ] Ledger updated: {STATE_FILE.name}")
    except IOError as e:
        print(f"[ - ] L0 Write Failure: {e}")

def init_parser():
    parser = argparse.ArgumentParser(
        description="MLAOS-Prime Logic Engine: Paraconsistent Reality CLI",
        prog="ml-logic"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    mission_parser = subparsers.add_parser("run-mission", help="Execute a specific narrative/structural mission")
    mission_parser.add_argument("mission_id", type=str, help="The designated ID of the operation")
    mission_parser.add_argument("--force", action="store_true", help="Bypass standard checks")

    subparsers.add_parser("stand-down", help="Retract weapons and secure Sector-01")

    return parser

def execute_mission(mission_id: str, force: bool):
    if mission_id == "MP_01_SILICON_EYE":
        print("[ ! ] SECURITY BREACH DETECTED IN SECTOR-01")
        print("[ * ] Initiating extraction protocol for Aurelia-9...")
        combat_state = {
            "encounter_active": True,
            "mission_id": mission_id,
            "threat_level": "CRITICAL",
            "active_perimeter": "Zk_Kinetic",
            "aurelia_loadout": {
                "weapon_drawn": "Sy-As_Edge",
                "magnetism_level": 100
            },
            "force_flag_active": force
        }
        fossilize_state(combat_state)
        print("[ + ] Sentinel Encounter deployed.")
    else:
        print(f"[ - ] Error: Mission ID '{mission_id}' is not recognized.")

def secure_sector():
    print("[ * ] Retracting Zekian Kinetic perimeter...")
    print("[ * ] Powering down Sy-As Edge...")
    calm_state = {
        "encounter_active": False,
        "threat_level": "SECURE",
        "active_perimeter": "STANDBY",
        "aurelia_loadout": {
            "weapon_drawn": "None",
            "magnetism_level": 0
        }
    }
    fossilize_state(calm_state)
    print("[ + ] Sector-01 SECURE. Awaiting command.")

def main():
    parser = init_parser()
    args = parser.parse_args()

    if args.command == "run-mission":
        execute_mission(args.mission_id, args.force)
    elif args.command == "stand-down":
        secure_sector()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
