# steam-price-scraper
A program to track the price of a game you want on the Steam store and send an email alert when the price drops below input. 

***Please note that I use text wrap on my text editor for this in order to see long URLs and to keep input < 80 characters.

This is a program I used to learn the smtp library (smtplib).
I plan on making it a REST API to add or remove games and possibly manipulate other settings.

In order to run the program, just input 'python3 steam_price_checker.py' into your terminal.
If you would like to change the game you are tracking, just copy and paste the URL from the Steam store into line 18 "URL = ' ' "
(Please note that you will want to also paste the URL into the "body" variable on line 67.)
