# BeautifulSoup is used to scrape webpages
# requests will be used for GET requests on the web page selected
# Simple Mail Transfer Protocol will be used to access my gmail
# Time isn't needed, but it will timestamp sent emails and runs

### you SHOULD have two-factor auth enabled on your google account
### https://www.google.com/landing/2step/
### https://myaccount.google.com/apppasswords <-- use to create unique PW

from bs4 import BeautifulSoup
import time
import requests
import smtplib
 

localTime = time.asctime( time.localtime(time.time()) )
# this is the item in the Steam store we will track
URL = "https://store.steampowered.com/app/462770/Pyre/"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }


def steam_price_checker():

    """ The price checker will scrape the html of the Steam store on the selected product page. The title was friendly enough, but you will want to strip the price in order to rid the random whitespace for slicing. This program will check the current price and the discount price since Steam uses two different class divs for these prices. """

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    game_title = soup.find(attrs={"apphub_AppName"}).get_text()
    game_price = soup.find(attrs={"game_purchase_price price",}).get_text()
    discount = soup.find(attrs={"discount_final_price"}).get_text()

    # Steam has tons of html whitespace on the L and R of the price. Strip is needed
    # Next, convert to int and create a slice of the whole dollar amount
    # Have to use price and discount depending on which class used on Steam
    stripped_price = game_price.strip()
    current_price = int(stripped_price[1:3])
    current_discount = int(discount[1:3])   

    print(f"The game being tracked is: {game_title}\nThe current price is: ${current_price}\nThe current discount price is {current_discount}")

    if current_price < 10 or current_discount < 10: # this is where you will set your price
        notify_email()     
    
    else:
        print(f"\nLast price check run: {localTime}")
        print()

# This function will run at the end of price checker if price condition is met.
def notify_email():

    """ Function will make a call to selected login email to access and send email to selected recipient. .starttls will encrypt. You don't need 2 factor auth, but if you're using gmail, it makes it much easier to just auto generate a password instead of passing your own password in (and of course, less dangerous)"""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # This is where your email and your google app password will input.
    server.login('ibkoets@gmail.com', 'tnoirxbynqzdncfs') 

    subject = f'Price for tracked game has has reduced below $10: {localTime}'
    body = 'Check Steam for the reduced price. \n\nClick this link: https://store.steampowered.com/app/462770/Pyre/'
    # subject and body have to be made into msg for the sendmail() method
    msg = f"Subject: {subject}\n\n{body}"
    # remember that sendmail() takes three arguments. one HAS to be msg
    server.sendmail('ibkoets@gmail.com', 'ibkoets@gmail.com', msg)

    print('An email was sent to the requested email.')
    # SHUT YOUR SERVER!
    server.quit()

# The loop will run until the game drops below desired price. time uses unit seconds so this loop will run twice a day.
while True:
    steam_price_checker()
    time.sleep(60 * 60 * 12)