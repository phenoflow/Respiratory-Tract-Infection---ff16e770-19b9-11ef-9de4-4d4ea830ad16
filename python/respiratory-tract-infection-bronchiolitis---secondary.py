# Rebecca M Joseph, Mohammad Movahedi, William G Dixon, Deborah P M Symmons, 2024.

import sys, csv, re

codes = [{"code":"490","system":"icd9"},{"code":"466","system":"icd9"},{"code":"J20.8","system":"icd9"},{"code":"J40","system":"icd9"},{"code":"J21","system":"icd9"},{"code":"J20.3","system":"icd9"},{"code":"J20.9","system":"icd9"},{"code":"J21.8","system":"icd9"},{"code":"J20.7","system":"icd9"},{"code":"J20","system":"icd9"},{"code":"J21.9","system":"icd9"},{"code":"J20.6","system":"icd9"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('respiratory-tract-infection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["respiratory-tract-infection-bronchiolitis---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["respiratory-tract-infection-bronchiolitis---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["respiratory-tract-infection-bronchiolitis---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
