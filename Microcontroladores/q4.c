//#include <P18F4550.h>
#include <xc.h>
//#include <delays.h>

// Configuração do microcontrolador
#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config WDT = OFF
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config XINST = OFF
#define _XTAL_FREQ 48000000

void delay_ms(unsigned int tempo) {
    while (tempo--) {
        __delay_ms(5);  // Aproximadamente 1ms para Fosc = 20MHz
    }
}

void main_q4(void) {
    TRISBbits.TRISB0 = 1;  // RB0 como entrada (Chave 1)
    TRISBbits.TRISB1 = 1;  // RB1 como entrada (Chave 2)
    TRISD = 0x00;          // RD0 como saída (LED)

    while (1) {
        unsigned char chave1 = PORTBbits.RB0;
        unsigned char chave2 = PORTBbits.RB1;

        if (chave1 == 1 && chave2 == 1) { 
            PORTDbits.RD0 = 0; // Nenhuma ação (LED apagado)
        } 
        else if (chave1 == 0 && chave2 == 1) {
            PORTDbits.RD0 = 1; 
            __delay_ms(500);  // Meio segundo (1Hz)
            PORTDbits.RD0 = 0; 
            __delay_ms(500);
        } 
        else if (chave1 == 1 && chave2 == 0) {
            PORTDbits.RD0 = 1; 
            __delay_ms(62);  // Aproximadamente 8Hz (62ms de delay)
            PORTDbits.RD0 = 0; 
            __delay_ms(62);
        } 
        else {
            PORTDbits.RD0 = 1; // LED aceso constantemente
        }
    }
 }