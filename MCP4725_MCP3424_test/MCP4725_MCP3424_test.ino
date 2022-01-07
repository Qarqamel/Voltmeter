#include <Wire.h>
#include <MCP342x.h>
#include <MCP4725.h>

uint8_t address = 0x68;
MCP342x adc = MCP342x(address);

MCP4725 dac(0x60);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(-1);
  Wire.begin();

  MCP342x::generalCallReset();
  delay(1);
  Wire.requestFrom(address, (uint8_t)1);
  if(Wire.available()){
    Serial.println("ADC connected");
  }
  else{
    Serial.println("Error");
  }
  
  dac.begin();
}

void loop() {
  unsigned int val = Serial.readStringUntil('\n').toInt();
  
  if(val > 4095 || val<0){
    Serial.println("Wrong value");
  }
  else{
    Serial.println("Value set");
    dac.setValue(val);
  }

  long value = 0;
  MCP342x::Config stat;

  uint8_t error = adc.convertAndRead(MCP342x::channel1, MCP342x::oneShot,
                                     MCP342x::resolution18, MCP342x::gain1,
                                     1000000, value, stat);
  if(error){
    Serial.println(error);
  }
  else{
    Serial.println(value);
  }
}
