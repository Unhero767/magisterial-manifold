import argparse
import ast
import os
import shutil

class GlitchScanner:
    """A Magisterial active-containment tool with Telemetry."""
    def __init__(self, target_path=".", purge_mode=False):
        self.target_path = target_path
        self.purge_mode = purge_mode
        self.burns = 0
        self.scanned = 0
        self.skipped = 0
        # The absolute path to the Stasis Chamber
        self.vault_path = os.path.expanduser("~/magisterial-manifold/glitch_vault")

    def scan(self):
        print(f"📡 [SCAN] Targeted Resonance: {self.target_path}")
        if self.purge_mode:
            print("⚠️ [SOVEREIGN COMMAND] Auto-Purge Protocol ENGAGED.")
            
        GLITCH_WASTES = {'.git', '__pycache__', 'venv', '.venv', 'node_modules', 'glitch_vault'}
        
        for root, dirs, files in os.walk(self.target_path):
            dirs[:] = [d for d in dirs if d not in GLITCH_WASTES and not d.startswith('.')]
            for file in files:
                full_path = os.path.join(root, file)
                if file.endswith(".py"):
                    self._check(full_path)
                else:
                    self.skipped += 1
        
        self._report()

    def _check(self, path):
        self.scanned += 1
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                if content.strip():
                    ast.parse(content)
            print(f"  💎 {path}: OK")
        except (SyntaxError, IndentationError) as e:
            print(f"  🔥 {path}: BURN [{type(e).__name__}] at line {e.lineno}")
            self.burns += 1
            if self.purge_mode:
                self._quarantine(path)
        except Exception:
            self.skipped += 1

    def _quarantine(self, path):
        if not os.path.exists(self.vault_path):
            os.makedirs(self.vault_path)
            print(f"  🏛️ [VAULT] Constructed Stasis Chamber at {self.vault_path}")
        
        filename = os.path.basename(path)
        dest = os.path.join(self.vault_path, filename)
        shutil.move(path, dest)
        print(f"  ☣️ [QUARANTINE] Artifact displaced to glitch_vault/{filename}")

    def _report(self):
        print("\n--- 📜 Magisterial Telemetry Report ---")
        status = "🛡️ PURE" if self.burns == 0 else f"🔥 {self.burns} BURNS"
        print(f"  [STATUS]     {status}")
        print(f"  [SCANNED]    {self.scanned} Artifacts")
        print(f"  [SKIPPED]    {self.skipped} Noise/Foreign Files")
        print(f"  [EFFICIENCY] {round((self.scanned / (self.scanned + self.skipped + 1)) * 100, 2)}% Logic Density")
        print("---------------------------------------\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Magisterial Resonance Scanner")
    parser.add_argument("target", nargs="?", default=".", help="Target sector to scan")
    parser.add_argument("--purge", action="store_true", help="Engage the Auto-Purge protocol")
    args = parser.parse_args()
    
    GlitchScanner(target_path=args.target, purge_mode=args.purge).scan()
