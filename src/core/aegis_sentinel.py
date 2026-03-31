# PROTOCOL: TIER 1
# Aegis Sentinel: Threshold & Density Monitor

def monitor_mass(current_mass):
    """Checks the Logic Mass and enforces Density Laws."""
    print(f"🛡️ [SENTINEL] Current Logic Mass: {current_mass}")
    
    if current_mass >= 1000:
        print("⚠️ [SENTINEL] MILLENNIAL THRESHOLD ACTIVE.")
        return True
    return False

def check_density(file_path, line_count):
    """Enforces the Law of 30% (Max 300 lines per artifact)."""
    if line_count > 300:
        print(f"🔥 [DENSITY BURN] {file_path} is too massive ({line_count} lines).")
        return False
    return True
