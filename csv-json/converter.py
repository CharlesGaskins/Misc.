import os
import json
import csv
import sys
from collections import OrderedDict

print("You have entered the conversion zone...")
print("The following script will convert a CSV to JSON and JSON to CSV")
def main(argv):
    filename = ''
    out_file = ''


    try:
        print("Which file do you want to convert?")
        filename = input("Filename: ")
        extension = filename.split(".")[-1].lower()
        open_file = open(filename)
        if extension == "csv":
            data = list(csv.reader(open_file))
            print("CSV uploaded")
        else:
            print("unsupported file type ... exiting")
            exit()
    except Exception as e:
        # error loading file
        print("Error loading file ... exiting:",e)
        exit()        
    else: 
        if extension == "csv":
            keys = data[0]
            converted = []
            for d in range(1, len(data)):
                obj = OrderedDict()
                for k in range(0, len(keys)):
                    if len(data[d][k]) > 0:
                        obj[keys[k]] = data[d][k]
                    else:
                        obj[keys[k]] = None
                converted.append(obj)
            
        c_file_name = os.path.basename(filename).split(".")[0]
        c_file_extension = ".json" if extension == "csv" else ".csv"
          
        if(os.path.isfile(c_file_name + c_file_extension)):
              counter = 1
              while os.path.isfile(c_file_name + " (" + str(counter) + ")" 
                                   + c_file_extension):
                  counter += 1
              
              c_file_name = c_file_name + " (" + str(counter) + ")"
          
        try:
              if c_file_extension == ".json":
                  with open(c_file_name + c_file_extension, 'w') as out_file:
                      json.dump(converted, out_file)
                 
        except:
            print("Error creating file ... exiting")
        else:
            print("File created:", c_file_name + c_file_extension)

if __name__ == "__main__":
   main(sys.argv[1:])         
          
            
             
    
    
    