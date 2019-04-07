/* limit switch test */
#define neglim 10
#define poslim 9
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(neglim, INPUT_PULLUP);
  pinMode(poslim, INPUT_PULLUP);
}

// the loop routine runs over and over again forever:
void loop() {
  if(digitalRead(neglim) == LOW)
    Serial.print("LOW");
  else
    Serial.print("HIGH");
  if(digitalRead(poslim) == LOW)
    Serial.println("\tLOW");
  else
    Serial.println("\tHIGH");
}
