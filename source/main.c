/*	Author: Tyler Pastor tpast001@ucr.edu
 *  Partner(s) Name: N/A
 *	Lab Section: 023
 *	Assignment: Lab #5  Exercise #2
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

unsigned char A;
unsigned char C;

enum SM1_STATES {SM1_SMStart, SM1_up, SM1_down, SM1_Wait, SM1_reset, SM1_Waitup, SM1_Waitdown} SM1_STATE;
void Tick_Toggle() {
	switch(SM1_STATE) {
     		case SM1_SMStart:
      			SM1_STATE = SM1_Wait;
         		break;

		case SM1_Wait:
			if(A == 0x01 && C != 9){
				SM1_STATE = SM1_up;
			}
			else if(A == 0x02 && C != 0){
				SM1_STATE = SM1_down;
			}
			else if(A == 0x03){
				SM1_STATE = SM1_reset;
			}
			else{
				SM1_STATE = SM1_Wait;
			}
			break;

		case SM1_up:
			SM1_STATE = SM1_Waitup;
			break;

		case SM1_down:
			SM1_STATE = SM1_Waitdown;
			break;

		case SM1_reset:
			SM1_STATE = SM1_Wait;
			break;

		case SM1_Waitdown:
			if(A == 0x01){
				SM1_STATE = SM1_Waitdown;
			}
			else if(A == 0x00){
				SM1_STATE = SM1_Wait;
			}
			else if(A == 0x03){
				SM1_STATE = SM1_reset;
			}
			break;

		case SM1_Waitup:
			if(A == 0x02){
				SM1_STATE = SM1_Waitup;
			}
			else if(A == 0x00){
				SM1_STATE = SM1_Wait;
			}
			else if(A == 0x03){
				SM1_STATE = SM1_reset;
			}
			break;

      		default:
         		SM1_STATE = SM1_Wait;
         		break;
   	}

   	switch(SM1_STATE) {
      		case SM1_SMStart:
         		break;

		case SM1_Wait:
         		break;

		case SM1_up:
         		PORTC++;
         		break;

      		case SM1_down:
         		PORTC--;
        		break;

		case SM1_reset:
         		PORTC = 0x00;
        		break;

		case SM1_Waitdown:
        		break;

		case SM1_Waitup:
        		break;
	}
}

int main(void) {
	DDRA = 0x00; PORTA = 0xFF;
	DDRC = 0xFF; PORTC = 0x00;

	PORTC = 0x07;

	SM1_STATE = SM1_SMStart;

	while(1){
		A = ~PINA;
		C = PORTC;
		Tick_Toggle();
	}

	return 0;
}
