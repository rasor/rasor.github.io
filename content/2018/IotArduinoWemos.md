Title: Connexting a WeMos ES8266 Arduino borad to AWS
Date: 2099-01-01 00:00
Category: Dev
Tags: #iot, #arduino, #wemos, #es8266, #aws

At [EMS Heart Hack](https://ideation-emshearthack.bemyapp.com/#/event)athon I connected a [D1 mini [WEMOS]](https://wiki.wemos.cc/products:d1:d1_mini) to AWS together with [Allan Yde](http://www.inyourmind.world/).  

The WeMos D1 Mini board has a WiFi module build in through which it can communicate with AWS.  
You can connect sensors to WeMos, so it can send its sensor data to AWS.  

# Installation

You need to use Arduino IDE to manage the WeMos board.  
First you need to install a WeMos driver and then you need to upload a program to the WeMos board.  
After that the board is started, when it is powered on and it connects to the world through WiFi.

## WeMos board

* Install Arduino IDE
* Install [WEMOS D1 driver](https://wiki.wemos.cc/tutorials:get_started:get_started_in_arduino#using_boards_manager)
    * Set Arduino IDE - File - Preferences to point to WeMos json file  
    ![Arduino IDE - File - Preferences](img/2018/2018-09-16-hack-arduino1.PNG)]
    * Download ES8266 board (Arduino IDE - Tools - Board - Board Manager - Download):  
    ![Arduino IDE - Tools - Board - Board Manager - Download](img/2018/2018-09-16-hack-arduino2.PNG)]
    * Upload default program to board (Arduino IDE - Upload program):  
    ![Arduino IDE - Upload program](img/2018/2018-09-16-hack-arduino4.PNG)]
* Pins: [Setup - Micropython on ESP8266 Workshop 1.0 documentation](https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/setup.html#development-board)
* eBook: [ESP8266 Internet of Things Cookbook](https://www.packtpub.com/hardware-and-creative/esp8266-internet-things-cookbook)

## NodeMCU

* [NodeMcu -- An open-source firmware based on ESP8266 wifi-soc.](http://www.nodemcu.com/index_en.html#fr_54745c8bd775ef4b99000011)
* [nodemcu/nodemcu-firmware](https://github.com/nodemcu/nodemcu-firmware)
* [Overview - NodeMCU Documentation](https://nodemcu.readthedocs.io/en/master/)
* [Uploading code - NodeMCU Documentation](https://nodemcu.readthedocs.io/en/master/en/upload/)
* [NodeMCU MQTT Client with Arduino IDE | NodeMCU ](https://www.electronicwings.com/nodemcu/nodemcu-mqtt-client-with-arduino-ide)
* [MQTT Version 3.1.1](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718027)

### Lua

* [The Programming Language Lua](https://www.lua.org/)

## Adafruit Dashboard

* [Adafruit IO Basics: Dashboards](https://learn.adafruit.com/adafruit-io-basics-dashboards/creating-a-dashboard)

## Blynk

* [Wemos D1 Mini + 0.96 Inch SSD1306 OLED Display Using SPI](https://www.instructables.com/id/Wemos-D1-Mini-096-SSD1306-OLED-Display-Using-SPI/)
* [Blynk](https://docs.blynk.cc/)
* [blynkkk/blynkkk.github.io](https://github.com/blynkkk/blynkkk.github.io)
* eBook: [Hands-On Internet of Things with Blynk](https://www.packtpub.com/application-development/hands-internet-things-blynk)

## Alternatives to ESP8266

### ESP32

* Compare: [ESP32 vs ESP8266 | Circuits4you.com](https://circuits4you.com/2019/03/02/esp32-vs-esp8266/)
* eBook: [Internet of Things Projects with ESP32](https://www.packtpub.com/hardware-and-creative/internet-things-projects-esp32)

## AWS

![AWS IoT - thing installed](img/2018/2018-09-16-hack-arduino5.PNG)]


# Buy

* WeMos
    * [wemos - Buy Cheap wemos - From Banggood](https://www.banggood.com/search/wemos.html)
* WeMos D1 Mini
    * USD 3.5 + ship [Aliexpress.com](https://www.aliexpress.com/store/product/D1-mini-Mini-NodeMcu-4M-bytes-Lua-WIFI-Internet-of-Things-development-board-based-ESP8266/1331105_32529101036.html)
    * DKR 27 incl ship [banggood](https://www.banggood.com/Wemos-D1-Mini-V3_0_0-WIFI-Internet-Of-Things-Development-Board-Based-ESP8266-4MB-p-1264245.html?rmmds=category)
* WeMos D1 Mini Pro + WiFi Wireless Antenna
    * DKR 49 incl ship [banggood](https://www.banggood.com/WeMos-D1-Mini-Pro-16-Module-ESP8266-Series-WiFi-Wireless-Antenna-p-1144951.html?rmmds=category)
* NodeMCU ESP-12E
    * DKR 39 [Geekcreit® NodeMcu Lua ESP8266 ESP-12E WIFI Development Board](https://www.banggood.com/Geekcreit-Doit-NodeMcu-Lua-ESP8266-ESP-12E-WIFI-Development-Board-p-985891.html?rmmds=detail-top-buytogether-auto)
* Sensors - Input modules
    * DHT22: [AM2302 DHT22 Temperature And Humidity Sensor Module For Arduino SCM](https://www.banggood.com/AM2302-DHT22-Temperature-And-Humidity-Sensor-Module-For-Arduino-SCM-p-937403.html?rmmds=category)
    * GPS: [GYNEO6MV2 GPS Module NEO-6M GY-NEO6MV2 Board With Antenna For Arduino](https://www.banggood.com/GYNEO6MV2-GPS-Module-NEO-6M-GY-NEO6MV2-Board-With-Antenna-For-Arduino-p-1196661.html?rmmds=search)
    * GPS: [APM2.6 2.8 GPS Module High Precision Ublox NEO-M8N GPS With Electronic Compass PIXHAWK](https://www.banggood.com/APM2_6-2_8-GPS-Module-High-Precision-Ublox-NEO-M8N-GPS-With-Electronic-Compass-PIXHAWK-p-1240362.html?rmmds=category)
    * GPS Tracker: [KROAK Mini GPS Tracker Positioner Module GPS+AGPS+LBS Multiple Locator SOS Alarm Web APP Tracking High Integration PCBA For Kids Children Pets Car](https://www.banggood.com/KROAK-Mini-GPS-Tracker-Positioner-Module-GPSAGPSLBS-Multiple-Locator-SOS-Alarm-Web-APP-Tracking-p-1245615.html?rmmds=search)
    * Air Pressure: [CJMCU-280E BME280 High Precision Atmospheric Pressure Sensor For Arduino](https://www.banggood.com/CJMCU-280E-BME280-High-Precision-Atmospheric-Pressure-Sensor-For-Arduino-p-1103115.html?rmmds=category)
    * Air Pressure: [GY-BMP280-3.3 High Precision Atmospheric Pressure Sensor Module For Arduino](https://www.banggood.com/GY-BMP280-3_3-High-Precision-Atmospheric-Pressure-Sensor-Module-For-Arduino-p-1111135.html?rmmds=detail-top-buytogether-auto)
    * Gyro, 3 axis: [6DOF MPU-6050 3 Axis Gyro With Accelerometer Sensor Module For Arduino](https://www.banggood.com/6DOF-MPU-6050-3-Axis-Gyro-With-Accelerometer-Sensor-Module-For-Arduino-p-80862.html?rmmds=category)
    * Gyro, 9 axis: [MPU9250 Integrated 9DOF 9-Axis Attitude Accelerometer Gyro Compass Magnetic Field Sensor For Arduino](https://www.banggood.com/MPU9250-Integrated-9DOF-9-Axis-Attitude-Accelerometer-Gyro-Compass-Magnetic-Field-Sensor-For-Arduino-p-1101005.html?rmmds=detail-top-buytogether-auto)
    * 16 bit AD converter [CJMCU-ADS1115 16Bit ADC Development Board Module](https://www.banggood.com/CJMCU-ADS1115-16Bit-ADC-Development-Board-Module-p-986645.html?rmmds=detail-top-buytogether-auto)
    * Microphone: [3pcs CJMCU-9812 MAX9812L Electret Microphone Amplifier Development Board Sensor Module For Arduino](https://www.banggood.com/3pcs-CJMCU-9812-MAX9812L-Electret-Microphone-Amplifier-Development-Board-Sensor-Module-For-Arduino-p-1105009.html?rmmds=detail-left-hotproducts__8)
    * Smoke: [MQ-2 Smoke Gas LPG Butane Gas Sensor Tester For Arduino](https://www.banggood.com/MQ2-Smoke-Gas-LPG-Butane-Gas-Sensor-Tester-For-Arduino-p-1144079.html?rmmds=detail-left-hotproducts__3)
    * Distance: [Geekcreit&reg; Ultrasonic Module HC-SR04 Distance Measuring Ranging Transducer Sensor DC 5V 2-450cm](https://www.banggood.com/Wholesale-Geekcreit-Ultrasonic-Module-HC-SR04-Distance-Measuring-Ranging-Transducer-Sensor-DC-5V-2-450cm-p-40313.html?rmmds=detail-top-buytogether-auto)
    * Stepmotor: [Geekcreit&reg; L298N Dual H Bridge Stepper Motor Driver Board For Arduino](https://www.banggood.com/Wholesale-Dual-H-Bridge-DC-Stepper-Motor-Drive-Controller-Board-Module-Arduino-L298N-p-42826.html?rmmds=detail-top-buytogether-auto)
    * Water sensors: [water sensor - Buy Cheap water sensor - From Banggood](https://www.banggood.com/search/water-sensor/0-0-0-1-3-44-0-price-0-0_p-1.html?sortType=asc)
    * Water level: [10W Black SidE-mount Water Level Sensor Controller Liquid Float Switch](https://www.banggood.com/10W-Black-Side-Mount-Water-Level-Sensor-Controller-Liquid-Float-Switch-p-961256.html?rmmds=detail-left-hotproducts__4)
    * Water level: [109mm Stainless Steel Water Level Sensor Liquid Vertical Float Switch for Hydroponics Gardening](https://www.banggood.com/109mm-Stainless-Steel-Water-Level-Sensor-Liquid-Vertical-Float-Switch-for-Hydroponics-Gardening-p-1171139.html?rmmds=search)
* Transmitters - Output modules:
    * OLED: [Geekcreit® 0.91 Inch 128x32 IIC I2C Blue OLED LCD Display DIY Oled Module SSD1306 Driver IC DC 3.3V 5V For Arduino PIC](https://www.banggood.com/0_91-Inch-128x32-IIC-I2C-Blue-OLED-LCD-Display-DIY-Oled-Module-SSD1306-Driver-IC-DC-3_3V-5V-p-1140506.html?rmmds=category)
    * OLED: [Wemos® OLED Shield V2.0.0 For Wemos D1 Mini 0.66](https://www.banggood.com/Wemos-OLED-Shield-V2_0_0-For-Wemos-D1-Mini-0_66-Inch-64X48-IIC-I2C-Two-Button-p-1267299.html?rmmds=detail-bottom-alsobought__4)
    * LED ring: [Wemos® X-Ring RGB WS2812b LED Module For RGB Built-in LED 12 Colorful LED Module For WAVGAT ESP8266 RGB](https://www.banggood.com/Wemos-X-Ring-RGB-WS2812b-LED-Module-For-RGB-Built-in-LED-12-Colorful-LED-Module-For-WAVGAT-ESP8266-p-1176172.html?rmmds=detail-top-buytogether-auto)
    * Laser: [3Pcs KY-008 Laser Transmitter Module For Arduino AVR PIC](https://www.banggood.com/3Pcs-KY-008-Laser-Transmitter-Module-For-Arduino-AVR-PIC-p-943280.html?rmmds=detail-top-buytogether-auto)
* Kits: [Arduino Compatible SCM & DIY Kits](https://www.banggood.com/Wholesale-Arduino-Compatible-SCM-and-DIY-Kits-c-2153.html)

# Projects

* List of [D1 mini Shields [WEMOS Electronics]](https://wiki.wemos.cc/products:d1_mini_shields)
* Heart-rate: [Heart-rate monitor uses a Wemos, a small OLED display and MicroPython](https://www.recantha.co.uk/blog/?p=18671)
* PIR: [A Super Simple ESP8266 IOT Motion (PIR) Sensor](https://hackaday.com/2018/07/19/a-super-simple-esp8266-iot-motion-sensor/)
* Temperature with LM35: [Monitoring data from sensors using ESP 8266 and arduino](https://medium.com/@angelinmaryjohn/monitoring-data-from-sensors-using-esp-8266-and-arduino-bb9132d88488)
* Temperature and humidity with DHT22: [Getting Started With the ESP8266 and DHT22 Sensor](https://www.losant.com/blog/getting-started-with-the-esp8266-and-dht22-sensor)
* Barometer and temperature: [Wemos mini bmp180 sensor example - esp8266 learning](http://www.esp8266learning.com/wemos-mini-bmp180-sensor-example.php)
* D1 as webserver: [Wemos webserver example - esp8266 learning](http://www.esp8266learning.com/wemos-webserver-example.php)
* [WiFi scanner with Wemos D1 mini](https://blog.robberg.net/wifi-channel-scanner-with-wemos-d1-mini/)

## QR Codes on OLED

* [Wemos D1 Mini + 0.96 Inch SSD1306 OLED Display Using SPI](https://www.instructables.com/id/Wemos-D1-Mini-096-SSD1306-OLED-Display-Using-SPI/)
* [QR Code Minimum Size: Find the ideal size for your use case](https://scanova.io/blog/blog/2015/02/20/qr-code-minimum-size/)
* [Adafruit_SSD1306_Wemos_OLED](https://github.com/stblassitude/Adafruit_SSD1306_Wemos_OLED)
* [OLED Shield [WEMOS Electronics]](https://wiki.wemos.cc/products:d1_mini_shields:oled_shield) - 64*48 pixels - QR needs 31*31 pixels for showing SN - serial number.
* [Wemos OLED shield example - esp8266 learning](http://www.esp8266learning.com/wemos-oled-shield-example.php)
* [Wemos OLED Shield](http://garybake.com/wemos-oled-shield.html)
* [ESP32 With Integrated OLED (WEMOS/Lolin) - Getting Started](https://www.hackster.io/johnnyfrx/esp32-with-integrated-oled-wemos-lolin-getting-started-07ac5d)
* [ESP32 Arduino SSD1306 OLED: Drawing a QR Code](https://techtutorialsx.com/2017/12/16/esp32-arduino-ssd1306-oled-drawing-a-qr-code/)
* [OnionIoT/oledQrCodeGenerator](https://github.com/OnionIoT/oledQrCodeGenerator)
* [QR Codes Using Onion Omega](https://www.hackster.io/22769/qr-codes-using-onion-omega-b326bd)
* [QR](https://www.adafruit.com/qr)
* [QR Code Stencil Generator and QR Hobo Codes | F.A.T.](http://fffff.at/qr-stenciler-and-qr-hobo-codes/)

# Other

* Tmp proj dir: p4Projs\2018-EmsHackathon\IotBooks\AWS
* [Intel® System Studio](https://software.intel.com/en-us/system-studio)

The End