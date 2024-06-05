try:
    
    x = 10 / 0  
except ZeroDivisionError:
   
    print("Error: Division by zero is not allowed.")
except Exception as e:
   
    print("An error occurred:", str(e))