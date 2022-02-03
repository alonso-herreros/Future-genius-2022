// C++ code
//

int ledPin = 13;				//Define led control pin
int tempSensorPin = 0;			//Define tmp sensor reading pin
float overheatingLimit = 35;	//Define overheating limit temperature

float offset_mV = 0.5 * 1000.0;
float mV_per_C = 10.0;

//This function runs once when you turn your Arduino on
void setup()
{
  //by default all pins are input pins, so we don�t need to
  //define the temp sensor pin as input

  pinMode(ledPin, OUTPUT);	//Define the led pin as output pin
  Serial.begin(9600);		//Start the communications with the serial monitor
  							//where temperature reading will be displayed
}

void loop()
{
  //Compute the temperature value from the temperature sensor reading
  int reading = analogRead(tempSensorPin);          //read the sensor's 'analog port value

  float voltage_mV = reading * (5000.0/1024.0);	    //scale the value to obtain the millivolts reading value
  float voltage_V = voltage_mV/1000.0;		        //convert from mV to V

  float temperature_C = (voltage_mV - offset_mV) / mV_per_C; // use offset and scaling to get temperature


  //Display the temperature and the voltage value in the serial monitor
  Serial.print("Voltage = " + String(voltage_V) + " V\n");
  Serial.print("Temperature = " + String(temperature_C) + " C\n");
  delay(1000); // Wait for 200 millisecond(s), to make the displayed values look nicer
  
  //Turn on the alarm led if the temperature is above the overheating limit
  if(temperature_C > overheatingLimit)
  {
    digitalWrite(ledPin, HIGH);
  }
  else  //Turn off the alarm led if the temperature is under the overheating limit
  {
    digitalWrite(ledPin, LOW);
  }
}