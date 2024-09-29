#include <stdio.h>
int n;
int main()
{
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        for (int j=n;j<i-1;j++) {
            printf(" ");
        }
        for (int k=0;k<2*i-1;k++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}