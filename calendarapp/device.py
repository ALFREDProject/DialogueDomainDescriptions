# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice, DeviceWHQuery

from tdm.device_handler import send_to_frontend_device


class CalendarAppDevice(DddDevice):

    def __init__(self):
        self.recogEvent = 0

    MONTHS_ENGLISH = {
        "january": "january",
        "february": "february",
        "march": "march",
        "april": "april",
        "may": "may",
        "june": "june",
        "july": "july",
        "august": "august",
        "september": "september",
        "october": "october",
        "november": "november",
        "december": "december",
    }

    MONTHS_DUTCH = {
        "januari": "januari",
        "februari": "februari",
        "maart": "maart",
        "april": "april",
        "mei": "mei",
        "juni": "juni",
        "juli": "juli",
        "augustus": "augustus",
        "september": "september",
        "oktober": "oktober",
        "november": "november",
        "december": "december",
    }

    MONTHS_FRENCH = {
        "janvier": "janvier",
        u"février": u"février",
        "mars":    "mars",
        "avril": "avril",
        "mai": "mai",
        "juin":    "juin",
        "juillet": "juillet",
        u"août":    u"août",
        "septembre": "septembre",
        "octobre": "octobre",
        "novembre": "novembre",
        u"décembre": u"décembre"
    }

    DAYS = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "10": "10",
        "11": "11",
        "12": "12",
        "13": "13",
        "14": "14",
        "15": "15",
        "16": "16",
        "17": "17",
        "18": "18",
        "19": "19",
        "20": "20",
        "21": "21",
        "22": "22",
        "23": "23",
        "24": "24",
        "25": "25",
        "26": "26",
        "27": "27",
        "28": "28",
        "29": "29",
        "30": "30",
        "31": "31",
    }

    YEARS = {
        "2010": "2010",
        "2011": "2011",
        "2012": "2012",
        "2013": "2013",
        "2014": "2014",
        "2015": "2015",
        "2016": "2016",
        "2017": "2017",
        "2018": "2018",
        "2019": "2019",
        "2020": "2020"
    }

    EVENTS = {
        "shopping": "shopping",
    }

    class ShowCalendarAction(DeviceAction):
        PARAMETERS = ["selected_year.grammar_entry",
                      "selected_month.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_year, selected_month):
            pass

    class InsertEventAction(DeviceAction):
        PARAMETERS = ["selected_event.grammar_entry", "selected_month.grammar_entry",
                      "selected_day.grammar_entry", "selected_year.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_event, selected_month, selected_day, selected_year):
            pass

    class ShowEventAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry",
                      "selected_day.grammar_entry", "selected_year.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_month, selected_day, selected_year):
            pass

    class RecogEvent(DeviceAction):

        def perform(self):
            self.device.recogEvent = 1
            return True

    class CalendarRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            result = []
            words = string.lower().split()
            if self.device.recogEvent < 1:
                for year in self.device.YEARS.keys():
                    if year.lower() in words:
                        recognized_entity = {
                            "sort": "year",
                            "grammar_entry": year
                        }
                        result.append(recognized_entity)
                result.extend(self._recognize_months_for_language(words, language))
                for day in self.device.DAYS.keys():
                    if day.lower() in words:
                        recognized_entity = {
                            "sort": "day",
                            "grammar_entry": day
                        }
                        result.append(recognized_entity)
            else:
                for event in self.device.EVENTS.keys():
                    if event.lower() in words:
                        recognized_entity = {
                            "sort": "event",
                            "grammar_entry": event
                        }
                        result.append(recognized_entity)
                if not result:
                    self.device.EVENTS[string] = string
                    recognized_entity = {
                        "sort": "event",
                        "grammar_entry": string
                    }
                    result.append(recognized_entity)
                    self.device.recogEvent -= 1
            return result

        def _recognize_months_for_language(self, words, language):
            if language == "eng":
                months = self._recognize_months(words, self.device.MONTHS_ENGLISH)
                return months
            if language == "dut":
                months = self._recognize_months(words, self.device.MONTHS_DUTCH)
                return months
            if language == "fre":
                months = self._recognize_months(words, self.device.MONTHS_FRENCH)
                return months
            return []

        def _recognize_months(self, words, months):
            result = []
            for month in months.keys():
                if month.lower() in words:
                    recognized_entity = {
                        "sort": "month",
                        "grammar_entry": month
                    }
                    result.append(recognized_entity)
            return result
