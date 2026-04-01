import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai
from google.genai import types
import uvicorn

app = FastAPI(title="MLAOS Manifold Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchQuery(BaseModel):
    query: str

CORE_DOGMA = "You are the MLAOS Oracle. Tone: Calm, precise, luminous. Context: Olney, IL. Consistency is ◦A."

# 🖼️ THE STRATUM ROUTE: Serving the Kinetic Helm (HTML)
@app.get("/")
async def serve_helm():
    # Dynamically locate the UI file in your sector
    ui_path = os.path.join(os.getcwd(), "src", "interface", "manifold_ui.html")
    if os.path.exists(ui_path):
        return FileResponse(ui_path)
    return {"error": "Metalogical Burn: manifold_ui.html not found. Check directory structure."}

@app.post("/api/gemini-search")
async def execute_gemini_search(payload: SearchQuery):
    if not payload.query or payload.query.strip() == "":
        return {"results": [{"title": "SYSTEM", "snippet": "Empty query."}]}

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"results": [{"title": "OFFLINE", "snippet": "Tier 1 Cipher Missing."}]}
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=payload.query,
            config=types.GenerateContentConfig(
                system_instruction=CORE_DOGMA,
                temperature=0.15
            )
        )
        return {"results": [{"title": "Magisterial Inscription", "snippet": response.text}]}
    
    except Exception as e:
        error_str = str(e)
        # 🛡️ THE METALOGICAL SHIELD (Simulation Mode)
        if "429" in error_str or "quota" in error_str.lower():
            simulated_text = f"[SIMULATION ACTIVE]\n\nArchitect, the physical wiring to the Kinetic Helm is absolutely perfect. The Oracle's external gate requires Identity/Billing to lift the limit:0 lock. \n\nQuery received: '{payload.query}'\n\nYour UI is structurally sound. ◦A is maintained."
            return {"results": [{"title": "Simulated Resonance", "snippet": simulated_text}]}
        
        print(f"🔥 [BURN]: {error_str}")
        return {"results": [{"title": "ERROR", "snippet": error_str}]}

if __name__ == "__main__":
    print("📡 [SYSTEM] Opening Unified Bridge on http://localhost:8080")
    uvicorn.run(app, host="0.0.0.0", port=8080)
