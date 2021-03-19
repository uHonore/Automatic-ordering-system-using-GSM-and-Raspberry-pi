#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); //Initialize the lcd 
SoftwareSerial nss(0, 9); // (RX, TX);

const int buttonPin = 8;
int dailyOrders = 0;
int buttonState = 0;

void setup()

{

  pinMode (buttonPin, INPUT);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // serial port communications from Arduino to Bluetooth module H05 // Bluetooth module defaults to 115.2k BAUD. Change to 57.6k BAUD.
  nss.begin(57600);
  Serial.begin(57600);
  //clear parallel LCD and set the cursor to the first row, first column.
  lcd.clear();

  lcd.setCursor(0, 0);
}
// enter the code to run continuously void loop() { char x; //set a data of type char char y;//set a data of type char

if (nss.available()){ // check if serial data are available 
  
  x=Serial.read(); // read the incoming data
} 

if (x=='m'){ // check if the incoming data is m 
  
  nss.print("1.UMUCERI"); // print to bluetooth serial 
  
  lcd.setCursor(0,0); //set cursor to the first row,first column 
  
  lcd.print("order coming"); //print to the LCD screen
} else if(x=='1')

{ // check if the 2nd data is 1 
  
  nss.print("press 1 to confirm"); // print to bluetooth serial
} y=Serial.read(); // 

if(y=='1'){ 
  
  nss.println("1.UMUCERI confirmed");
}
lcd.clear(); 

lcd.setCursor(0,0); 

lcd.print("1.UMUCERI"); 

lcd.setCursor(0,1); 

lcd.print("Order Confirmed");
} else if(x=='2'){ 
  
  nss.println("press 2 to confirm");
} 

y=Serial.read();
if(y=='2'){
nss.println("2.UBUGARI confirmed");
lcd.clear(); 

lcd.setCursor(0,0); 

lcd.print("2.UBUGARI"); 

lcd.setCursor(0,1); 

lcd.print("Order Confirmed");

}
buttonState= digitalRead (buttonPin); 

if( buttonState==LOW)
{ dailyOrders++; 

lcd.clear(); 

lcd.setCursor(0,0); 

lcd.print("Order Served"); 

delay(5000); lcd.clear (); 

lcd.print("daily Orders="); 

lcd.println(dailyOrders);
}
