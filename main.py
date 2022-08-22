import smtplib
import datetime as dt
import random

my_email = "diamondtuskstest@gmail.com"
password = "jkhqjiomubyvuxne"

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()
    quote_of_the_day = random.choice(quotes)

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()   # makes it secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="diamondtusks@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}")

print(quote_of_the_day)
