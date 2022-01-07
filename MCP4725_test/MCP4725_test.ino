#include <Wire.h>

#include <MCP4725.h>

MCP4725 DAC(0x60);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(-1);
  //Serial.println("Hello!");

  Wire.begin();
  DAC.begin();

  if(DAC.isConnected()){
    Serial.println("DAC connected");
  }
  else{
    Serial.println("Error");
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned int val = Serial.readStringUntil('\n').toInt();

  if(val > 4095 || val<0){
    Serial.println("Wrong value");
  }
  else{
    Serial.println("Value set");
    DAC.setValue(val);
  }
}
