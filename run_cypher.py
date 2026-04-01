from neo4j import GraphDatabase
import os

class LoomRunner:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def seed_manifold(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            print("--- [LOOM] Query Executed. The grain is set. ---")
            return result

if __name__ == "__main__":
    # Standard local Neo4j defaults; adjust if using a different port/auth
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "password" # Ensure this matches your local Neo4j credentials

    loom = LoomRunner(URI, USER, PASSWORD)
    
    # Seeding: The Awakening in the Glitch-Wastes (Sovereign Bind)
    seed_query = """
    MERGE (a:Archetype {name: 'Sovereign', effective_kappa: 0.82})
    CREATE (e:Event {
        name: 'The Awakening in the Glitch-Wastes',
        description: 'You emerge from the ash, the Braided Lead of your logic still warm.',
        base_tension: 0.3
    })
    MERGE (a)-[:BINDS {initial_weight: 0.3}]->(e)
    RETURN e.name as Event;
    """
    
    loom.seed_manifold(seed_query)
    loom.close()
