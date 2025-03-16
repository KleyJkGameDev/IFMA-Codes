//=====================================================================
//                                Exsto Tecnologia
//=====================================================================
//
//                                        Josï¿½ Domingos Adriano
//                                        domingos@exsto.com.br
//                                        (c) 2009 Exsto Tecnologia
//=====================================================================

#include <xc.h>

//// Configurï¿½ï¿½es
//#pragma config    PLLDIV = 5                // PLL para 20MHz    
//#pragma config    CPUDIV = OSC1_PLL2        // PLL desligado
//#pragma config    FOSC = HS                // Fosc = 20MHz        Tcy = 200ns
//#pragma config    WDT = OFF                // Watchdog desativado
//#pragma config    PBADEN = OFF            // Pinos do PORTB comeï¿½am como digitais
//#pragma config    LVP = OFF                // Desabilita gravaï¿½ï¿½o em baixa tensï¿½o
//#pragma config    XINST = OFF                
//#define _XTAL_FREQ 48000000 // Define o clock para 48 MHz (ajuste conforme seu projeto)

// Declarações das funções
void main_q1(void);
void main_q2(void);
void main_q3(void);
void main_q4(void);
void main_pr03(void);

void main (void)
{

    //main_q1();
    //main_q2();
    //main_q3();
    //main_q4();
    main_pr03();

    while(1){    
        //PORTD = 0x00;    
        //__delay_ms(250); // Atraso de 100 ms no XC8
        //PORTD = 0xFF;
        //__delay_ms(250); // Atraso de 100 ms no XC8
        //main_q1();
        //main_q2();
        //main_q3();
        //main_q4();
        main_pr03();
    }

}
