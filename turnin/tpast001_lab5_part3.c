/*	Author: Tyler Pastor tpast001@ucr.edu
 *  Partner(s) Name: N/A
 *	Lab Section: 023
 *	Assignment: Lab #5  Exercise #3
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */


//LINK TO DEMO: https://www.youtube.com/watch?v=arXRXarZipk

#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

unsigned char A;
unsigned char B;
int count;
int temp;

enum SM1_STATES {SM1_SMStart, SM1_Wait2, SM1_mult, SM1_div, SM1_Wait, SM1_Waitmult, SM1_Waitdiv} SM1_STATE;
void Tick_Toggle() {
	switch(SM1_STATE) {
     		case SM1_SMStart:
      			SM1_STATE = SM1_Wait;
         		break;

		case SM1_Wait:
			if(A == 0x00){
				SM1_STATE = SM1_Wait;
			}
			if(A == 0x01 && temp == 0){
				SM1_STATE = SM1_mult;
			}
			else if(A == 0x01 && temp == 6){
				SM1_STATE = SM1_div;
			}
			else{
				SM1_STATE = SM1_Wait;
			}
			break;

		case SM1_mult:
			count++;

			if(B == 0x00){
				PORTB = 0x01;
			}
			if(count != 6){
				temp = 0;
			}
			else{
				temp = 6;
			}
			SM1_STATE = SM1_Waitmult;
			break;

		case SM1_div:
			count--;

			if(count != 0){
				temp = 6;
			}
			else{
				temp = 0;
			}
			SM1_STATE = SM1_Waitdiv;
			break;

		case SM1_Waitdiv:
			if(A == 0x01){
				SM1_STATE = SM1_Waitdiv;
			}
			else if(A == 0x00)
				SM1_STATE = SM1_Wait2;
			else
				SM1_STATE = SM1_Waitdiv;
			break;

		case SM1_Waitmult:
			if(A == 0x01){
				SM1_STATE = SM1_Waitmult;
			}
			else if(A == 0x00)
				SM1_STATE = SM1_Wait2;
			else
				SM1_STATE = SM1_Waitmult;
			break;

		case SM1_Wait2:
			if(A == 0x00)
				SM1_STATE = SM1_Wait;
			else
				SM1_STATE = SM1_Wait2;
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

		case SM1_mult:
         		PORTB = PORTB * 2;
         		break;

      		case SM1_div:
         		PORTB = PORTB / 2;
        		break;

		case SM1_Waitdiv:
        		break;

		case SM1_Waitmult:
        		break;

		case SM1_Wait2:
			break;
	}
}

int main(void) {
	DDRA = 0x00; PORTA = 0xFF;
	DDRB = 0xFF; PORTB = 0x00;

	SM1_STATE = SM1_SMStart;

	while(1){
		A = ~PINA;
		B = PORTB;
		Tick_Toggle();
		while(~PINA == 0x01);
	}

	return 0;
}
