def check_marks():
    user_input = input("Enter student marks: ")
    
    try:
        marks = int(user_input)
        
        print("Valid Marks Entered")
        
    except ValueError:

        print("Invalid Marks")

check_marks()