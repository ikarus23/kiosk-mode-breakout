# Kiosk Mode Breakout Tips & Tricks

A collection of tips & tricks on how to escape a kiosk mode environment on a system. A kiosk mode environment is
a system setup where a device or application is locked down to only allow specific functionality, preventing users
from accessing anything outside of the intended purpose. It's commonly used in public terminals, retail stores,
museums, and corporate settings where organizations want to ensure users interact with only designated applications
or websites.

Some typical characteristics are:
* The interface is streamlined and restricted.
* Users can't access system settings or other applications.
* Security measures prevent unauthorized modifications.
* It often runs a single application, like a web browser.



## Table of Content

- [Kiosk Mode Breakout Tips \& Tricks](#kiosk-mode-breakout-tips--tricks)
  - [Table of Content](#table-of-content)
  - [What is this Collection? And what not?](#what-is-this-collection-and-what-not)
  - [Contribute](#contribute)
  - [Breaking out](#breaking-out)
    - [Kiosk Application](#kiosk-application)
    - [Touch Screen and Mouse](#touch-screen-and-mouse)
    - [Keyboard](#keyboard)
    - [(Re-)booting \& Login screen](#re-booting--login-screen)
    - [Crashing](#crashing)
    - [USB](#usb)
    - [Network (Ethernet/Wi-Fi)](#network-ethernetwi-fi)
    - [Android](#android)
    - [Other](#other)
    - [Tools](#tools)
  - [Useful resources](#useful-resources)



## What is this Collection? And what not?

This collection mainly **focuses on devices** (for now). Other typical appearances of kiosk mode environments,
e.g. terminal server or solutions like [Citrix](https://www.citrix.com/), are a bit out of scope. However,
some of the tips & tricks might still apply in such environments.

The vast majority of the tips & tricks regard Windows-based systems running an application in a kiosk mode.
But there are at least some tips & tricks which targeted Linux-based systems. Furthermore, some tips for
Windows might also apply to Linux-based systems.

Privilege escalation attacks, after breaking out of the kiosk mode, are not in scope for this collection
of tips & tricks.

This collection is very likely not exhaustive. Breaking out of a kiosk mode environment is often a creative
task that requires to work with the restrictions of that environment. Sharing and contributing new ideas
is very welcome.



## Contribute

Contributions are very welcome! As there is no definitive answer on how to break out of kiosk mode environment,
collecting ideas and creative approaches is all that matters. Feel free to open an issue/pull request and
improve this collection.



## Breaking out

These section has all the tips & tricks. It is divided into subsections which represent different attack
angles when it comes to breaking out of the kiosk mode environment.

The general idea is always the same: find some way to access critical applications like the Task Manager
(`taskmgr.exe`), the Explorer (`explorer.exe`), or the command line interface (`cmd.exe`). Once you have access
to these applications you have successfully broken out of the kiosk mode environment and can now look deeper
into the system. Maybe you want to escalate your privileges to an administrator level, but that is out of scope
for this collection.

The typical "way" to access these critical applications is split into two tasks:
1. Find a way to make the system behave unexpected.
2. Find a way from that unexpected behavior to launching/accessing the critical applications.

The first step could be to e.g. find a link somewhere in the main application that is clickable. By pressing
on it a web browser window might open. The second step is to find a way from that popup/window to critical
applications like the `cmd.exe`. In the example of previously opened edge browser it could be: press the three dots
(menu) -> chose "Downloads" -> press the folder symbol (open downloads folder) -> navigate in the file browser to
`C:\windows\system32` and double click on `osk.exe` -> then double click on `cmd.exe`. Now you have command line
interface with a full keyboard on a device that might only have a touch screen.

Keep in mind that there can be challenges and pitfalls. Some typical examples are: finding hidden shortcuts,
stateful behavior (e.g. keyboard shortcut works only during boot), and differences between Windows/Linux/Android/etc.
and their different versions and distributions.

Have fun and happy hacking!



### Kiosk Application

Sometimes it is possible to break out of the kiosk mode right from within the application that is run in the foreground.
Some things to look out:
* **Save/open dialogs**: A lot of applications use the default open or save dialog provided by Windows. This can be
  abused to e.g. run any other program. You can simply write `cmd` in the path field. The open and save dialog
  also often have a help button, which opens a browser by default. You can also go into the properties of the
  dialog which has a link into the Windows control panel.
* **Links**: Some application contain links. They are very common in help/about dialogs and privacy or legal pages.
  By default, Windows opens links with a browser. From there it is easy to open an explorer
  (e.g. downloads -> show download folder) to start other processes. But other things can be likely done though
  links as well. You might even directly access the Windows settings or open an app on an Android system.
  Even more ideas can be found in the URI handler section of the ["Other"](#other) chapter.
* **Embedded elements**: Applications typically use some embedded elements. An example would be to render a
  HTML site with an browser-like embedded element. Some of these elements offer quite a lot of additional features.
  An embedded browser element might have a "view source" or "print site" option in the context menu. Both
  typically allow to break out of the kiosk mode environment. Sometimes a text element allows you to mark a section
  and to "search" for it -- which opens a browser.

There is often an intended way to get out of the kiosk mode (or at least into advanced settings menu).
Most of the time this is used by service personal. In some cases, there is no additional authentication
(e.g. a password) needed once you find a hidden function. Some points to look out for:
* **Logos**: Try clicking on logos. Try multiple quick clicks, long presses, right-clicking.
* **"Static" text**: Try clicking on static text. Some good examples are copyright notices, clocks, or other small
  text that does not look interesting to users. Try multiple quick clicks, long presses, right-clicking.
* **Special keyboard shortcuts**: Some developers hide their kiosk mode breakout function behind a hidden
  keyboard shortcut. There is no optimal way to search for them. Often there are F-keys involved. Also, not only
  look for combinations with modifier keys. Sometimes it is just something like pressing a and b together.
  For tips on automating keyboard inputs, have a look at the [keyboard](#keyboard) section.



### Touch Screen and Mouse

Most devices running a kiosk environment do have a touch screen. Sometimes, having touch input or a mouse
is enough to break out. Apart from breaking out, having a keyboard is also very viable in these situations.
Therefore, starting an on screen keyboard (e.g. `C:\Windows\System32\osk.exe`) can be very helpful.

* **Long touch/right click**: Typically opens the context menu. There you will find, depending on the context,
  more functions, which might aid in breaking out. Try this also on e.g. selected text (tripple click on
  touch screens), it might offer more options.
* **Drag & Drop**: Regardless of mouse or touch screen, dragging and dropping can be quite helpful to break out of
  kiosk environments. It typically allows for coping or executing files. A useful example would be to drag
  a file over the `cmd.exe`. This will open up a terminal, regardless of the file dragged over.
* **Screen corners and edges**: Try moving the mouse curser to screen corners and edges. Sometimes elements
  like the Windows task bar are just hidden and will pop in, when the cursor is close by. This might also work
  on touch screen by tapping in corners and edges.
* **Gestures** (on Windows [source](https://support.microsoft.com/en-us/windows/touch-gestures-for-windows-a9d28305-4818-a5df-4e2b-e5590f850741)):
  * Show all open windows: Swipe with three fingers up on the screen.
  * Show the desktop: Swipe with three fingers down on the screen.
  * Switch to the last open app: Swipe with three fingers to the left or right on the screen.
  * Open notification center: Swipe with one finger in from the right edge of the screen.
  * See widgets: Swipe with one finger in from the left edge of screen.
  * Switch desktops: Swipe with four fingers to the left or right on the screen.



### Keyboard

If the device has a keyboard the chances increase to find a successful way to break out of the kiosk mode
environment. However, keyboards come in many different forms as some terminals only provide on screen keyboards (OSK)
with a subset of keys - sometimes even depending on the input field context. In other situations you might be able
to plug in your own keyboard via USB or connect one via Bluetooth. Remember, it is very likely that **a lot of
keyboard shortcuts have been disabled** by the kiosk mode environment. Furthermore, there might be really sneaky
things like **stateful or custom keyboard shortcuts**. This means that you might encounter situations in which you
have to first press one secret shortcut to then enable other shortcuts. And sometimes these shortcuts can be very
unintuitive -- e.g. pressing the "2" and "9" key together. Also, keep in mind that not all shortcuts work on all
Windows versions or Linux distributions.

Hopefully some of the following tips might help.

Windows:
* **Ctrl+Alt+Del or Ctrl+Shift+Esc or Win+X**: These shortcuts will give you access to the Windows Taskmanager
  from which any other process can be started.
* **Win+R**: This shortcut will give you access to a dialog that allows you to run other programs
  by typing in their name (e.g. "cmd").
* **Win+E**: This shortcut will open the Windows explorer (file browser). From there you can easily run other
  programs.
* **Alt+Tab or Alt+Esc or Win+Tab**: These shortcuts will switch between open windows. This mit help you to reach
  other running programs which might allow for an easy kiosk breakout.
* **F1**: This does often open a help dialog. Some of the typical Windows-based help dialogs have more options
  (e.g. open a web browser) which help in breaking out.
* **Alt+F4**: Closes the focused program. Sometimes there are other open programs running beneath the main application
  in foreground, which might aid in breaking out. If you are really lucky, the explorer process is running und you can
  directly access the task bar.
* **Win+D**: Will show the desktop. This might help to force foreground windows to be minimized. If the explorer
  is running, this should give full system access.
* **Shift+F10 or Alt+Space**: This shows the context menu of the currently focused element or window. Context menus
  sometimes have options that aid in breaking out. For example, the window context menu of the `cmd.exe` has
  a "Settings"/"Properties" entry. From there you will find options (links, "Open JSON file", etc.) to break out.
* **Shift x5**: Shows the "Sticky Keys" dialog. This is a good one! Just press the shift key five times in rapid
  succession. The dialog has a link which will open the system settings from where you can launch any other program.
  But there is more! Sometimes this dialog is deactivated. However, this typically only applies to logged in users.
  If you reboot the device and hammer shift during the Windows login screen, the dialog will show up - this time
  without a link to the system settings. Just activate sticky keys by pressing "Yes". Wait for the system to
  login and to start the application in kiosk mode. Then press Ctrl, Alt and Delete one key at a time. Sticky keys
  will translate that to the Ctrl+Alt+Del shortcut. Since the shortcut is triggered virtually, it is typically
  not blocked. The sticky keys dialog can also be accessed via the URI `shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}`.
* **Shift+Alt+NumLock**: Shows the "Mouse Keys" dialog. The dialog has a link which will
  open the system settings from where you can launch any other program. Furthermore, activating the mouse
  key option might actually help, as it allows you to control the mouse cursor using the numpad.
* **Shift+Alt+Print**: Shows the "High Contrast" dialog. The dialog has a link which will
  open the system settings from where you can launch any other program.
* **More interesting keyboard shortcuts**: Some versions of Windows allow to disable certain keys and shortcuts
  via registry keys. The functionality is handled by the MsKeyboardFilter and the registry keys can be found
  at `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Embedded\KeyboardFilter`. A full list of filters/shortcuts can be
  found in [the official documentation](https://learn.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/microsoft-windows-embedded-keyboardfilterservice).
  Maybe you can find a helpful shortcut on the list that is not disabled/filtered.
* **Miscellaneous**: These shortcuts might help in some situations, but are not directly linked to a quick
  kiosk mode breakout:
  * Win+P: Switch screens
  * Win++: Open screen magnifier
  * Ctrl+Shift+Win+B: Restart graphics driver

Linux:
* **Ctrl+Alt+T**: On most distributions, this will open a terminal.
* **Ctrl+Alt+F1/F2/F3/Fx**: This will typically switch between TTYs.
* **Ctrl+Alt+Backspace**: This will kill the XServer (GUI).
* **Ctrl+Alt+Del**: Typically restarts the system (can be configured). If a XServer (or something similar)
  is running, it is sometimes linked to the user logout operation.
* **Alt+Print+R/E/I/S/U/B**: These are so called "Magic SysRq keys". On most Linux systems you can
  control some functions of the kernel with them. A typical use case with explanations can be found in the
  [Arch Linux Wiki](https://wiki.archlinux.org/title/Keyboard_shortcuts#Rebooting). For more details please
  refer to [Magic SysRq key on Wikipedia](https://en.wikipedia.org/wiki/Magic_SysRq_key).

Other:
* **Media/special keys**: Some keyboards provide keys for e.g. volume control, media control (play/pause/skip) or
  have dedicated keys for opening a web browser or the default mail program. These keys are sometimes overlooked
  and are therefore not blocked. From e.e. an open web browser it is easy to escape to the operating system.
* **Alt+Shift+I**: Sometimes the application running in foreground is based on Electron. This means, they basically
  run in a Chrome-based browser. Depending on the configuration, this shortcut will open the developer tools.
  Form there you have a good chance of escaping the kiosk mode or to directly run programs on the underlying system.
* **F12**: Sometimes the application running in foreground is just a web application in a web browser.
  Depending on the configuration, this shortcut will open the developer tools. Form there you have a good chance
  of escaping the kiosk mode.
* **Ctrl+S/O/J**: This will cause many browsers to show dialog, which can be used to break out.
* **Ctrl+P**: In a lot of situations, this will open up a print dialog. Print dialogs can be application specific
  but there is a good chance you can also access the Windows print settings. This provides a good change of
  escaping the kiosk mode, sometimes using a detour over the system settings.
* **Ctrl+Alt+F12**: In some older versions, this will open the Intel HD Graphics menu. There should be some
  options that might help in breaking out.



### (Re-)booting & Login screen

Sometimes you might find yourself in front of a kiosk terminal that you can reboot. It might be as easy as
unplugging the power, a button inside the application or access to the Windows lock screen (which typically has
a reboot power-off/reboot option). This might help in order to break out of the kiosk mode environment.

* **Reboot**: There is a chance to break out during a normal reboot. Some kiosk environments are poorly designed
  and you will see some other open windows during system start. Sometimes you can even access the Windows taskbar
  for a brief period. Another common example would be a `cmd.exe` executing a script. There is a small
  time window where you might be able to e.g. right click on the window of the`cmd.exe`, go to the settings,
  and break out from there.
* **Hard power reset**: Hard power resets might leave a damaged file system. Windows knows that and sometimes
  offers to access the advanced boot options after automatic diagnosis. This offers interesting options like booting
  from a different source or to enter safe mode. Choosing "Enable Safe Mode with Command Prompt" in safe mode
  might help to perform system changes that help to escape the kiosk mode.
* **Unlocked BIOS/UEFI**: Some terminals have a unlocked BIOS/UEFI. This offers interesting options like booting
  from a different source (e.g. USB flash drive), disabling secure boot, and more. If the internal storage is
  not encrypted, booting a Linux from a flash drive can be used to modify the kiosk environment and to break out.
* **Known BIOS/UEFI password**: Some BIOS/UEFIs have known master passwords or password recovery mechanisms
  with public key generators. If you can bypass the BIOS/UEFI password the consequences are the same as having
  no password at all (see previous point).
* **Shift+Restart**: You might have access to a Windows reboot button (e.g. in the login/lock screen). Pressing shift
  while choosing the reboot option will give you access to the advanced boot options. This offers interesting options like booting from a different source or to enter safe mode. Both likely help with breaking out (see previous points).
* **Network/VPN/other settings on login screen**: The login/lock screen sometimes offers more options. A typical
  example would be to change network settings or to connect to a Wi-Fi. Depending on installed software there might
  be more options, like configuring a VPN. Maybe you find a setting that helps you to break out. Since all tools
  within the login screen run with system privileges, this might also provide a privilege escalation.
* **Unlocked bootloader**: Sometimes you might come across a unlocked second stage bootloader (after BIOS/UEFI).
  A typical example would be "grub" on a Linux-based system. In grub you an press C for a rescue shell or E
  to edit a boot entry temporarily. Editing a boot entry might help you break out. An example would be to
  change/add the `init` kernel parameter and set it to something like `/bin/sh`. This tells the Linux kernel
  to start a shell right after booting.
* **Change date/time**: Sometimes, even is the BIOS/UEFI is locked with a password, an empty password is accepted.
  This might still allow for the system time to be changed. In other cases the system time can be changed
  directly from the application in kiosk mode. Providing an NTP server over network might also work.
  Changing the system time can help to break out of the kiosk mode in some rare cases. An example would be
  kiosk terminal running a locked down Firefox web browser in full screen. It you change the time into the far
  future, Firefox will think it was not used for several month. It then offers an option to reset the profile,
  giving you the change to escape.



### Crashing

Some kiosk environments are designed with the goal to keep the main application on top and in full screen. If there
are no other good mechanics in place and the Windows explorer process is running, crashing the main application in
order to break out is a viable option. But even if not, crashing might help. If you succeed in crashing the
full system, an automatic reboot lets you explore attacks vectors from the
[(Re-)booting \& Login screen](#re-booting--login-screen) section.

* **Overexert application**: Some applications offer a function, that cause for a comparatively big work load.
  An example could be the change of the interface language, since resources have to been reloaded. If the
  software architecture is really bad, these exhaustive operations run in the main (GUI) thread.
  This could lead to an application crash or to a dialog offered by Windows to terminate the application
  ("The application is not responding"). With the main application out of the way, you might be able to
  break out further.
* **Resource exhaustion**: If the main system is busy and all resources are exhausted, there is a change the
  application running in foreground crashes and allows to access the underlying operating system. One example
  to achieve this might be a simple [SYN flood attack](https://en.wikipedia.org/wiki/SYN_flood) over the network.
* **Slow resources**: Similar to the first tip ("Overexert application") an application might not
  be responding if a requested resource is very slow. An example would be to simulate a slow USB flash drive
  which is used by the application. If the access to the drive is too slow, Windows might offer a dialog to
  end the program. A slow USB flash drive can be emulated with a
  [Facedander21](https://goodfet.sourceforge.net/hardware/facedancer21/)
  or a [GreatFET One](https://greatscottgadgets.com/greatfet/one/) hardware and the
  [facedacer software library](https://github.com/greatscottgadgets/facedancer).
* **Blue screen crash**: If you are able to crash the system with a blue screen of death (BSoD), the file system
  might be damaged. Windows knows that and sometimes offers to access the advanced boot options after a blue screen
  reboot. This offers interesting options like booting from a different source or to enter safe mode.
  Choosing "Enable Safe Mode with Command Prompt" in safe mode might help to perform system changes that help
  to escape the kiosk mode.



### USB

* **Windows co-driver auto-installation**: This feature is typically enabled on Windows systems by default.
  If a new USB device is plugged in and Windows knows a co-driver for that device, it downloads and executes
  that "driver"-software automatically (requires Internet). For example, plugging in a Logitech mouse can result
  in a popup for downloading and installing Logitech Options. A Razer mouse can lead to the download and
  execution of Razer Synapse ([this video](https://youtu.be/0myDcqmtt0U?t=169) shows it happen). An example
  on how to use your [Flipper Zero](https://flipperzero.one/) to emulate a SteelSeries device - which will also
  trigger a popup/download - can be found in the
  [co-driver folder of the examples](https://github.com/ikarus23/kiosk-mode-breakout/tree/main/examples/co-driver-install).
  The helpful part of this whole mechanic are the windows and popups that show up when plugging in such a device.
  Most of them have buttons or links that can help with breaking out of the kiosk mode. Others might ask for
  administrative permissions. You may be able to break out from the User Account Control (UAC) dialog.
* **Corrupt USB flash drive**: File systems like FAT32 have a so called "dirty bit" that identifies, if the USB
  drive was ejected/unmounted correctly. If a USB flash drive with a set dirty bit is plugged into a Windows system,
  a dialog typically pops up for automatically repairing the device. The result screen of the repair has a link
  which might let you break out of the kiosk environment. You can set the dirty bit from a Windows system
  with the command `fsutil dirty set F:` (see [fsutil dirty](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-dirty)).
  If the explorer process is not running, there might be no auto-repair functionality.
* **USB to Ethernet dongles**: The network interface of terminals with a kiosk mode might sometimes be hard to reach
  or not existent in the first place. Plugging in a USB to Ethernet adapter might broadly increase the attack surface.
  Sometimes this even bypasses network configurations and firewalls, as the new interface might be unmanaged.
  This does not lead directly to a way to break out of a kiosk environment. But any exposed service on the
  network might help. See also the [Network section](#network-ethernetwi-fi) for more ideas.
* **USB Bluetooth Dongle**: If the device has no built-in Bluetooth support, you might get this via a USB dongle
  (and then use it to connect a keyboard or transfer data).
* **Mouse as keyboard**: Some systems have filter rules for USB devices. Most simple systems are based on the vendor
  and product ID (VID, PID) of the device. If the two 2 byte values of a whitelisted device are known, they can be
  easily spoofed. Tools like a [Flipper Zero](https://flipperzero.one/) or a [Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky)
  have these functions build-in. Other systems might have class/subcass/protocol-based filter - like USB Guard for Linux.
  Lets assume devices with class 0x03 (HID), subclass 0x01 (Boot Interface) and protocol 0x01 (Keyboard) are forbidden.
  This means that keyboards are effectively blocked by the filter. However, sometimes these filters can be bypassed.
  In this case by simulating a USB mouse (protocol 0x02) that has all the functions/keys of a keyboard.
  A simple way to achieves this is to use a [Facedancer](https://github.com/greatscottgadgets/facedancer) compatible
  device. This allows you to emulate a USB keyboard with a simple Python script. Details about the emulated device
  (e.g. the protocol) can easily be changed.
* **BitLocker To Go** (Windows 7 only): BitLocker is the drive encryption solution by Microsoft. The "To Go" variant is meant for USB
  flash drives. Plugging in a BitLocker encrypted flash drive into a Windows 7 system will show a popup to unlock
  the device. The popup, however, has links that can be used to break out of a kiosk mode environment. Unfortunately,
  the same dialog on Windows 10 or 11 does not have options to break out.
* **MTP/Mobile phone**: The Media Transfer Protocol (MTP) is most commonly used when connecting a Android phone
  with a computer using a USB cable. On modern Android versions you have to activate the file transfer manually.
  Connecting a MTP device can have two effects wich might help to break out of a kiosk mode environment.
  First, it can bypass some USB filter rules. MTP devices are not mass storage device like USB flash drives. This can
  help with file exchange on restricted devices. Second, it may trigger an auto play popup. Clicking on it allows
  you to chose what to do when an MTP device gets connected - e.g. opening an explorer window allowing you to break out.
  If the explorer process is not running, there might be no auto play functionality. Also, some behavior depends on
  the Windows version.
* **External USB SSDs**: External USB SSDs can sometimes also be used to bypass some USB filter rules, because they are
  USB Attached SCSI (UAS) devices and not mass storage devices.
* **External DVD Drives**: External USB DVD drives can sometimes also be used to bypass some USB filter rules, because
  they are yet another device class.
* **Second screen**: Plugging in a second screen can help with breaking out of kiosk mode environments. If there
  no e.g. HDMI port, try attaching a USB-to-HDMI adapter. On the second screen, where the main application is likely
  not running, the input might be filtered different or not at all. Sometimes it is enough to plug in a mouse,
  move the pointer to the second screen and right click.



### Network (Ethernet/Wi-Fi)

Using access to the network interface of a device in kiosk mode, might also help in breaking out or compromising the
system. However, there is no general tips and tricks here, as this highly depends on the available services.
Just do a port scan and work from there. Maybe you find e.g. a network share with very lax permissions and no
authentication.

* Attach a USB Wi-Fi dongle and check if you can connect to your own network. You can then scan the system itself,
  try to intercept the network traffic or copy files from/to your own system.
* Try to enable the Windows [mobile hotspot](https://support.microsoft.com/en-us/windows/use-your-windows-device-as-a-mobile-hotspot-c89b0fad-72d5-41e8-f7ea-406ad9036b85)
  feature via the quick settings or the settings menu ([directlink](ms-settings:network-mobilehotspot?activationSource=SMC-IA-4027762)).
  You can then access the internal network where the Kiosk system is connected to. This can also be done if the
  network uses Network Access Control (NAC) and you can't connect your own system.


### Android

Some systems run Android as their operating system. Since this is quite different from e.g. Windows, it deserves
its on section here. Most tips & ticks for Android are brought to you by
[Syed's awesome Pentest Wiki](https://wiki.smhuda.com/pentesting/application-security/mobile-security/android-application-testing/kiosk-mode-breakout-testing).

* Check if USB debugging is enabled or not, try connecting device with USB and see if you can use ADB commands or not.
* The application running in kiosk mode can be an exit by long pressing on the “Background process”.
* Check if you can root the device or not
* If the application itself has an upload option, try to install burp cert and proxy or adb.
* Use a help/faq which may have any external link of web reference which will be opened by default tablet browser
  can be used to download malicious apk afterward.
* Try to open android device in safe mode and disable/uninstall kiosk application.
* Check if kiosk application has any exit button which requires a password, then give 0000 as default password
  or go to the kiosk application vendor website and find if there is any fallback/reset functionality procedure
  mentioned or not which you can use in your testing.
* Check if USB debugging is enabled and you can install FRIDA hooking application, then use FRIDA to disable
  kiosk running on startup.
* Sometimes USB debugging is disabled in normal mode, but it can be enabled in fastboot/samemode boot mode.
  So try opening tablet in safeboot or fastboot mode and then check if USB debugging is working or not.
* Sometimes installing alternative homescreen can also bypass kiosk browser lockdown.
* Try to find out which kiosk lockdown software (commercial/free) that company is using, go to their website
  find documentation if there are default password or anything like that you can access. Check for any
  backdoor in the configuration file.
* Try to find out if any researcher/company in the world has bypassed it or produced any
  vulnerability/exploit regarding that software, if yes apply it in your engagement.
* Try attaching a USB keyboard. Some keys or shortcut might help you break out. A list of keys and shortcuts
  can be found over at [appt.org](https://appt.org/en/docs/android/features/keyboard-access) (may vary on devices).
* Try to open as many activities (windows) as you can. Having too many of them open might cause a crash that
  breaks you out (only on older Android versions).
* Look out for links again. On Android links can be used to open apps. If they are not installed, Android might
  even open the Google Play store which lets you install them. One scenario could be: you can access a web site.
  Form there you find links to e.g. facebook, instagram, etc. They in turn let you access the google search. You
  then switch to picture search, click on the camera icon, and Google Lense will open, or even better, the Google Play
  store.



### Other

This section houses some tips, tricks and ideas that did not really fit in any other section.

* **NFC enabled Android devices**: A lot of Android systems have a NFC reader. The initial tag discovery is handled
  by Android. If an tag contains NDEF formatted entries, Android can handle that directly. For example, if there
  is a URL to a website programmed on it, the browser will open to that page. It is even possible to directly open
  other apps. Since the Android settings are also an app, this can be used to break out. Apps like
  [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc) allow to format/clear and write
  lots of different NFC tags. To make a tag that opens up the settings (default Android configuration):
  1. Format/clear the tag.
  2. Create a new NDEF "application" record.
  3. Enter "com.android.settings" as package name.
* **Bluetooth keyboards**: Some devices allow you to pair Bluetooth peripherals. Connecting a Bluetooth keyboard
  greatly improves the the chance of finding a successful kiosk mode breakout. If you do not have
  a Bluetooth keyboard at had, you can simulate one with your laptop or phone.
  If a device uses an old BlueZ Bluetooth stack (mostly Linux and Android) it might be vulnerable to CVE-2023-45866.
  This issue allows you to force-pair a keyboard as long as you know the Bluetooth address of the target. An
  easy to use implementation is called [BlueDucky](https://github.com/pentestfunctions/BlueDucky).
* **URI handlers**: Web browsers typically can open way more than just websites. Instead of putting in a common URL
  using the HTTP(S) protocol, other URI with different protocols/types can be used.
  Most browsers support other protocols than just HTTP(S). One popular example would be FTP. Accessing an
  FTP server can be done by specifying the protocol in the URI, e.g. `ftp://example.com`. Even the local file
  system can be accessed by specifying e.g. `file:///c:/windows/system32/cmd.exe`. It can also be used
  access programs linked to a protocol. For example, `mailto:test@example.com` will open the standard mail program.
  If no program is associated, a dialog will show up which lets the user choose a program.
  `shell` URI handlers might also be a good way to access functions on the system.
  More information and examples can be found at:
  * ["Unassociated Protocols", Kiosk Escape and Jail Breakout by Swissky](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/escape-breakout/#unassociated-protocols)
  * ["Shell URI Handlers", Kiosk Escape and Jail Breakout by Swissky](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/escape-breakout/#shell-uri-handlers)
  * [Tools section](#tools) offers some website you can visit that have a lot of handy links that exploit URI
  behavior.
* **QR code or barcode reader**: Some terminals in kiosk mode have a QR or barcode scanner. A lot of these
  readers emulate a keyboard that types in what it read from the code. Therefore, scanning specially crafted
  codes can aid in breaking out of a kiosk mode. Most HID-based readers even allow key combinations like
  Ctrl+Alt+Delete. Sometimes it is necessary to reconfigure the scanner to allow such special codes, but typically
  this can also be done though barcodes. If possible, find out what reader is used and look up the manual.
  An example for some Honeywell readers can be found [here](https://sps-support.honeywell.com/s/article/CTRL-ALT-DEL-function-barcode).
  It requires Code 39 to be enabled, in full ASCII mode and allow for "special key interpretation".
  User manuals (like [this from a Honeywell Genesis XP 7680g](https://www.posnet.com.pl/files/products_download/509/7680-en-ug.pdf))
  are likely to have barcodes to setup all the required features without accessing an application.



### Tools

There is some hardware and software out there which might help with breaking out of a kiosk mode environment.

* [iKAT V (2011, Defcon 19)](https://swin.es/k/): Website which host a lot of links and functions which might
  help to break out of a terminal running a web browser in kiosk mode.
* [iKAT v3 (2010, Defcon 18)](http://www.ikat.kronicd.net/): Older version of the previous website which host
  a lot of links and functions which might help to break out of a terminal running a web browser in kiosk mode.
* [Kiosk Breakout by Phrack](https://www.phrack.me/tools/2022/11/02/Kiosk-Breakout.html): Another website hosting
  a lot of links which might help to break out of a terminal running a web browser in kiosk mode.
* USB adapters: There are situations where having a some USB adapters might help. An example would be a terminal,
  where you can disconnect the USB wire between the touch screen and the internal terminal. This leaves you with
  probably with a Standard-B plug. If you want to connect e.g. a keyboard, you need an adapter with a Standard-B
  receptacle and a Standard-A receptacle or USB-C receptacle. Some examples of useful adapters:
  * [Standard-B receptacle to Standard-A receptacle](https://a.co/d/8O0an0I)
  * [USB-C plug to Standard-A retractable](https://a.co/d/0luS65H)
  * [Standard-A plug to USB-B retractable](https://a.co/d/asl7AwY)
  * [Standard-B plug to Standard-A retractable](https://a.co/d/gZ4pXLk)
  * [USB hub](https://a.co/d/7cx2w5F)
  * [USB to Ethernet, to HDMI](https://a.co/d/hhb4Fsc)
  * [USB to Ethernet, to HDMI, to SD card reader](https://a.co/d/cUo2fpY)

  USB adapters that allow to plug in e.g. a flipper (USB C) if the device lets you unplug
  a USB B cable to e.g. the touch screen. Also USB Hub



## Useful resources

* [Introduction to Kiosk Breakout, SecQuest](https://www.secquest.co.uk/white-papers/introduction-to-kiosk-breakout)
* [Kiosk Escape and Jail Breakout, InternalAllTheThings, Swissky](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/escape-breakout/)
* [Kiosk Mode / Breakout Testing, Syed M. Huda](https://wiki.smhuda.com/pentesting/application-security/mobile-security/android-application-testing/kiosk-mode-breakout-testing)
