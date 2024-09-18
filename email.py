email = input("Enter Your Email: ")  # g@g.in abdul@gmail.com
k, j, d = 0, 0, 0

if len(email) >= 6:
    if email[0].isalpha():  # Ensure first character is a letter
        if ('@' in email) and (email.count('@') == 1):  # Must have one @
            local, domain = email.split('@')  # Split local and domain parts
            if domain.endswith('.com') or domain.endswith('.in'):  # Check if domain is valid
                for i in local:  # Validate local part
                    if i.isspace():  # Check for spaces
                        k = 1
                    elif i.isupper():  # Check for uppercase letters
                        j = 1
                    elif i.isdigit():  # Allow digits
                        continue
                    elif i in ['.', '_']:  # Allow periods and underscores in the local part
                        continue
                    elif i.isalpha():  # Allow alphabetic characters
                        continue
                    else:  # Any other character is invalid
                        d = 1
                if k == 1 or j == 1 or d == 1:  # If there's a space, uppercase letter, or invalid character
                    print("Wrong Email 5")
                else:
                    print("Right Email.")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")
