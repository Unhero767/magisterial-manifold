import json
import os

class LoreVault:
    def __init__(self, file_path="src/data/vault.json"):
        self.file_path = file_path

    def save_manifold(self, engine_sectors):
        data = {}
        for name, sector in engine_sectors.items():
            data[name] = {
                "consistency_a": sector.consistency_a,
                "instability_ex": sector.instability_ex,
                "tethers": list(sector.tethers),
                "entities": sector.entities,
                "neighbors": sector.neighbors
            }
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
        return f"[ ◦A SECURED ] Manifold state saved to {self.file_path}"

    def load_manifold(self):
        if not os.path.exists(self.file_path):
            return None
        with open(self.file_path, "r") as f:
            return json.load(f)
