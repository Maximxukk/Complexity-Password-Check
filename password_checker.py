# This program is used to check the complexity of your password.
while True:
    def check_password_strength(password):
        score = 0
        feedback = []
        if len(password) < 8: 
            feedback.append("Your password needs more than 8 characters.")
        else:
            score += 1
    
        if any(char.isupper() for char in password):
            score += 1
        else: 
            feedback.append("At least one character should be uppercase!")
    
        if any(char.islower() for char in password):
            score += 1
        else: 
            feedback.append("At least one character should lowercase!")
    
        special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
        if any(char in special_characters for char in password):
            score += 1
        else:
            feedback.append("At least one special character")
    
        if any(char.isdigit() for char in password):
            score += 1
        else:
            feedback.append("There should be at least one digit.")
    
        if score <= 2:
            strength = 'Weak'
        elif score <= 4:
            strength = 'Good'
        else:
            strength = 'Strong'
    
        print("Your password is", strength , "\nHere is your feedback! \n", feedback)

    user_password = input('What is your password: ')
    check_password_strength(user_password)

    redo = input("Would you like to try another password? ").lower()


    if redo == 'no':
        break
    else:
        print("Continuing....")
