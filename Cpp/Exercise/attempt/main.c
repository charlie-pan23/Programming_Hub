#include <stdio.h>

int fact(int n) {
    int sum = 1;
    if (n == 0 || n == 1) {
        return 1;
    }    //return n * fact(n - 1);
        for (int i = 2; i <= n; i++) {
            sum *= i;
    }
        return sum;
}

int main() {
        printf("%d\n", fact(3));
        printf("%d\n", fact(4));
        printf("%d\n", fact(1));
        return 0;
    }