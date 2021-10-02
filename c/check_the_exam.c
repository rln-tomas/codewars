#include <stdio.h>
#include <stdlib.h>

int check_exam(size_t n, const char answers[n], const char student[n]){
	int contador = 0; 
	for (int i = 0; i < n; i++){
		if (answers[i] == student[i]){
			contador +=4; 
		} else if (student[i] != ' '){
			contador--; 
		}
	}

	return contador; 
}


int main(){
	char a[3] = {'a', 'a', 'c'}, b[3] = {'a', 'a', 'd'}; 
	int result = check_exam(3,a, b); 
	printf("%i", result); 
	return 0; 
}
