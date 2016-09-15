# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction, DeviceWHQuery

from navigationapp.device import NavigationAppDevice


class NavigationAppDevice(NavigationAppDevice):

    class result_location(DeviceWHQuery):

        def perform(self):
            status_entity = {
                "grammar_entry": "Berlin",
            }
            return [status_entity]

    class ShowWayToTownAction(DeviceAction):
        PARAMETERS = ["selected_place.grammar_entry","selected_transport.grammar_entry"]

        def perform(self, selected_place, selected_transport):
            return True
