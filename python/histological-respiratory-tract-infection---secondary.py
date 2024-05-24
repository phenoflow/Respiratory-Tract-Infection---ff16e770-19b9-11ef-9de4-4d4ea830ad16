# Rebecca M Joseph, Mohammad Movahedi, William G Dixon, Deborah P M Symmons, 2024.

import sys, csv, re

codes = [{"code":"109.5","system":"icd9"},{"code":"101.5","system":"icd9"},{"code":"119.5","system":"icd9"},{"code":"113.5","system":"icd9"},{"code":"A16.1","system":"icd9"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('respiratory-tract-infection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["histological-respiratory-tract-infection---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["histological-respiratory-tract-infection---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["histological-respiratory-tract-infection---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
