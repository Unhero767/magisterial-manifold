# Multi-stage build for Magisterial Manifold
# Neuro-integrated MTP (Meaning-Typed Programming) architecture with Neo4j

# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /build

# Install system dependencies for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .
COPY . .

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Install project as editable for development
RUN pip install --no-cache-dir -e . 2>/dev/null || \
    pip install --no-cache-dir neo4j

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Install only runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/neo4j/data /app/neo4j/logs /app/reports /app/hall_of_records

# Create __init__.py files for Python packages
RUN touch /app/src/__init__.py \
    && touch /app/src/core/__init__.py \
    && touch /app/src/tools/__init__.py \
    && touch /app/src/interface/__init__.py

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 7474 7687

# Default command runs the CLI
CMD ["python", "-m", "src.core.ml_cli"]
