
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
import datetime
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase
import psutil
import gpiozero
from gpiozero import CPUTemperature

logger = logging.getLogger(__name__)


class SystemFunctions(CBPiExtension):

    def __init__(self,cbpi):
        self.cbpi = cbpi
        self._task = asyncio.create_task(self.run())

    async def run(self):

        plugin = await self.cbpi.plugin.load_plugin_list("cbpi4-system")
        self.version=plugin[0].get("Version","0.0.0")
        self.name=plugin[0].get("Name","cbpi4-system")

        self.system_update = self.cbpi.config.get(self.name+"_update", None)

        logger.info('Starting System Functions background task')
        await self.systemparameters()

        while True:
            self.Reboot = self.cbpi.config.get("AutoReboot", "No")

            if self.Reboot == "Yes":
                RebootTime = self.cbpi.config.get("AutoRebootTime", 0)
                Rebootminute = 0 
                Reboottimelow = datetime.time(RebootTime,Rebootminute)
                Reboottimehigh = datetime.time(RebootTime, Rebootminute,15)
                currentdate = datetime.datetime.now()
                currenttime = datetime.datetime.time(currentdate)
                if currenttime >= Reboottimelow and currenttime < Reboottimehigh:
                    os.system('systemctl reboot')

            await asyncio.sleep(1)

    async def systemparameters(self):
        autoreboot = self.cbpi.config.get("AutoReboot", None)
        reboottime = self.cbpi.config.get("AutoRebootTime", None)
        
        if autoreboot is None:
            logger.info("INIT AutoReboot parameter")
            try:
                await self.cbpi.config.add("AutoReboot", "No", type=ConfigType.SELECT, description="Reboot Pi once a day at selected time",
                                                                                                    source=self.name,
                                                                                                    options=[{"label": "Yes", "value": "Yes"},
                                                                                                        {"label": "No", "value": "No"}])
                                                                                                        
            except:
                logger.warning('Unable to update config')
        else:
            if self.system_update == None or self.system_update != self.version:
                try:
                    await self.cbpi.config.add("AutoReboot", autoreboot, type=ConfigType.SELECT, description="Reboot Pi once a day at selected time",
                                                                                                    source=self.name,
                                                                                                    options=[{"label": "Yes", "value": "Yes"},
                                                                                                        {"label": "No", "value": "No"}])
                                                                                                        
                except:
                    logger.warning('Unable to update config')               
                

        if reboottime is None:
            logger.info("INIT RebootTime parameter")
            try:
                await self.cbpi.config.add("AutoRebootTime", "0", type=ConfigType.SELECT, description="Time for daily reboot", 
                                                                                                        source=self.name,
                                                                                                      options=[{"label": "0", "value": 0},
                                                                                                        {"label": "1", "value": 1},
                                                                                                        {"label": "2", "value": 2},
                                                                                                        {"label": "3", "value": 3},
                                                                                                        {"label": "4", "value": 4},
                                                                                                        {"label": "5", "value": 5},
                                                                                                        {"label": "6", "value": 6},
                                                                                                        {"label": "7", "value": 7},
                                                                                                        {"label": "8", "value": 8},
                                                                                                        {"label": "9", "value": 9},
                                                                                                        {"label": "10", "value": 10},
                                                                                                        {"label": "11", "value": 11},
                                                                                                        {"label": "12", "value": 12},
                                                                                                        {"label": "13", "value": 13},
                                                                                                        {"label": "14", "value": 14},
                                                                                                        {"label": "15", "value": 15},
                                                                                                        {"label": "16", "value": 16},
                                                                                                        {"label": "17", "value": 17},
                                                                                                        {"label": "18", "value": 18},
                                                                                                        {"label": "19", "value": 19},
                                                                                                        {"label": "20", "value": 20},
                                                                                                        {"label": "21", "value": 21},
                                                                                                        {"label": "22", "value": 22},
                                                                                                        {"label": "23", "value": 23}])
                                                                                                    
            except:
                logger.warning('Unable to update config')
        else:
            if self.system_update == None or self.system_update != self.version:
                try:
                    await self.cbpi.config.add("AutoRebootTime", reboottime, type=ConfigType.SELECT, description="Time for daily reboot", 
                                                                                                        source=self.name,
                                                                                                      options=[{"label": "0", "value": 0},
                                                                                                        {"label": "1", "value": 1},
                                                                                                        {"label": "2", "value": 2},
                                                                                                        {"label": "3", "value": 3},
                                                                                                        {"label": "4", "value": 4},
                                                                                                        {"label": "5", "value": 5},
                                                                                                        {"label": "6", "value": 6},
                                                                                                        {"label": "7", "value": 7},
                                                                                                        {"label": "8", "value": 8},
                                                                                                        {"label": "9", "value": 9},
                                                                                                        {"label": "10", "value": 10},
                                                                                                        {"label": "11", "value": 11},
                                                                                                        {"label": "12", "value": 12},
                                                                                                        {"label": "13", "value": 13},
                                                                                                        {"label": "14", "value": 14},
                                                                                                        {"label": "15", "value": 15},
                                                                                                        {"label": "16", "value": 16},
                                                                                                        {"label": "17", "value": 17},
                                                                                                        {"label": "18", "value": 18},
                                                                                                        {"label": "19", "value": 19},
                                                                                                        {"label": "20", "value": 20},
                                                                                                        {"label": "21", "value": 21},
                                                                                                        {"label": "22", "value": 22},
                                                                                                        {"label": "23", "value": 23}])

                except:
                    logger.warning('Unable to update config')      

        if self.system_update == None or self.system_update != self.version:
            try:
                 await self.cbpi.config.add(self.name+"_update", self.version,type=ConfigType.STRING,description="cbpi4 system version update",source="hidden")         
            except Exception as e:
                logger.warning('Unable to update config') 
                logger.warning(e)
                
@parameters([Property.Select("Type", options=["CPU Load [%]", "Available Memory [Mb]", "Used Memory [%]", "CPU Temp"], description="Select type of system data you want to monitor.")])
class SystemSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
        super(SystemSensor, self).__init__(cbpi, id, props)
        self.value = 0
        self.Type = self.props.get("Type","CPU Load")
        self.Timer = 15

    async def run(self):
        counter = 0
        while self.running is True:
            if counter == 0:
                TEMP_UNIT=self.get_config_value("TEMP_UNIT", "C")
                FAHRENHEIT = False if TEMP_UNIT == "C" else True
                try:
                    if self.Type == "CPU Load [%]":
                        self.value = round(psutil.cpu_percent(interval=None),1)
                    elif self.Type == "Available Memory [Mb]":
                        mem = psutil.virtual_memory()
                        self.value = round((int(mem.available) / (1024*1024)),1)
                    elif self.Type == "Used Memory [%]":
                        mem = psutil.virtual_memory()
                        self.value = round(float(mem.percent),1)
                    else:
                        temp = CPUTemperature()
                        self.value = round(temp.temperature,1)

                    self.push_update(self.value)                       
                    self.log_data(self.value)
                    
                except Exception as e:
                    logging.info(e)
                pass
            counter += 1
            if counter == self.Timer:
                counter = 0
            self.push_update(self.value,False)    
            #self.cbpi.ws.send(dict(topic="sensorstate", id=self.id, value=self.value))
            await asyncio.sleep(1)

   
    def get_state(self):
        return dict(value=self.value)

def setup(cbpi):
    cbpi.plugin.register("SystemSensor", SystemSensor)
    cbpi.plugin.register("SystemFunctions", SystemFunctions)
    pass
