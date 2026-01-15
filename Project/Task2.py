import random

def main():
    # 1. Get Password
    password = input("Enter your password: ")
    print() # Empty line for spacing

    # 2. Check Length
    if len(password) < 9:
        print("Password too short.")
        return

    # 3. Security Loop
    for i in range(3):
        # Pick a random index (0 to length-1)
        index = random.randint(0, len(password) - 1)
        
        # Ask user (we add 1 to index because humans count from 1, not 0)
        guess = input(f"Enter letter at position {index + 1}: ")
        print() 

        # Check if it matches
        if guess != password[index]:
            print("Incorrect")
            print("Security check failed.")
            return # Stop the program immediately
        else:
            print("Correct")
            print()

    # 4. Success message
    print("Security check passed.")

if __name__ == "__main__":
    main()