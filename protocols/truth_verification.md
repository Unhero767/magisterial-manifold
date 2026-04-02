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
