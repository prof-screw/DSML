from calculator_pkg import add, subtract, multiply, divide

def calculator():
    print("simple calculator")
    print("operations: + - * /")
    
    try:
        a= float(input("enter first number: "))
        op= input("enter operation (+ - * /)").strip()
        b=float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered.")
        return
    
    operations= {"+": add, "-": subtract, "*": multiply, "/": divide }
    
    if op not in operations:
        print("invalid operation")
        return
    
    try:
        result= operations[op](a,b)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        
if __name__== "__main__":
    calculator()