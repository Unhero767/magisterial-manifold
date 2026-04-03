import { clampToBoundary, normalizeVec2, insideBoundary, R36, type Vec2 } from "../manifold/r36_topology";

describe("R36 Topology Module", () => {
  describe("R36 constant", () => {
    test("boundary should be 36", () => {
      expect(R36.boundary).toBe(36);
    });
  });

  describe("clampToBoundary function", () => {
    test("clamps values greater than boundary to boundary", () => {
      expect(clampToBoundary(50)).toBe(R36.boundary);
    });

    test("clamps values less than negative boundary to negative boundary", () => {
      expect(clampToBoundary(-50)).toBe(-R36.boundary);
    });

    test("returns value if within boundary", () => {
      expect(clampToBoundary(10)).toBe(10);
      expect(clampToBoundary(-10)).toBe(-10);
      expect(clampToBoundary(0)).toBe(0);
    });

    test("throws error if value is not finite", () => {
      expect(() => clampToBoundary(Infinity)).toThrow("value must be finite");
      expect(() => clampToBoundary(NaN)).toThrow("value must be finite");
    });
  });

  describe("normalizeVec2 function", () => {
    test("clamps x and y components to boundary", () => {
      const input: Vec2 = { x: 50, y: -50 };
      const normalized = normalizeVec2(input);
      expect(normalized.x).toBe(R36.boundary);
      expect(normalized.y).toBe(-R36.boundary);
    });

    test("does not change vector if components are within boundary", () => {
      const input: Vec2 = { x: 10, y: -10 };
      const normalized = normalizeVec2(input);
      expect(normalized.x).toBe(10);
      expect(normalized.y).toBe(-10);
    });
  });

  describe("insideBoundary function", () => {
    test("returns true for points inside or on the boundary", () => {
      expect(insideBoundary({ x: 0, y: 0 })).toBe(true);
      expect(insideBoundary({ x: R36.boundary, y: R36.boundary })).toBe(true);
      expect(insideBoundary({ x: -R36.boundary, y: -R36.boundary })).toBe(true);
    });

    test("returns false for points outside the boundary", () => {
      expect(insideBoundary({ x: R36.boundary + 1, y: 0 })).toBe(false);
      expect(insideBoundary({ x: 0, y: -R36.boundary - 1 })).toBe(false);
      expect(insideBoundary({ x: R36.boundary + 10, y: R36.boundary + 10 })).toBe(false);
    });
  });
});
