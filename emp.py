
def gross_salary(basic, hra, da):
    return basic + hra + da


def deductions(gross):
    pf = gross * 0.12
    tax = gross * 0.10
    return pf + tax


def net_salary(gross, deduction):
    return gross - deduction