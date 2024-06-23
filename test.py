import csv
def read_csv_data():
    csv_files = "./dataset/cosmetic_clean_final.csv"
    all_data = []  # List to hold all data rows with column names
    
    with open(csv_files, 'r', encoding='utf-8') as file:
        csv_text = file.read()
    csv_reader = csv.reader(csv_text.splitlines())
    
    headers = next(csv_reader)  # Extracting the header row
    for row in csv_reader:
        if row:  # Ensuring the row is not empty
            row_data = {headers[i]: row[i] for i in range(len(row))}  # Create a dict with column names
            all_data.append(row_data)
    return all_data  # Return the list of dictionaries
print(read_csv_data())