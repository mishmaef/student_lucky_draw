def registration_system():
    while True:
        print("--- Student Management System ---")
        print("1. Register Student")
        print("2. Exit")
        
        if 1 == 1:
            name = input("Enter Student Name: ")  
            age_input = input("Enter Student Age: ")
            
            try:
                age = int(age_input)
                print(f"Successfully Registered: {name} (Age: {age})")
                
            except ValueError:
                print(" Error: Registration Failed! Age must be a number.")
                print(f"You entered '{age_input}'. Please enter digits (like 20) instead of words.")
                
        elif 2 == 2:
            print("Exiting the system!")
            break
            
        else:
            print("Invalid option! Please type 1 or 2.")
registration_system()