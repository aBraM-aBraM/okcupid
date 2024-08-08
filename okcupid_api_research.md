# OkCupid API Research

## Setup

### Methodology

I've started by trying to research using chrome devtools. 
This is not useful its a much better and its a much better idea to research phone apps instead.

I've researched using frida and adding hooks to send functions but ultimately was convinced https mitm
is the best solution. I needed to get a rooted android with google play to install the app.

I first tried using android studio's google-play images which seems [very hard](https://docs.mitmproxy.org/stable/howto-install-system-trusted-ca-android/). 

I've also tried using a base android image and extract the apk from another similar google-play android image but again this is a waste of time.

Finally I've used bluestacks for a virtualization which can easily be rooted with google play.

> TLDR; use mitm, use bluestacks for virtualization

### Bluestacks Setup & Root

Bluestacks has multiple options for images. I need bluestacks 5 
because that's the local version. Pie & Nougat models did not fit
and I couldn't install okcupid due to `Device isn't compatible with this app` error. Instead I used Android 11 64-Bit.

To root bluestacks I used [this article](https://kimlisoft.com/how-to-root-bluestacks-5/). It's outdated but I just searched
this regex `root.*=` in bluestacks, found them in `bluestacks.conf` to find the config and changed the values to 1.

### Android Certificates

Bluestacks uses virtualbox behind the scenes. I used [this reddit thread](https://www.reddit.com/r/BlueStacks/comments/104dydc/comment/jyrhbt3/) to find how to add certificates as root.

The TLDR is shutdown bluestacks, use the "Readonly" regex on the bluestacks dir to
change `<HardDisk uuid="{85c80f25-92fb-4c74-9a21-d7527e3eedcf}" location="Root.vhd" format="VHD" type="Readonly"/>` type attribute to "Normal" instead of "Readonly". My filename is `Android.bstk.in`
but it seems different online. 

Afterwards you can use `mount -o remount,rw /system` and set
certificates.

I used [mitmproxy](https://docs.mitmproxy.org/stable/concepts-certificates/#quick-setup) set my proxy settings in windows and go to http://mitm.it
and download the android certificates.

I used [KitasuneMask](https://github.com/RobThePCGuy/Root-Bluestacks-with-Kitsune-Mask) (which seems like another version of Magisk) and chose `install system`.
After installing I was able to install the mitmproxy magisk module from the kitasune mask app.

### MitmProxy

bluestacks 5 doesn't have proxy settings, bluestacks 4 has but doesn't have an android version that supports OkCupid.
In order to use a proxy you need to set it. I used proxifier to tunnel all incoming traffic from bluestacks to mitmproxy (127.0.0.1:8080)

