#import csv
import csv

#open file in write mode
csvfile = open("triangles.csv", "w")

#create the csv writer
csvwriter = csv.writer(csvfile, delimeter=",")

#write to the file
csvwriter.writerow([1, 2, 3])

#close file
file.close()