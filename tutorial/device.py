# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceWHQuery, DddDevice, Validity, DeviceAction
from tdm.device_handler import send_to_frontend_device


class TutorialDevice(DddDevice):

    def __init__(self):
        self.should_recognize_name = False
        self.should_recognize_age = False

    class RecognizeName(DeviceAction):
        def perform(self):
            self.device.should_recognize_name = True
            self.device.should_recognize_age = False
            return True

    class RecognizeAge(DeviceAction):
        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_age = True
            return True

    class TutorialRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
            result = []
            if self.device.should_recognize_name:
                result.append({"sort": "name", "grammar_entry": string})
                self.device.should_recognize_name = False
            elif self.device.should_recognize_age:
                result.append({"sort": "age", "grammar_entry": string})
                self.device.should_recognize_age = False
            return result

    class CommandStart(DeviceAction):
        @send_to_frontend_device
        def perform(self):
            pass

    class CommandContinue(DeviceAction):
        @send_to_frontend_device
        def perform(self):
            pass

    class CommandIUnderstand(DeviceAction):
        @send_to_frontend_device
        def perform(self):
            pass

    class CommandPlayASound(DeviceAction):
        @send_to_frontend_device
        def perform(self):
            pass

    class CommandShowAnImage(DeviceAction):
        @send_to_frontend_device
        def perform(self):
            pass

    class CommandWhatIsYourName(DeviceAction):
        PARAMETERS = ["selected_name.grammar_entry"]
        @send_to_frontend_device
        def perform(self, selected_name):
            pass

    class CommandAge(DeviceAction):
        PARAMETERS = ["selected_age.grammar_entry"]
        @send_to_frontend_device
        def perform(self, selected_age):
            pass
