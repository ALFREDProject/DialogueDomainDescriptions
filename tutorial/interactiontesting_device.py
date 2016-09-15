# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceWHQuery, Validity, DeviceAction

from tutorial.device import TutorialDevice


class TutorialDevice(TutorialDevice):

    class CommandWhatIsYourName(DeviceAction):
        PARAMETERS = ["selected_name"]

        def perform(self, selected_name):
            return True

    class CommandAge(DeviceAction):
        PARAMETERS = ["selected_age"]

        def perform(self, selected_age):
            return True

    class CommandStart(DeviceAction):

        def perform(self):
            return True

    class CommandContinue(DeviceAction):

        def perform(self):
            return True

    class CommandIUnderstand(DeviceAction):

        def perform(self):
            return True

    class CommandPlayASound(DeviceAction):

        def perform(self):
            return True

    class CommandShowAnImage(DeviceAction):

        def perform(self):
            return True
