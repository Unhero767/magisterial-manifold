import os
import sys
from datetime import datetime

# FORCE PATHING: Add the directory containing this script to the search path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from bio_parser import BioSemanticParser
except ImportError as e:
    print(f"[!] Logic Storm: BioSemanticParser still unreachable. {e}")
    sys.exit(1)

def initiate_archive_log():
    parser = BioSemanticParser()
    entry = parser.generate_telemetry()
    
    # Use absolute path for the log to ensure it finds the root
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    log_path = os.path.join(root_dir, "docs/archives/telemetry/manifold_pulse.log")
    
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        f.write(f"{entry}\n")
    print(f"[Σ-7] Pulse Recorded: {entry}")

if __name__ == "__main__":
    initiate_archive_log()
