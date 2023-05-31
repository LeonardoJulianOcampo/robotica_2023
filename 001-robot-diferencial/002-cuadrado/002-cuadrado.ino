#define R 65/2
#define b 130

#define STOP      127 
#define TWISTCW   255
#define TWISTCCW    0

#define MOTORS_ENABLE PA4
#define MOTOR_IZQ PA3
#define MOTOR_DER PA2

#define ENCODERS_ENABLE PB6
#define ENC_DER PB5
#define ENC_IZQ  PB4

uint8_t PWM = STOP;

uint8_t PWM1 = STOP;
uint8_t PWM2 = STOP;




void moveForward(unsigned long ms){
	PWM = STOP;

	while(PWM <= 254){
		analogWrite(MOTOR_DER, PWM);
		analogWrite(MOTOR_IZQ, PWM);
		delay((unsigned long)((ms/4)/127));
		PWM = PWM + 1;
	}	

	delay((unsigned long)(((ms/2))));
	

	while(PWM >= 128){
		analogWrite(MOTOR_DER, PWM);
		analogWrite(MOTOR_IZQ, PWM);
		delay((unsigned long)(((ms/4)/127)));
		PWM = PWM - 1;
	}
}






void halt(unsigned long ms){
	analogWrite(MOTOR_DER, STOP);
	analogWrite(MOTOR_IZQ, STOP);
	delay(ms);
}









void moveBackward(unsigned long ms){
	PWM = STOP;

	while(PWM >= 1){
		analogWrite(MOTOR_DER, PWM);
		analogWrite(MOTOR_IZQ, PWM);
		delay((unsigned long)((ms/4)/127));
		PWM = PWM - 1;
	}
	PWM = 0;
  analogWrite(MOTOR_DER, PWM);
  analogWrite(MOTOR_IZQ, PWM);  
	delay((unsigned long)((ms/2)));
	
	while(PWM <= 125){
		analogWrite(MOTOR_DER,PWM);
		analogWrite(MOTOR_IZQ,PWM);
		delay((unsigned long)((ms/4)/127));
		PWM = PWM +1;
	}
}








void twist(int ms){
	
	PWM1 = 128;
  PWM2 = 126;
  
	while(PWM1 <= 254){

    if(PWM1 == 128){
      PWM1 = PWM1 + 1;
      PWM2 = 126;
      }
    else{
      PWM1 = PWM1 + 1;
      PWM2 = ~PWM1;
      }
		analogWrite(MOTOR_DER,  PWM1);
		analogWrite(MOTOR_IZQ,  PWM2);
		delay((unsigned long)((ms/4)/127));
	}	


	PWM1 =  255;
  PWM2 = ~PWM1;
	analogWrite(MOTOR_DER,  PWM1);
	analogWrite(MOTOR_IZQ,  PWM2);
	delay((unsigned long)(((ms/2)/127)));
	

	while(PWM1 >= 128){
		PWM1 =  PWM1 - 1;
    PWM2 = ~PWM1;
    analogWrite(MOTOR_DER,  PWM1);
    analogWrite(MOTOR_IZQ,  PWM2);
    delay((unsigned long)(((ms/4)/127)));
	}

}






void setup() {
    pinMode(MOTOR_DER, OUTPUT);
    pinMode(MOTOR_IZQ, OUTPUT);
    pinMode(MOTORS_ENABLE, OUTPUT);
    digitalWrite(MOTORS_ENABLE, HIGH);
  
}

void loop(){

  moveForward(1000);
  halt(500);
  
  twist(1000);
  halt(500);
  
  moveForward(1000);
  halt(500);
  
  twist(1000);
  halt(500);
  
  moveForward(1000);
  halt(500);  
  
  twist(1000);
  halt(500);

  moveForward(1000);
  halt(500);

}
