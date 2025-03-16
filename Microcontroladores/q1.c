//#include <P18F4550.h>
#include <xc.h>
//#include <delays.h>

//// Configura??es
#pragma config    PLLDIV = 5                // PLL para 20MHz    
#pragma config    CPUDIV = OSC1_PLL2        // PLL desligado
#pragma config    FOSC = HS                // Fosc = 20MHz        Tcy = 200ns
#pragma config    WDT = OFF                // Watchdog desativado
#pragma config    PBADEN = OFF            // Pinos do PORTB come?am como digitais
#pragma config    LVP = OFF                // Desabilita grava??o em baixa tens?o
#pragma config    XINST = OFF   
#define _XTAL_FREQ 48000000             


void main_q1(void) {
    TRISD = 0x00;  // PORTD como saída
    TRISB = 0xFF;  // PORTB como entrada

    while (1) {
        if (PORTBbits.RB0) {  
            PORTD = 0xFF;
            __delay_ms(125);  
            PORTD = 0x00;
            __delay_ms(125);
        } else {
            PORTD = 0xFF;
            __delay_ms(25);  
            PORTD = 0x00;
            __delay_ms(25);
        }
    }
}