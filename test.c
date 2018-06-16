#include <stdio.h>
#include <math.h>

int add(int a, int b)
{
    return (a + b);
}

int main(int argc, char const *argv[])
{
    int a, b;
    scanf("%d%d", &a, &b);
    printf("Hello World %d", a);
    printf("a + b = %d", a + b);
    return 0;
}

