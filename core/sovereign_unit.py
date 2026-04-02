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
