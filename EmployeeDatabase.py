import json
  
def companyRegistery(name):
    #opening database file
    f = open('employee.json')
    
    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in data['emp_details']:
        #checking if the record matches the name
        if(i['name'] == name):
            return i
    
    # Closing file
    f.close()
