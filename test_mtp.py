from src.core.rule_engine import RuleEngine

def ritual_log(protocol, message):
    print(f"[{protocol.upper()}] {message}")

def test_mtp_resonance():
    engine = RuleEngine()
    intent_int = {'return_type': "<class 'int'>"}

    print("🧪 [SCENARIO 2] Testing Type-Bleed (String vs Int)...")
    try:
        # This intentionally violates the MTP constraint 
        engine.enforce_ground_truth(intent_int, "forty-two")
    except TypeError as e:
        # The engine successfully protects the CORE from logic-bleed 
        print(f"✅ PURGE SUCCESSFUL: {e}")
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    test_mtp_resonance()
