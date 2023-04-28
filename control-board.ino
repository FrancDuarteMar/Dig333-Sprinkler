#include <SoftwareSerial.h>

SoftwareSerial HC12(10, 11);  // HC-12 TX Pin, HC-12 RX Pin
int incByte = 0;
char text[4] = "";
int mainPower = 22;
int power1 = 23;
int power2 = 24;
int power3 = 25;

void setup() {
  Serial.begin(9600);  // Serial port to computer
  HC12.begin(9600);    // Serial port to HC12
  pinMode(mainPower, OUTPUT);
  digitalWrite(mainPower, LOW);
  pinMode(power1, OUTPUT);
  digitalWrite(power1, LOW);
  pinMode(power2, OUTPUT);
  digitalWrite(power2, LOW);
  pinMode(power3, OUTPUT);
  digitalWrite(power3, LOW);
}

void loop() {
  while (HC12.available() > 0) {
    String data = HC12.readStringUntil('\n');

    if (data == "1") {
      Serial.println("Open 1");
      digitalWrite(mainPower, !digitalRead(mainPower));
      Serial.print("Current Status for pin 22 aka main power: ");
      Serial.println(digitalRead(mainPower));
    }
    if (data == "2") {
      Serial.println("Open 2");
      digitalWrite(power1,!digitalRead(power1));
      Serial.print("Current Status for pin 23 aka Power 1: ");
      Serial.println(digitalRead(power1));
    }
    if (data == "3") {
      Serial.println("Open 3");
      digitalWrite(power2,!digitalRead(power2));
      Serial.print("Current Status for pin 24 aka Power 2: ");
      Serial.println(digitalRead(power2));
    }
    if (data == "4") {
      Serial.println("Open 4");
      digitalWrite(power3,!digitalRead(power3));
      Serial.print("Current Status for pin 25 aka Power 3: ");
      Serial.println(digitalRead(power3));
    }
    Serial.println(data);
    
  }

}