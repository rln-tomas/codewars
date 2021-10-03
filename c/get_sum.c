int get_sum(int a, int b){
    int i,initial, final, result = 0; 
    if (a == b) return a; 
    if (a > b) {
        initial = b; 
        final = a; 
    } else{
        initial = a; 
        final = b; 
    }    
    for (i =initial; i <= final; i++){
        result += i; 
    }
    return result; 
}