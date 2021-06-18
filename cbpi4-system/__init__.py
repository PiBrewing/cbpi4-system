
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *

logger = logging.getLogger(__name__)



@parameters([])
class SystemActor(CBPiActor):

    @action("System Restart", parameters={})
    async def Restart(self, **kwargs):
        os.system('systemctl reboot') 
        pass

    @action("System Shutdown", parameters={})
    async def Shutdown(self, **kwargs):
        os.system('systemctl poweroff') 
        pass
   
    def init(self):
        self.state = False
        pass

    async def on(self, power=0):
        self.state = True

    async def off(self):
        self.state = False

    def get_state(self):
        return self.state
    
    async def run(self):
        pass


def setup(cbpi):
    cbpi.plugin.register("System", SystemActor)
    pass
