#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>


const int base = 100000000;

typedef struct
{
    int a[40];
} uint1024_t;
 
 uint1024_t from_uint(unsigned int x)
{
    uint1024_t b;
    int i = 0;
    if (x == 0)
    {
        b.a[i] = 0;
        i++;
        while (i != 40)
        {
            b.a[i] = -1;
            i++;
        }
    }
    else
        while (i != 40)
        {
            if (x != 0)
            {
                b.a[i] = x % base;
                x /= base;
            }
            else 
            {
                b.a[i] = -1;  
            }
            i++;
        }
    return b;
}

void printf_value(uint1024_t x)
{
    int proof = 0;
    for (int i = 0; i <= 39; i++)
        if (x.a[i] != -1 && x.a[i] != 0){
            proof = 1;
            break;
        }
    if (proof == 1)
    {
    int flag = 1;
    for (int i = 39; i>=0; i--)
        if (x.a[i] != -1)
        {
            if (flag != 1)
            {
                int len_of_digit;
                if (x.a[i] == 0)
                    len_of_digit = 1;
                else
                    len_of_digit = floor(log10(abs(x.a[i]))) + 1;
                for (int j = 0; j < (8 - len_of_digit); j++)
                    printf ("0");
                printf ("%d", x.a[i]);
            }
            else
            {
                flag = 0;
                if (x.a[i] != 0)
	                printf ("%d", x.a[i]);
            }
        }
    }
    else
        printf("0");

}

uint1024_t subtr_op(uint1024_t x, uint1024_t y) 
{
    int flag = 0;
    for (int i = 0; i <= 39; i++)
    {
        if(flag == 1)
        {
            if (x.a[i] >= 1)
            {
                x.a[i] -= 1;
                flag = 0;
            }
            else
            {
                x.a[i] += 99999999;
            }
        }
        if (x.a[i] != -1 && y.a[i] != -1)
        {
	        if (x.a[i] >= y.a[i])
            {
                x.a[i] -= y.a[i];
            }
            else
            {
                x.a[i] += base - y.a[i];
                flag = 1;
            }
                
        }
    }
    return x;
}

uint1024_t add_op(uint1024_t x, uint1024_t y)
{
    int flag = 0;
    for (int i = 0; i <= 39; i++)
    {
            if (x.a[i] != -1 && y.a[i] != -1)
            {
	            x.a[i] += y.a[i];
                if (flag == 1)
                {
                    x.a[i] += 1;
                    flag = 0;
                }
                if (x.a[i] / base >= 1)
                {
                    flag = 1;
                    x.a[i] = x.a[i] % base;
                }
            }
            else if (x.a[i] + y.a[i] > -2)
            {
                if (x.a[i] < y.a[i])
                {
                    x.a[i] = y.a[i];    
                }
                if (flag == 1)
                    {
                    x.a[i] += 1;
                    flag = 0;
                    }
                if (x.a[i] / base >= 1)
                    {
                    flag = 1;
                    x.a[i] = x.a[i] % base;
                    }
                    
            }
            else
            {
                if (flag == 1)
                    x.a[i] = 1;
                    flag = 0;
            }
    }
    return x;
}

void scanf_value(uint1024_t *x)
{
    char *str;
    str = (char *)(malloc(315 * sizeof(char)));
    scanf("%s", str);
    for (int i = 0; i <= 39; i++)
    {
        x->a[i] = -1;
    }
    int n = strlen(str);
    for (int i = 0; i <= 39; i++)
    {
        char substring[8] = "00000000";
        int flag = 0;
        for (int j = 7; j >= 0; j--)
        {
            if (n >= 1)
            {
                flag = 1;
                substring[j] = str[n - 1];
                n -= 1;
            }
            else
                break;

        }
        if (flag == 1)
        {
            x -> a[i] = (int) atoi (substring);
        }

    }
}

uint1024_t mult_op(uint1024_t x, uint1024_t y)
{
    uint1024_t z;
    for (int i = 0; i <= 39; i++)
    {
        z.a[i] = 0;
    }
     
    for (int i = 0; i <= 39; i++)
    {
        long long remains = 0;
        for (int j = 0; i + j <= 39; j++)
        {
            if (x.a[i] != -1 && y.a[j] != -1){
            long long res = (long long)(z.a[i + j]) + ((long long)(x.a[i]) * (long long)(y.a[j])) + remains;
            z.a[i + j] = (int)(res % (long long)(base));
            remains = (long long)(res / base);
            }
            else if (remains != 0)
            {
                z.a[i + j] = (int)(remains);
                remains = 0;
            }

        }
    }
    for (int i = 39; i >= 0; i--)
    {
        if (z.a[i] == 0)
            z.a[i] = -1;
        else
            break;
    }
        
    return z;
}

int main() 
{
    uint1024_t a;
    uint1024_t b, v;
    scanf_value(&a);
    scanf_value(&b);
    printf("multiplication: ");
    v = mult_op(a, b);
    printf_value(mult_op(a, b));
    printf("\ndifference: ");
    printf_value(subtr_op(a, b));
    printf("\namount: ");
    printf_value(add_op(a, b));
    return 0;
}

