#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct infoTurma
{
    char turma[10];
    char curso[50];
};


void infoTurma()
{
    int q;

    printf("\n -- Registro de Turma --\n");
    printf("Quantidade de turmas: ");
    scanf("%d", &q);

    struct infoTurma *inf = (struct infoTurma*) malloc(q * sizeof(struct infoTurma));

    for (int i = 0; i < q; i++)
    {
        printf("Registro [%d]:\n", i+1);
        printf(" - Turma: ");
        scanf("%s", &inf[i].turma);
        printf(" - Curso: ");
        scanf("%s", &inf[i].curso);
    }
    for (int c = 0; c < q; c++)
    {
        printf("\nRegistro [%d]:\n", c+1);
        printf(" - Turma: %s\n", inf[c].turma);
        printf(" - Curso: %s\n", inf[c].curso);
    }

    //free(inf);
}

struct Aluno
{
    char nome[20];
    int nota1;
    int nota2;
} al;


void insereAluno()
{
    
}

void save()
{
    FILE *arq;
    arq = fopen("registro.txt", "w");
    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    fprintf(arq, " --- REGISTRO GERAL --- \n");
    struct infoTurma *inf = (struct infoTurma*) malloc(1 * sizeof(struct infoTurma));
    printf("\nturma REGISTRO: %s", inf[0].turma);

    fclose(arq);
}


int main()
{
    infoTurma();
    save();

    return 0;
}