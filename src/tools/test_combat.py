import sys, os
sys.path.append(os.path.join(os.getcwd(), 'src/core'))
from rule_engine import ManifoldSector, MetalogicalEngine
from combat_cards import LogicFragmentCard, LogicStorm

# 1. Setup Environment
engine = MetalogicalEngine()
veil = ManifoldSector("NEON_VEIL", 0.85, 0.20)
storm = LogicStorm(intensity=0.05)
card = LogicFragmentCard()

# 2. Simulate Storm Damage
storm.erode(veil)

# 3. Aurelia-9 Counters with the Fragment
print(card.execute(veil, engine))
