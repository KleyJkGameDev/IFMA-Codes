#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct alunos
{
    char nick[20];
    int codigo;
    float nota1;
    float nota2;
};

void programa()
{
    FILE *arq;
    arq = fopen("texto4.bin", "rb");

    if (arq == NULL)
    {
        printf("Erro ao abrir o arquivo\n");
        return 1;
    }

    // Mover ponteiro para o final do arquivo e armazenar seu valor
    // dentro de arq, mover 0 bytes desde o fim do arquivo(SSEK_END)
    fseek(arq, 0, SEEK_END);
    // ftell retorna um valor long int da posição atual do ponteiro
    long int tamanho_arq = ftell(arq);
    // Voltar o ponteiro ao inicio do arquivo
    rewind(arq);

    int num_reg = 0;
    // Calcular número de registros de alunos no arquivo
    // Enquanto posição atual (em bytes) do ponteiro < tamanho_arq:
    while (ftell(arq) < tamanho_arq)
    {
        // Primeiro digito do arquivo é o tamanho do nome a ser lido
        int tam_nome;
        // Ler quantidade de unidade de dados
        // Atribuir o primeiro digito do arquivo a variavel tam_nome
        // Ler uma unidade a partir da posição do ponteiro (inicio)
        fread(&tam_nome, sizeof(int), 1, arq);
        // Mover ponteiro 
        fseek(arq, (tam_nome * sizeof(char) + 3 * sizeof(int)), SEEK_CUR);
        // 4 * bytes_char(nome) + 3 * bytes_int(codigo, nota1 e nota2)

        num_reg++;
    }
    
    int loop = 0;
    // Ler o tamanho_nome, nome, codigo e notas
    // Criando memoria dinamica para a struct secundaria
    
    struct alunos *alu = (struct alunos*) malloc(num_reg * sizeof(struct alunos));
    if (alu == NULL)
    {
        printf("Erro ao alocar memoria\n");
        return 1;
    }
    

    // Garantindo que o ponteiro esteja na posicao inicial do arquivo
    fseek(arq, 0, SEEK_SET);
    while (loop < num_reg)
    {
        // Lendo o primeiro digito(tamanho do nome)
        int t_nome;
        // Atribuindo o tamanho do nome a t_nome
        fread(&t_nome, sizeof(int), 1, arq);
        //printf("Posicao ponteiro depois do fread(nome): %d\n", posi);
        // Ler a cadeia string(nome) a partir do t_nome até o caractere nulo '\0'
        fread(alu[loop].nick, sizeof(char), t_nome, arq);
        // adicionando o caractere nulo '\0'
        alu[loop].nick[t_nome] = '\0';

        // Lendo o codigo do aluno e notas
        int posi = ftell(arq);
        printf("Posicao ponteiro antes do codigo: %d\n", posi);
        // Ler o bloco de bytes(codigo) a partir da posicao atual do ponteiro
        fread(&alu[loop].codigo, sizeof(int), 1, arq);
        fread(&alu[loop].nota1, sizeof(int), 1, arq);
        fread(&alu[loop].nota2, sizeof(int), 1, arq);

        printf("Tamanho nome: %d\n", t_nome);
        printf("Nome: %s\n", alu[loop].nick);
        printf("Codigo: %d\n", alu[loop].codigo);
        printf("Nota 1: %.2f\n", alu[loop].nota1);
        printf("Nota 2: %.2f\n", alu[loop].nota2);
        
        loop++;
    }

    // Calcular média, mostrar aprovados e reprovados
    float mediaAluno, mediaTurma, soma;
    mediaAluno = mediaTurma = soma =0;
    for (int c = 0; c < num_reg; c++)
    {
        soma = alu[c].nota1 + alu[c].nota2;
        mediaAluno = soma/2;

        if (soma < 14)
        {
            printf("\nAluno: %s -- REPROVADO | media: %.2f", alu[c].nick, mediaAluno);
        }else
        {
            printf("\nAluno: %s -- APROVADO | media: %.2f", alu[c].nick, mediaAluno);
        }
        
        mediaTurma += soma/(num_reg*2);

    }
    
    printf("\nMedia da turma: %.2f", mediaTurma);
    
    printf("\nNumero de registros: %d", num_reg);

    free(alu);
    fclose(arq);
}


int main()
{

    programa();

    return 0;
}