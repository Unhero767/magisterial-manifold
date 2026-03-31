import os

TAXONOMY = {
    "aletheic_matrix.py": "🏛️ [TIER 0] Fundamental Truth Engine",
    "ml_cli.py": "📡 [TIER 1] Sovereign Command Interface",
    "aegis_sentinel.py": "🛡️ [TIER 1] Perimeter Defense",
    "rule_engine.py": "⚖️ [TIER 1] Axiomatic Processor",
    "observer.py": "👁️ [TIER 2] Environmental Monitor",
    "master_weaver.py": "🕸️ [TIER 2] Relationship Orchestrator",
    "logic_storm.py": "🌩️ [TIER 3] Chaotic Processing Unit",
    "lore_vault.py": "📚 [TIER 3] Narrative Persistence",
    "mission_vault.py": "📦 [STRATUM] Objective Archive",
    "ex_recovery.py": "🔥 [EMERGENCY] Ex∘ Containment",
    "layer_alpha.py": "💎 [STRATUM] Initial Logic Base"
}

def generate_map():
    print("🌌 --- MANIFOLD TOPOLOGY MAP --- 🌌")
    path = os.path.expanduser("~/magisterial-manifold/src")
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}📂 {os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith(".py"):
                label = TAXONOMY.get(f, "📄 [UNCLASSIFIED] Raw Logic Artifact")
                print(f"{sub_indent}{label} -> {f}")

if __name__ == "__main__":
    generate_map()
