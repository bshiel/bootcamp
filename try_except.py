file_name = "test.csv"
default_file="rodents.csv"

try:
    a= open(file_name)
except:
    a= open(default_file)
    
    print a.readline()
