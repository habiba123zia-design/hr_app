def  calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5:
         bonus_percentage = 0.2
    elif performance_rating == 4 or performance_rating == 3:
        bonus_percentage = 0.1
    else:
        bonus_percentage = 0.00
    return base_salary * bonus_percentage

def  calculate_tax(gross_salary):
    
    if gross_salary >7000:
        tax_rate = 0.15
    elif gross_salary >= 3000: 
        tax_rate = 0.10
    else:
        tax_rate =0.00
    return gross_salary * tax_rate       
def main_hr_app():
    print("--- Corporate Payroll System ---")
    employee_name =input("enter your name: ")
    department =input("enter your department: ")
    base_salary =float(input("enter your base salary: "))
    performance_rating=int(input("enter your performance rating between (1-5): "))
    if performance_rating <1 or performance_rating>5 or base_salary <0:
        print(" Invalid data entered. Please restart and check your inputs.")
        return
    bonus = calculate_bonus(base_salary, performance_rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax
    print("--- Payroll Summary ---")
    print(f"employee name :{employee_name}")
    print(f"department :{department}")
    print(f"base salary is :{base_salary}")
    print(f"------the bonus-----")
    print(f" your rating is :{performance_rating}")
    print(f"the bonus you earned is :{bonus}")
    print(f"your gross salary is :{gross_salary}")
    print("------the tax-----")
    print(f"the tax is :{tax}")
    print(f"your net salary is :{net_salary}")
main_hr_app()