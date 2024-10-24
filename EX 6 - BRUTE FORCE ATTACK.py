# -*- coding: utf-8 -*-
"""
EXERCISE6
BRUTE FORCE ATTACK
"""

correct_password = "12345"


max_attempts = 5
attempts = 0  

while attempts < max_attempts:
    user_input = input("Enter the password please: ")
    
    if user_input == correct_password:
        print("PASSWORD CORRECT! WELCOMEEE :DD")
        break 
    else:
        attempts += 1  
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Thats it, no more trying. YOURE DONE. ")

#i barely survived this :') 