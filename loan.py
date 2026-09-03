

def loan_calculation(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest

    return interest, total_amount