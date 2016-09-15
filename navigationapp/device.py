# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction, DeviceWHQuery, DddDevice, EntityRecognizer
from tdm.device_handler import send_to_frontend_device


class NavigationAppDevice(DddDevice):

    def __init__(self):
        self.recogPlace = 0

    PLACES = {
        "test": "test",
    }

    MODES_ENGLISH = {
        "walk": "walk",
        "bike": "bike",
        "car": "car",
    }

    MODES_FRENCH = {
        "marche": "marche",
        u"vélo": u"vélo",
        "voiture": "voiture",
    }

    MODES_DUTCH = {
        "lopen": "lopen",
        "fiets": "fiets",
        "auto": "auto",
        "doorvoer": "doorvoer",
        "transit": "transit",
    }

    class RecogPlace(DeviceAction):

        def perform(self):
            self.device.recogPlace = 1
            return True

    class result_location(DeviceWHQuery):

        @send_to_frontend_device
        def perform(self):
            pass

    class ShowWayToTownAction(DeviceAction):
        PARAMETERS = ["selected_place.grammar_entry","selected_transport.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_place, selected_transport):
            pass

    class NavigationRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            result = []
            words = string.lower().split()
            if self.device.recogPlace > 0:
                for place in self.device.PLACES.keys():
                    if place.lower() in words:
                        recognized_entity = {
                            "sort": "place",
                            "grammar_entry": place
                        }
                        result.append(recognized_entity)
                if not result:
                    self.device.PLACES[string] = string
                    recognized_entity = {
                        "sort": "place",
                        "grammar_entry": string
                    }
                    result.append(recognized_entity)
                    self.device.recogPlace -= 1
            else:
                result.extend(self._recognize_modes_for_language(words, language))
            return result

        def _recognize_modes_for_language(self, words, language):
            if language == "eng":
                modes = self._recognize_modes(words, self.device.MODES_ENGLISH)
                return modes
            if language == "dut":
                modes = self._recognize_modes(words, self.device.MODES_DUTCH)
                return modes
            if language == "fre":
                modes = self._recognize_modes(words, self.device.MODES_FRENCH)
                return modes
            return []

        def _recognize_modes(self, words, modes):
            result = []
            for mode in modes.keys():
                if mode.lower() in words:
                    recognized_entity = {
                        "sort": "transport",
                        "grammar_entry": mode
                    }
                    result.append(recognized_entity)
            return result
