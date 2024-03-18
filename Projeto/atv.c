#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

struct serie
{
    float val;
} s;

float res_serie()
{
    int qtd = 0;
    float res = 0.0;
    int ent;
    int cont = 0;
    printf("\n------------------------------------------------------------\n");
    printf("\n - Quantidade de resistores: ");
    scanf("%d", &qtd);
    struct serie *ser= (struct serie*)malloc(qtd*sizeof(struct serie));
    getchar();
    for (int i = 0; i < qtd; i++)
    {
        printf("\n- Valor resistência [%d] em Ohms: ", i+1);
        scanf("%f", &ser[i].val);
        //getchar();
        //printf("valor[%d]: %.2f", i+1, ser[i].val);
        res += ser[i].val;
    }
    printf("\n------------------------------------------------------------\n");
    printf("\nResistência equivalente = %.2f Ohms\n", res);
    printf("\n------------------------------------------------------------\n");
    free(ser);
}

struct prll
{
    float vl;
    float inverso;
} p;

float res_paralelo()
{
    int qtd = 0;
    float res_eq = 0.0;
    float soma = 0.0;
    float inv_soma = 0.0;
    printf("\n------------------------------------------------------------\n");
    printf(" - Quantidade de resistores: ");
    scanf("%d", &qtd);
    struct prll *pl = (struct prll*)malloc(qtd*sizeof(struct prll));

    for (int i = 0; i < qtd; i++)
    {
        printf("- Valor da resistência [%d]: ", i+1);
        scanf("%f", &pl[i].vl);
        pl[i].inverso = (1/pl[i].vl);
        soma += pl[i].inverso;
    }
    inv_soma = (1/soma);
    printf("\n------------------------------------------------------------\n");
    printf("\nReistência equivalente = %.2f Ohms", inv_soma);
    printf("\n------------------------------------------------------------\n");
    free(pl);
}

float res_mista(int q_s, int q_p, float soma_s, float soma_p)
{
    float res_eq = 0.0;
    float inv_p = 0;
    inv_p = (1/soma_p);
    res_eq = (soma_s + inv_p);

    return res_eq;
}

void programa()
{
    int loop;
    loop = 0;
    while (loop == 0)
    {
        int esc;
        printf("\n =========== RESISTÊNCIA EQUIVALENTE DO CIRCUITO =========== \n");
        printf("\n------------------------------------------------------------\n");
        printf("\n - Associação em Série [1]\n");
        printf("\n - Associação Paralela [2]\n");
        printf("\n - Associação Mista [3]\n");
        printf("\n - Fechar programa [0]\n");
        printf("\n - Escolha: ");
        scanf("%d", &esc);
        printf("\n------------------------------------------------------------\n");
        getchar();
        if (esc > 3 || esc < 0)
        {
            printf("Opção Inválida!!\n");
        }
        if (esc == 0)
        {
            printf("Saindo do programa...\n");
            loop = 1;
        }
        if (esc == 1)
        {
            res_serie();
            printf("\n============================================================\n");
        }
        if (esc == 2)
        {
            res_paralelo();
            printf("\n============================================================\n");
        }
        if (esc == 3)
        {
            int qs, qp;
            qs = qp = 0;
            float resposta = 0.0;
            printf("\n------------------------------------------------------------\n");
            printf("\n - Quantidade de resistores em série: ");
            scanf("%d", &qs);
            printf("\n - Quantidade de resistores em paralelo: ");
            scanf("%d", &qp);
            float ls, lp, ss, sp, iv;
            ls = lp = ss = sp = iv = 0;
            if (qs >= 1)
            {
                printf("\n------- Em Série --------\n");
                for (int i = 0; i < qs; i++)
                {
                    printf("\n- Valor [%d]: ", i+1);
                    scanf("%f", &ls);
                    ss += ls;
                    //printf("valor atual: %.2f", ss);
                }
            }
            if (qp >= 1)
            {
                printf("\n------ Em Paralelo ------\n");
                for (int i = 0; i < qp; i++)
                {
                    printf("\n- Valor [%d]: ", i+1);
                    scanf("%f", &lp);
                    iv = (1/lp);
                    sp += iv;
                }
            }
            
            resposta = res_mista(qs, qp, ss, sp);
            printf("\n------------------------------------------------------------\n");
            printf("\n - Resistência equivalente = %.2f Ohms", resposta);
            printf("\n------------------------------------------------------------\n");
            printf("\n============================================================\n");
        }
        
    }
    
}

int main(){
setlocale(LC_ALL, "Portuguese");

    programa();

    return 1;
}