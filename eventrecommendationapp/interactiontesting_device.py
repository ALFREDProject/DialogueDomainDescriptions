# -*- coding: utf-8 -*-

import re

from tdm.lib.device import DeviceAction, DeviceWHQuery, DddDevice, EntityRecognizer, Validity
from tdm.device_handler import send_to_frontend_device


class EventRecommendationAppDevice(DddDevice):

    ALLOWED_AMOUNTS = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10"
    }
	
    class ShowEventRecommendationAction(DeviceAction):

        def perform(self):
            return True
			
    class ShowEventDetailsAction(DeviceAction):
        PARAMETERS = ["selected_event_number"]

        def perform(self, selected_event_number):
            return True
			
    class GoToEventAction(DeviceAction):
        PARAMETERS = ["selected_event_number"]

        def perform(self, selected_event_number):
            return True
			
    class DontGoToEventAction(DeviceAction):
        PARAMETERS = ["selected_event_number"]

        def perform(self, selected_event_number):
            return True

    class EventRecommendationRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
            result = []        
            words = string.lower().split()
            for number in self.device.ALLOWED_AMOUNTS.keys():
                if number.lower() in words:
                    recognized_entity = {
                        "sort": "event_number",
                        "grammar_entry": number
                    }
                    result.append(recognized_entity)				
            return result
