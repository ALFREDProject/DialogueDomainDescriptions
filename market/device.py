# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DddDevice, DeviceAction
from tdm.device_handler import send_to_frontend_device

class MarketDevice(DddDevice):
    SEARCH_TERMS_ENG = [
        "tools",
    ]
    SEARCH_TERMS_DUT = [
        "gereedschap",
    ]
    SEARCH_TERMS_FRE = [
        "outils"
    ]

    def __init__(self):
        self.should_recognize_search_term = False

    class RecognizeSearchTerm(DeviceAction):

        def perform(self):
            self.device.should_recognize_search_term = True
            return True

    class SearchTerm(DeviceAction):
        PARAMETERS = ["selected_market_search_string.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_market_search_string):
            pass

    class MarketRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            result = []
            if self.device.should_recognize_search_term:
                entity = self._market_search_string_entity(string)
                result.append(entity)
                self.device.should_recognize_search_term = False

            try:
                search_terms = self._search_terms_of_language(language)
            except:
                return result
            for search_term in search_terms:
                if search_term in string.lower():
                    entity = self._market_search_string_entity(search_term)
                    result.append(entity)
            return result

        def _market_search_string_entity(self, search_term):
            return {"sort": "market_search_string", "grammar_entry": search_term}

        def _search_terms_of_language(self, language):
            if language == "eng":
                return self.device.SEARCH_TERMS_ENG
            elif language == "dut":
                return self.device.SEARCH_TERMS_DUT
            elif language == "fre":
                return self.device.SEARCH_TERMS_FRE
            else:
                raise Exception("Got unexpected language %s" % language)
