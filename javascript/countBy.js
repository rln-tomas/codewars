function countBy(x, n){
    return Array.from({
          length: n
      }, (v, k) => (k+1)*x );
}

module.exports = countBy;
