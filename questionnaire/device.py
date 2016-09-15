# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceWHQuery, DddDevice, Validity, DeviceAction
from tdm.device_handler import send_to_frontend_device


class QuestionnaireDevice(DddDevice):
    INFO_TYPES_ENGLISH = {
        "culture": "culture",
        "sport": "sports",
        "sports": "sports",
        "exhibitions": "exhibitions",
        "world": "world",
        "cinema": "cinema",
        "movies": "cinema",
        "curiosities": "curiosities",
    }

    INFO_TYPES_DUTCH = {
        "cultuur": "culture",
        "sport": "sports",
        "sports": "sports",
        "tentoonstellingen": "exhibitions",
        "werelds": "world",
        "bioscoop": "cinema",
        "curiosa": "curiosities",
    }

    INFO_TYPES_FRENCH = {
        "culture": "culture",
        "sport": "sports",
        "sports": "sports",
        "expositions": "exhibitions",
        "monde": "world",
        u"cinéma": "cinema",
        u"curiosités": "curiosities",
    }

    class GetInfo(DeviceAction):
        PARAMETERS = ["selected_info_type"]

        @send_to_frontend_device
        def perform(self, selected_info_type):
            pass

    class QuestionnaireRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            words = string.lower().split()
            if language == "eng":
                colors = self._recognize_info_types(words, self.device.INFO_TYPES_ENGLISH)
                return colors
            if language == "dut":
                colors = self._recognize_info_types(words, self.device.INFO_TYPES_DUTCH)
                return colors
            if language == "fre":
                colors = self._recognize_info_types(words, self.device.INFO_TYPES_FRENCH)
                return colors
            return []

        def _recognize_info_types(self, words, info_types):
            result = []
            for info_type_grammar_entry, info_type in info_types.iteritems():
                if info_type_grammar_entry.lower() in words:
                    recognized_entity = {
                        "name": "info_type_%s" % info_type,
                        "sort": "info_type",
                        "grammar_entry": info_type_grammar_entry
                    }
                    result.append(recognized_entity)
            return result
