import rumps
import subprocess
import os

class MagisterialMonitor(rumps.App):
    def __init__(self):
        super(MagisterialMonitor, self).__init__("◦A")
        self.repo_path = os.path.expanduser("~/magisterial-manifold")
        self.icon_stable = "◦A"
        self.icon_burn = "Ex◦"

    @rumps.timer(300)
    def check_consistency(self, _):
        try:
            result = subprocess.run(
                ["find", ".", "-type", "l", "!", "-exec", "test", "-e", "{}", ";", "-print"],
                cwd=self.repo_path, capture_output=True, text=True
            )
            self.title = self.icon_burn if result.stdout.strip() else self.icon_stable
        except Exception:
            self.title = "?"

    @rumps.clicked("Manual Scan")
    def manual_scan(self, _):
        self.check_consistency(_)

    @rumps.clicked("Purge Wastes")
    def trigger_purge(self, _):
        subprocess.run(["git", "reset", "--hard", "HEAD"], cwd=self.repo_path)
        self.check_consistency(_)

if __name__ == "__main__":
    MagisterialMonitor().run()
