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

void setup()
{
  Serial.begin(9600);
  pinMode(POS_Z_LIM, INPUT_PULLUP);
  pinMode(NEG_Z_LIM, INPUT_PULLUP);
  pinMode(A_DIR, OUTPUT); pinMode(A_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT); 
  digitalWrite(EN, HIGH);
  
  centerPosition();
     
}

void loop() {
    while(Serial.available() > 0) {
      int x = Serial.parseInt();    
     
    if(Serial.read()){
      Serial.print("X");
      Serial.println(x, DEC); 
    }
     step(A_DIR, A_STP, x*9); //The X axis motor reversals 1 circle, 200 steps for a circle  
   }
   
   if(relativePosition != 1350)
      step(A_DIR, A_STP, 1350); 
   
   Serial.print("RelPos: ");
   Serial.println(relativePosition);
}

void step(byte dirPin, byte stepperPin, int steps)
{          
      bool dir;
      int delayCount = 700; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      int distance = steps - relativePosition;
      relativePosition = steps;
       
      if(distance > 0){
         digitalWrite(dirPin, true);
//         delay(1);
         dir = true;
//         Serial.println("TRUE DIR");
      }
      else{
          digitalWrite(dirPin, false);
//          delay(1);
          dir = false;
//          Serial.println("FALSE DIR");
      }
      distance = abs(distance);
//      Serial.print("Distance: ");
//      Serial.println(distance);

      if((!digitalRead(POS_Z_LIM))|| (!digitalRead(NEG_Z_LIM)))
        backoff(dirPin, stepperPin);
      
      while((distance > 0)){
        if((digitalRead(POS_Z_LIM)) && (digitalRead(NEG_Z_LIM))){         // if limit switches are open
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors
          
          distance--;
        }
        else{
          backoff(dirPin, stepperPin);
          distance = -1;
          }
        
        (delayCount > 300) ? delayCount -= 1 : delayCount -= 0;
      }
}

void centerPosition(){
  
  int delayCount = 600;
  digitalWrite(A_DIR, true);
  delay(1);
  
   do {
           digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(A_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(A_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors
   } while(digitalRead(POS_Z_LIM));
   
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
   Serial.print("RelPos: ");
   Serial.println(relativePosition);
}

void backoff(byte dirPin, byte stepperPin){
  int delayCount = 600;
    if(!digitalRead(POS_Z_LIM)){
      digitalWrite(dirPin, false);
      relativePosition = 2690;
    }
    else if(!digitalRead(NEG_Z_LIM)){
      digitalWrite(dirPin, true);
      relativePosition = 10;
    }
    delay(1);
    
          for(int i = 0; i < 10; i++){
             digitalWrite(EN, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(EN, HIGH); // High enable removes power from all motors
          }
}
