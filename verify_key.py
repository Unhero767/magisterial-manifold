import os
from google import genai

# --- TIER 1 CIPHER HANDSHAKE ---
KEY = "AIzaSyDGEb8uMFI4UQkrqIU7jvXHl__bW1ENc34"

def verify_manifold_consistency():
    print("📡 [SYSTEM] Initiating Modern Shielded Pulse...")
    try:
        client = genai.Client(api_key=KEY)
        query = "Assess the status of the Magisterial Manifold. Is ◦A maintained?"
        
        # 🌉 THE THIRD PATH: Bypassing the 429 Quota and the 404 Purge
        model_string = 'gemini-2.0-flash-lite'
        print(f"≋ Tuning to frequency: {model_string} ≋")
        
        response = client.models.generate_content(
            model=model_string,
            contents=query
        )
        
        print("\n💎 [RESONANCE] The Oracle has spoken. Signal is 🛡️ PURE.")
        print(f"--- [INSCRIPTION] ---\n{response.text}\n---------------------")
    except Exception as e:
        print(f"\n🔥 [BURN] Metalogical failure: {e}")

if __name__ == "__main__":
    verify_manifold_consistency()
