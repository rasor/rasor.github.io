Title: Moveslink 2 crash
Status: published
Date: 2018-01-11 19:00
Category: DevOps
Tags: #ambit, #moveslink, #drivers, #windows, #suuntoapp

A few days ago I [resat my Windows 10](https://support.microsoft.com/ml-in/help/12415/windows-10-recovery-options), so I could start from scratch.

## Problem

The USB driver for my GPS watch, Suunto Ambit 2 misbehaved.

I just connected the watch with USB cable.  
Then I installed [Moveslink2](http://www.movescount.com/connect/moveslink).

I would see Moveslink in the taskbar and the taskmanager for a while and then it would disappear.

I thought it was a problem that I had the watch connected while I installed Moveslink, but no.

## Solution

It turned out that it is a [known error](http://www.suunto.com/Support/faq-articles/features/what-should-i-do-if-moveslink2-does-not-start-after-installing-the-windows-10-fall-creators-update/) which appears with Windows 10 Fall Creators Update (1709).

The problem causes moveslink2 to crash.

What I had to do to make it disappear was:

* Turn off Wifi
* Reconnect watch with USB wire  
=> Now moveslink would show
* Turn on Wifi
* Sign in to movescount.com

All back to normal - Me happy

## How you can troubleshoot

In System Information I could see  
![Error in System Information](img/2018/2018-01-11-Ambit4.PNG)

In Event Viewer I could see  
![Error in Event Viewer](img/2018/2018-01-11-Ambit5.PNG)

In Devices and Printers I could see Ambit (after all was back to normal)  
![Ambit in Devices and Printers](img/2018/2018-01-11-Ambit1.PNG)

Ambit has two drivers  
![Ambit has to drivers](img/2018/2018-01-11-Ambit2.PNG)

In Devices Manager I could not see Ambit, but now I knew which drivers it used  
![Ambit in Devices Manager](img/2018/2018-01-11-Ambit3.PNG)

## My related articles

* [Garmin 305 display misbehaving](https://rasor.wordpress.com/2012/11/09/garmin-305-display-misbehaving/)
* [Suunto Ruter (in danish)](https://rasordk.wordpress.com/2015/01/08/suunto-ruter/)
* [Moveslink2 is dead - Suunto App long live](https://www.facebook.com/soren.raarup/posts/10158624883721939)
    * [How do I use the Suunto services with Ambit2?](https://www.suunto.com/da-dk/Support/faq-articles/transition/how-do-i-use-the-suunto-services-with-ambit2/)

The End