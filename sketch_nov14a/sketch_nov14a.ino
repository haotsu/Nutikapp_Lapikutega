#include <f401reMap.h>
#include <Wire.h>

//int a = pinMap(12);

void setup()
{
  //pinMode(a, OUTPUT);
  Wire.begin(12);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(sendData);      // Set up the function to call when master requests data
  Serial.begin(115200);           // start serial for output
}

void loop()
{
  
}
byte off = 0;
  byte no[3] = {3,4};
void sendData() {
   // Data to be sent to the master
  Serial.println(no[1]);
  Wire.write(no,3);  // Send the data to the master
}
// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  int x;
  while(0 < Wire.available()) // loop through all but the last
  {
    int c = Wire.read(); // receive byte as a character
    Serial.println(c);         // print the character
  }

  //Wire.beginTransmission(1); // transmit to device #
  //Wire.write(7);              // sends one byte  
  //Wire.endTransmission();    // stop transmitting

  //int x = Wire.read();    // receive byte as an integer
  //Serial.println(x);         // print the integer
}