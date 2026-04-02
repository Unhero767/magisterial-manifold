.PHONY: help up down logs test shell clean docker-build prod-up prod-down prod-logs

help:
	@echo "Magisterial Manifold - Available Commands"
	@echo ""
	@echo "Development:"
	@echo "  make up              - Start dev environment (Neo4j + App)"
	@echo "  make down            - Stop all containers"
	@echo "  make logs            - View application logs"
	@echo "  make test            - Run test suite"
	@echo "  make shell           - Access application shell"
	@echo ""
	@echo "Database:"
	@echo "  make neo4j-shell     - Connect to Neo4j console"
	@echo "  make reset-db        - Reset database (dev only)"
	@echo ""
	@echo "Production:"
	@echo "  make prod-up         - Start production stack"
	@echo "  make prod-down       - Stop production"
	@echo "  make prod-logs       - View production logs"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build    - Build Docker image"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean           - Remove containers and volumes"

up:
	docker compose -f docker-compose.dev.yml up -d
	docker compose -f docker-compose.dev.yml logs -f manifold

down:
	docker compose -f docker-compose.dev.yml down

logs:
	docker compose -f docker-compose.dev.yml logs -f manifold

test:
	docker compose -f docker-compose.dev.yml --profile test up test

shell:
	docker compose -f docker-compose.dev.yml exec manifold bash

neo4j-shell:
	docker compose -f docker-compose.dev.yml exec neo4j cypher-shell -u neo4j -p magisterium_password_dev

reset-db:
	docker compose -f docker-compose.dev.yml down -v
	docker compose -f docker-compose.dev.yml up -d neo4j
	@echo "Waiting for Neo4j to be ready..."
	sleep 5
	docker compose -f docker-compose.dev.yml exec -T neo4j cypher-shell -u neo4j -p magisterium_password_dev "MATCH (n) DETACH DELETE n;"

prod-up:
	docker compose -f docker-compose.prod.yml up -d

prod-down:
	docker compose -f docker-compose.prod.yml down

prod-logs:
	docker compose -f docker-compose.prod.yml logs -f manifold

docker-build:
	docker build -t magisterial-manifold:latest .

clean:
	docker compose -f docker-compose.dev.yml down -v
	docker compose -f docker-compose.prod.yml down -v
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

.DEFAULT_GOAL := help
