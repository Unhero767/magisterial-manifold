import ast
import os
import sys

class GlitchScanner:
    """A Magisterial diagnostic tool with Telemetry tracking."""
    def __init__(self, target_path="."):
        self.target_path = target_path
        self.burns = 0
        self.scanned = 0
        self.skipped = 0

    def scan(self):
        print(f"📡 [SCAN] Targeted Resonance: {self.target_path}")
        GLITCH_WASTES = {'.git', '__pycache__', 'venv', '.venv', 'node_modules'}
        
        for root, dirs, files in os.walk(self.target_path):
            # 🛡️ SEAL THE BOUNDARY
            dirs[:] = [d for d in dirs if d not in GLITCH_WASTES and not d.startswith('.')]
            
            for file in files:
                full_path = os.path.join(root, file)
                if file.endswith(".py"):
                    self._check(full_path)
                else:
                    # 🌫️ TRACK NOISE: Increment skipped count for non-python files
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
        except Exception:
            self.skipped += 1

    def _report(self):
        print("\n--- 📜 Magisterial Telemetry Report ---")
        status = "🛡️ PURE" if self.burns == 0 else f"🔥 {self.burns} BURNS"
        print(f"  [STATUS]    {status}")
        print(f"  [SCANNED]   {self.scanned} Artifacts")
        print(f"  [SKIPPED]   {self.skipped} Noise/Foreign Files")
        print(f"  [EFFICIENCY] {round((self.scanned / (self.scanned + self.skipped + 1)) * 100, 2)}% Logic Density")
        print("---------------------------------------\n")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    GlitchScanner(target).scan()
