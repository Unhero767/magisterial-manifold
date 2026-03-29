import json
import argparse
import os
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

VAULT_PATH = "src/data/vault.json"

def load_vault(path=VAULT_PATH):
    if not os.path.exists(path):
        # Create a dummy vault if none exists to prevent crash
        return {"CORE": {"consistency_a": 1.0, "instability_ex": 0.0, "neighbors": [], "entities": {}}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def filter_sectors(data, min_ca=None, max_ex=None):
    filtered = {}
    for name, sector in data.items():
        ca = sector.get("consistency_a", 0)
        ex = sector.get("instability_ex", 0)
        if (min_ca is None or ca >= min_ca) and (max_ex is None or ex <= max_ex):
            filtered[name] = sector
    return filtered

def generate_json_report(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"JSON report saved to {output_path}")

def generate_markdown_report(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    lines = [f"# Manifold Sector Report - {datetime.now().isoformat()}\n"]
    for name, sector in sorted(data.items()):
        ca = sector.get("consistency_a", 0)
        ex = sector.get("instability_ex", 0)
        neighbors = ", ".join(sector.get("neighbors", [])) or "None"
        entities = sector.get("entities", {})
        top_entity = max(entities.items(), key=lambda x: x[1])[0] if entities else "None"
        lines.append(f"## {name}\n- Consistency (◦A): {ca:.3f}\n- Instability (Ex◦): {ex:.3f}\n- Neighbors: {neighbors}\n- Top Entity: {top_entity}\n")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Markdown report saved to {output_path}")

def visualize_manifold(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    G = nx.Graph()
    for name, sector in data.items():
        ca = sector.get("consistency_a", 0)
        ex = sector.get("instability_ex", 0)
        G.add_node(name, consistency=ca, instability=ex)
        for neighbor in sector.get("neighbors", []):
            if neighbor in data:
                G.add_edge(name, neighbor)

    if not G.nodes():
        print("No nodes to visualize.")
        return

    pos = nx.spring_layout(G, seed=42)
    node_colors = [G.nodes[n]['consistency'] for n in G.nodes]
    node_sizes = [5000 * (1 - G.nodes[n]['instability']) for n in G.nodes]

    plt.figure(figsize=(12, 9))
    nodes = nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=plt.cm.viridis, node_size=node_sizes)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_color="white", font_weight="bold")
    plt.colorbar(nodes, label="Consistency (◦A)")
    plt.title("Manifold Sector Network Visualization")
    plt.axis('off')
    plt.savefig(output_path, facecolor='#07080b')
    plt.close()
    print(f"Manifold visualization saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Manifold Automation: Reports and Visualization")
    parser.add_argument("--min-ca", type=float, help="Minimum consistency (◦A) to include")
    parser.add_argument("--max-ex", type=float, help="Maximum instability (Ex◦) to include")
    parser.add_argument("--json-out", default="reports/sector_report.json", help="JSON report output path")
    parser.add_argument("--md-out", default="reports/sector_report.md", help="Markdown report output path")
    parser.add_argument("--viz-out", default="reports/manifold_graph.png", help="Visualization output path")
    args = parser.parse_args()

    data = load_vault()
    filtered = filter_sectors(data, args.min_ca, args.max_ex)
    generate_json_report(filtered, args.json_out)
    generate_markdown_report(filtered, args.md_out)
    visualize_manifold(filtered, args.viz_out)

if __name__ == "__main__":
    main()
