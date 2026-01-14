# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 10:24:27 2025
Random Quote Generator
@author: shannon leigh comeaux
"""

  
import requests
import pyperclip


def get_quote():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        response.raise_for_status()
        data = response.json()[0]  # ZenQuotes returns a list with one dict
        return {'quote': data['q'], 'author': data['a']}
    except requests.exceptions.RequestException as e:
        print(f"We've encountered an error: {e}")
        return None

def display_quote(quote_data):
    print(f"\nQuote: {quote_data['quote']}")
    print(f"Author: {quote_data['author']}")

def menu_display():
    print("\nGreetings! Enjoy receiving a lovely new quote any time you need it.")
    print("1. Receive your Quote and enjoy.")
    print("2. Save/Copy the quote to your clipboard and read at your leisure.")
    print("3. Exit Quotes")

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
