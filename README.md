# L2L Badge Reader example application #

L2L Badge Reader example application for operator check in (clock in) to a 
production line. This application uses an RFID/Magstrip/Barcode scanner (keyboard wedge) to read the 
user's badge with the value stored as the user's externalID in L2L. 

For best results, configure your scanner to append an Enter(Return) after the scan.

Author: Tyler Whitaker
Copyright 2022, L2L Inc"
Version 1.0.0

<hr>

## Requirements ##

You will need Python 3 and pip installed. The requirements.txt file will help you install the local python libraries you need.

```$ pip install -r requirements.txt```

## Configuration ##

Use the config_sample.json file to create the config.json file with the correct Server, API key, site number, linecode, etc. Below is an example:

```
{
    "server":"https://companyname.leading2lean.com",
    "apikey":"Put your api key here",
    "site":25,
    "linecode":"Coil Line 2",
    "verbose":false,
    "logdirectory":"logs/"
}
```

## Running from the Command Line ##

```bash
# run the application for operator check in (clock in)
$ python3 l2l-badge-reader.py

# run the administrator application setup a users badge in the system as the users's externalID
$ python3 l2l-setup-user-badge.py
```

Remember for the application to work correctly the user must click on this command line 
window to make it active before scanning so the scan data is captured by the app.

<hr>

## License ##

This project is under license from MIT. For more details, see the [LICENSE](license.txt) file.

<hr>

## Reader/Scanner used during development ##

I used the following RFID reader but any barcode/magstrip/RFID reader should work if it has the equvilent functionality below:
1. Scanner/Reader should act as a Keyboard Wedge (Insert scan data as if it was typed on a keyboard)
2. Are configured to send an "Enter" after the scan.

RFID Reader Details:

- Brand/Manufacturer: FissaiD
- Model: EH301
- FCC ID:2A4U3-EH301
- 125 KHz Proximity Reader
- Get Instruction manual & Questions anwsered at www.fissid.cn/eh301
- Email: Taylor@szjat.com.cn
- Purchased from Amazon here: https://www.amazon.com/dp/B07TMNZPXK?psc=1&ref=ppx_yo2ov_dt_b_product_details


## Reader/Scanner Reader Config Output:

```Support email. taylor@szjat.com.cn

Download user manual/video. www.fissaid.cn/eh301

Fm ver 5.1

Default setting is
     8h-10d.          
     With enter
     Buzzer sound
     Disable hid raw 
     Normal
     Usa keyboard

Important-
Use short or long read card method to choice or disable items
 Short read card = read card till 1 beep,then remove card
 Long read card =. Read card till 2 beep,then remove card

Config reader …if format 1-11 not same as your hid card , try advanced config

01 8h-10d.           short read card = skip.    Long read card = save.    Skip
02 2h-3d 4h-5d.      short read card = skip.    Long read card = save.    Skip
03 4h-5h.            short read card = skip.    Long read card = save.    Skip
04 5h-7d.            short read card = skip.    Long read card = save.    Skip
05 6h-8d.            short read card = skip.    Long read card = save.    Skip
06 7h-9d.            short read card = skip.    Long read card = save.    Skip
07 4h-5d 4h-5d.      short read card = skip.    Long read card = save.    Skip
08 8h.               short read card = skip.    Long read card = save.    Skip
09 6h.               short read card = skip.    Long read card = save.    Skip
10 10h.              short read card = skip.    Long read card = save.    Skip
11 10h-13d.          short read card = skip.    Long read card = save.    Skip

12 with enter.    ?  short read card = with enter.       Long read card = without enter.   With enter
13 buzzer sound.  ?  short read card = buzzer sound.     Long read card = disable buzzer.  Buzzer sound
14 enable hid raw ?  short read card = disable hid raw.  Long read card = enable hid raw.  Disable hid raw 
15 reverse data.  ?  short read card = normal data.      Long read card = reverse data.    Normal
16 keyboard layout?  Short read card = usa keyboard.     Long read card = Europe keyboard. Usa keyboard

Repeat or quit config.     Short read card = repeat.      Long read card = quit.     
Restart…

Test Scans after it rebooted:
0002706836
0002706836
4294967295
4294967295
```