# needs beautifulsoup (aptitude install python3-bs4)
# make sure that the fr_FR.utf8 locales are installed

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime, timedelta
import locale
import time
import json
import os

import config

# we make sure that we use the french locale
locale.setlocale(locale.LC_ALL, 'fr_FR.utf8')

def my_print(text):
    '''
    Writing in the log file
    '''
    if os.path.exists(config.log_file):
        with open(config.log_file, "a") as f:
            f.write(text + "\n")
    else:
        with open("log.txt", "w") as f:
            f.write(text + "\n")

def send_mail(sender, receivers, message, psswd):
    '''
    Sends a mail to the receivers informing them an appointment has been found
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, psswd)
    server.sendmail(sender, receivers, message)
    server.quit()
    my_print("Successfully sent email")


def get_page():
    '''
    Get the html of the url
    '''
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    my_print(str(current_time)+" : No appointement found.")
    req = Request(config.url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return webpage

def get_next_appointement(content):
    '''
    Get the next date available
    '''
    soup = BeautifulSoup(content, "lxml")
    dates = soup.findAll("p")
    jsonDate = json.loads(str(dates[0])[3:-4])
    return datetime.strptime(jsonDate["next_slot"], '%Y-%m-%d')

def main():
    content = get_page()
    next_appointement = get_next_appointement(content)
    appointement_wanted = datetime.strptime(config.date, '%d-%m-%Y')
    while True:
        if(appointement_wanted > next_appointement):
            send_mail(config.sender, config.receivers, config.message, config.auth_pwd)
            with open(config.log_file, "a") as f:
                f.write("appointement wanted = {}\n".format(appointement_wanted))
                f.write("next appointement = {}\n".format(next_appointement))
            appointement_wanted = next_appointement - timedelta(1)      
        else:
            content = get_page()
            next_appointement = get_next_appointement(content)
            with open("log.txt", "w") as f:
                f.write("{}: {}\n".format(time.strftime("%H:%M:%S"), next_appointement))
            time.sleep(config.time_to_refresh*60)

if __name__ == "__main__":
    main()
