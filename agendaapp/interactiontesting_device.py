from tdm.lib.device import DeviceAction, EntityRecognizer

from agendaapp.device import AgendaAppDevice


class AgendaAppDevice(AgendaAppDevice):

    class SetAgendaAction(DeviceAction):
        PARAMETERS = ["selected_alert_time.grammar_entry",
                      "selected_agenda_mode.grammar_entry"]

        def perform(self, selected_alert_time, selected_agenda_mode):
            return True
