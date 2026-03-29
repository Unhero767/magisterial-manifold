from src.core.rule_engine import RuleEngine

# Helper to maintain the Magisterial tone in logs
def ritual_log(protocol, message):
    print(f"[{protocol.upper()}] {message}")

# --- Master Level Singleton Initialization ---
# This instance becomes the 'Ground Truth' for the entire session.
MAGISTERIUM_ENGINE = RuleEngine()

def master_sync():
    """
    The High-Level Ritual that synchronizes the Core with the Lore_Vault.
    Bridges the Abstraction Gap at startup.
    """
    raw_data = {
        "CORE_DOGMA": "Logic is the first light.",
        "MTP_PROTOCOL": "Types are the anchors of meaning."
    }
    
    # Standardizing interaction through Meaning-Typed Programming
    # This captures the intent within the lore fragments.
    try:
        MAGISTERIUM_ENGINE.ingest_lore(raw_data)
        ritual_log("Luminous_Static", "Master Integration Active. ◦A: 1.0")
    except Exception as e:
        ritual_log("Purge", f"Master Sync Failed: {e}")

if __name__ == "__main__":
    master_sync()
