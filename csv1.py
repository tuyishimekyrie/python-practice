import csv

with open('data.csv') as file:
    writer = csv.writer(file);
    writer.writerow(["Transaction ID","Product ID","Price"]);
    writer.writerow([1000,1,5]);
    writer.writerow([1001,2,15]);
    writer.writerow([1002,3,25]);