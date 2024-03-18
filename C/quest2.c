#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct atleta
{
    char nome[20];
    char esporte[20];
    int idade;
    float altura;
} at;

void looping()
{
    FILE *arq;
    struct atleta atVelho;
    struct atleta atAlto;
    atAlto.altura = 0.0;
    atVelho.idade = 0;
    arq = fopen("texto.bin", "wb");
    int i;
    for (i = 1; i < 3; i++)
    {
        printf("\nAtleta[%d]", i);
        printf("\n - Nome: ");
        scanf("%s", &at.nome);
        printf(" - Esporte: ");
        scanf("%s", &at.esporte);
        printf(" - Idade: ");
        scanf("%d", &at.idade);
        printf(" - Altura: ");
        if (atVelho.idade < at.idade)
        {
            atVelho = at;
        }
        scanf("%f", &at.altura);
        if (atAlto.altura < at.altura)
        {
            atAlto = at;
        }
        fprintf(arq, "Atleta [%d]:\n - Nome: %s\n - Esporte: %s\n", i, at.nome, at.esporte);
        fprintf(arq, " - Idade: %d\n - Altura: %.2f\n\n", at.idade, at.altura);
    }
    fprintf(arq, "\n- Mais velho: %s, Idade: %d", atVelho.nome, atVelho.idade);
    fprintf(arq, "\n- Mais Alto: %s, Altura: %.2f", atAlto.nome, atAlto.altura);
    fclose(arq);
}

int main()
{

    looping();

    return 0;
}