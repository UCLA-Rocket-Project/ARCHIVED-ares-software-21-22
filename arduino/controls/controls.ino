#include <MCP23S17.h>

#define NVALVES 16
#define BUFFER 500

char command[BUFFER];
int i = 0;
int pins[NVALVES] = {11, 13, 6, 13, 13, 4, 3, 12, 8, 10, 5, 13, 2, 7, 13, 9};

void setup()
{
  Serial.begin(9600);
  for (int i = 0; i < 14; i++)
  {
    pinMode(i, OUTPUT);
    digitalWrite(i, HIGH);
  }
}

void loop()
{
  if (i == BUFFER)
  {
    i = 0;
  }
  
  if (Serial.available() > 0)
  {
    command[i] = Serial.read();
    i++;
    
    if (command[i - 1] == '\n')
    {
      for (int j = 0; j < i; j++)
      {
        Serial.print(command[j]);
      }
      i--;

      if (i == NVALVES + 2 && command[0] == 'S' && command[i - 1] == 'E')
      {
        for (int j = 1; j < i - 1; j++)
        {
          int pin = pins[j - 1];
          if (command[j] == '1')
          {
            digitalWrite(pin, LOW);
          }
          else
          {
            digitalWrite(pin, HIGH);
          }
        }
      }
      i = 0;
    }
  }
}
