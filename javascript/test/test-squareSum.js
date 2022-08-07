const assert = require("chai").assert;
const squareSum = require('../squareSum');

describe("Tests SquareSum", () => {
    it("test", () => {
      assert.strictEqual(squareSum([1,2]), 5);
      assert.strictEqual(squareSum([0, 3, 4, 5]), 50);
      assert.strictEqual(squareSum([]), 0);
    });
  });