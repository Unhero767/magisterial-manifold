class Archetype:
    def __init__(self, name, kappa_offset=0.0):
        self.name = name
        self.base_kappa = 0.62
        self.effective_kappa = self.base_kappa + kappa_offset

    def validate_consistency(self, current_resonance):
        return abs(current_resonance) * self.effective_kappa <= 1.0

class Sovereign(Archetype):
    def __init__(self):
        super().__init__("The Sovereign", kappa_offset=0.2)
        self.structural_role = "Anchor"

class Trickster(Archetype):
    def __init__(self):
        super().__init__("The Trickster", kappa_offset=-0.15)
        self.structural_role = "Braid-Breaker"

MANIFEST = {
    "SOVEREIGN": Sovereign(),
    "TRICKSTER": Trickster()
}
