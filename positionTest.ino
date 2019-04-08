
 void setup() {
 Serial.begin(9600);
// Serial.setTimeout(10);
}

void loop() {
    while(Serial.available() > 0) {
      int x = Serial.parseInt();    
  
//       Serial.flush();
     if(Serial.read()){
      
      Serial.print("X");
      Serial.println(x);
    }
   }
}
