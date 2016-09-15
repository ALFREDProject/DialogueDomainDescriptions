# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice, DeviceWHQuery
from tdm.device_handler import send_to_frontend_device


class ContactsAppDevice(DddDevice):
    CONTACTS_NAMES = {
        "John": "John"
    }

    class ContactsComparisonAction(DeviceAction):
        PARAMETERS = ["selected_contact_name.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_contact_name):
            pass

    class ContactsAppRecognizer(EntityRecognizer):

        def recognize_entity(self, string):
            result = []
            words = string.lower().split()
            for cname in self.device.CONTACTS_NAMES.keys():
                if cname.lower() in words:
                    recognized_entity = {
                        "sort": "contact_name", "grammar_entry": cname
                    }
                    result.append(recognized_entity)
            return result
