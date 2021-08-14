#include<stdio.h>
int main()
{   int k =0;
    double b = k++ + ++k +k--;
    printf("%d",k);
    return 0;
}