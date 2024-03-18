#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cad
{
    char nome[20];
    int codigo;
    float nota1;
    float nota2;
};


void programa()
{
    int numAluno = 0;
    printf("Quantidade de alunos: ");
    scanf("%d", &numAluno);

    struct cad *cd = (struct cad*) malloc(numAluno * sizeof(struct cad));

    if (cd == NULL)
    {
        printf("Erro ao alocar memória\n");
        return 1;
    }

    for (int i = 0; i < numAluno; i++)
    {
        printf("Aluno [%d]\n", (i+1));
        printf(" - Nome: ");
        scanf("%s", &cd[i].nome);
        printf(" - Codigo: ");
        scanf("%d", &cd[i].codigo);
        printf(" - Nota 1: ");
        scanf("%f", &cd[i].nota1);
        printf(" - Nota 2: ");
        scanf("%f", &cd[i].nota2);
    }
    
    FILE *arq;
    arq = fopen("texto4.bin", "wb");

    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo\n");
        free(cd);
        return 1;
    }
    

    for (int i2 = 0; i2 < numAluno; i2++)
    {
        int tamanho_nome = strlen(cd[i2].nome);
        
        fwrite(&tamanho_nome, sizeof(int), 1, arq);
        fwrite(cd[i2].nome, sizeof(char), tamanho_nome, arq);
        fwrite(&cd[i2].codigo, sizeof(int), 1, arq);
        fwrite(&cd[i2].nota1, sizeof(int), 1, arq);
        fwrite(&cd[i2].nota2, sizeof(int), 1, arq);
    }
    
    printf("\nDados armazenados:\n");
    for (int i = 0; i < numAluno; i++) {
        printf("\nAluno %d:\n", i + 1);
        printf("Nome: %s\n", cd[i].nome);
        printf("Codigo: %d\n", cd[i].codigo);
        printf("Nota 1: %.2f\n", cd[i].nota1);
        printf("Nota 2: %.2f\n", cd[i].nota2);
    }

    free(cd);

    fclose(arq);


}


int main()
{

    programa();

    return 0;
}