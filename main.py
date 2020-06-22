from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date

if __name__ == '__main__':
    print(f"Today is {date.today()}. It's time to work!")
    get_employees()
    calculate_salary()
