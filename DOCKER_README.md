# Magisterial Manifold - Containerized

A containerized neuro-integrated MTP (Meaning-Typed Programming) architecture with Neo4j graph database.

## 🏛️ Overview

The Magisterial Manifold is a system designed to bridge the gap between human intent and machine logic through:

- **Rule Engine** - Deterministic ground truth
- **Lore Vault** - Semantic richness and documentation
- **MTP Logic** - Bridge across the abstraction gap
- **Sovereign CLI** - Command interface (`magisterium`)

## 🚀 Quick Start

### Development

```bash
# Start services
make up

# View logs
make logs

# Run tests
make test

# Access Neo4j
make neo4j-shell

# Open shell in app
make shell
```

### Production

```bash
# Copy and configure environment
cp .env.example .env
nano .env

# Start production
make prod-up

# View logs
make prod-logs

# Stop production
make prod-down
```

## 📁 Project Structure

```
.
├── Dockerfile                 # Multi-stage build
├── docker-compose.dev.yml     # Development environment
├── docker-compose.prod.yml    # Production deployment
├── .dockerignore               # Build optimization
├── .env.example                # Configuration template
├── Makefile                    # CLI commands
├── README.md                   # This file
│
├── src/
│   ├── core/                   # Core modules
│   │   ├── ml_cli.py          # Main CLI
│   │   ├── rule_engine.py     # Rule validation
│   │   ├── lore_vault.py      # Semantic vault
│   │   └── ...
│   ├── tools/                  # Tools and utilities
│   └── interface/              # Interface modules
│
├── archetypes/                 # Archetype definitions
├── protocols/                  # Protocol specifications
├── data/                       # Data files
├── reports/                    # Generated reports
├── hall_of_records/            # Record storage
│
├── run_cypher.py              # Neo4j query runner
├── sync_lore.py               # Lore synchronization
├── verify_key.py              # Key verification
└── test_mtp.py                # MTP tests
```

## 🐳 Services

### Development (docker-compose.dev.yml)

- **neo4j** - Neo4j 5.13 graph database (port 7474, 7687)
- **manifold** - Main application (interactive)
- **test** - Test runner (profile: test)

### Production (docker-compose.prod.yml)

- **neo4j** - Neo4j with larger memory allocation
- **manifold** - Production application
- **test** - Batch test runner (profile: test)

## 🔧 Configuration

### Environment Variables

```bash
cp .env.example .env
nano .env
```

Key variables:

```env
NEO4J_PASSWORD=magisterium_dev
NEO4J_URI=bolt://neo4j:7687
NEO4J_USER=neo4j

MTP_MODE=development
LOG_LEVEL=INFO
SANDBOX_MODE=true
RULE_ENGINE_ENABLED=true
LORE_VAULT_ENABLED=true
```

## 📊 Technology Stack

- **Language**: Python 3.11
- **Database**: Neo4j 5.13 (Graph)
- **Architecture**: Neuro-integrated MTP
- **CLI**: Python Click/Typer style

## 🎯 Core Concepts

### Rule Engine (⚙️)
Validates all operations against defined rules. Prevents invalid state changes.

### Lore Vault (📚)
Semantic repository of docstrings and documentation. Extracted and indexed for intelligent processing.

### MTP Logic (⚖️)
Meaning-Typed Programming bridge between human intent and machine logic.

### Sovereign CLI (⚡)
The `magisterium` power word that wakes up and controls the system.

## 🗄️ Database

Neo4j stores:
- Archetypes (conceptual entities)
- Events (temporal facts)
- Bindings (relationships and weights)
- Narratives (story/logic structures)

### Connect to Database

```bash
make neo4j-shell

# Or directly
docker compose -f docker-compose.dev.yml exec neo4j cypher-shell
```

### Reset Database (Dev Only)

```bash
make reset-db
```

## 🧪 Testing

```bash
# Run tests
make test

# Or manually
docker compose -f docker-compose.dev.yml exec manifold python -m pytest tests/ -v
```

## 📈 Development Workflow

```bash
# 1. Start development
make up

# 2. Edit code (volumes mount source)
nano src/core/ml_cli.py

# 3. Changes reflect immediately

# 4. Run tests
make test

# 5. Access database
make neo4j-shell

# 6. View logs
make logs
```

## 🚀 Deployment

### Production Setup

```bash
# 1. Configure environment
cp .env.example .env
# Edit with production credentials
nano .env

# 2. Build image
make docker-build

# 3. Start production
make prod-up

# 4. Monitor
make prod-logs
```

### Kubernetes (Optional)

See DEPLOYMENT.md for K8s manifests.

## 📖 Documentation

- `README.md` - This file (overview)
- `architecture/` - System design documents
- `protocols/` - Protocol specifications
- Inline code comments

## 🔒 Security

✓ Non-root user execution (appuser)
✓ Multi-stage build
✓ Environment-based secrets
✓ Resource limits
✓ Health checks

## 🛠️ Troubleshooting

### Neo4j Won't Start

```bash
docker compose -f docker-compose.dev.yml logs neo4j

# Reset and restart
make reset-db
```

### Application Connection Error

```bash
# Check environment
cat .env

# Verify Neo4j is running
make neo4j-shell
```

### Clean Rebuild

```bash
make clean
make docker-build
make up
```

## 📞 Commands

All commands available via Makefile:

```bash
make help
```

## 👤 Author

Kenneth Dallmier (kennydallmier@gmail.com)

## 📄 License

See LICENSE file.
