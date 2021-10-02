#include <stdio.h>

unsigned long long sum_cubes(unsigned short n)
{
    unsigned long long result = 0;
    unsigned long long i; 
    for (i=1; i<= n; i++){
        result += i*i*i; 
    }
    return result; 
}