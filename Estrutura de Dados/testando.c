#include <stdio.h>
#include <stdlib.h>

typedef struct aluno
{
    int idade;
    struct aluno* prox;
} A;

typedef struct lista
{
    A* ini;
    A* fim;
    int tamanho;
} L;

/* Função de criação: retorna uma lista vazia */
L* iniLista(void){
    L* lista = (L*) malloc(sizeof(L));
    lista->ini = lista->fim = NULL;
    lista->tamanho;
    return lista;
}

/* Função de criação de nós */
A* criando(int valor){
    A* no = (A*) malloc(sizeof(A));
    no->prox = NULL;
    no->idade = valor;
    return no;
}

/* Função de inserir elemento na primeira posição*/
void inserirIni(L *lista, int valor){
    A *novo = criando(valor);
    novo->prox = lista->ini;
    if (lista->ini == NULL)
    {
        lista->fim = novo;
    }
    lista->ini = novo;
    lista->tamanho++;
}

/* Função de inserir elemento na última posição*/
void inserirFim(L *lista, int valor){
    if (lista->ini == NULL)
    {
        inserirIni(lista, valor);
    }else{        
        A *novo = criando(valor);
        A *ultimo = lista->fim;
        ultimo->prox = novo;
        lista->fim = novo;
        lista->tamanho++;
    }
}

/* Função verificadora de posição válida*/
int verificaPosition(L *lista, int position){
    if (position == 1 || position == (lista->tamanho)+1)
    {
        return 1;
    }
    if (1 > position || position > lista->tamanho)
    {
        return 0;
    }
}

/* Função de inserir elemento em qualquer posição*/
void inserirMeio(L *lista, int valor, int position){
    if (verificaPosition(lista, position)) /*se retornar 1 (verdadeiro/válida)*/
    {        
        if (position == 1)
        {
            inserirIni(lista, valor);
        }else{
            if(position == (lista->tamanho)+1)
            {
                inserirFim(lista, valor);
            }else
            {
                A *novo = criando(valor);
                A *atual = lista->ini;
                A *anterior;

                for (int i = 1; i < position; i++)
                {
                    anterior = atual;
                    atual = atual->prox;
                }
                anterior->prox = novo;
                novo->prox = atual;
                lista->tamanho++;
            }        
        } 
    }else{
        printf("Posição inválida!!");
        exit(1);
    }    
}

/* Função de remover primeiro item*/
void removerInicio(L *lista){
    if (lista->tamanho == 0)
    {
        printf("Erro!\nLista VAZIA");
        exit(1);
    }
    A *aux = lista->ini;
    A *primeiro = aux->prox;
    free(aux);
    lista->ini = primeiro;
    if (lista->ini == NULL)
    {
        lista->fim = NULL;
    }
    lista->tamanho--;
}

void removerFim(L *lista){
    if (lista->tamanho == 0)
    {
        printf("Erro!\nLista VAZIA");
        exit(1);
    }
    A *ult = lista->ini;
    A *pen;
    for (int i = 0; i < lista; i++)
    {
        pen = ult;
        ult = ult->prox;
    }
    pen->prox = NULL;
    free(ult);
    lista->fim = pen;
    lista->tamanho--;
}

int main(){
    
    
    
    
    return 0;
}


