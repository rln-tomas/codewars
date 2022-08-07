const assert = require("chai").assert;
const mergeArrays = require('../mergeArrays');

describe("Tests MergeArrays", () => {
  it("test", () => {
    assert.deepEqual(mergeArrays([1,2,3,4], [5,6,7,8]), [1,2,3,4,5,6,7,8], "Basic tests");
    assert.deepEqual(mergeArrays([1,3,5,7,9], [10,8,6,4,2]), [1,2,3,4,5,6,7,8,9,10], "Basic tests");
    assert.deepEqual(mergeArrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12]), [1,2,3,4,5,7,9,10,11,12], "Basic tests");
  });
});