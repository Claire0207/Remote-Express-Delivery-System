#include "qxmbot1.h"



QXMBOT_cloudServo G_QXMBOT_cloudServo1(9, OUTPUT);



QXMBOT1_buzzer g_QXMBOT1_buzzer1(A3);



QXMBOT1_motor  g_QXMBOT1_CarControl(2, 3, 4, 7, 5, 6);



void IR_Tracking() {

  if (HIGH == digitalRead(11) && HIGH == digitalRead(8)) {

    g_QXMBOT1_CarControl.QXMBOT1_arCarForward(110, 110);



  } else if (LOW == digitalRead(11) && HIGH == digitalRead(8)) {

    g_QXMBOT1_CarControl.QXMBOT1_arCarRight(120, 110);

  } else if (HIGH == digitalRead(11) && LOW == digitalRead(8)) {

    g_QXMBOT1_CarControl.QXMBOT1_arCarLeft(110, 120);

  }

}



QXMBOT_SR04  g_QXMBOT_SR04Ult1(A4, A5);



QXMBOT1_trackSensor  g_QXMBOT1_trackSensor1(11, 8);



void setup()

{

  G_QXMBOT_cloudServo1.cloudServoContrl(90,100);

  g_QXMBOT1_buzzer1.buzzerOFF(A3);

  pinMode(11, INPUT);

  pinMode(8, INPUT);

}



void loop()

{

  if (g_QXMBOT_SR04Ult1.QXMBOT_getDistance() < 30) {

    g_QXMBOT1_buzzer1.buzzerON(A3);

    g_QXMBOT1_CarControl.QXMBOT1_arCarStops(110, 110);

    delay(60);

    while (g_QXMBOT_SR04Ult1.QXMBOT_getDistance() < 30) {

      delay(60);

    }

    g_QXMBOT1_buzzer1.buzzerOFF(A3);

    if ((LOW == g_QXMBOT1_trackSensor1.getTrackStatus_L()) && (LOW == g_QXMBOT1_trackSensor1.getTrackStatus_R())) {

      g_QXMBOT1_CarControl.QXMBOT1_arCarStops(110, 110);



    }



  } else {

    for (int i = 1; i <= 3600; i = i + (1)) {

      IR_Tracking();

    }



  }



}