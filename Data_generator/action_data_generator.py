import csv
import random

entry_percentage = {'ice_cream_parlor': 0.2, 'french_fries': 0.6, 'drink': 0.5, 'souvenir': 0.05}

def generate_data():
    with open(r'C:\...\action.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['identification_card_id', 'ice_cream_parlor', 'french_fries', 'drink', 'souvenir'])

        for i in range(1, 629471 + 1):
            ice_cream_parlor = random.randint(0, 6) if random.random() < entry_percentage['ice_cream_parlor'] else 0
            french_fries = random.randint(0, 3) if random.random() < entry_percentage['french_fries'] else 0
            drink = random.randint(0, 3) if random.random() < entry_percentage['drink'] else 0
            souvenir = random.randint(0, 6) if random.random() < entry_percentage['souvenir'] else 0

            writer.writerow([i, ice_cream_parlor, french_fries, drink, souvenir])

if __name__ == '__main__':
    generate_data()
