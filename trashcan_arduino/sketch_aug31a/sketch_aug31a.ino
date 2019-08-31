#include <Servo.h>

Servo bottomservo;
Servo topservo;

int angle = 0;
int angle_t = 0;
void setup() 
{
  topservo.attach(9);
  bottomservo.attach(8);
  
  Serial.begin(9600);
  bottomservo.write(0);
  topservo.write(0);
  angle = 0;
  angle_t = 0;
  
}
z

void loop() 
{
  if (Serial.available())
  {
    int i = Serial.parseInt();
    Serial.println(i);
    switch(i)
    {
        case 1:
          for(int i = angle; i >= 0; i--){bottomservo.write(i);delay(8);}angle = 0;
          break;
          
        case 2: 
          if(angle >=89){for (int i = angle; i >= 89; i--){ bottomservo.write(i);delay(8);} angle = 89;}
          else if(angle <89){for (int i = angle; i < 89; i++){bottomservo.write(i);delay(8);}angle = 89;}
           break;
           
        case 3: 
          for(int i = angle; i <= 179; i++){bottomservo.write(i);delay(8);}angle = 179;
          break;
          
        case 4: 
          for(int i = angle_t; i >= 0; i--){topservo.write(i);delay(15);}angle_t = 0;
          break;
          
        case 5: 
          for(int i = angle_t; i <= 97; i++){topservo.write(i);delay(15);}angle_t = 97;
          break;
    }
  }
}
