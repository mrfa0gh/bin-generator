import random
from datetime import datetime

def luhn_check(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:  # Double every second digit
            digit *= 2
            if digit > 9:  # Subtract 9 if the result is greater than 9
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0

def generate_card(bin_format):
    while True:
        card = ""
        for char in bin_format:
            if char == 'x' or char == 'X':
                card += str(random.randint(0, 9))
            else:
                card += char
        
        # Validate using Luhn algorithm
        if luhn_check(card):
            return card

def generate_cvv():
    return str(random.randint(100, 999))

def generate_expiry_date():
    current_year = datetime.now().year
    current_year_short = int(str(current_year)[-2:])  # Last two digits of the year
    current_month = datetime.now().month

    month = random.randint(1, 12)
    year = random.randint(current_year_short, current_year_short + 10)  # Up to 10 years ahead

    return f"{month:02d}|{year:02d}"  # Format as MM/YY

def main():
    print("Valid Card Generator with CVV and Expiry Date")
    bin_format = input("Enter BIN : ").strip()
    
    if not bin_format or 'x' not in bin_format.lower():
        print("Invalid BIN format. Please include 'x' for random digits.")
        return
    
    try:
        count = int(input("How many card numbers to generate? "))
        if count <= 0:
            print("The count should be greater than 0.")
            return
    except ValueError:
        print("Invalid count. Please enter a number.")
        return
    
    print("\nGenerated Cards (Card Number | CVV | Expiry Date):")
    for _ in range(count):
        card = generate_card(bin_format)
        cvv = generate_cvv()
        expiry_date = generate_expiry_date()
        print(f"{card}|{cvv}|{expiry_date}")

if __name__ == "__main__":
    main()
