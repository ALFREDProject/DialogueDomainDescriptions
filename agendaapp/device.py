# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction, DddDevice, EntityRecognizer
from tdm.device_handler import send_to_frontend_device


class AgendaAppDevice(DddDevice):

    def __init__(self):
        self.recogAgenda = 0

    MINUTES = {
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
        "15": "15",
        "20": "20",
        "25": "25",
        "30": "30",
        "35": "35",
        "40": "40",
        "45": "45",
        "50": "50",
        "55": "55",
        "60": "60"
    }

    AGENDAS = {
        "sleep": "sleep"
    }

    class RecogAgenda(DeviceAction):

        def perform(self):
            self.device.recogAgenda = 1
            return True

    class SetAgendaAction(DeviceAction):
        PARAMETERS = ["selected_alert_time.grammar_entry",
                      "selected_agenda_mode.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_alert_time, selected_agenda_mode):
            pass

    class AgendaRecognizer(EntityRecognizer):

        def recognize_entity(self, string):
            result = []
            words = string.lower().split()
            if self.device.recogAgenda < 1:
                for alert_time in self.device.MINUTES.keys():
                    if alert_time.lower() in words:
                        recognized_entity = {
                            "sort": "alert_time",
                            "grammar_entry": alert_time
                        }
                        result.append(recognized_entity)
            else:
                for agenda_mode in self.device.AGENDAS.keys():
                    if agenda_mode.lower() in words:
                        recognized_entity = {
                            "sort": "agenda_mode",
                            "grammar_entry": agenda_mode
                        }
                        result.append(recognized_entity)
                if not result:
                    self.device.AGENDAS[string] = string
                    recognized_entity = {
                        "sort": "agenda_mode",
                        "grammar_entry": string
                    }
                    result.append(recognized_entity)
                    self.device.recogAgenda -= 1
            return result
