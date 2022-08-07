const countBy = require('../countBy');

const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;

describe("CountByX Tests",function(){
  it("test", () => {
    assert.deepEqual(countBy(1,10), [1,2,3,4,5,6,7,8,9,10], "Array does not match")
    assert.deepEqual(countBy(2,5), [2,4,6,8,10], "Array does not match")
  });
});