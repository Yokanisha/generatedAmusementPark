import csv
import random
from datetime import datetime, timedelta
from workalendar.europe import Germany

country_percentage = {'germany': 0.7, 'switzerland': 0.1, 'france': 0.02, 'other': 0.08}
entry_id_percentage = {1: 0.1, 2: 0.4, 3: 0.3, 4: 0.19, 5: 0.01}

def generate_unique_id():
    id_counter = 1
    while True:
        yield id_counter
        id_counter += 1

def generate_data(start_date, end_date):
    cal = Germany()
    unique_id_generator = generate_unique_id()

    with open(r'C:\...\visitor.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'country', 'entry_id', 'identification_card_id'])

        count = 0

        current_date = start_date
        while current_date <= end_date:
            if cal.is_working_day(current_date):
                for _ in range(random.randint(2250, 2750)):
                    country = random.choices(list(country_percentage.keys()), weights=list(country_percentage.values()))[0]
                    entry_id = random.choices(list(entry_id_percentage.keys()), weights=list(entry_id_percentage.values()))[0]
                    writer.writerow([current_date.strftime('%d.%m.%Y'), country, entry_id, next(unique_id_generator)])
                    count += 1
            current_date += timedelta(days=1)
    print(count)

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

if __name__ == '__main__':
    generate_data(start_date, end_date)
