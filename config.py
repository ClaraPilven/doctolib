log_file = "log.txt" # link to the log file

sender_mail = "" # mail of the sender
sender_pwd = "" # password of the sender (Don't push online if it is written here)

receivers = [""] # list of the receivers of the mail

url = "" 
# url we get from the doctolib page, telling us when the next appointement is.

message = """From: From You You You <yourname@domain.com>
To: To Person <example@domain.com>
Subject: An Appointement is available !
Go on doctolib ! An appointement to what you were looking for is available !
"""
# The mail we send 

time_to_refresh = 10 # It will look about a new appointment every 10 minutes

date = "01-01-2022" # The limit date we want the appointement to be.