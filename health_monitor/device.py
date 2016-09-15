# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery, DddDevice
from tdm.device_handler import send_to_frontend_device


class HealthMonitorDevice(DddDevice):
    VITAL_PARAMETERS_ENGLISH = {
        "temperature": "temperature",
        "heartrate": "heartrate",
        "pulse": "pulse",
        "respiration": "respiration",
        "steps": "steps",
    }

    VITAL_PARAMETERS_FRENCH = {
        u"température": "temperature",
        "rythmecardiaque": "heartrate",
        "pouls": "pulse",
        "respiration": "respiration",
        u"fréquencerespiratoire": "respiration",
        "pas": "steps",
        u"podomètre": "steps",
    }

    VITAL_PARAMETERS_DUTCH = {
        "lichaamstemperatuur": "temperature",
        "temperatuur": "temperature",
        "hartslag": "heartrate",
        "polsslag": "pulse",
        "ademfrequentie": "respiration",
        "ademhaling": "respiration",
        "aantalstappen": "steps",
    }

    class VitalParameterRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            if language == "eng":
                months = self._recognize_parameters(string, self.device.VITAL_PARAMETERS_ENGLISH)
                return months
            if language == "dut":
                months = self._recognize_parameters(string, self.device.VITAL_PARAMETERS_DUTCH)
                return months
            if language == "fre":
                months = self._recognize_parameters(string, self.device.VITAL_PARAMETERS_FRENCH)
                return months
            return []

        def _recognize_parameters(self, string, parameters):
            result = []
            words = string.lower().split()
            for spoken_phrase in parameters.keys():
                if spoken_phrase.lower() in words:
                    recognized_entity = {
                        "sort": "vital_parameter",
                        "grammar_entry": spoken_phrase,
                    }
                    result.append(recognized_entity)
            return result

    class value_of_vital_parameter(DeviceWHQuery):
        PARAMETERS = ["selected_vital_parameter.grammar_entry"]

        @send_to_frontend_device
        def perform(self, vital_parameter):
            pass
