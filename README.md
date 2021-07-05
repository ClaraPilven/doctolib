# Requirements

beautifulsoup (`aptitude install python3-bs4`)

make sure that the fr_FR.utf8 locales are installed

# doctolib

This script checks every given minutes (by default 10) whether an appointement for a doctor is free before a set date.

If a date has been freed, it will send a mail to tell the receivers of the mail.

To use, complete the config file with the different entries:
- The sender mail.
- The sender password (on google, you will need to activate the access to less secure Apps).
- The receivers mail.
- The URL (explained a little lower).
- The limit date you want the appointement to be available.
- The log file name (by default log.txt).
- The message that will be sent by mail (You will have to change the mails inside).

After, on a console, just run 
```
usage: python3 doctolib.py 
```

# To run in the background

To suspend : `Ctrl Z`

To start in background : `bg %[job]`

To remove from the terminal : `disown %[job]`

# How to get the URL

Go on the URL of the doctor you want an appointement with

Right click on the page and go to Network

Reload

Change the week for the appointement

On the network window, click on the last GET and look at the address on the right panel ("Request URL").

Paste this URL in the config file (you can change the date if needed).


