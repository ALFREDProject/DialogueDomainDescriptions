# -*- coding: utf-8 -*-

from tdm.lib.device import DddDevice, DeviceAction
from tdm.device_handler import send_to_frontend_device


class HelpDevice(DddDevice):

    class NeedHelp(DeviceAction):

        def perform(self):
            return True

    class ContactCaregiver(DeviceAction):

        def perform(self):
            return True
