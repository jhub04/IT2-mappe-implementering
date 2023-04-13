import csv

input_file = "List_of_world_cities_by_population_density.csv"
output_file = "Cleaned_List_of_world_cities_by_population_density.csv"

with open(input_file, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    with open(output_file, 'w', newline='') as output_csvfile:
        csv_writer = csv.writer(output_csvfile)

        for row in csv_reader:
            cleaned_row = [cell.replace('[', '').replace(']', '') for cell in row]
            csv_writer.writerow(cleaned_row)

print(f"Cleaned CSV file saved as: {output_file}")
