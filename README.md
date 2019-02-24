# sensio-mbus-server
My implementation of a modbus server to communicate with Sensio 

#### steps to run as service on your raspberry pi

1. Log in to your raspberry 
2. Make sure git is installed. If that is not the case - ```sudo apt-get install git```
3. Clone my github-repo ```git clone git://github.com/oysteoh/sensio-mbus-server.git```
4. cd into newly created folder and open server.py to modify some settings
   - Most important
       - Change ip-address with your raspberry pi's address
       - Location of your data-file needs to be provided (default is fine)
5. Create data-file at your specified location and add some random data like <br />
```1;20;300;45;53;62;71;865;924;1024``` <br />
The addresses exposed through my modbus interface from 0-10 would reflect indicies in this file when splitted on the separator specified in the config. 
6. Install uModbus package needed ```pip install uModbus```
7. Make the package run as a service on your raspberry
   - ```sudo vim /lib/systemd/system/mbus.service```
   -  ```
      [Unit]
      Description=Modbus server running as a service
      After=network.target

      [Service]
      ExecStart=/usr/bin/python -u server.py
      WorkingDirectory=/home/pi/sensio-mbus-server
      StandardOutput=inherit
      StandardError=inherit
      Restart=always
      User=pi

      [Install]
      WantedBy=multi-user.target
      ```
