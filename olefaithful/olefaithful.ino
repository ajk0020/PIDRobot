///////// CNC Shield for Arduino UNO test //////////

/*
 * Defined are the pins associated with the CNC Shield
 */
 
#define X_EN        22       //The step motor makes the power end, low level is effective
#define Y_EN        28       //The step motor makes the power end, low level is effective
#define Z_EN        32       //The step motor makes the power end, low level is effective
#define A_EN        30       //The step motor makes the power end, low level is effective
#define X_DIR     26       //The x-axis moves in the direction of the motor
#define Y_DIR     6       //The y-axis moves in the direction of the motor
#define Z_DIR     36       //The z-axis moves in the direction of the motor
#define X_STP     24       //The x axis stepper control
#define Y_STP     3       //The y axis stepper control
#define Z_STP     34       //The z axis stepper control
#define A_DIR     13      //The a axis moves in the direction of the motor
#define A_STP     12      //The a axis stepper control
#define POS_X_LIM 10   //The y axis pos limit switch
#define NEG_X_LIM 9   //The y axis neg limit switch
#define POS_Z_LIM 11   //The y axis pos limit switch
#define NEG_Z_LIM 53   //The y axis neg limit switch


int ZrelativePosition = 0;
int oldZ = 0;
int XrelativePosition = 0;
int oldx = 0;

void setup()
{
  
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(POS_Z_LIM, INPUT_PULLUP);
    pinMode(NEG_Z_LIM, INPUT_PULLUP);
      pinMode(POS_X_LIM, INPUT_PULLUP);
        pinMode(NEG_X_LIM, INPUT_PULLUP);
  pinMode(A_DIR, OUTPUT); pinMode(A_STP, OUTPUT);
    pinMode(Z_DIR, OUTPUT); pinMode(Z_STP, OUTPUT);
      pinMode(X_DIR, OUTPUT); pinMode(X_STP, OUTPUT);
        pinMode(Y_DIR, OUTPUT); pinMode(Y_STP, OUTPUT);
  pinMode(X_EN, OUTPUT); 
    pinMode(Y_EN, OUTPUT); 
      pinMode(Z_EN, OUTPUT); 
        pinMode(A_EN, OUTPUT); 
  digitalWrite(X_EN, HIGH);
    digitalWrite(Y_EN, HIGH);
      digitalWrite(Z_EN, HIGH);
        digitalWrite(A_EN, HIGH);
//  centerPositionX();
  centerPositionZ();
     
}

void loop() {
    
    while(Serial.available() > 0) {
//      char termX = '$';
//      String numX = Serial.readStringUntil(termX);
//      numX = Serial.readStringUntil(termX);
//      //int x = Serial.parseInt();    
//     int x = numX.toInt();
     
      char termZ = '<';
      String numZ = Serial.readStringUntil(termZ);
      numZ = Serial.readStringUntil(termZ);
      //int x = Serial.parseInt();    
     int Z = numZ.toInt();
     if(Z != 999){
     Z = Z-150;
     Z = 150-Z;
     }
//    Serial.print("Z NUM ");
//    Serial.println(Z);
    if(Serial.read()){
      
      //Serial.print("X");
      //Serial.println(x); 
//  
//      
//      if((x <= 300) && (x > 0))
//      {
//        //Serial.println("moving");
//        stepX(A_DIR, A_STP, A_EN, x*9); //The X axis motor reversals 1 circle, 200 steps for a circle
//        //Serial.println("done");
//      }
//      else if (x == 999){
//        XstepHIT(Z_DIR, Z_STP, Z_EN, 500);
//      }
      
      if((Z <= 300) && (Z > 0))
      {
        //Serial.println("moving");
        stepZ(Y_DIR, Y_STP, Y_EN, Z*9); //The X axis motor reversals 1 circle, 200 steps for a circle
        //Serial.println("done");
      }
      else if (Z == 999){
        ZstepHIT(X_DIR, X_STP, X_EN, 500);
      }
       //step(Z_DIR, Z_STP, 1); //The X axis motor reversals 1 circle, 200 steps for a circle
    }  
    Serial.println(XrelativePosition);
//        Serial.println(ZrelativePosition);
   }
   //if(relativePosition != 1350)
      //step(A_DIR, A_STP, 1350); 
   //Serial.write(relativePosition);
}

void stepX(byte dirPin, byte stepperPin, byte enablePin, int steps)
{   
      
      bool dir;
      int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      int distance = steps - XrelativePosition;
      XrelativePosition = steps;
       
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

      if((!digitalRead(POS_X_LIM))|| (!digitalRead(NEG_X_LIM)))
        backoffX(dirPin, stepperPin, enablePin);
      
      while((distance > 0)){
        if((digitalRead(POS_X_LIM)) && (digitalRead(NEG_X_LIM))){         // if limit switches are open
           digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
          
          distance--;
        }
        else{
          backoffX(dirPin, stepperPin, enablePin);
          distance = -1;
          }
        
        (delayCount > 200) ? delayCount -= 1 : delayCount -= 0;
      }
     
}

void stepZ(byte dirPin, byte stepperPin, byte enablePin, int steps)
{   
      
      bool dir;
      int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      int distance = steps - ZrelativePosition;
      ZrelativePosition = steps;
       
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
        backoffZ(dirPin, stepperPin, enablePin);
      
      while((distance > 0)){
        if((digitalRead(POS_Z_LIM)) && (digitalRead(NEG_Z_LIM))){         // if limit switches are open
           digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
          
          distance--;
        }
        else{
          backoffZ(dirPin, stepperPin, enablePin);
          distance = -1;
          }
        
        (delayCount > 300) ? delayCount -= 1 : delayCount -= 0;
      }
//     Serial.println(ZrelativePosition);
}

void XstepHIT(byte dirPin, byte stepperPin, byte enablePin, int steps)
{   
      if(XrelativePosition >= 1350)
        digitalWrite(dirPin, false);
      else
        digitalWrite(dirPin, true);
     
      int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      
      for(int i = 0; i < steps; i++){
           digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
        }        
        (delayCount > 300) ? delayCount -= 1 : delayCount -= 0;
     
}

void ZstepHIT(byte dirPin, byte stepperPin, byte enablePin, int steps)
{   
      if(ZrelativePosition >= 1350)
        digitalWrite(dirPin, false);
      else
        digitalWrite(dirPin, true);
     
      int delayCount = 500; // we start accelerating at 10 rpm, 1/(delayE-6*200steps)
      
      for(int i = 0; i < steps; i++){
           digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
        }        
        (delayCount > 300) ? delayCount -= 1 : delayCount -= 0;
     
}


void centerPositionX(){
  
  int delayCount = 600;
  digitalWrite(A_DIR, true);
  delay(1);
  
   do {
           digitalWrite(A_EN, LOW);  // Low enable provides power to all motors
            digitalWrite(A_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(A_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(A_EN, HIGH); // High enable removes power from all motors
   } while(digitalRead(POS_X_LIM));
   
   if(!digitalRead(POS_X_LIM)){
    XrelativePosition = 0;
    digitalWrite(A_DIR, false);
    for(int c = 0; c < 1350; c++){
           digitalWrite(A_EN, LOW);  // Low enable provides power to all motors
            digitalWrite(A_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(A_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(A_EN, HIGH); // High enable removes power from all motors

        XrelativePosition++;
    } 
   }
//   Serial.println(XrelativePosition);
}


void centerPositionZ(){
  
  int delayCount = 600;
  digitalWrite(Y_DIR, true);
  delay(1);
  
   do {
           digitalWrite(Y_EN, LOW);  // Low enable provides power to all motors
            digitalWrite(Y_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(Y_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(Y_EN, HIGH); // High enable removes power from all motors
   } while(digitalRead(POS_Z_LIM));
   
   if(!digitalRead(POS_Z_LIM)){
   ZrelativePosition = 0;
    digitalWrite(Y_DIR, false);
    for(int c = 0; c < 1350; c++){
           digitalWrite(Y_EN, LOW);  // Low enable provides power to all motors
            digitalWrite(Y_STP, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(Y_STP, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(Y_EN, HIGH); // High enable removes power from all motors

        ZrelativePosition++;
    } 
   }
//   Serial.println(ZrelativePosition);
}


void backoffX(byte dirPin, byte stepperPin, byte enablePin){
  int delayCount = 600;
    if(!digitalRead(POS_X_LIM)){
      digitalWrite(dirPin, false);
      XrelativePosition = 2690;
    }
    else if(!digitalRead(NEG_X_LIM)){
      digitalWrite(dirPin, true);
      XrelativePosition = 10;
    }
    delay(1);
    
          for(int i = 0; i < 10; i++){
             digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
          }
}

void backoffZ(byte dirPin, byte stepperPin, byte enablePin){
  int delayCount = 600;
    if(!digitalRead(POS_Z_LIM)){
      digitalWrite(dirPin, false);
      ZrelativePosition = 2690;
    }
    else if(!digitalRead(NEG_Z_LIM)){
      digitalWrite(dirPin, true);
      ZrelativePosition = 10;
    }
    delay(1);
    
          for(int i = 0; i < 10; i++){
             digitalWrite(enablePin, LOW);  // Low enable provides power to all motors
            digitalWrite(stepperPin, HIGH);
            delayMicroseconds(delayCount);
            digitalWrite(stepperPin, LOW);
            delayMicroseconds(delayCount);      
           digitalWrite(enablePin, HIGH); // High enable removes power from all motors
          }
}
