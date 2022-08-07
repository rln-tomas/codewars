
// My first solution:
function squareSum(numbers){
    let sum = 0;
    numbers.forEach(n => {
        sum += n**2;
    });

    return sum;
}

// other solution:

function squareSum2(numbers) {
    return numbers.reduce((sum, n) => {
        return sum + n**2;
    }, 0);
}

module.exports = squareSum;