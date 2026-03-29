import json
import os

class MissionVault:
    def __init__(self, path="src/data/mission_vault.json"):
        self.path = path
        if not os.path.exists("src/data"):
            os.makedirs("src/data")

    def anchor_mission(self, mission_data):
        missions = self.load_all()
        missions[mission_data["mission_id"]] = mission_data
        with open(self.path, "w") as f:
            json.dump(missions, f, indent=4)
        return f"[ MISSION ANCHORED ]: {mission_data['mission_id']} is live in the grid."

    def load_all(self):
        if not os.path.exists(self.path): return {}
        with open(self.path, "r") as f:
            return json.load(f)
