from rodents import Rodent

rodents = {}
for line in open('rodents.csv'):
    
    column = line.split(',')
    ID = column[0]
    weight = column[1].strip()
    weight=float(weight)

    if ID not in rodents:
        rodents[ID]= weight
    elif ID in rodents:
        rodents[ID] = rodents[ID],weight
        
wanted_id = raw_input('type ID')
print rodents[ID]        


