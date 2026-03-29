from src.core.rule_engine import RuleEngine

def professional_sync():
    # Initialize the Magisterial Engine
    engine = RuleEngine()
    
    # Raw Data from your "MTP Logic Bridge" Analysis [cite: 6, 8]
    raw_fragments = {
        "MTP_Paradigm": "Transition from deterministic to neuro-integrated architectures.",
        "Abstraction_Gap": "The friction between code semantics and natural language.",
        "Semantic_Richness": "Function signatures and type annotations as carriers of intent."
    }
    
    # The Neuro-Integrated Ingestion Ritual [cite: 13, 14]
    try:
        # Pass the inherently rich fragments through the RuleEngine
        engine.ingest_lore(raw_fragments)
        print("✅ [LORE_SYNC] Professional Ingestion Complete. ◦A: 1.0")
    except TypeError as e:
        # Trigger the Purge Protocol if logic-bleed is detected
        print(f"❌ [PURGE] Semantic Mismatch: {e}")
    except AttributeError:
        print("❌ [ERROR] Ensure 'ingest_lore' is properly inscribed in src/core/rule_engine.py.")

if __name__ == "__main__":
    professional_sync()
