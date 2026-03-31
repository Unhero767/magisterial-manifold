import argparse, ast, os, sys, shutil, datetime
import aegis_sentinel
import aletheic_matrix  # Importing the Tier 0 Bedrock

class GlitchScanner:
    def __init__(self, target_path=".", purge_mode=False):
        # --- [DOGMA ENFORCEMENT] ---
        print(f"\n📜 [CORE_DOGMA] {aletheic_matrix.CORE_DOGMA}")
        print(f"📍 [SECTOR] Olney, IL | {aletheic_matrix.COORDINATES}")
        print("-" * 45)
        
        self.target_path = target_path
        self.purge_mode = purge_mode
        self.burns = 0
        self.logic_mass = 0

    def scan(self):
        print(f"📡 [SCAN] Targeted Resonance: {self.target_path}")
        GLITCH_WASTES = {'.git', '__pycache__', 'venv', '.venv', 'node_modules', 'glitch_vault', 'hall_of_records'}
        for root, dirs, files in os.walk(self.target_path):
            dirs[:] = [d for d in dirs if d not in GLITCH_WASTES and not d.startswith('.')]
            for file in files:
                if file.endswith(".py"):
                    self._check(os.path.join(root, file))
        if self.burns == 0:
            self._manifest_certificate()
            if aegis_sentinel.monitor_mass(self.logic_mass):
                print("⚡ [ACTION] Deep Resonance active.")
        print(f"\n--- [REPORT] Status: {'🛡️ PURE' if self.burns == 0 else f'🔥 {self.burns} BURNS'} ---")

    def _check(self, path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                line_count = len(content.splitlines())
                if not aegis_sentinel.check_density(path, line_count):
                    self.burns += 1
                ast.parse(content)
                self.logic_mass += line_count
            print(f"  💎 {path}: OK ({line_count} lines)")
        except Exception as e:
            print(f"  🔥 {path}: BURN detected.")
            self.burns += 1

    def _manifest_certificate(self):
        hall_path = os.path.expanduser("~/magisterial-manifold/hall_of_records")
        if not os.path.exists(hall_path): os.makedirs(hall_path)
        cert_fn = f"CERT_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(os.path.join(hall_path, cert_fn), "w") as f:
            f.write(f"DOGMA: {aletheic_matrix.CORE_DOGMA}\nMASS: {self.logic_mass}\nSTATUS: ◦A VERIFIED")
        print(f"  🏛️ [ARCHIVE] Certificate logged: {cert_fn}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ml-logic")
    sub = parser.add_subparsers(dest="command")
    m = sub.add_parser("run-mission")
    m.add_argument("--path", default="."); m.add_argument("--purge", action="store_true")
    args = parser.parse_args()
    if args.command == "run-mission":
        GlitchScanner(args.path, args.purge).scan()
