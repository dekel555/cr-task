import json
import pandas as pd


def delID(data):
    for user in data:
        del user['_id']

def cap(data):
    for user in data:
        user['firstname'] = user['firstname'].capitalize()
        user['lastname'] = user['lastname'].capitalize()

def hidePass(data):
    for user in data:
        user['password'] = '*' * len(user['password'])

def manipulateData():

    with open ("exData.json",'r') as f:

        usersData = [json.loads(line) for line in f]
        
        # remove the object ID field 
        delID(usersData)
        
        # capitalize firstname and lastname fields
        cap(usersData)
        
        # hiding plaintext passwords
        hidePass(usersData)
        
        # sorting data by firstname field
        usersData = sorted(usersData, key = lambda k: k['firstname'])

        return usersData

def saveToHtmlPage(data):
    df = pd.DataFrame(data)
    df.to_html('index.html')


def main():
    data = manipulateData()
    saveToHtmlPage(data)



if __name__ == "__main__":
    main()
