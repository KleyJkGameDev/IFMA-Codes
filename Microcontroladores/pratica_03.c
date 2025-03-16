//#include <P18F4550.H>
//#include <delays.h>
#include <xc.h>

// Configurações
#pragma config PLLDIV = 5         // PLL para 20MHz    
#pragma config CPUDIV = OSC1_PLL2 // PLL desligado
#pragma config FOSC = HS          // Fosc = 20MHz        Tcy = 200ns
#pragma config WDT = OFF          // Watchdog desativado
#pragma config PBADEN = OFF       // Pinos do PORTB como digitais
#pragma config LVP = OFF          // Desabilita gravação em baixa tensão
#pragma config XINST = OFF        

#define LEDs PORTD
#define _XTAL_FREQ 48000000


// ISR de alta prioridade (não usada, pois IPEN = 0)

// ISR de alta prioridade OU se não houver prioridade. 
void HighPriorityISR(void)
{


	unsigned char i,j;
	//LEDs = 0b11111111;
    LEDs = 0xFF;

	if(INTCON3bits.INT1IF == 1){		// ISR de INT1
        LEDs = 0xFF;
        //LEDs = (LEDs - 1);
        __delay_ms(500);
        for (j = 0; j < 255; j++)
        {
            LEDs = (LEDs >> 1);
            __delay_ms(300);
        }
		LEDs = 0x00;
		LEDs = 0b00000000;
        INTCON3bits.INT1IF = 0;
	}

	if(INTCON3bits.INT2IF == 1){		// ISR de INT2
        LEDs = 0x00;
        for (j = 1; j <= 8; j++)
        {
            LEDs = (LEDs << 1)|1;
            __delay_ms(300);
        }
		LEDs = 0b11111111;
        INTCON3bits.INT2IF = 0;

	}

}


void main_pr03 (void)
{
	// declaração de variáveis
	unsigned char i,j, Desloc;

	// *** Configuração dos portais
	DDRD = 0b00000000;		// PORTD é saída

	OSCCON = 0b01010000;	// oscilador interno a 4MHz ==> Tcy = 1us

    LEDs = 0xFF;

	for(;;){	// pisca-pisca de 2 Hz
	//Configura  o das interrup  es
		RCONbits.IPEN = 0;		// <== Não há prioridade
        
		INTCON3bits.INT2IF = 0;	// zera flag da interrupção
		INTCON3bits.INT1IF = 0;	// zera flag da interrupção

		INTCON3bits.INT2IP = 1;	// interrupção INT2 é baixa	<== não tem efeito
		INTCON3bits.INT1IP = 1;	// interrupção INT1 é alta <== não tem efeito

		INTCON3bits.INT2IE = 1;	// habilita INT2
		INTCON3bits.INT1IE = 1;	// habilita INT1

		INTCONbits.PEIE = 1;
		INTCONbits.GIEL = 1;	// habilita interrupções de baixa prioridade
		INTCONbits.GIEH = 1;	// habilita interrupções de alta prioridade
        Nop();
        Nop();
        Nop();
        
	}
	
}
