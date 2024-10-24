# -*- coding: utf-8 -*-
"""
EXERCISE3
BIOGRAPHY
"""

name = input("Enter your name: ").strip()
hometown = input("Enter your hometown: ").strip()


while True:
    try:
        age = int(input("Enter your age: ").strip())
        break
    except ValueError:
        print("Invalid. Please enter your age as a number.")


user_info = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}


print(f"\nName: {user_info['Name']}\nHometown: {user_info['Hometown']}\nAge: {user_info['Age']}")
#ermm