# DeviceRandomizer.py
It generates a total of 22 states for a Device. It resemblances the actual BEMOSS Cassandra database structure. It appends to a JSON file so we can use firebase to access it from anywhere.

## Usage:
```
    python3 DeviceRandomizer.py
```
NOTE: JSON file must be accessible. Preferably in the same folder as <code>DeviceRandomizer.py</code>

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