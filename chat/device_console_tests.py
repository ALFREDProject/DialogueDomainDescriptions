# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction

from chat.device import ChatDevice


class ChatDevice(ChatDevice):
    class Call(DeviceAction):
        PARAMETERS = ["selected_contact"]
        def perform(self, selected_contact):
            return True

    class VideoCall(DeviceAction):
        PARAMETERS = ["selected_contact"]
        def perform(self, selected_contact):
            return True

    class SendMessage(DeviceAction):
        PARAMETERS = ["selected_contact", "selected_message"]
        def perform(self, selected_contact, selected_message):
            return True