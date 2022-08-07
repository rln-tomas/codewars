const assert = require("chai").assert;
const guessBlue = require('../guessBlue');

describe("GuessBlue tests", () => {
    it("test", () => {
        assert.equal(guessBlue(5, 5, 2, 3), 0.6);
        assert.equal(guessBlue(5, 7, 4, 3), 0.2);
        assert.equal(guessBlue(12, 18, 4, 6), 0.4);
    });
});
