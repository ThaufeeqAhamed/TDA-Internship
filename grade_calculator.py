def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work!"
    elif 80 <= marks < 90:
        return "B", "Very Good! Keep it up!"
    elif 70 <= marks < 80:
        return "C", "Good effort! You can do even better"
    elif 60 <= marks < 70:
        return "D", "You passed, Work harder next time"
    elif 0 <= marks < 60:
        return "F", "Unfortunately, you failed. Don't give up!"
    else:
        return None, None 

def main():
    print("--- Student Grade Calculator ---")
    
    name = input("Enter student name: ")
    while True:
        try:
            marks_input = input("Enter marks (0-100): ")
            marks = float(marks_input)
            if 0 <= marks <= 100:
                break
            else:
                print("Error: Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

    grade, message = calculate_grade(marks)

    print("\n" + "="*30)
    print(f"📊 RESULT FOR {name.upper()}:")
    print(f"Marks:   {marks}/100")
    print(f"Grade:   {grade}")
    print(f"Message: {message}")
    print("="*30 + "\n")

if __name__ == "__main__":
    main()