# Starting our program loop
while True:
    # Get the three inputs from user
    quiz1 = float(input("Enter mark for Quiz 1: "))
    quiz2 = float(input("Enter mark for Quiz 2: "))
    quiz3 = float(input("Enter mark for Quiz 3: "))

    # Calculate the average mark
    average = (quiz1 + quiz2 + quiz3) / 3

    # Display the average
    print(f"Average Mark: {average:.2f}")

    # Determine whether the student pass or fail
    if average >= 50:
        print("Result: PASS!")
    else:
        print("Result: FAIL!")

    # Allow other students marks to be entered
    another = input("Do you want to enter marks for another student? (yes/no): ")
    if another.lower() != 'yes' and another.lower() != 'y':
        print("Goodbye!")
        break