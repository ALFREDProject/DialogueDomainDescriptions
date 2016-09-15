# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DddDevice, DeviceAction
from tdm.device_handler import send_to_frontend_device


class NewsDevice(DddDevice):

    def __init__(self):
        self.should_recognize_news_search_string = False

    class RecognizeNewsSearchString(DeviceAction):

        def perform(self):
            self.device.should_recognize_news_search_string = True
            return True

    class GetNews(DeviceAction):
        PARAMETERS = ["selected_news_search_string.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_news_search_string):
            pass

    class NewsRecognizer(EntityRecognizer):

        def recognize_entity(self, string):
            result = []
            if self.device.should_recognize_news_search_string:
                result.append({"sort": "news_search_string", "grammar_entry": string})
                self.device.should_recognize_news_search_string = False
            return result
