# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction

from contactsapp.device import ContactsAppDevice


class ContactsAppDevice(ContactsAppDevice):

    class ContactsComparisonAction(DeviceAction):
        PARAMETERS = ["selected_contact_name.grammar_entry"]

        def perform(self, selected_contact_name):
            return True
