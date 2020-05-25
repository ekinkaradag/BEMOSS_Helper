import netifaces
import os

#Get local IP address of the machine
IPs = []
ip_string = ''
interfaces = netifaces.interfaces()
for i in interfaces:
    if i == 'lo':
        continue
    iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
    if iface is not None:
        for j in iface:
            IPs.append(j['addr'])
            ip_string += str(j['addr'])


version = os.listdir('/etc/postgresql')

# Read postgresql.conf
fullFilePath = '/etc/postgresql/' + version[0] + '/main/postgresql.conf'
textFile =open(fullFilePath, "r")
lines = textFile.readlines()
textFile.close()

newLine = "listen_addresses = '*' \t\t\t# what IP address(es) to listen on;\n"
# Modify postgresql.conf if needed
if( lines[58] != newLine):
    lines[58] = newLine

    # Write to postgresql.conf
    textFile =open(fullFilePath, "w")
    textFile.writelines(lines)
    textFile.close()
    print("postgresql.conf line 59 has been changed to: " + newLine)


lines=[] # Delete all the elements from lines[]

# Read pg_hba.conf
fullFilePath = '/etc/postgresql/' + version[0] + '/main/pg_hba.conf'
textFile =open(fullFilePath, "r")
lines = textFile.readlines()
textFile.close()

# Add the line to pg_hba.conf
newLine = "host    all             all             " + ip_string + "/32            md5\n"
if(lines[92] == "# IPv6 local connections:\n"):
    lines.insert(92, newLine)
    # Write to postgresql.conf
    textFile =open(fullFilePath, "w")
    textFile.writelines(lines)
    textFile.close()
    print("Line inserted to pg_hba.conf: " + newLine)
else:
    # Only change the line if needed
    if(lines[92] != newLine):
        lines[92] = newLine
        
        # Write to postgresql.conf
        textFile =open(fullFilePath, "w")
        textFile.writelines(lines)
        textFile.close()
        print("pg_hba.conf line changed to: " + newLine)

lines=[] # Delete all the elements from lines[]

# Read multinode_data.json for Node1
fullFilePath = 'multinode_data.json'
textFile =open(fullFilePath, "r")
lines = textFile.readlines()
textFile.close()

newLine = '            "address": "tcp://' + ip_string + ':9000"\n'
# Write to multinode_data.json if needed
if(lines[8] != newLine):
    lines[8] = newLine

    # Write to postgresql.conf
    textFile =open(fullFilePath, "w")
    textFile.writelines(lines)
    textFile.close()

