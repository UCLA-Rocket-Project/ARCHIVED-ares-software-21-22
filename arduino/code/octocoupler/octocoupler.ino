#include <MCP23S17.h>

#define NVALVES 16

MCP23S17 io(&SPI, 10, 0);
byte values[NVALVES];

void setup()
{
  Serial.begin(115200);
  io.begin();
  for (int i = 0; i < NVALVES; i++)
  {
    io.pinMode(i, INPUT_PULLUP);
  }
  /*
  for (int i = 0; i < NVALVES; i++)
  {
    values[i] = io.digitalRead(i);
  }
  */
}

void loop() {
  for (int i = 0; i < NVALVES; i++)
  {
    char value = io.digitalRead(i);
    /*
    if (value != values[i])
    {
      Serial.print("Value changed!");
      values[i] = value;
    }
    */
    Serial.print(value);
    Serial.print(",");
  }
  
  Serial.print('\n');
}
