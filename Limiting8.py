number=(input("Input 8 Numbers: Click Enter First")) 
#Making sure inputted 8 Numbers
numbers = []
# Loop 8 numbers using While loop
i = 0
while i < 8:
    try:
        number = int(input(f"Enter Number {i + 1}: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        print(" ")
        continue
    # condition for founding negative numbers
    if number < 0:
        print("Negative number found, converting to positive...")
        print(" ")
        number = abs(number) #using abs means the negative number should converted automatically to positive
    #condition of founding zero
    if number == 0:
        print("Found Zero, The program skipped...")
        print(" ")
        continue #skipping
    #condition if number is greater than 50 should minus 10
    if number > 50:
        number -= 10
    # Check if number is even or odd
    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
    # executing calculation of average
    avg = sum(range(1, number + 1)) / number
    print(f"Average of all inputted Numbers by users is {avg}")
    print(" ")
    # Add the number to the list
    numbers.append(number)
    
    i += 1

# Calculate averages for even and odd numbers
evenNum = [num for num in numbers if num % 2 == 0]
oddNum = [num for num in numbers if num % 2 != 0]

if evenNum:
    even_avg = sum(evenNum) / len(evenNum)
    print(f"Average of Even Numbers: {even_avg}")
else:
    print("No even numbers entered.") 
if oddNum:
    odd_avg = sum(oddNum) / len(oddNum)
    print(f"Average of Odd Numbers: {odd_avg}")
else:
    print("No odd numbers entered.")
    
