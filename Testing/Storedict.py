import json

def save_dict(_dict,filepath):
    json.dump(_dict,open(filepath,'w'))
    print("Dictonary saved")

#This function takes dictonary as an argument and save it

#TEST
#file is created or not 
#and file contain dictonary or not 
#it prints Dictonary saved