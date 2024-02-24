import requests
import smtplib
from datetime import datetime

MY_LAT = 20.593683
MY_LONG = 78.962883


def is_iss_overhead():
    # getting iss latitude and longitude
    r = requests.get(url="http://api.open-notify.org/iss-now.json")
    r.raise_for_status()
    iss_data = r.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_long = float(iss_data["iss_position"]["longitude"])
    # checking your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True


def is_night():
    # getting sunset and sunrise time
    parameters = {"lat": MY_LAT, "lng": MY_LONG}
    response = requests.get("https://api.sunrisesunset.io/json?", params=parameters)
    response.raise_for_status()
    data = response.json()
    # converts the sunrise and sunset times from a string format to datetime objects.
    sunrise = datetime.strptime(data["results"]["sunrise"], "%I:%M:%S %p")
    sunset = datetime.strptime(data["results"]["sunset"], "%I:%M:%S %p")

    # getting current time
    now = datetime.now()

    # check if day or night
    if sunrise.time() > now.time() > sunset.time():
        return True


while True:
    if is_iss_overhead() and is_night():
        my_email = "nikhiltelase@gmail.com"
        password = "kcpiidljiiafbimn"
        to_mail = "nikhiltelase17@gmai.com"
        message = f"Subject: Look Up👆👆 \n\nThe is above you in the sky."

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # seure
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=[to_mail],
                                msg=message)
        print("I send a birthday letter")
