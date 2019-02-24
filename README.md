# sensio-mbus-server
My implementation of a modbus server to communicate with Sensio 

#### steps to run as service on your raspberry pi

1. Log in to your raspberry 
2. Make sure git is installed. If that is not the case - ```sudo apt-get install git```
3. Clone my github-repo ```git clone git://github.com/oysteoh/sensio-mbus-server.git```
4. cd into newly created folder and open server.py to modify some settings
   - Most important
       - Change ip-address with your raspberry pi's address
       - Location of your data-file needs to be provided


5. Install uModbus package needed ```pip install uModbus```
