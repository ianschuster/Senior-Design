#include <Servo.h>

Servo yservo;  Servo xservo; // servos for x and y
//set initial values for x and y
int ypos = 0;
int xpos= 0;
const int laser=3; //pin value for laser
int L = 0;

void setup(){
  pinMode(laser, OUTPUT);
  digitalWrite(laser, LOW); //turn off the laser
  xservo.attach(8); //pin for the x servo
  yservo.attach(4);  //pin for the y servo

  Serial.begin(115200); // 115200 is the rate of communication
}

void loop() {
  static int v = 0; // value to be sent to the servo (0-180)
  if ( Serial.available()) {
    char ch = Serial.read(); // read in a character from the serial port and assign to ch
    switch(ch) { // switch based on the value of ch
      case '0'...'9': // if it's numeric
        v = v * 10 + ch - '0';
        /*
           so if the chars sent are 45x (turn x servo to 45 degs)..
           v is the value we want to send to the servo and it is currently 0
           The first char (ch) is 4 so
           0*10 = 0 + 4 - 0 = 4;
           Second char is 4;
           4*10 = 40 + 5 = 45 - 0 = 45;
           Third char is not a number(0-9) so we  drop through...
        */
        break;
      case 'x': // if it's x
      /*
       ....and land here
       where we send the value of v which is now 45 to the x servo
       and then reset v to 0
      */
        xservo.write(v);
        Serial.println("x: " + v);
        v = 0;
        break;
      case 'y':
        yservo.write(v);
        Serial.println("y: " + v);
        v = 0;
        break;
      case 'L':
        if(L == 0){
          L = 1;
          digitalWrite(laser, HIGH);
          Serial.println("laser on");
        }
        else if(L == 1){
          L = 0;
          digitalWrite(laser, LOW);
          Serial.println("laser off");
        }
        break;
    }
  }
}
