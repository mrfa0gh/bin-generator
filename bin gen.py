import random
from datetime import datetime

def luhn_check(card_number):
    digits = [int(d) for d in card_number]
    checksum = 0
    reverse_digits = digits[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

def generate_card(bin_format):
    while True:
        card = ""
        for char in bin_format:
            if char in ['x', 'X']:
                card += str(random.randint(0, 9))
            else:
                card += char
        while len(card) < 16:
            card += str(random.randint(0, 9))
        if luhn_check(card):
            return card

def generate_cvv():
    return str(random.randint(100, 999))

def generate_expiry_date():
    now = datetime.now()
    current_month = now.month
    current_year = now.year % 100
    while True:
        month = random.randint(1, 12)
        year = random.randint(current_year, current_year + 10)
        if year > current_year or (year == current_year and month >= current_month):
            return f"{month:02d}|{year:02d}"

def validate_expiry_date(month, year):
    now = datetime.now()
    current_month = now.month
    current_year = now.year % 100
    return (year > current_year) or (year == current_year and month >= current_month)

def main():
    print("Valid Card Generator with CVV and Expiry Date")
    user_input = input("Enter BIN or BIN|MM|YY : ").strip()

    if not user_input:
        print("Input cannot be empty.")
        return

    parts = user_input.split('|')
    bin_format = parts[0]
    expiry_manual = False
    expiry_month = expiry_year = None

    if len(parts) == 3:
        try:
            expiry_month = int(parts[1])
            expiry_year = int(parts[2])
            if not (1 <= expiry_month <= 12):
                raise ValueError
            if not validate_expiry_date(expiry_month, expiry_year):
                print("Invalid expiry date. Cannot be in the past.")
                return
            expiry_manual = True
        except ValueError:
            print("Invalid expiry date format.")
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
        if expiry_manual:
            expiry = f"{expiry_month:02d}|{expiry_year:02d}"
        else:
            expiry = generate_expiry_date()
        print(f"{card}|{cvv}|{expiry}")

if __name__ == "__main__":
    main()
