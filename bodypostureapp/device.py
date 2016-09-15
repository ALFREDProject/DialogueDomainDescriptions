# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice
from tdm.device_handler import send_to_frontend_device


class BodyPostureAppDevice(DddDevice):

    BODY_POSITIONS_ENGLISH = {
        "sit": "sit",
        "stand": "stand",
        "lie": "lie",
    }

    BODY_POSITIONS_FRENCH = {
        "asseoir": "assis",
        "assis": "assis",
        "debout": "debout",
        u"allongé": u"allongé",
    }

    BODY_POSITIONS_DUTCH = {
        "zit": "zit",
        "sta": "sta",
        "lig": "lig",
        "ik zit": "zit",
        "ik sta": "sta",
        "ik lig": "lig",
    }

    class HowToPostureAction(DeviceAction):
        PARAMETERS = ["selected_bodyposture.grammar_entry"]

        @send_to_frontend_device
        def perform(self):
            pass

    class PostureRecognizer(EntityRecognizer):
        def recognize(self, string, language):
            if language == "eng":
                return self._recognize_posture(string, self.device.BODY_POSITIONS_ENGLISH)
            if language == "dut":
                return self._recognize_posture(string, self.device.BODY_POSITIONS_DUTCH)
            if language == "fre":
                return self._recognize_posture(string, self.device.BODY_POSITIONS_FRENCH)
            return []

        def _recognize_posture(self, string, positions):
            result = []
            words = string.lower().split()
            for bodyposture in positions.keys():
                if bodyposture.lower() in words:
                    recognized_entity = {
                        "sort": "bodyposture",
                        "grammar_entry": positions[bodyposture]
                    }
                    result.append(recognized_entity)
            return result
