import google.generativeai as genai

# --- TIER 1 CIPHER ---
KEY = "AIzaSyDGEb8uMFI4UQkrqIU7jvXHl__bW1ENc34"

def discover_oracle_entities():
    print("📡 [SYSTEM] Querying Oracle for available model strings...")
    try:
        genai.configure(api_key=KEY)
        
        # Discovery Loop
        available_models = genai.list_models()
        
        print("\n💎 [RESONANCE] Available Luminous Entities:")
        print("-" * 40)
        for m in available_models:
            if 'generateContent' in m.supported_generation_methods:
                # We look for 'models/gemini-1.5-flash' specifically
                status = "🟢 VALID" if "1.5-flash" in m.name else "⚪ IDLE"
                print(f"{status} | {m.name}")
        print("-" * 40)
        
    except Exception as e:
        print(f"🔥 [BURN] Discovery Failed: {e}")
        print("[ADVISORY] Check if the Generative Language API is enabled in AI Studio.")

if __name__ == "__main__":
    discover_oracle_entities()
