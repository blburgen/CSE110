print("\nEnter a rating from 1 (low/poor) to 10 (high/good) for the following:\n")

loan_size = float(input("How large is the loan? "))
credit_history = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down_payment = float(input("How large is your down payment? "))

if loan_size >= 5:
    
    if credit_history >= 7 and income >= 7:
        loan_decision = "yes"
    
    elif  credit_history >= 7 or income >= 7:
        
        if down_payment >= 5:
            loan_decision = "yes"
        
        else:
            loan_decision = "no"
            
    else:
         loan_decision = "no"
         
else:
    
    if credit_history < 4:
        loan_decision = "no"
    
    else:
        
        if income >= 7 or down_payment >= 7:
            loan_decision = "yes"
        
        elif income >= 4 and down_payment >= 4:
            loan_decision = "yes"
            
        else:
            loan_decision = "no"
            
print(f"\nYour loan decision is {loan_decision}\n")