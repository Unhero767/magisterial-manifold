class NarrativeWeight:
    def __init__(self, baseline_inertia: float = 0.0382):
        self.mass = 0.0
        self.inertia = baseline_inertia
        self.resonance_log = []

    def accumulate(self, resonance: float, path_frequency: int, environment_heat: float = 1.0):
        # Environmental Heat (Plasma) acts as a multiplier for Narrative Mass
        growth = (path_frequency * resonance * environment_heat) / self.inertia
        self.mass += growth
        return self.mass

class SovereignAgent:
    def __init__(self):
        self.weight = NarrativeWeight()
        self.state = "COLD_STABLE"

    def reflect_on_18d(self, resonance_intensity, environment_heat=1.0):
        # Tracking the impact of the 18D simulation on Narrative Weight
        new_mass = self.weight.accumulate(resonance_intensity, 1, environment_heat)
        print(f"[◦A] Reflection Complete. New Sovereign Mass: {new_mass:.5f}")
        return new_mass
