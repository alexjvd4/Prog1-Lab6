# Alejandro Velez's decode function

def decode(in_pass):
    out_pass = ""
    while int(in_pass) > 0:
        num = int(in_pass)%10
        if num-3>=0:
            num-=3
            out_pass = str(num) + out_pass
        else:
            num+=7
            out_pass = str(num) + out_pass
        in_pass = str(int(in_pass)//10)
    return out_pass

if __name__ == "__main__":
    remain=True
    encoded_password = ""
    while remain == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        user_choice=input("Please enter an option: ")
        #My individual code
        if user_choice == "1":
            password=(input("Please enter your password to encode: "))
            encoded_password = ""
            for num in password:
                if num == "0" or num == "1"or num == "2"or num == "3"or num == "4"or num == "5"or num == "6":
                    num = int(num)
                    num+=3
                    encoded_password+=str(num)
                elif num == "7":
                    encoded_password+="0"

                elif num == "8":
                    encoded_password+="1"

                elif num == "9":
                    encoded_password+="2"

            print("Your password has been encoded and stored!")
            print("")


        #Alejandro Velez's code
        elif user_choice == "2":
            print("The encoded password is " + encoded_password+", and the original password is " + decode(encoded_password) +".\n")




        elif user_choice == "3":
            remain = False