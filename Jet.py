mistakes=0
try:
    archivo = open("config","r")
except:
    archivo = open("config", "w")
    archivo.close()
    print("\nJet the text calculator")
    print("By __UniqueD__\n")
    print("Press Ctrl + C to exit the program\n")
try:
    while True:
        try:
            mistakes=mistakes+1
            if mistakes<10:
                num1=(float(input("\nFirst number: ")))
                num2=(float(input("Second number: ")))
                break
            else:
                print("You tried", mistakes, "times...")
                exit()
        except ValueError:
            print("\nThat's not a number\n")
    print("\n--> Select an operation\n")
    print("---(1) Addition, (2) Multiplication, (3) Substraction or (4) Division----\n")
    operation=input()
    if operation=="Addition" or operation=="2":
        print("\nThe answer is: ", num1+num2)
    elif operation=="Substraction" or operation=="3":
        print("\nThe answer is: ", num1-num2)
    elif operation=="Multiplication" or operation=="1":
        print("\nThe answer is: ", num1*num2)
    elif operation=="Division" or operation=="4":
        try:
            print("\nThe answer is: ", num1/num2)
        except ZeroDivisionError:
            print("\nYou can't divide by zero")
    else:
        print("\nWrong operation")
except KeyboardInterrupt:
    print("\n\nExiting Jet...")
