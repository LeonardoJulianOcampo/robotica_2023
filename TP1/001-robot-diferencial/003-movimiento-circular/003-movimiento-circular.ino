#define MOTORS_ENABLE PA4
#define MOTOR_IZQ PA3
#define MOTOR_DER PA2

void setup(){
	pinMode(MOTOR_DER, OUTPUT);
	pinMode(MOTOR_IZQ, OUTPUT);
	pinMode(MOTORS_ENABLE, OUTPUT);
	digitalWrite(MOTORS_ENABLE, HIGH);
}

int PWM1 = 128;
int PWM2 = 128;

void loop(){
	
	analogWrite(MOTOR_DER,PWM1+50);
	analogWrite(MOTOR_DER,PWM2+30);


}


