#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[]) {
    freopen(argv[2], "r", stdin);
    if ((strcmp(argv[1], "-l") == 0) || (strcmp(argv[1], "--lines") == 0))
    {
        int n = 0;
        int str = getchar();
        int str1;
        if (str == EOF) 
        {
            printf("incorect file name or file is empty");
        }
        else
        {
            while (str != EOF)
            {
                str1 = str;
                if (str == '\n') n += 1;
                str = getchar();
            }
        printf("%d", n + 1);
        }
    }
    else if ((strcmp(argv[1], "-w") == 0) || (strcmp(argv[1], "--words") == 0))
    {
        int n = 0, isword = 0;
        int str = getchar();
        if (str == EOF) printf("incorect file name or file is empty");
        else
        {
        while (str != EOF)
        {
            if ((str == '\n' || str == ' ' || str == '\t')  && isword == 1) 
            {
                isword = 0;
                n += 1;
            }
            else if (str != '\n' && str != ' ' && str != '\t') 
            {
                isword = 1;
            }
            str = getchar();
        }
        
        if (isword == 1) n +=1;  
        printf("%d", n);
        }
    }
    else if ((strcmp(argv[1], "-c") == 0) || (strcmp(argv[1], "--bytes") == 0))
    {
        int str = getchar(), n = 0;
        if (str == EOF) printf("incorect file name or file is empty");
        else
        {
        while (str != EOF)
        {
            if (str == '\n') n += 2;
            else n += 1;
            str = getchar();
        }
        printf("%d", n);
        }
    }
    else printf("incorrect option name");
    fclose(stdin);
    return 0;
}