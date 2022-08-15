#include <BfButton.h>
#include <BfButtonManager.h>

int btnPin = 3;
int DT = 4;
int CLK = 5;

BfButton btn(BfButton::STANDALONE_DIGITAL, btnPin, true, LOW);

int counter = 0;
int angle = 0;
int aState;
int aLastState;

//Press of a button
void pressHandler (BfButton *btn, BfButton::press_pattern_t pattern) {
  switch (pattern) {
    case BfButton::SINGLE_PRESS:
      Serial.println("x");
      break;

    case BfButton::DOUBLE_PRESS:
      Serial.println("y");
      break;

    case BfButton::LONG_PRESS:
      Serial.println("z");
      break;
  }
}




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.println(angle);
  Serial.println(0);
  pinMode(CLK, INPUT_PULLUP);
  pinMode(DT, INPUT_PULLUP);
  aLastState = digitalRead(CLK);

  //Button Settings
  btn.onPress(pressHandler)
  .onDoublePress(pressHandler)
  .onPressFor(pressHandler, 1000);

}

void loop() {
  // put your main code here, to run repeatedly:
  //wait for button-press to excecute command
  btn.read();

  aState = digitalRead(CLK);

  //encoder rotator tracking
  if (aState != aLastState) {
    if (digitalRead(DT) != aState) {
      counter++;
      angle++;
    }
    else {
      counter--;
      angle--;
    }
    if (counter >= 1) {
      counter = 1;
    }
    if (counter <= -1) {
      counter = -1;
    }
    Serial.println(counter);
    //Serial.println(1);
  }
  aLastState = aState;

}
