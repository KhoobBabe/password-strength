#this function check the strength of the password
def pass_stre(passw):
    score = 0
    #gives 2 score if if the characters are between 8 and 16
    if 16>len(passw)>8:
        score+=2

    #gives 2 score if there are upper and lowercase characters
    if passw.isupper() == False and passw.islower() == False:
        score+=2

    #cgives 3 score if there are alphabets and digits
    if passw.isalpha() == False and passw.isdigit() == False:
        score+=3

    #gives 3 score if any of the three characters is present
    for i in passw:
        if i == '@' or i == '#' or i == '$':
            score+=3
            break
        
    return score
        

while True:
    #password input given here
    passw = input("Enter password: ")
    print()
    pass_stre(passw)

    #saves the password in a file if the strength is >8
    if pass_stre(passw) > 8:
        print(f"the password strength is {pass_stre(passw)}\n")
        file = open("password.txt", mode = "w")
        file.write(f"{passw}")
        file.close()
        print("password has been saved")
        break

    #if the strength is <=8 then it asks to enter again          
    else:
        print(f"the password strength is {pass_stre(passw)}\n")
        print("Your pasword is not strong enough\n")
        print("not stonks\n")
        
