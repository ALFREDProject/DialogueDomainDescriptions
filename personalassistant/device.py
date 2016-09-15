# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery, DddDevice

from tdm.device_handler import send_to_frontend_device


class PersonalAssistantDevice(DddDevice):

    MIC_COLORS_ENGLISH = {
        "green": "green",
        "black": "black",
        "purple": "purple",
        "grey": "grey",
        "blue": "blue",
        "orange": "orange",
    }

    MIC_COLORS_FRENCH = {
        "gris": "gris",
        "bleu": "bleu",
        "vert": "vert",
        "noir": "noir",
        "violet": "violet",
        "orange": "orange",
    }

    MIC_COLORS_DUTCH = {
        "groen": "groen",
        "zwart": "zwart",
        "oranje": "oranje",
        "paars": "paars",
        "grijs": "grijs",
        "blauw": "blauw"
    }

    class ChangeMicrophoneColorAction(DeviceAction):
        PARAMETERS = ["selected_mircophone_color.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_microphone_color):
            pass

    class MicrophoneColorRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            words = string.lower().split()
            if language == "eng":
                colors = self._recognize_colors(words, self.device.MIC_COLORS_ENGLISH)
                return colors
            if language == "dut":
                colors = self._recognize_colors(words, self.device.MIC_COLORS_DUTCH)
                return colors
            if language == "fre":
                colors = self._recognize_colors(words, self.device.MIC_COLORS_FRENCH)
                return colors
            return []

        def _recognize_colors(self, words, colors):
            result = []
            for color in colors.keys():
                if color.lower() in words:
                    recognized_entity = {
                        "sort": "color",
                        "grammar_entry": colors[color]
                    }
                    result.append(recognized_entity)
            return result
