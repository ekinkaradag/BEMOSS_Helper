# DeviceRandomizer.py
It generates a total of 22 states for a Device. It resemblances the actual BEMOSS Cassandra database structure. It appends to an existing JSON file so we can use Firebase to access it from anywhere and expand the database we already have. After the script is done, you must import the resulting JSON file to Firebase manually.

## Usage:
```
    python3 DeviceRandomizer.py
```
<u><b>NOTE:</b></u> JSON file must be accessible. Preferably in the same folder as <code>DeviceRandomizer.py</code>

After running the script just follow the instructions.
Example:
```
    Enter the json file's name: bemoss.json

    Enter a device name (e.g. Device13): Device2

    Enter a agent_id (e.g. Sock_2212): Sock_3333

    Enter a username (e.g. backupsave): admin

    Enter the maximum amount of power the device can draw in Watts (e.g. 60): 60

    Enter the number of times the device has been turned off (e.g. 2): 3
```

# modifyIP.py
This script eliminates a setup step that needs user to manipulate sensitive data. Normally in order to run BEMOSS smoothly PostgreSQL needs to be configured properly. BEMOSS does not handle IP configuration of PostgreSQL and needs the user enter it manually everytime the local ip changes. That results in a complicated and unneccesarry work for the user. To eliminate that work, I wrote this script. This script automatically changes those IP address fields, if neccesarry. If you follow the steps below, this can be done automatically everytime BEMOSS launches.

## Usage:
- To implement this script to every-day usage, this script needs to be in ~/BEMOSS3.5/GUI folder
- Add the line <code>sudo python3 modifyIP.py</code> to ~/BEMOSS3.5/GUI/startBEMOSS_GUI.sh
    - It has to be run as root(sudo) because the files that need to be changed are for root-access only.
    - Make sure to add this line just before <code>python GUI.py</code> so it should look like this:

    ```bash
        #!/bin/sh

        #Get project path
        mypath=$(readlink -f "$0")
        echo $mypath
        guipath=$(dirname "$mypath")
        echo $guipath
        projectpath=$(dirname "$guipath")

        NET_Installed=$(dpkg-query -W --showformat='${Status}\n' python-netifaces|grep "install ok      installed")
        echo $NET_Installed

        if [ "$NET_Installed" = "install ok installed" ]; then
        	echo "Package Installed"
        else
        	echo "Installing Package..."
        	sudo apt-get install python-netifaces --assume-yes
        fi
        TK_Installed=$(dpkg-query -W --showformat='${Status}\n' python-imaging-tk|grep "install ok      installed")
        echo $TK_Installed

        if [ "$TK_Installed" = "install ok installed" ]; then
        	echo "Package Installed"
        else
        	echo "Installing Package..."
        	sudo apt-get install python-imaging-tk --assume-yes
        	# Tested on Odroid, this board looks like need the package below.
        	sudo apt-get install python-imaging --assume-yes
        fi

        #run GUI in virtual environment
        cd $guipath
        sudo python3 modifyIP.py
        python GUI.py
    ```