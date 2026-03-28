import curses, subprocess, os, time
from datetime import datetime

COLOR_STABLE, COLOR_BURN, COLOR_HEADER = 2, 3, 4

class TacticalDashboard:
    def __init__(self):
        self.repo_path = os.path.expanduser("~/magisterial-manifold")
        self.log_path = os.path.expanduser("~/Library/Logs/Magisterium/monitor_err.log")

    def run(self):
        curses.wrapper(self.draw)

    def draw(self, stdscr):
        curses.start_color()
        curses.init_pair(COLOR_STABLE, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(COLOR_BURN, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(COLOR_HEADER, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.curs_set(0)
        stdscr.nodelay(1)

        while True:
            stdscr.erase()
            h, w = stdscr.getmaxyx()
            stdscr.addstr(0, 0, "=" * w, curses.color_pair(COLOR_HEADER))
            stdscr.addstr(0, (w-20)//2, " MAGISTERIAL DASHBOARD ", curses.A_REVERSE)
            
            # [1] Grid Health
            stdscr.addstr(2, 2, " [1] GRID HEALTH ", curses.A_BOLD)
            res = subprocess.run(["find", ".", "-type", "l", "!", "-exec", "test", "-e", "{}", ";", "-print"], 
                               cwd=self.repo_path, capture_output=True, text=True)
            if res.stdout.strip():
                stdscr.addstr(4, 4, "STATUS: Ex◦ (BURN DETECTED)", curses.color_pair(COLOR_BURN))
            else:
                stdscr.addstr(4, 4, "STATUS: ◦A STABILIZED", curses.color_pair(COLOR_STABLE))

            # [2] Sentinel Status
            stdscr.addstr(7, 2, " [2] SENTINEL STATUS ", curses.A_BOLD)
            l_check = subprocess.run(["launchctl", "list", "com.unhero.magisterial.monitor"], capture_output=True)
            status = "LIVE" if l_check.returncode == 0 else "OFFLINE"
            color = COLOR_STABLE if status == "LIVE" else COLOR_BURN
            stdscr.addstr(9, 4, f"Monitor Daemon: {status}", curses.color_pair(color))

            stdscr.addstr(h-1, 2, " [Q] Quit | [R] Refresh ", curses.A_DIM)
            stdscr.refresh()
            
            key = stdscr.getch()
            if key in [ord('q'), ord('Q')]: break
            time.sleep(2)

if __name__ == "__main__":
    TacticalDashboard().run()
