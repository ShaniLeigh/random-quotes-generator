# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 10:24:27 2025
Random Quote Generator
@author: shannon leigh comeaux
"""
#Import the required modules: requests & pyperclip
#Have link to website copied to clipboard and ready to use.

import requests
import pyperclip

#I'm using a try block, incase the website is unavailable, inside function to retrieve quote
#This will be called in the generate quote/user input function
def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        response.raise_for_status()
        data = response.json()[0]  # ZenQuotes returns a list with one dict
        return {'quote': data['q'], 'author': data['a']}
    except requests.exceptions.RequestException as e:
        print(f"We've encountered an error: {e}")
        return None

#Created a function to display the quote and the author's name
def display_quote(quote_data):
    print(f"\nQuote: {quote_data['quote']}")
    print(f"Author: {quote_data['author']}")

#Menu display function, exit
def menu_display():
    print("\nGreetings! Enjoy receiving a lovely new quote any time you need it.")
    print("1. Receive your Quote and enjoy.")
    print("2. Save/Copy the quote to your clipboard and read at your leisure.")
    print("3. Exit Quotes")

#Created final functions that calls the helper functions to generate and display quote.
def generate_quote():
    current_quote = None
    while True:
        menu_display()
        user_selection = input("Please select from the menu options (1, 2, or 3): ").strip()
        
        if user_selection == "1":
            current_quote = get_quote()
            if current_quote:
                display_quote(current_quote)
        elif user_selection == "2":
            if current_quote:
                quote_text = f"{current_quote['quote']} — {current_quote['author']}"
                pyperclip.copy(quote_text)
                print("Your quote has been copied to your clipboard.")
            else:
                print("Please generate a quote first.")
        elif user_selection == "3":
            print("\nThank you for using 'Quotes' today!")
            print("Remember: How you do anything is how you do everything.")
            break
        else:
            print("Please enter a valid command (1, 2, or 3).")

generate_quote()

