import os
import sys
from datetime import datetime

# Bridge the pathing gaps
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from bio_parser import BioSemanticParser
except ImportError:
    print("[!] Logic Storm: BioSemanticParser not found.")
    sys.exit(1)

def initiate_archive_log():
    parser = BioSemanticParser()
    entry = parser.generate_telemetry()
    log_path = "docs/archives/telemetry/manifold_pulse.log"
    
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as f:
        f.write(f"{entry}\n")
    print(f"[Σ-7] Pulse Recorded: {entry}")

if __name__ == "__main__":
    initiate_archive_log()
