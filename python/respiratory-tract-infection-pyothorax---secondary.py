# Rebecca M Joseph, Mohammad Movahedi, William G Dixon, Deborah P M Symmons, 2024.

import sys, csv, re

codes = [{"code":"112.6","system":"icd9"},{"code":"118.1","system":"icd9"},{"code":"108.1","system":"icd9"},{"code":"108.3","system":"icd9"},{"code":"128.6","system":"icd9"},{"code":"110.6","system":"icd9"},{"code":"101.6","system":"icd9"},{"code":"118","system":"icd9"},{"code":"109.6","system":"icd9"},{"code":"114.6","system":"icd9"},{"code":"118.6","system":"icd9"},{"code":"108.5","system":"icd9"},{"code":"118.3","system":"icd9"},{"code":"128.5","system":"icd9"},{"code":"115.6","system":"icd9"},{"code":"128.1","system":"icd9"},{"code":"118.2","system":"icd9"},{"code":"123.6","system":"icd9"},{"code":"117.6","system":"icd9"},{"code":"108","system":"icd9"},{"code":"113.6","system":"icd9"},{"code":"100.6","system":"icd9"},{"code":"120.6","system":"icd9"},{"code":"118.5","system":"icd9"},{"code":"128","system":"icd9"},{"code":"128.3","system":"icd9"},{"code":"128.2","system":"icd9"},{"code":"108.2","system":"icd9"},{"code":"J86","system":"icd9"},{"code":"J86.0","system":"icd9"},{"code":"J86.9","system":"icd9"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('respiratory-tract-infection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["respiratory-tract-infection-pyothorax---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["respiratory-tract-infection-pyothorax---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["respiratory-tract-infection-pyothorax---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
