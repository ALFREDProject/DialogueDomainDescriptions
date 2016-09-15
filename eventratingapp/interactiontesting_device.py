# -*- coding: utf-8 -*-

import re

from tdm.lib.device import DeviceAction, DeviceWHQuery, DddDevice, EntityRecognizer, Validity
from tdm.device_handler import send_to_frontend_device


class EventRatingAppDevice(DddDevice):

    ALLOWED_AMOUNTS = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5"
    }

    class RateEventAction(DeviceAction):
        PARAMETERS = ["selected_stars_size"]

        def perform(self, selected_stars_size):
            return True

    class EventRatingRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
            result = []        
            words = string.lower().split()
            for number in self.device.ALLOWED_AMOUNTS.keys():
                if number.lower() in words:
                    recognized_entity = {
                        "sort": "stars_size",
                        "grammar_entry": number
                    }
                    result.append(recognized_entity)
            return result 
			