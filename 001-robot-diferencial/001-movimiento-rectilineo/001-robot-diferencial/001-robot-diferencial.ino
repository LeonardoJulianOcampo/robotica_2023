#define MOTORS_ENABLE PA4
#define MOTOR_IZQ PA3
#define MOTOR_DER PA2
#define LED       PC13


void giraDer(void){
	analogWrite(MOTOR_DER, 255);
	analogWrite(MOTOR_IZQ,   0);
	digitalWrite(LED_BUILTIN,LOW);
	delay(1000);
  }


void giraIzq(void){
	analogWrite(MOTOR_DER,   0);
	analogWrite(MOTOR_IZQ, 255);
	digitalWrite(LED_BUILTIN,LOW);
	delay(1000);
  }

void rect(int PWM){
	analogWrite(MOTOR_DER, PWM);
	analogWrite(MOTOR_IZQ, PWM);
	digitalWrite(LED_BUILTIN,HIGH); 
	delay(1000);
  }

int acel(int mode){
	int pwm = 0;
	if(mode == 0){
		return pwm;
	}
	if(mode == 1) //aceleracion
		while(pwm<255){
			pwm ++;
			return pwm;
			}
	if(mode == 2) //desaceleracion
		while(pwm > 0)
			pwm --;
	
}

void setup() {
  // put your setup code here, to run once:
  pinMode(MOTOR_DER, OUTPUT);
  pinMode(MOTOR_IZQ, OUTPUT);
  pinMode(MOTORS_ENABLE,OUTPUT);
  digitalWrite(MOTORS_ENABLE, HIGH);
}


int Valor_PWM = 0;
void loop() {
        rect(255);
        giraIzq();
        rect(255);
        giraIzq();
        rect(255);
        giraIzq();
        rect(255);
    }
