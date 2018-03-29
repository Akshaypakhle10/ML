from datetime import datetime

time = datetime.now()
user_input = input("Enter any of these choices: 1)US 2)UK 3)India")


def format_time(user_input):
    if user_input == "US" or "UK":
        print (time.strftime("%m/%d/%Y %H:%M:%S"))
    elif user_input == "India":
        print ("haha")



format_time(user_input)

