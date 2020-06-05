# DeviceRandomizer.py
It generates any number of states for a Device. It resemblances the actual BEMOSS Cassandra database structure. It can be then transferred to Firebase to access it from anywhere and expand the database we already have. After the script is done, you must import the resulting JSON file to Firebase manually.

<u><b>NOTE:</b></u> When importing to Google Firebase, make sure to import it in a Device subfolder, not the root directory! If there is not one for the device you want to import, create one.

## Usage:
```
    python3 DeviceRandomizer.py
```


After running the script just follow the instructions.

Example:
```

!!!CAUTION!!!
The script will write to bemoss-device.json file on this folder. If you already have bemoss-device.json file make sure to back it up, because it will overwrite!

Enter the agent_id (e.g. Sock_2212): Sock_3333
Enter the username (e.g. backupsave): admin
Enter the maximum amount of power the device can draw in Watts (e.g. 60): 200
Enter the start date in YYYY-MM-DD format (e.g. 2020-01-01): 2020-01-01
Enter the end date in YYYY-MM-DD format (e.g. 2020-02-25): 2020-02-23
Enter the number of state records this device should have (e.g. 20): 63
Enter the number of times the device has been turned off (e.g. 2): 4
WRITE SUCCESSFUL!
```

# modifyIP.py
This script eliminates a setup step that needs user to manipulate sensitive data. Normally in order to run BEMOSS smoothly PostgreSQL needs to be configured properly. BEMOSS does not handle IP configuration of PostgreSQL and needs the user enter it manually everytime the local ip changes. That results in a complicated and unneccesarry work for the user. To eliminate that work, I wrote this script. This script automatically changes those IP address fields, if neccesarry. If you follow the steps below, this can be done automatically everytime BEMOSS launches.

## Usage:
- To implement this script to every-day usage, this script needs to be in ~/BEMOSS3.5/GUI folder
- Add the line <code>sudo python3 modifyIP.py</code> to ~/BEMOSS3.5/GUI/startBEMOSS_GUI.sh
    - You must run it as root(sudo) because the files that need to be changed are for root-access only.
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
