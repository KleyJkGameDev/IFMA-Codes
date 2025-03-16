//#include <P18F4550.h>
#include <xc.h>
// Configuração do microcontrolador
#pragma config PLLDIV = 5
#pragma config CPUDIV = OSC1_PLL2
#pragma config FOSC = HS
#pragma config WDT = OFF
#pragma config PBADEN = OFF
#pragma config LVP = OFF
#pragma config XINST = OFF
#define _XTAL_FREQ 48000000

void main_q2(void) {
    TRISBbits.TRISB0 = 1;  // RB0 como entrada (Chave 1 - INT0)
    TRISBbits.TRISB1 = 1;  // RB1 como entrada (Chave 2 - INT1)
    TRISD = 0x00;          // PORTD como saída (LEDs)

    while (1) {
        // Lê os estados das chaves
        unsigned char chave1 = PORTBbits.RB0;
        unsigned char chave2 = PORTBbits.RB1;

        // Aplica a lógica da tabela
        if (chave1 == 0 && chave2 == 0) {
            PORTD = 0x00;  // Ambos LEDs apagados
        } else if (chave1 == 0 && chave2 == 1) {
            PORTD = 0x02;  // LED 2 aceso (RD1)
        } else if (chave1 == 1 && chave2 == 0) {
            PORTD = 0x01;  // LED 1 aceso (RD0)
        } else {  // chave1 == 1 && chave2 == 1
            PORTD = 0x00;  // Ambos LEDs apagados
        }
    }
}