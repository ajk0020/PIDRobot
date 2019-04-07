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
#define POS_Z_LIM 10   //The y axis pos limit switch
#define NEG_Z_LIM 9   //The y axis neg limit switch

int relativePosition = 0;

void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{          
      int delayCount = 600; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      int distance = steps - relativePosition;
     
      if(distance > 0){
         digitalWrite(Z_DIR, true);
      }
      else{
          digitalWrite(Z_DIR, false);
      }
      distance = abs(distance);
      
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
//       for (int i = 0; ((i < steps) && (digitalRead(POS_Z_LIM)) && (digitalRead(NEG_Z_LIM))); i++) {
          
      while((distance > 0) && (digitalRead(POS_Z_LIM)) && (digitalRead(NEG_Z_LIM))){
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors
          
          distance--;
      }
//            (delayCount > 300) ? delayCount -= 1 : delayCount -= 0;
            
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
//                  break;
                  }
                  Serial.print("RelPos: ");
                  Serial.println(relativePosition);
}

void centerPosition(){
  int delayCount = 600;
  digitalWrite(A_DIR, true);
  
  while(digitalRead(POS_Z_LIM)) {
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(A_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(A_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors
   }
   
   if(!digitalRead(POS_Z_LIM)){
    relativePosition = 0;
    digitalWrite(A_DIR, false);
    for(int c = 0; c < 1350; c++){
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(A_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(A_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors

        relativePosition++;
    } 
   }
}

void setup()
{
  Serial.begin(9600);
  pinMode(POS_Z_LIM, INPUT_PULLUP);
  pinMode(NEG_Z_LIM, INPUT_PULLUP);
  pinMode(A_DIR, OUTPUT); pinMode(A_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT); 
  
  centerPosition();
     
}

void loop() {
    while(Serial.available() > 0) {
      int x = Serial.parseInt();    
     
     if(Serial.read()){

      Serial.print("X");
      Serial.println(x, DEC);
      
      step(true,A_DIR, A_STP, x); //The X axis motor reversals 1 circle, 200 steps for a circle

    }
   }
}
