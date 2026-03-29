import pygame
import json
import os

class RealityObserver:
    def __init__(self, state_path="src/data/reality_state.json"):
        self.state_path = state_path
        self.last_modified_time = 0
        self.current_state = {}

    def poll_ledger(self):
        """Checks if the ml-logic CLI has updated the state file."""
        if not os.path.exists(self.state_path):
            return False

        mtime = os.path.getmtime(self.state_path)
        
        if mtime > self.last_modified_time:
            self.last_modified_time = mtime
            try:
                with open(self.state_path, "r") as f:
                    self.current_state = json.load(f)
                return True
            except json.JSONDecodeError:
                pass 
        return False
