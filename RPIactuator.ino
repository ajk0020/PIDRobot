#define EN 8
#define X_DIR 5
#define X_STP 2


void step(boolean dir, byte dirPin, byte stepperPin, int steps){
  int delayCount = 600;
  digitalWrite(dirPin, dir);
  delay(1);
  for (int i = 0; i < steps; i++){
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(delayCount);
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(delayCount);

    if (delayCount > 300)
      delayCount -= 5;
  }
}

void setup() {
 Serial.begin(9600);
 pinMode(X_DIR,OUTPUT); pinMode(X_STP, OUTPUT);
 pinMode(EN,OUTPUT);
// digitalWrite(EN,HIGH);
}

void loop() {
    while(Serial.available() > 0) {
     int x = Serial.parseInt();  
//    if(Serial.read() == '\n'){
//     Serial.print("X");/
     Serial.println(x, DEC);
   
       digitalWrite(EN, LOW);
       step(true,X_DIR,X_STP,x);
       step(false,X_DIR,X_STP,x);
       digitalWrite(EN,HIGH);
   
//      }
    }
}
