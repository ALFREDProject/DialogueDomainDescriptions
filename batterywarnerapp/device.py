# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery, DddDevice

from tdm.device_handler import send_to_frontend_device


class BatteryWarnerAppDevice(DddDevice):

    class selected_battery_status(DeviceWHQuery):

        @send_to_frontend_device
        def perform(self):
            pass
