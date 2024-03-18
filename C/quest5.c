#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct cad
{
    char matricula[20];
    char nome[20];
    char sobrenome[20];
    int nascimento;
};

void programa()
{
    int numAluno = 0;
    printf("Quantidade de alunos: ");
    scanf("%d", &numAluno);

    // Ponteiro *aluno recebe uma memória dinâmica (aumenta conforme o necessário)
    struct cad *aluno = (struct cad*) malloc(numAluno * sizeof(struct cad));
    /* *aluno agora pode apontar para a scruct e ser tratada como vetor*/

    if (aluno == NULL)
    {
        printf("Erro ao alocar memória\n");
        return 1;
    }

    // Perguntar e guardar os dados na struct
    for (int i = 0; i < numAluno; i++)
    {
        printf("Aluno [%d]:\n", (i+1));
        printf("- Matricula: ");
        scanf("%s", &aluno[i].matricula);
        printf("- Nome: ");
        scanf("%s", &aluno[i].nome);
        printf("- Sobrenome: ");
        scanf("%s", &aluno[i].sobrenome);
        printf("- Ano/Nascimento: ");
        scanf("%d", &aluno[i].nascimento);
    }

    FILE *arq;
    arq = fopen("texto.bin", "wb");
    fprintf(arq, " --- REGISTRO DE ALUNOS ---\n");

    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo\n");
        free(aluno);
        return 1;
    }
    
    
    // Gravação dos dados no arquivo .bin
    for (int i2 = 0; i2 < numAluno; i2++)
    {
        // Escreve os dados da maneira como esta representado a seguir:
        fprintf(arq, "Aluno [%d]:", (i2+1));
        fprintf(arq, "\n - Matricula: %s", aluno[i2].matricula);
        fprintf(arq, "\n - Nome:: %s", aluno[i2].nome);
        fprintf(arq, "\n - Sobrenome: %s", aluno[i2].sobrenome);
        fprintf(arq, "\n - Ano Nascimento: %d\n", aluno[i2].nascimento);
    }

    // Exibição dos dados registrados
    printf("\n == Dados Registrados == \n");
    for (int i3 = 0; i3 < numAluno; i3++)
    {
        printf("Aluno [%d]:", (i3+1));
        printf("\n - Matricula: %s", aluno[i3].matricula);
        printf("\n - Nome:: %s", aluno[i3].nome);
        printf("\n - Sobrenome: %s", aluno[i3].sobrenome);
        printf("\n - Ano Nascimento: %d\n", aluno[i3].nascimento);
    }
    
    
    // Limpar memória dinâmica alocada ao ponteiro
    free(aluno);

    fclose(arq);

}

int main()
{

    programa();

    return 0;
}