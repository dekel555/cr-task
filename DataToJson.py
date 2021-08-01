import json


# Converting the 'data.txt' file to json file for the mongoimport command

def main():
    filename = 'data.txt'
    
    users = []
    
    with open(filename) as f:
        for line in f:
            fields = list(line.split(', ', 4))
            i = 0
            dict1 = {}
            while i<4:
                value = fields[i].strip().split(": ")
                dict1[value[0]]= value[1]
                i = i + 1
                    
            users.append(dict1)
    
          
    with open("users.json", 'w+') as out_file:
        json.dump(users, out_file, indent = '\t')
        


if __name__ == "__main__":
    main()
