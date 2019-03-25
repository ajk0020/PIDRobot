///////// CNC Shield for Arduino UNO test //////////

/*
 * Defined are the pins associated with the CNC Shield
 */
 
#define EN        8       //The step motor makes the power end, low level is effective
#define X_DIR     5       //The x-axis moves in the direction of the motor
#define Y_DIR     6       //The y-axis moves in the direction of the motor
#define Z_DIR     7       //The z-axis moves in the direction of the motor
#define X_STP     2       //The x axis stepper control
#define Y_STP     3       //The y axis stepper control
#define Z_STP     4       //The z axis stepper control
#define A_DIR     13      //The a axis moves in the direction of the motor
#define A_STP     12      //The a axis stepper control
#define POS_Z_LIM 8   //The y axis pos limit switch
#define NEG_Z_LIM 9   //The y axis neg limit switch

  int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
  int relativePosition = 0;
  int stepsCMD = 0;
  int distance = 0;
  bool dirStatus = true;
/*
//function: step function: control step motor direction, step number.
//parameter: the dir direction control, dirPin corresponds to the step of the step motor's dir, stepperPin corresponds to step by step of the step motor, steps forward
//no return value

// 3-1-2019 NEMA 23 fastest acceleration is 700/150-1 @ 24V on A4988, 800/140-5 works too.
    // NEMA 23 fastest acceleration with MP6500 is 600/100-1 @ 24V
*/
void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{          
      int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
 
      digitalWrite(dirPin, dir);
//      delay(1);  
     if(!digitalRead(POS_Z_LIM) || !digitalRead(NEG_Z_LIM)){
        digitalWrite(dirPin, !dir);
        delayCount = 500;
         for (int i = 0; i < 100; i++) {
          digitalWrite(EN, LOW);  // Low enable provides power to all motors
          digitalWrite(stepperPin, HIGH);
          delayMicroseconds(delayCount);
          digitalWrite(stepperPin, LOW);
          delayMicroseconds(delayCount); 
          digitalWrite(EN, HIGH); // High enable removes power from all motors
         }
      }
      else{
          for (int i = 0; ((i < steps) && (digitalRead(POS_Z_LIM)) && (digitalRead(NEG_Z_LIM))); i++) {
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors

            (delayCount > 200) ? delayCount -= 1 : delayCount -= 0;
         
                  if(!digitalRead(POS_Z_LIM) || !digitalRead(NEG_Z_LIM)){
                   digitalWrite(dirPin, !dir);
                   delayCount = 500;
                   for (int i = 0; i < 500; i++) {
                    digitalWrite(EN, LOW);  // Low enable provides power to all motors
                      digitalWrite(stepperPin, HIGH);
                      delayMicroseconds(delayCount);
                      digitalWrite(stepperPin, LOW);
                      delayMicroseconds(delayCount); 
                    digitalWrite(EN, HIGH); // High enable removes power from all motors
                     }
                  break;
                  }
         }
      }
      
}

void setup()
{
  Serial.begin(9600);
  pinMode(POS_Z_LIM, INPUT_PULLUP);
  pinMode(NEG_Z_LIM, INPUT_PULLUP);
  pinMode(A_DIR, OUTPUT); pinMode(A_STP, OUTPUT);
  pinMode(X_DIR, OUTPUT); pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT); pinMode(Y_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT); 

//  digitalWrite(EN, LOW);  // Low enable provides power to all motors

// step(true, Z_DIR, Z_STP, 1000); //The X axis motor reversals 1 circle, 200 steps for a circle
 step(false,Z_DIR, Z_STP, 4500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(true, X_DIR, X_STP, 3500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(false,X_DIR, X_STP, 3500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(true, Y_DIR, Y_STP, 500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(false,Y_DIR, Y_STP, 500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(true, Z_DIR, Z_STP, 500); //The X axis motor reversals 1 circle, 200 steps for a circle
// step(false,Z_DIR, Z_STP, 500); //The X axis motor reversals 1 circle, 200 steps for a circle
  
//  digitalWrite(EN, HIGH); // High enable removes power from all motors

}
void loop(){

//  if(Serial.available() > 0){
//    stepsCMD = Serial.parseInt();
//    distance = stepsCMD - relativePosition;
//    Serial.println(relativePosition);
//  }
//
//    if(distance > 0){
//       digitalWrite(Z_DIR, true);
//       dirStatus = true;
//    }
//    else{
//        digitalWrite(Z_DIR, false);
//        dirStatus = false;
//    }
//    int absdistance = abs(distance);
//    
//    while(absdistance > 0 && digitalRead(9)){
////    digitalWrite(EN, LOW);  // Low enable provides power to all motors
////        digitalWrite(Z_STP, HIGH);
////        delayMicroseconds(delayCount);
////        digitalWrite(Z_STP, LOW);
////        delayMicroseconds(delayCount);  
//////        
//        Serial.println(absdistance);
//        absdistance--;        
//////        (delayCount > 500) ? delayCount -= 1 : delayCount -= 0;
////    digitalWrite(EN, HIGH); // High enable removes power from all motors
//    }
//      relativePosition = stepsCMD;
//      Serial.println(relativePosition);
}
