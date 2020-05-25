import json
import sys
import random

numberOfStates = 22

def randomPower(watt, newOff, numberOfStates):
    states = []
    for i in range(newOff):
        states.append(0)
        
    for i in range(numberOfStates-newOff):
        states.append(random.uniform(0.1, watt))
    
    random.shuffle(states)
    return states

#(randomPower(100,2,numberOfStates))
def main():
    try:
        jsonfile= str(input("Enter the json file's name: "))
        with open(jsonfile) as f:
            data = json.load(f)
    except:
        print(jsonfile, " file couldn't be found")
        return

    # print(data['Device1'][0]['date_id'])

    newDevice = str(input('Enter a device name (e.g. Device13): '))
    newAgentID = str(input('Enter a agent_id (e.g. Sock_2212): '))
    newUser = str(input('Enter a username (e.g. backupsave): '))
    newPower = int(input('Enter the maximum amount of power the device can draw in Watts (e.g. 60): '))
    newOff = int(input('Enter the number of times the device has been turned off (e.g. 2): '))
    powerStates = randomPower(newPower, newOff, numberOfStates)
    newDict = {newDevice : []}

    for i in range(numberOfStates):
        if powerStates[i] != 0:
            stateDict = {'agent_id':newAgentID,
                         'date_id':data['Device1'][i]['date_id'],
                         'power':powerStates[i],
                         'status': 'ON',
                         'time':data['Device1'][i]['time'],
                         'user':newUser }
        else:
            stateDict = {'agent_id':newAgentID,
                         'date_id':data['Device1'][i]['date_id'],
                         'power':0,
                         'status': 'OFF',
                         'time':data['Device1'][i]['time'],
                         'user':newUser }
        
        # Append to older JSON
        newDict[newDevice].append(stateDict)
        data.update(newDict)

    # Write to file
    with open('bemoss.json', 'w') as json_file:
        json.dump(data, json_file, indent = 4, sort_keys=True)

if __name__ == "__main__":
    main()