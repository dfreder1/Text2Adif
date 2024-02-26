# Purpose 

   This is a python3 script to read lines of qso information from a simple text file and parse it into an ADIF formatted file for importing into any logging program that accepts the format.

   The idea is that I often use a very simple handwritten log, and this tool makes it easy to get that handwritten data into a logging file by creating a simple text file as an intermediate step.

   If I have many handwritten contacts I'll have the xyl read them out loud while I type the values into the text file, hitting the spacebar in between the fields. Very fast. 

   I suppose you could also use a dictation program. 

   Also, it can be a convenient way to quickly enter a qso with just a simple text editor.
   
# Instructions

   The input file which this script reads must be named 'textinput.txt'. Enter your data directly into this file, or copy your other text file into this file.

   The script will create a file called 'adiforimport.adi'. Rename that file 'something.adi' to save it, or just import it wherever it needs to go, and write over it next time.

   Each QSO is a single line of the text file similar to the format of the physical hand-written ARRL Logbook: 

`date/freq/mode/power/time/station worked/report sent/report rec'd/operator/comments`

   Note that ithis list does not include common items such as qth, name, qsl via, etc. I just put these in the comments data field and then move them over once they are in my digital log.

# The Deets

   In your text input file:

* You can make the first line "date/freq/mode/power/time/station worked/report sent/report rec'd/time off/comments" as a guide and the conversion script will ignore it.
* Data can be either upper or lower case, the script converts it all to upper case.
* Each field should be separated by spaces, except the Comments field which can have spaces, all other fields should have no spaces within them.
* All 10 fields must be included, but can be "0" if you want to keep it blank
* The date should be entered as 20200730 to represent July 30 2020
* The frequency must be entered in kHz, and can include decimals.
* The script will convert to MHz, so if you input 14062.9 it will put 14.0629 in the adx.
* The time should be entered as 0435 to represent 4:35 UTC.
* The time should be entered as 1422 to represent 14:22 UTC

This website was used for testing adif files: www.rickmurphy.net/cgi-bin/adifupload.php
   
# Examples

   Below are valid text lines for a file:
date / freq / mode / power / time / station worked / report sent / report rec'd / operator (you) / comments
20201127 14062 cw 100 1950 kt0a 559 579 WA6L sota w0d/bb-033  8pts
20210727 7034 cw 100 2140 ke7bgm 559 559 WA6L pota k-3459 Carillo State Park 
20211027 5332 usb 100 2152 k6hpx 559 579 WA6L gud dx

