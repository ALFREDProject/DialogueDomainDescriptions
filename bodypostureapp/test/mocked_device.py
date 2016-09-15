from tdm.lib.device import DeviceAction

from bodypostureapp.device import BodyPostureAppDevice


class BodyPostureAppDevice(BodyPostureAppDevice):

    class HowToPostureAction(DeviceAction):
        PARAMETERS = ["selected_bodyposture.grammar_entry"]

        def perform(self, selected_bodyposture):
            return True