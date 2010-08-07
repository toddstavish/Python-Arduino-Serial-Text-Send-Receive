/* Serial Text Sender
 * ------------------- 
 * Send text over a serial port.
 * Print out "arduino" and blink pin 13 LED every second.
 *
 */

int ledPin = 13;   // select the pin for the LED
int i=0;           // simple counter to show we're doing something

void setup()
{
  pinMode(ledPin,OUTPUT);    // declare the LED's pin as output
  Serial.begin(9600);        // connect to the serial port
}

void loop ()
{
  Serial.print(i++);
  Serial.println("arduino");  // print out arduino
  digitalWrite(ledPin, HIGH);
  delay(500);
  digitalWrite(ledPin, LOW);
  delay(500);
}
