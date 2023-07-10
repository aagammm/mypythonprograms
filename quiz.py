
def ans():
    match opt:
        case 2:
            print("Your answer is correct")
        case _:
            print("Your answer is wrong")

q1=print("What is the capital of India?")
print("1.Mumbai   2.New delhi\n3.Kolkata  4.Chandigarh")
opt=int(input("Enter your option:"))
ans()
