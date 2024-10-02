# Dylan Nelson
# October 02, 2024
# multiply_10_loop.py

PROMPT = "Please enter a number. "

userNumber = int(input(PROMPT))

while userNumber < 100:
    salesNumber = userNumber * 10
    print(salesNumber)
    if salesNumber >= 100:
        print(f"{salesNumber} is greater than or equal to 100. Breaking loop.")
        break
    userNumber = int(input(PROMPT))
