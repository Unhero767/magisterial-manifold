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
