import json
import os
import re
from typing import List, Dict, Tuple

class AletheicMatrix:
    """
    The Aletheic Query Matrix.
    Performs semantic proximity searches across the Manifold's topological ledger.
    """
    def __init__(self, vault_path="src/data/vault.json"):
        self.vault_path = vault_path
        self.stop_words = {"what", "is", "the", "a", "of", "in", "and", "to", "how", "where", "are"}

    def _extract_keywords(self, query: str) -> set:
        words = re.findall(r'\b\w+\b', query.lower())
        return {w for w in words if w not in self.stop_words}

    def interrogate(self, query: str) -> str:
        if not os.path.exists(self.vault_path):
            return "[!] THE VAULT IS EMPTY. No truth to reveal."

        with open(self.vault_path, "r") as f:
            manifold = json.load(f)

        keywords = self._extract_keywords(query)
        if not keywords:
            return "[?] Query lacks semantic weight. Ask a more specific question."

        results: List[Tuple[float, str]] = []

        # Scan the grid for semantic resonance
        for sector_name, data in manifold.items():
            for entity_id, weight in data.get("entities", {}).items():
                # In a true MT-Runtime, this uses high-dimensional embeddings.
                # Here, we simulate resonance via keyword overlap and string proximity.
                score = 0.0
                target_text = f"{sector_name} {entity_id}".lower()
                
                for kw in keywords:
                    if kw in target_text:
                        score += 1.0
                
                if score > 0:
                    resonance = min(1.0, score / len(keywords))
                    revelation = (
                        f"   - [Entity]: {entity_id} (Sector: {sector_name})\n"
                        f"     [◦A]: {data['consistency_a']:.3f} | [Weight]: {weight}"
                    )
                    results.append((resonance, revelation))

        if not results:
            return f"[ 0 ] Resonance. The concept '{query}' does not exist in the current timeline."

        # Sort by highest resonance and return the top 3 revelations
        results.sort(key=lambda x: x[0], reverse=True)
        
        output = f"\n[ ALETHEIC REVELATION ] Translating query: '{query}'...\n"
        for i, (res, rev) in enumerate(results[:3]):
            output += f"\n{i+1}. Resonance {res*100:.1f}%\n{rev}\n"
            
        return output

if __name__ == "__main__":
    matrix = AletheicMatrix()
    print(matrix.interrogate("Where is the algorithm?"))
