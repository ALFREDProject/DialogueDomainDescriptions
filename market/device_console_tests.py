# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction

from market.device import MarketDevice


class MarketDevice(MarketDevice):

    class SearchTerm(DeviceAction):
        PARAMETERS = ["selected_market_search_string.grammar_entry"]

        def perform(self, selected_market_search_string):
            return True
