Title: Moving photos from iPhone to cloud
Date: 2099-01-01 00:00
Category: DevOps
Tags: #ios, #mac, #pcloud, #photos

# HowTo move photos from iPhone to PCloud without using iCloud

## Intro

* **iPhone** holds more than 80GB
* **iCloud** only holds free 5GB
* On **PCloud** we have 2TB

So obviosly we wants to move the files to PCloud instead of iCloud.

## Problems

When we did this the last time we were using iTunes - probably from PC.  
Now I tried also to use iTunes on PC, but it does not contain photos.  

Then I tried to use Windows Explorer. You can import from iPhone, when you right-click on the iPhone (after you have trusted both on phone and PC). It takes 10th of minutes before the PC has read all the DCIM folders on the iPhone.  
Select "delete after import".  
Problem is that the import stalls after a while. And then you'll have to start all over. You'll never get a chance to get all imported.

On Mac, if you have updated to OS `Catalina`, then you can't install iTunes (though a tool - [Retroactive](https://github.com/cormiertyshawn895/Retroactive) lets you).

## Solution

On Mac running Catalina `iTunes` were split into the programs normally handling the files.  
So images files now uses `Photos`, audio files now uses `Music`. And I guess the rest are handled via `Finder`.  
It seems like the `Photos` app is storing all photos in one library into a database file for that library - so when we want to move the photos further on to a cloud drive, then you have to export the images out.  

There is a way to become able to handle all files manually - see video below. But that requires all iCloud settings on the phone has been disabled. When you disable them, then the phone wants to delete all the files on the phone, so you don't want to do that.  

Instead we'll just use Photos program for import.

* Disconnect Phone from iCloud
    * On Phone open `Settings`
    * Open `iCloud`
    * Open `Photos`
    * Turn off all the options, that does not delete files on the phone
* Disable sync from phone to Mac
    * Connect iPhone to Mac
    * In `Finder` select your phone under `Locations`
    * Select tab `Photos`
    * Unselect `Sync`
    * Press `Apply`
* Import from phone to Mac
    * In `Photos` select your phone under `Devices`
    * Change target from `Library` to `New Album` to avoid mixing the imported photos with others.
    * Press `Delete after import`
    * Press `import`
    * It happens the connection to the phone gets lost. But when you restart the import, then it won't import photos you already have imported.
* Move files from Mac to cloud
    * TBD ....
* Delete copied photos on phone
    * On phone open `Photos`
    * TBD ....

## Links

* Vid: [How to Transfer Music, Videos to iPhone, iPad in macOS Catalina?](https://www.youtube.com/watch?v=BSkHVZIY8EA)
* Guide: [How to Transfer Photos from Mac to External Drive [Solved]](https://www.cleverfiles.com/howto/move-photos-hard-drive.html)
* [Move your Photos library to save space on your Mac](https://support.apple.com/en-us/HT201517)

The End
