#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

int teste()
{
    FILE *file;
    char string[100];
    int i = 0;

    file = fopen("texto.txt","w");
    //fprintf(file, "bom dia");

    if (file == NULL)
    {
        printf("Erro ao abrir o arquivo em questão.\n");
        system("pause");
        exit(1);
    }

    printf("Nome: ");
    gets(string);

    for (i = 0; i < strlen(string); i++)
    {
        fputc(string[i], file);
    }
    fflush(file);
    fclose(file);
}
void ler()
{
    FILE *op;
    char c;
    int tamanho = 0;
    op = fopen("texto.txt", "r");

    while((feof(op)) == 0)
    {
        c = fgetc(op);
        printf("%c", c);
    }
    fseek(op, 0, SEEK_END);
    tamanho = ftell(op);
    printf("\ntamanho: %i", tamanho);
    fclose(op);
}

int teste2()
{
    FILE *arq;
    char str[20];
    printf("nome: ");
    gets(str);
    int result;
    arq = fopen("texto.txt", "w");

    result = fputs(str, arq);
    //fputs("VIRUS", arq);
    if (result == EOF)
    {
        printf("Erro de gravação\n");
    }
    fclose(arq);
}

void ler2()
{
    FILE *lt;
    char *result, str[20];
    // str (array onde será guardado o texto lido)
    lt = fopen("texto.txt", "r");
    result = fgets(str, 20, lt);
    printf("\n%s", str);
    fclose(lt);
}

int teste3()
{
    FILE *fp;
    char nome[20], idade[3];
    int i;
    float a;
    fp = fopen("texto.txt", "r");

    fscanf(fp, "%s %s", nome, idade);
    printf("%s %s \n", nome, idade);
    fscanf(fp, "%s %d", nome, i);
    printf("%s %d \n", nome, i);
    fscanf(fp, "%s %f", nome, a);
    printf("%s %f \n", nome, a);

    fclose(fp);
}

int main()
{
setlocale(LC_ALL, "Portuguese");
    
    //teste();
    //teste2();
    //ler();
    //ler2();
    teste3();

    return 0;
}