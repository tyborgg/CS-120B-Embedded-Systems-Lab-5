/*	Author: Tyler Pastor tpast001@ucr.edu
 *  Partner(s) Name: N/A
 *	Lab Section: 023
 *	Assignment: Lab #5  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
	DDRA = 0x00; PORTA = 0xFF; 
	DDRC = 0xFF; PORTC = 0x00;
	unsigned char tempA = 0;
	unsigned char tempC = 0;
	
    	while (1) {
		tempA = ~PINA & 0x0F;
		
		if(tempA == 0){
			tempC = 0x40;
		}
		else if(tempA == 1 || tempA == 2){
			tempC = 0x60;
		}
		else if(tempA == 3 || tempA == 4){
			tempC = 0x70;
		}
		else if(tempA == 5 || tempA == 6){
			tempC = 0x38;
		}
		else if(tempA == 7 || tempA == 8 || tempA == 9){
			tempC = 0x3C;
		}    
		else if(tempA == 10 || tempA == 12 || tempA == 11){
			tempC = 0x3E;
		}	
		else{
			tempC = 0x3F;
		}

		PORTC = tempC;
	}
	
	return 0;
}
