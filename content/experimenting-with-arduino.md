Title: Experimenting with Arduino
Date: 2011-09-10 18:47
Slug: experimenting-with-arduino
Summary: I just started with my minor, called Mobile Life, as part of my studies Computer Science. This course, taught by Rimmert Zelle, is all about Arduino & Ubiquitous Computing. The idea is, that by the end of the course we've developed a Proof of Concept utilizing the Arduino platform. The problem is, that me and my project teammate have too many ideas! So in this blog post I intend to share 3 ideas, and I hope readers will give their opinions and deliver some feedback on the proposals!

I just started with my minor, called Mobile Life, as part of my studies Computer Science. The first course, taught by [Rimmert Zelle](http://twitter.com/rimmertzelle "Rimmert Zelle"), is all about [Arduino](http://www.arduino.cc/ "Arduino") & Ubiquitous Computing. The idea is, that by the end of the course we've developed a Proof of Concept utilizing the Arduino platform. The problem is, that me and [my project teammate](http://www.vandorp.biz/ "Daniel van Dorp") have too many ideas! So in this blog post I intend to share 3 ideas, and I hope readers will give their opinions and deliver some feedback on the proposals!

Without further ado...

### Help! [My girlfriend](http://twitter.com/joy_nl "My lovely girlfriend...") can't choose between twitter and the television!    

Well, maybe she doesn't have to. After all, in this modern age, we should be able to combine any data we want right? Using [this arduino shield](http://nootropicdesign.com/ve/ "Video Experimenter"), called the Video Experimenter, we want to build a system that shows a new Twitter @mention overlayed on the tv screen, whenever the user gets one. Checking for new tweets will be done by polling the twitter service on set intervals. We could do the twitter checking either by hooking the system up to a computer or by using the [ethernet shield](http://www.arduino.cc/en/Main/ArduinoEthernetShield "Ethernet Shield") and hooking up the system to the internet directly.

### Turning the news or a talkshow into a multimedia experience

Inspired by the [Enough Already](http://www.engadget.com/2011/08/16/enough-already-arduino-mutes-tvs-overexposed-celebrities-frees/ "Enough Already") experiment shown to us during one of the lectures, we got the idea to develop a way to integrate relevant twitter searches into the program you're watching on tv, using Arduino. Again, we'd use the [Video Experimenter](http://nootropicdesign.com/ve/ "Video Experimenter") and maybe the [ethernet shield](http://www.arduino.cc/en/Main/ArduinoEthernetShield "Ethernet Shield") for interfacing with the television set and optionally the internet (instead of through a computer). Utilizing the close captioning channel, we will do a word count of anything non-common (ie: "the" "a" "one" etc), and if the count of a particular word reaches a threshold, we'll do a twitter search on that word and show the results in an overlay on the tv screen.

### What's all that noise?!

Can't I just watch television in peace?

Apparently that's quite hard when you live next to a tram line in the middle of the city centre. This is what we intend to do about it: We'll use Arduino to measure the sound levels in the environment, using a [cheap microphone-like solution](http://tinkerlog.com/2007/05/20/cheap-sound-sensor-for-avr/ ""). When the SPL's go above certain thresholds, the system will act like a remote control to adjust the volume on the TV set.

I hope you like the ideas, and please leave a comment with your thoughts!