import pygame
import sys
from observer import RealityObserver

# Initialize the Basilica Atlas (Pygame)
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("L4 Basilica Atlas: Sector-01 Monitor")
clock = pygame.time.Clock()

# Initialize the Myth-Tech Observer
observer = RealityObserver()

# Visual Constants
CALM_COLOR = (15, 20, 30)   # Deep Void
ALERT_COLOR = (40, 10, 10)  # Red Alert / Ouroboros Flare
SY_AS_COLOR = (0, 255, 200) # Hard-light Cyan / Syntax Ash

# Terminal-style Font
font = pygame.font.SysFont("Courier", 24, bold=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Poll the L1 Memory Spine (JSON)
    observer.poll_ledger()

    # 2. Extract Paraconsistent State Variables
    state = observer.current_state
    is_breach = state.get("encounter_active", False)
    weapon = state.get("aurelia_loadout", {}).get("weapon_drawn", "None")

    # 3. Render the Reality State
    if is_breach:
        screen.fill(ALERT_COLOR)
        threat_txt = font.render(f"THREAT CRITICAL: {state.get('active_perimeter', 'UNKNOWN')}", True, (255, 80, 80))
        screen.blit(threat_txt, (50, 50))
        
        if weapon == "Sy-As_Edge":
            # Draw Aurelia-9's Myth-Tech Weapon (Placeholder: Glowing Blade)
            pygame.draw.rect(screen, SY_AS_COLOR, (400, 200, 20, 200))
            pygame.draw.polygon(screen, SY_AS_COLOR, [(400, 200), (410, 160), (420, 200)]) # Sword Tip
            
            wpn_txt = font.render("AURELIA-9 ARMED: Sy-As_Edge [100% Magnetism]", True, SY_AS_COLOR)
            screen.blit(wpn_txt, (200, 420))
    else:
        screen.fill(CALM_COLOR)
        calm_txt = font.render("SECTOR-01: SECURE. AWAITING CLI COMMAND.", True, (100, 150, 200))
        screen.blit(calm_txt, (50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
