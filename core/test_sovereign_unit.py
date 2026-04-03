import pytest
from core.sovereign_unit import (
    SovereignUnitError,
    require_nonempty_str,
    require_mapping,
    Seal,
)

def test_require_nonempty_str_valid():
    assert require_nonempty_str("hello") == "hello"
    assert require_nonempty_str("  trimmed  ") == "trimmed"

def test_require_nonempty_str_invalid():
    with pytest.raises(SovereignUnitError):
        require_nonempty_str("")
    with pytest.raises(SovereignUnitError):
        require_nonempty_str("   ")
    with pytest.raises(SovereignUnitError):
        require_nonempty_str(None)

def test_require_mapping_valid():
    assert require_mapping({"key": "value"}) == {"key": "value"}

def test_require_mapping_invalid():
    with pytest.raises(SovereignUnitError):
        require_mapping("not a mapping")
    with pytest.raises(SovereignUnitError):
        require_mapping(123)

def test_seal_validate_pass():
    seal = Seal(unit="UNHERO767::MANIFOLD::SOVEREIGN_UNIT", version="0.1.0")
    seal.validate()  # Should not raise

def test_seal_validate_fail():
    from core.sovereign_unit import Seal
    seal = Seal(unit="", version="0.1.0")
    with pytest.raises(SovereignUnitError):
        seal.validate()
