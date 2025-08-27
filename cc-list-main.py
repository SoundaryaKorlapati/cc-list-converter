import csv
import ast

input_file = 'today_inlays.csv'
output_file = 'output.csv'

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:

    writer = csv.writer(outfile)
    writer.writerow(['id', 'userId', 'createdAt', 'name', 'cycleCount'])

    next(infile)  

    for line in infile:
        try:
            parts = line.strip().split(',', 4)  
            if len(parts) != 5:
                print(f"Skipping malformed line: {line}")
                continue

            id_, userId, createdAt, name_raw, cycle_raw = parts
            name = name_raw.strip().strip("'")
            cycle_raw = cycle_raw.strip()

            # Clean the cycle list string
            if cycle_raw.startswith('"') and cycle_raw.endswith('"'):
                cycle_raw = cycle_raw[1:-1]  # Remove outer quotes

            cycle_list = ast.literal_eval(cycle_raw)

            for cycle in cycle_list:
                writer.writerow([id_, userId, createdAt, name, cycle])

        except Exception as e:
            print(f"Skipping line due to parsing error: {line} ({e})")
