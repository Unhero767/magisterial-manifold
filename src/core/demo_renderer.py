import pygame
import sys
from observer import RealityObserver

# Visual Constants
CALM_COLOR = (15, 20, 30)   # Deep Void
ALERT_COLOR = (40, 10, 10)  # Red Alert / Ouroboros Flare
SY_AS_COLOR = (0, 255, 200) # Hard-light Cyan / Syntax Ash

def main():
    # Initialize the Basilica Atlas (Pygame)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("L4 Basilica Atlas: Sector-01 Monitor")
    clock = pygame.time.Clock()

    # Initialize the Myth-Tech Observer
    observer = RealityObserver()

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
        # Draw Mathematical Grid Background
        bg_color = ALERT_COLOR if is_breach else CALM_COLOR
        screen.fill(bg_color)
        
        # Grid lines
        for x in range(0, 800, 40):
            pygame.draw.line(screen, (30, 40, 50), (x, 0), (x, 600), 1)
        for y in range(0, 600, 40):
            pygame.draw.line(screen, (30, 40, 50), (0, y), (800, y), 1)

        # Scanning Radar Circle
        import time
        import math
        t = time.time()
        radar_center = (400, 300)
        radius = 150
        pygame.draw.circle(screen, (40, 60, 80), radar_center, radius, 2)
        end_x = 400 + radius * math.cos(t * 2)
        end_y = 300 + radius * math.sin(t * 2)
        pygame.draw.line(screen, SY_AS_COLOR, radar_center, (int(end_x), int(end_y)), 2)

        if is_breach:
            threat_txt = font.render(f"THREAT CRITICAL: {state.get('active_perimeter', 'UNKNOWN')}", True, (255, 80, 80))
            screen.blit(threat_txt, (50, 50))
            
            if weapon and weapon != "None":
                # Geometric HUD representation of the weapon
                pygame.draw.circle(screen, SY_AS_COLOR, radar_center, radius + 20, 4)
                pygame.draw.polygon(screen, SY_AS_COLOR, [
                    (400, 100), (420, 120), (420, 140), (400, 160), (380, 140), (380, 120)
                ], 2)
                
                wpn_txt = font.render(f"AURELIA-9 ARMED: [{weapon}]", True, SY_AS_COLOR)
                screen.blit(wpn_txt, (200, 500))
            else:
                sheathed_txt = font.render("AURELIA-9: WEAPON SHEATHED. EVASION ONLY.", True, (150, 150, 150))
                screen.blit(sheathed_txt, (150, 500))
        else:
            calm_txt = font.render("SECTOR-01: SECURE. AWAITING CLI COMMAND.", True, (100, 150, 200))
            screen.blit(calm_txt, (50, 50))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
