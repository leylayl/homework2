import datetime

def simple_calculator():
    print("--- Creative Logic Calculator ---")
    
    try:
        # 1. Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # 2. Perform calculations
        add = num1 + num2
        sub = num1 - num2
        mul = num1 * num2
        # Handle division by zero
        div = num1 / num2 if num2 != 0 else "Undefined (Division by zero)"

        # 3. Format results for display
        results_text = (
            f"Results for {num1} and {num2}:\n"
            f"  Addition:       {add}\n"
            f"  Subtraction:    {sub}\n"
            f"  Multiplication: {mul}\n"
            f"  Division:       {div}\n"
        )
        
        print("\n" + results_text)

        # 4. Save to history file with timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("calculator_history.txt", "a") as file:
            file.write(f"--- Calculation at {timestamp} ---\n")
            file.write(results_text)
            file.write("-" * 30 + "\n\n")
            
        print("Success: Results appended to 'calculator_history.txt'.")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    simple_calculator()
    