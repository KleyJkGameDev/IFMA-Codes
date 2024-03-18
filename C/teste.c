#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Aluno 
{
    char nome[50];
    int codigo;
    int nota1;
    int nota2;
};

int main() {
    FILE *arquivo;
    arquivo = fopen("texto4.bin", "rb");

    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    fseek(arquivo, 0, SEEK_END);
    long tamanho_arquivo = ftell(arquivo);
    rewind(arquivo);

    int num_registros = 0;

    // Calculando o número de registros (alunos) no arquivo
    while (ftell(arquivo) < tamanho_arquivo) {
        int tamanho_nome;
        fread(&tamanho_nome, sizeof(int), 1, arquivo);

        fseek(arquivo, tamanho_nome * sizeof(char) + 3 * sizeof(int), SEEK_CUR);

        num_registros++;
    }

    rewind(arquivo);

    struct Aluno *alunos = (struct Aluno *)malloc(num_registros * sizeof(struct Aluno));

    if (alunos == NULL) {
        printf("Erro ao alocar memoria.\n");
        fclose(arquivo);
        return 1;
    }

    // Lendo os dados dos alunos do arquivo
    for (int i = 0; i < num_registros; i++) {
        int tamanho_nome;
        fread(&tamanho_nome, sizeof(int), 1, arquivo);
        fread(alunos[i].nome, sizeof(char), tamanho_nome, arquivo);
        alunos[i].nome[tamanho_nome] = '\0';

        fread(&alunos[i].codigo, sizeof(int), 1, arquivo);
        fread(&alunos[i].nota1, sizeof(int), 1, arquivo);
        fread(&alunos[i].nota2, sizeof(int), 1, arquivo);
    }

    fclose(arquivo);

    // Calculando a média da turma e exibindo alunos aprovados e reprovados
    int aprovados = 0, reprovados = 0;
    float soma_notas = 0;

    for (int i = 0; i < num_registros; i++) {
        float media = (float)(alunos[i].nota1 + alunos[i].nota2) / 2.0;
        soma_notas += media;

        printf("Aluno: %s - Media: %.2f - ", alunos[i].nome, media);

        if (media >= 6.0) {
            printf("Aprovado\n");
            aprovados++;
        } else {
            printf("Reprovado\n");
            reprovados++;
        }
    }

    printf("\nTotal de Alunos: %d\n", num_registros);
    printf("Alunos Aprovados: %d\n", aprovados);
    printf("Alunos Reprovados: %d\n", reprovados);
    printf("Media da Turma: %.2f\n", soma_notas / num_registros);

    free(alunos);

    return 0;
}
