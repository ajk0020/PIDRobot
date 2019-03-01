
 void setup() {
 Serial.begin(9600);
// Serial.setTimeout(10);
}

void loop() {
    while(Serial.available() > 0) {
      int x = Serial.parseInt();    
        int y = Serial.parseInt(); 
          int z = Serial.parseInt(); 
//       Serial.flush();
     if(Serial.read()){
      
      Serial.print("X");
      Serial.print(x, DEC);
          
      Serial.print("Y");
      Serial.print(y, DEC);
     
      Serial.print("Z");
      Serial.println(z, DEC);
    }
   }
}
