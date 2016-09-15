# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice, DeviceWHQuery

from tdm.device_handler import send_to_frontend_device


class MeetingAppDevice(DddDevice):

    def __init__(self):
        self.should_recognize_subject = False
        self.should_recognize_location = False

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
        "31": "31"
    }

    YEARS = {
        "2016": "2016",
        "2017": "2017",
        "2018": "2018",
        "2019": "2019",
        "2020": "2020"
    }

    class CreateMeetingAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject.grammar_entry", "selected_location.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_month, selected_day, selected_year, selected_subject, selected_location):
            pass

    class CreateAppointmentAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_appointment.grammar_entry", "selected_location_appointment.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_month, selected_day, selected_year, selected_subject_appointment, selected_location_appointment):
            pass

    class CreateConferenceAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_conference.grammar_entry", "selected_location_conference.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_month, selected_day, selected_year, selected_subject_conference, selected_location_conference):
            pass

    class CreateInvitationAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_invitation.grammar_entry", "selected_location_invitation.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_month, selected_day, selected_year, selected_subject_invitation, selected_location_invitation):
            pass

    class OnShouldRecognizeSubject(DeviceAction):

        def perform(self):
            self.device.should_recognize_subject = True
            self.device.should_recognize_location = False
            return True

    class OnShouldRecognizeLocation(DeviceAction):

        def perform(self):
            self.device.should_recognize_subject = False
            self.device.should_recognize_location = True
            return True

    class OnShouldRecognizeNothing(DeviceAction):

        def perform(self):
            self.device.should_recognize_subject = False
            self.device.should_recognize_location = False
            return True

    class MeetingRecognizer(EntityRecognizer):

        def recognize(self, string, language):
            result = []
            words = string.lower().split()
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
            if self.device.should_recognize_subject:
                recognized_entity = {
                    "sort": "subject",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
            if self.device.should_recognize_location:
                recognized_entity = {
                    "sort": "location",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
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
