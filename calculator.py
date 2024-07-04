# Create a calculator 
user_input1 = int(input("number 1: "))
user_input2 = int(input("number 2: "))
operation = input("What operation do you want to do? ")

if operation == "+" or operation == "add":
    print(user_input1 + user_input2)
elif operation == "-" or operation == "subtract":
    print(user_input1 - user_input2)
elif operation == "/" or operation == "divide":
    if user_input2 == 0: 
        print("bruh that's not defined, you cannot divide by 0")
    else: print(user_input1 / user_input2)
    
elif operation == "*" or operation == "multiply":
    print(user_input1 * user_input2)
elif operation == "**" or operation == "power":
    print(user_input1 ** user_input2)
elif operation == "%" or operation == "percentage": 
    print(user_input1 / user_input2 * 100)    
else:
    print("We are sorry, this feature isn't available. Do your own math.")
