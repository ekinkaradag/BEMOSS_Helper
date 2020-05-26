import json
import sys
import random
import time

def random_date(start, end, const):
    stime = time.mktime(time.strptime(start, '%Y-%m-%d %H:%M'))
    etime = time.mktime(time.strptime(end, '%Y-%m-%d %H:%M'))

    ptime = stime + const * (etime - stime)
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(ptime))

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
    print("\n!!!CAUTION!!!")
    print("The script will write to bemoss-device.json file on this folder. If you already have bemoss-device.json file make sure to back it up, because it will overwrite!\n")

    # print(data['Device1'][0]['date_id'])

    newAgentID = str(input('Enter the agent_id (e.g. Sock_2212): '))
    newUser = str(input('Enter the username (e.g. backupsave): '))
    newPower = int(input('Enter the maximum amount of power the device can draw in Watts (e.g. 60): '))
    startDate = str(input('Enter the start date in YYYY-MM-DD format (e.g. 2020-01-01): '))
    endDate = str(input('Enter the end date in YYYY-MM-DD format (e.g. 2020-02-25): '))
    numberOfStates = int(input('Enter the number of state records this device should have (e.g. 20): '))
    newOff = int(input('Enter the number of times the device has been turned off (e.g. 2): '))
    powerStates = randomPower(newPower, newOff, numberOfStates)
    newList = []
    
    dateList= []
    # Generate random dates and sort them after the loop
    for i in range(numberOfStates):
        a = random_date(startDate + " 00:00", endDate + " 23:59", random.random())
        dateList.append(a)
    dateList.sort()
    
    for i in range(numberOfStates):
        time = dateList[i] + ":00.000Z"
        if powerStates[i] != 0:
            stateDict = {'agent_id':newAgentID,
                         'date_id':dateList[i][:10],
                         'power':powerStates[i],
                         'status': 'ON',
                         'time':time,
                         'user':newUser }
        else:
            stateDict = {'agent_id':newAgentID,
                         'date_id':dateList[i][:10],
                         'power':0,
                         'status': 'OFF',
                         'time':time,
                         'user':newUser }
        
        # Append to older JSON
        newList.append(stateDict)

    # Write to file
    with open('bemoss-device.json', 'w') as json_file:
        json.dump(newList, json_file, indent = 4)

    print("WRITE SUCCESSFUL!")

if __name__ == "__main__":
    main()