const howManyYears = function(date1, date2){
    date1 = date1.split('/')[0] 
    date2 = date2.split('/')[0]
    return Math.abs((parseInt(date2) - parseInt(date1)))
}

console.log(howManyYears('1994/01/23', '1923/01/23'))