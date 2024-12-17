import csv
from datetime import timedelta

def read_csv_file(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
            return data
        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def write_csv_file(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def data_to_string(data):
    output = ""
    for row in data:
        output += str(row) + "\n"
    return output

#Functions for editing data:

def halve_ride_times(data):
    headers = data[0]
    output = [headers]
    
    for row in data[1:]:
        hours, minutes, seconds = map(int, row[headers.index("Duration (hh:mm:ss)")].split(":"))
        totalSeconds = (hours * 3600 + minutes * 60 + seconds) // 2
        
        row[headers.index("Duration (hh:mm:ss)")] = str(timedelta(seconds = totalSeconds))
        row[headers.index("Average Speed (km/h)")] = str(float(row[headers.index("Average Speed (km/h)")]) * 2)
        
        output.append(row)
    
    return output



if __name__ == "__main__":
    path = "file path goes here"
    filename = "data.csv"   
    newFilename = "halvedTimes.csv"

    fileData = read_csv_file(path + filename)
    print("Ride data: ")
    print(data_to_string(fileData))

    fileData = halve_ride_times(fileData)
    print("Ride data with halved times: ")
    print(data_to_string(fileData))
    
    write_csv_file(fileData, path + newFilename)