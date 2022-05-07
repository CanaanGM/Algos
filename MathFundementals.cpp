
#include <iostream>
//  prime numbers
bool isPrime(int number){
    if (number <= 1  ) return false;
    for (int i = 2;  i < number; i++ )
        if(number % i == 0) return false;

    return true;
}

// prime factorization
int f[100], expo[100], len ;
void primeFactorization(int number){
    int divisor = 2;
    while ((1LL * divisor) * divisor <= number && number>1)
    {
        int k = 0;
        while (number % divisor == 0){
            k++;
            number /= divisor;
        }
        if (k > 0){
            len++;
            f[len] = divisor;
            expo[len] = k;
        }
    }
    if (number > 1){
        f[len] = number;
        expo[len] = 1;
    }
    
}

int main(){
    primeFactorization(13);
    for(int i = 1; i <= len; i++){

    std::cout<< f[i] << " " << expo[i] <<"\n";
    }
   std::cout<<isPrime(1);
    return 0;
}