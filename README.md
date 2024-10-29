# SMUX Automated Money Collection App

Hello Finance IC!

This payment tracking app was originally developed by me! (17th SMUX Skating Finance IC)

It filters DBS email notifications of incoming PayNow transactions only, so PayLah! transactions are not included

This app is hardcoded to only work for DBS accounts and emails (I felt that DBS had the cleanest incoming/outgoing transaction segregation)

## Setup
Create an app password for the gmail account tagged to your DBS account (needs google account 2FA to be enabled)
> You should receive a 16 digit password
> 
> DO NOT SHARE THIS PASSWORD WITH ANYONE (it's equivalent to your actual google password)

Create a file in the AutoMoneyCollection folder called .env and add these 2 lines to it:
> * USER=youremail@gmail.com
> * PASSWORD='abcd efgh ijkl mnop'
>
> don't share this file with anyone either

Install Python and PIP if you dont already have them installed
> If you can clone this repository from github, you probably already have these installed

In your command line/terminal
> Make sure the current directory is
> * C:\Users\xxx\AutoMoneyCollection for Windows
> * or /Users/xxx/AutoMoneyCollection for Mac
>
> and run this command: 
> * pip install -r requirements.txt
>
> wait for the packages to finish installing

Congrats, you're all done!

## Usage
Key in the collection start date and the output excel file to app.py

If there are multiple back-to-back collection dates, use the earliest date as the filter
> It's built to search for all transactions from the indicated start date until the present date and time, so you should be using this to check the payments on a weekly/adhoc basis

Hope this improves your quality of life as a Finance IC!

[Last updated in October 2024]