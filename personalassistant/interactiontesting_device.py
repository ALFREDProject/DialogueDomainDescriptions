from tdm.lib.device import DeviceAction

from personalassistant.device import PersonalAssistantDevice


class PersonalAssistantDevice(PersonalAssistantDevice):

    class ChangeMicrophoneColorAction(DeviceAction):
        PARAMETERS = ["selected_mircophone_color.grammar_entry"]

        def perform(self, selected_microphone_color):
            return True
