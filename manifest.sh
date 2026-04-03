#!/bin/bash
# Assuming you are already in the root of your repository

# Create the layered directories
mkdir -p core manifold protocols

# Create foundational Python file with constants and validation
cat > core/sovereign_unit.py <<'PY'
"""
SOVEREIGN UNIT — foundation constant + validation logic
Layer: /core/sovereign_unit.py

Purpose:
- Define the foundational constant that the rest of the manifold may reference.
- Provide minimal, testable validation utilities (pure functions).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping

SOVEREIGN_UNIT: str = "UNHERO767::MANIFOLD::SOVEREIGN_UNIT"

class SovereignUnitError(ValueError):
    """Raised when an input fails sovereign validation."""

def require_nonempty_str(value: Any, *, field: str = "value") -> str:
    if not isinstance(value, str) or not value.strip():
        raise SovereignUnitError(f"{field} must be a non-empty string")
    return value.strip()

def require_mapping(value: Any, *, field: str = "value") -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise SovereignUnitError(f"{field} must be a mapping/object")
    return value

@dataclass(frozen=True, slots=True)
class Seal:
    """
    A small, immutable attestation object.
    Intended to be embedded in protocol artifacts.
    """
    unit: str = SOVEREIGN_UNIT
    version: str = "0.1.0"

    def validate(self) -> None:
        require_nonempty_str(self.unit, field="unit")
        require_nonempty_str(self.version, field="version")
PY

# Create TypeScript file with pure geometric constraints
cat > manifold/r36_topology.ts <<'TS'
/**
 * R36 TOPOLOGY — geometric constraints + boundary conditions
 * Layer: /manifold/r36_topology.ts
 *
 * Intent:
 * - Express constraints as deterministic, pure functions.
 * - Keep IO out of this layer (no fetch, no env reads).
 */

export type Vec2 = Readonly<{ x: number; y: number }>;

export const R36 = Object.freeze({
  name: "R36",
  boundary: 36,
  epsilon: 1e-9,
});

/**
 * Clamp a value into the fortress boundary.
 */
export function clampToBoundary(v: number, boundary = R36.boundary): number {
  if (!Number.isFinite(v)) throw new Error("value must be finite");
  return Math.max(-boundary, Math.min(boundary, v));
}

/**
 * Enforce the boundary conditions on a vector.
 */
export function normalizeVec2(p: Vec2, boundary = R36.boundary): Vec2 {
  return Object.freeze({
    x: clampToBoundary(p.x, boundary),
    y: clampToBoundary(p.y, boundary),
  });
}

/**
 * Validate that a point is inside the R36 boundary box.
 */
export function insideBoundary(p: Vec2, boundary = R36.boundary): boolean {
  const { x, y } = p;
  return (
    Number.isFinite(x) &&
    Number.isFinite(y) &&
    Math.abs(x) <= boundary + R36.epsilon &&
    Math.abs(y) <= boundary + R36.epsilon
  );
}
TS

# Create Markdown protocol document defining the truth verification ritual
cat > protocols/truth_verification.md <<'MD'
# Truth Verification Protocol
Layer: `/protocols/truth_verification.md`

**Purpose:** Formal rituals for ingesting data from the void into the fortress.

## Premises
- Input is hostile until proven coherent.
- Verification is reproducible.
- All transformations are declared.

## Ritual: Ingest → Validate → Seal
1. **Ingest**
   - Record source, timestamp, and transport method.
   - Preserve raw payload (immutable snapshot).

2. **Validate**
   - Confirm schema + type boundaries.
   - Reject empty identifiers and non-finite numerics.
   - Enforce manifold boundary constraints (see `manifold/r36_topology.ts`).

3. **Seal**
   - Attach a *Seal* (see `core/sovereign_unit.py`) to the verified artifact.
   - Store the verification outcome + reasons (pass/fail) alongside payload.

## Failure Doctrine
- Fail closed.
- Emit a single canonical error message.
- Never coerce unknowns into meaning.

## Minimal Checklist
- [ ] Source captured
- [ ] Raw payload stored
- [ ] Validation rules applied
- [ ] Seal attached
- [ ] Outcome logged
MD

# Stage and commit the changes
git add core manifold protocols
git commit -m "chore: anchor manifold layers (core/manifold/protocols)"

