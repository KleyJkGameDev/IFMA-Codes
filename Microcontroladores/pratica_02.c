//=====================================================================
//                                Exsto Tecnologia
//=====================================================================
//
//                                        Jos  Domingos Adriano
//                                        domingos@exsto.com.br
//                                        (c) 2009 Exsto Tecnologia
//=====================================================================

#include<P18F4550.H>
#include<delays.h>

//// Configur  es
#pragma config    PLLDIV = 5                // PLL para 20MHz    
#pragma config    CPUDIV = OSC1_PLL2        // PLL desligado
#pragma config    FOSC = HS                // Fosc = 20MHz        Tcy = 200ns
#pragma config    WDT = OFF                // Watchdog desativado
#pragma config    PBADEN = OFF            // Pinos do PORTB come am como digitais
#pragma config    LVP = OFF                // Desabilita grava  o em baixa tens o
#pragma config    XINST = OFF                

#define LEDs    PORTD


// ISR de alta prioridade OU se nÃ£o houver prioridade.
void HighPriorityISR(void)
{
    unsigned char i;

    INTCON3bits.INT1IF = 0;
   
    for(i=3;i>0;i--){
        PORTD = 0x55;
        Delay10KTCYx(250);
        PORTD = 0xAA;
        Delay10KTCYx(250);
    }
    Nop();
}
//----------------------------------------------------------------------
// ISR de baixa prioridade
void LowPriorityISR (void)
{
    unsigned char Desloc,i,j;
   
    INTCON3bits.INT2IF = 0;

    Desloc = 0x01;
    for(i=3;i>0;i--){
        for(j=7;j>0;j--){
            PORTD = ~Desloc;        // LEDs baixo ativos
            Delay10KTCYx(100);
            Desloc = Desloc << 1;
        }
        for(j=7;j>0;j--){
            PORTD = ~Desloc;        // LEDs baixo ativos
            Delay10KTCYx(100);
            Desloc = Desloc >> 1;
        }
    }
}


void main (void)
{
    // declara  o de vari veis
    unsigned char i;

    // *** Configura  o dos portais
    DDRD = 0x00;        // PORTD   sa da

    OSCCON = 0b01010000;    // oscilador interno a 4MHz ==> Tcy = 1us

    //Configura  o das interrup  es
    RCONbits.IPEN = 1;        // habilita prioridade
    INTCON3bits.INT2IF = 0;    // zera flag da interrup  o
    INTCON3bits.INT1IF = 0;    // zera flag da interrup  o
    INTCON3bits.INT2IP = 0;    // interrup  o INT2   baixa
    INTCON3bits.INT1IP = 1;    // interrup  o INT1   alta
    INTCON3bits.INT2IE = 1;    // habilita INT2
    INTCON3bits.INT1IE = 1;    // habilita INT1
    INTCONbits.GIEL = 1;    // habilita interrup  es de baixa prioridade
    INTCONbits.GIEH = 1;    // habilita interrup  es de alta prioridade
   
    for(;;){    // pisca-pisca de 2 Hz
        LEDs = 0x00;
        Delay10KTCYx(250); //0,5 s
        LEDs = 0xFF;
        Delay10KTCYx(250); //0,5 s
    }
}
