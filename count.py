import csv
import os
import re

def extract_money(text):
    pattern = r'\$(\d+(\,\d{3})*(\.\d{2})?)'
    matches = re.findall(pattern, text)
    
    total_amount = 0.0
    for match in matches:
        amount = match[0].replace('$', '').replace(',', '')
        total_amount += float(amount)
    
    return total_amount

def calculate_total_money(csv_file):
    total_money = 0.0
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  
        
        for row in reader:
            for cell in row:
                total_money += extract_money(cell)
    
    return total_money

if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.abspath(__file__))
    csv_folder = os.path.join(script_folder, "csv")
    
    for filename in os.listdir(csv_folder):
        if filename.endswith(".csv"):
            csv_file = os.path.join(csv_folder, filename)
            total_money = calculate_total_money(csv_file)
            
            print(f"CSV File: {filename}")
            print(f"Total amount of money: ${total_money:.2f}")
            print("=" * 30)
