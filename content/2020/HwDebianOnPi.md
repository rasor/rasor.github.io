Title: Install "Raspberry Pi OS with desktop" on Pi 400
Date: 2099-01-01 00:00
Category: DevOps
Tags: #linux, #os, #debian

# Intro

I wanted to use a [Raspberry Pi 400](https://www.raspberrypi.org/products/raspberry-pi-400) as a desktop alternative to a ChromeBook meaning a cheap PC mostly just for browsing the internet.

## HW

The Pi 400 comes with

* quad-core 64-bit ARM processor
* 4GB of RAM
* wireless networking
* dual-display output, and 4K video playback
* a 40-pin GPIO header

Apart from the Pi 400 I also bought

* [Raspberry Pi 15.3W USB-C Power Supply](https://www.raspberrypi.org/products/type-c-power-supply)
* micro hdmi to hdmi adapter
* USB Reader for microSD
* microSD card, 128 GB
* Monitor + hdmi cable

## OS

Raspberry supplies  [two desktop OS's](https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit):

* Raspberry Pi OS with desktop and recommended software (Size: 2,949MB)
* Raspberry Pi OS with desktop (Size: 1,177MB)

Alternatively there is also a 3rd-party [Ubuntu Desktop](https://www.raspberrypi.org/software/operating-systems/#third-party-software)

I want to see if the minimal Pi without extra sw (#2 in the list) will be enough for my needs.  

Info: According to [Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) `Raspberry Pi OS` is a `Debian` distru (as also is Ubuntu). This will do just fine.  

The current `Pi OS` release `August 2020` includes

* Debian: `10 (Buster)`
* Browser: [GNOME Web](https://en.wikipedia.org/wiki/GNOME_Web) (a Webkit browser engine - like Safari)
* GUI/Desktop: LXDE
* GCC (GNU Compiler Collection): `8.3`
* Linux kernel: `5.4.51`

[![Linux OS Components](https://ostoday.org/wp-content/uploads/2019/06/what-is-gcc-in-linux-300x225.png)](https://ostoday.org/linux/what-is-gcc-in-linux.html)  
_(Image on ostoday.org)_

# Installation

## OS



Steps:

* Down
 
The End
