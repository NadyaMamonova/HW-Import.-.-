import salary
import people
from datetime import *
if __name__ == '__main__':
    print(f'Сейчас {datetime.today().strftime("%d-%m-%Y")}')

people.get_employees()
salary.calculate_salary()
