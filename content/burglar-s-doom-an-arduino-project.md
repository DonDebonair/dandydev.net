Title: Burglar's Doom - An Arduino Project
Date: 2012-01-19 16:51
Category: Computer Science Projects
Tags: how-to, school, arduino, twitter
Slug: burglar-s-doom-an-arduino-project
Summary: Keeping my blog up-to-date, while being busy with Uni and work is harder than I anticipated. So when I can squeeze in a little moment to share some stuff here, I'm always happy when there's a long overdue subject waiting to be covered! Today, I'm gonna share the result of a litte project with you that I built a few months ago during one of the courses in my minor, Mobile Life. It's centered around the [Arduino](http://www.arduino.cc/ "Arduino") and I built it together with [my classmate](http://www.vandorp.biz/ "Daniel van Dorp"). Sadly, because University failed to order the right sensors, [none of our original ideas](http://dandydev.net/blog/experimenting-with-arduino "Experimenting with Arduino") came to fruition. Instead, we decided to put together a burglary alarm that notifies the victim through Twitter. It's called.... Burglar's Doom!

Keeping my blog up-to-date, while being busy with Uni and work is harder than I anticipated. So when I can squeeze in a little moment to share some stuff here, I'm always happy when there's a long overdue subject waiting to be covered! Today, I'm gonna share the result of a litte project with you that I built a few months ago during one of the courses in my minor, Mobile Life. It's centered around the [Arduino](http://www.arduino.cc/ "Arduino") and I built it together with [my classmate](http://www.vandorp.biz/ "Daniel van Dorp").
Sadly, because University failed to order the right sensors, [none of our original ideas](http://dandydev.net/blog/experimenting-with-arduino "Experimenting with Arduino") came to fruition. Instead, we decided to put together a burglary alarm that notifies the victim through Twitter. It's called.... Burglar's Doom!

For those not familiar with Arduino, it's a cheap hardware platform with a programmable EEPROM, that can be used to do a wide variety of tasks. There are [tons](http://arduino.cc/en/Main/Hardware "Official Shields") of [sensors](http://www.hacktronics.com/Arduino/Arduino-Shields/View-all-products.html "Arduino Shields") available that you can hook up to it, and it's programmed using a [language derived from C/C++](http://arduino.cc/en/Reference/HomePage "Arduino language"). This is done through a dedicated IDE you can download from the [Arduino website](http://www.arduino.cc/ "Arduino").

If you're anxious to see the end result, [you can watch it right away on YouTube](http://www.youtube.com/watch?v=lk9teViKdKc "Burglar's Doom Video"). Apologies in advance for the fact that I was so daft to record it in portrait mode.

### Hardware
Let's start by mentioning what boards & sensors we used:
- [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno "ArduinoUno"): This was our Arduino board
- [Ethernet Shield](http://arduino.cc/en/Main/ArduinoEthernetShield "Ethernet Shield"): Used for communicating with Twitter. It's of course also possible to use a WiFi shield here.
- [PIR Motion Sensor](http://www.sparkfun.com/products/8630 "Motion Sensor"): Detecting Burglar's and other baddies.
- Standard switch button for turning it on and off. It comes with the Arduino I believe.

We hooked it up using [a breadboard](http://www.sparkfun.com/products/8800 "BreadBoard"), which makes it easy to play around in a plug-and-play way. I don't have proper schematics, but I'm sure you can figure it out from the pictures I present here:

_Overview 1_
![](|filename|/images/img_20111025_152826.jpg)

_Overview 2_
![](|filename|/images/img_20111025_152843.jpg)

_Arduino & Ethernetshield_
![](|filename|/images/img_20111104_102727.jpg)

_Breadboard & PIR Motion Sensor_
![](|filename|/images/img_20111104_102708.jpg)

_Final Overview_
![](|filename|/images/img_20111104_102657.jpg)

The Ethernet Shield was hooked up to a regular, cheap Cisco Router. In order for the Ethernet Shield to be able to communicate with the Internet, you have to give it a static IP. You could also use the [Arduino EthernetDHCP Library](http://gkaindl.com/software/arduino-ethernet/dhcp "EthernetDHCP").

### Code
You might be wondering how we programmed it. If you scroll down, you'll see the complete source code, thoroughly commented to explain what's happening. We used the following libraries to make it work:
- [Ethernet](http://arduino.cc/en/Reference/Ethernet "Ethernet"): For communicating with the Internet
- [SPI](http://arduino.cc/en/Reference/SPI "SPI"): For communicating with the PIR Motion Sensor
- [Twitter](http://www.markkurossi.com/ArduinoTwitter/ "Twitter Library"): This one does the Twitter magick using 2-legged OAuth
- [EEPROM](http://arduino.cc/en/Reference/EEPROM "EEPROM"): Used by Twitter for writing to memory
- [CryptoSuite](https://github.com/Cathedrow/Cryptosuite "CryptoSuite"): Used by Twitter for building hashes the API requires
- [Time](http://arduino.cc/playground/Code/Time "Time"): Used by Twitter for validating API calls

It's important to note that there is in fact [another Twitter library for Arduino](http://arduino.cc/playground/Code/TwitterLibrary "Twitter"). The big difference is, that the one we used, doesn't rely on a third-party service or website to relay the tweets, while the other one does. The library we used, works like a normal "Twitter App" using OAuth to authenticate and sign it's requests. In order to do that, you have to generate a valid access token and secret. You can do that by using the Java program supplied on their website. But you can just as easily do what we did: Tweet from a dedicated Twitter handle to a configurable Twitter handle. The former can be anyone you want to mention, the latter is the same Twitter account you use to sign up for a developer application. That way, you can use the supplied access token and secret, that can be found [here](https://dev.twitter.com/apps "") when you click on your app.
Also, we hardcoded Twitter's IP address. Another option is to [use a DNS library](http://gkaindl.com/software/arduino-ethernet/dns "EthernetDNS").

### Burglars be doomed!
Without further a do, I present to you the end result and the source code:

<iframe width="600" height="437" src="http://www.youtube.com/embed/lk9teViKdKc" frameborder="0" allowfullscreen></iframe>

```cpp
/*
  Burglar's Doom
  
  A Twitter enhanced burglar's alarm
  with adjustable timed behaviour.
*/

#include <SPI.h>
#include <Ethernet.h>
#include <Twitter.h>
#include <sha1.h>
#include <Time.h>
#include <EEPROM.h>

/* Ethernet configuration */
uint8_t mac[6] = {  0x90, 0xA2, 0xDA, 0x00, 0x6E, 0x03 };
uint8_t ip[4] = { 192,168,1,20 };

/* Twitter connect through HTTP proxy */
uint8_t twitter_ip[4] = { 199, 59, 148, 87 };
uint16_t twitter_port = 80;

/* buffer for twitter operations. 
   Large enough to hold consumer and token secrets
*/
char buffer[512];

char messagebuffer[160];

/* Consumer key and secret of Twitter application */
const static char consumer_key[] PROGMEM = "RafloxVUdyLfXf46gAtCYw";
const static char consumer_secret[] PROGMEM
= "zQNUxGvrdfsfEGi4sFGhTzqq14iRtjU86dwTASuY5k";

const unsigned int PIR_INPUT_PIN = 2;
const unsigned int BUTTON_PIN = 8;
const unsigned int BAUD_RATE = 9600;

/* Constants that define the behaviour of the alarm */

// Time(in s) that motion must be detected before alarm is raised
const unsigned int ALERT_TRESHOLD = 5;
// Time(in s) of motionless state before alarm stops
const unsigned int LAYLOW_TRESHOLD = 5;
// Time(in s) before another tweet will be sent
const unsigned int INTRUSION_REMINDER = 10;
// Twitter name to tweet to, and what to tweet
const char TWITTER_NAME[] = "@pcfluisteraar";
const boolean TWEET_ALARM = true;
const boolean TWEET_IN_PROGRESS = true;
const boolean TWEET_SAFE = true;

unsigned int detectedcounter = 0;
unsigned int silentcounter = 0;
unsigned int intrusioninprogress = 0;
char breakin[] = "%s There is a breakin in progress!";
char progress[] = "%s Intrusion still in progress!! %u seconds";
char detected[] = "Motion detected %u times";
char safe[] = "%s It's safe again. Duration of intrusion: %u";
boolean intruder_alert = false;
boolean checking = false;

// Build a twitter object
Twitter twitter(buffer, sizeof(buffer));

// Convenience class for accessing InfraredSensor  
class PassiveInfraredSensor {
  int _input_pin;

  public:

  PassiveInfraredSensor(const int input_pin) {
    _input_pin = input_pin;
    pinMode(_input_pin, INPUT);
  }
  
  const bool motion_detected() const {
    return digitalRead(_input_pin) == HIGH;
  }
};

// Make an object for IR sensor with input pin passed to constructor
PassiveInfraredSensor pir(PIR_INPUT_PIN);

// Setup Arduino
void setup() {
  Serial.begin(BAUD_RATE);
  
  Ethernet.begin(mac, ip);

  /* Setup twitter */
  twitter.set_twitter_endpoint(PSTR("api.twitter.com"),
                               PSTR("/1/statuses/update.json"),
                               twitter_ip, twitter_port, false);
  twitter.set_client_id(consumer_key, consumer_secret);
  

  // You can actually avoid regular OAuth dance by using two-legged OAuth
  // Get token & token Secret from your Twitter App setup page
  twitter.set_account_id(PSTR("397949318-LiXV5b4Yif9AyA4EO0pcSaYbcSbBhfNsStedmv89"),
                         PSTR("9hyMGxE23O6qBecGfKStaxqqJpBZxexh3JO9RAz5E"));
  delay(500);
}

// Start Arduino loop
void loop() {
  const int BUTTON_STATE = digitalRead(BUTTON_PIN);
  
  // Someone pushed the "on" button, so we reset the alarm counters and switch checkingstate
  if (BUTTON_STATE == HIGH) {
    detectedcounter = 0;
    silentcounter = 0;
    intrusioninprogress = 0;
    intruder_alert = false; 
    if(!checking) {
      Serial.println("Alarm is on!");
      checking = true;
    } else {
      Serial.println("Alarm is off!");
      checking = false;
    }  
  }
  
  // Are we checking?
  if(checking) {
    
    // We've detected motion long enough to tweet the alert  
    if(detectedcounter >= ALERT_TRESHOLD && !intruder_alert) {
      sprintf(messagebuffer, breakin, TWITTER_NAME);
      Serial.println(messagebuffer);
      detectedcounter = 0;
      intruder_alert = true;
      if(twitter.is_ready() && TWEET_ALARM) {
        if (twitter.post_status(messagebuffer))
              Serial.println("Twitter Status updated");
            else
              Serial.println("Twitter Update failed");
      }
    }
    
    // First alarm message was tweeted, but we're in the clear again for set amount of seconds
    if(intruder_alert && silentcounter >= LAYLOW_TRESHOLD) {
      sprintf(messagebuffer, safe, TWITTER_NAME, intrusioninprogress - LAYLOW_TRESHOLD);
      Serial.println(messagebuffer);
      silentcounter = 0;
      intruder_alert = false;
      intrusioninprogress = 0;
      if(twitter.is_ready() && TWEET_IN_PROGRESS) {
        if (twitter.post_status(messagebuffer))
              Serial.println("Twitter Status updated");
            else
              Serial.println("Twitter Update failed");
      }
    }
    
    // Motion detected? Start counting. No motion anymore? Start counting your blessings...
    if (pir.motion_detected()) {
      detectedcounter++;
      silentcounter = 0;
    } else {
      silentcounter++;
      detectedcounter = 0;   
    }
    
    if(detectedcounter > 0) {
      sprintf(messagebuffer, detected, detectedcounter);
      Serial.println(messagebuffer);
    }
    
    // Start counting how long the alarm bells have been ringing
    if(intruder_alert) {
      intrusioninprogress++;
    }
    
    // Intuder alert tweeted, and shit's still hitting the fan? Tell em!
    if(intruder_alert && intrusioninprogress % INTRUSION_REMINDER == 0) {
      sprintf(messagebuffer, progress, TWITTER_NAME, intrusioninprogress);
      Serial.println(messagebuffer);
      if(twitter.is_ready() && TWEET_IN_PROGRESS) {
        if (twitter.post_status(messagebuffer))
              Serial.println("Twitter Status updated");
            else
              Serial.println("Twitter Update failed");
      }
    }
  }
  
  // Do readings every 1 second
  delay(1000);
}
```
