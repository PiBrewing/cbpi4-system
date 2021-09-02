# CraftBeerPi4 System Functions Plugin

- Functions:
    - Plugin has capability to reboot Pi every day at a time that can be specified in the settings.

![Auto Reboot](https://github.com/avollkopf/cbpi4-system/blob/main/AutoReboot.png?raw=true)
	
	- Plugin will add system 'sensors' to monitor some system parameters. The psutil package is currently used for that purpose:
		- CPU Load: 		CPU load in % (psutil: cpu_perc)
		- Available Memory:	Available system memory in Mb (psutil: vitrual_memory -> available)
		- Used memory:		Used memory in percent (psutil: vitrual_memory -> percent)
		- CPU Temp:		CPU temperature (psutil: sensors_temperatures -> cpu_thermal)
	- Each parameter has to be added as individual sensor.
	
![Sensor Config](https://github.com/avollkopf/cbpi4-system/blob/main/SystemSensor.png?raw=true)

- Installation: 
    - clone from the GIT repo
	- sudo pip install ./cbpi4-system
    - cbpi add cbpi4-system
	
- Usage:
    - Add Hardware under Sensor and choose SystemSensor as Type
	- Configure Autoreboot in settings (Default is 'No') and specify time of day (0-23 -> Full hour)

- Changelog:
	- 02.09.21: Remove Actor to reboot / shutdown system. Add automatic reboot and add system sensors
	- 18.06.21: Initial commit with Actor to shutdown/reboot system