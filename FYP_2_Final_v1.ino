#include <Servo.h>
#include <Stepper.h>
//--------------------------------------------------
//Gantry motor
//--------------------------------------------------
const int stepPin = 51; 
const int dirPin = 50; 
const int stepPin2 = 42; 
const int dirPin2 = 43;
//--------------------------------------------------
//Servo Blade
//--------------------------------------------------
Servo ServoBlade;
int posBlade=0;
//--------------------------------------------------
//
//--------------------------------------------------
// initialize the stepper library on pins 8 through 11:
//Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);
//--------------------------------------------------
//
//--------------------------------------------------
void setup() {
  Serial.begin(9600);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  ServoBlade.attach(6);
  //--------------------------------------------------
  //     Limit switch motor
  //--------------------------------------------------
  pinMode(12, INPUT);
  pinMode(11, INPUT);
  pinMode(10, INPUT);
  pinMode(9, INPUT);
  //--------------------------------------------------
  //Gantry motor
  //--------------------------------------------------
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
  //--------------------------------------------------
  //
  //--------------------------------------------------
  
}
//--------------------------------------------------
//
//--------------------------------------------------
void loop() {
  Limitswitch();
  //Blade();
}
//--------------------------------------------------
//
//--------------------------------------------------
void Limitswitch(){
  if(digitalRead(12)==0){
    Serial.println("arm right");
    }
  else if (digitalRead(11)==0){
    Serial.println("Gantry back");
    }
  else if (digitalRead(10)==0){
    Serial.println("arm left");
    }
  else if (digitalRead(9)==0){
    Serial.println("gantry forward");
    }
}
//--------------------------------------------------
//
//--------------------------------------------------
void Blade(){
  for (posBlade = 0; posBlade <= 180; posBlade += 1) {
    ServoBlade.write(posBlade);              
    delay(15);                       
  }
  for (posBlade = 180; posBlade >= 0; posBlade -= 1) { 
    ServoBlade.write(posBlade);              
    delay(15);                       
  }

}
