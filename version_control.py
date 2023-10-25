#Alejandro Velez's encode function
def encode(in_password):
    out_password = ""
    while int(in_password) >0:
        num = int(in_password)%10
        if num+3<=9:
            num+=3
            out_password = str(num) + out_password
        else:
            num = (num+3) % 10
            out_password = str(num) + out_password
        in_password = str(int(in_password) // 10)
    return out_password

#Decode created by Jesse Bloom
def decode(out_password):
    decoded_password = ""
    for num in out_password:
        if num == "0":
            decoded_password += "7"
        elif num == "1":
            decoded_password += "8"
        elif num == "2":
            decoded_password += "9"
        else:
            num=int(num)
            num-=3
            decoded_password +=str(num)
    return decoded_password



if __name__ == "__main__":
    option = 0
    password = ""
    while(option!=3):
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option ==1:
            in_pass = input("Please enter your password to encode: ")
            out_password = encode(in_pass)
            print("Your password has been encoded and stored!\n")
        elif option ==2:
            decoded_password=decode(out_password)
            print("The encoded password is " + out_password+", and the original password is " + decoded_password+".\n")
        elif option ==3:
            break
        elif option !=3:
            print("Option not found.", end=" ")
            option = int(input("Choose another option: "))

