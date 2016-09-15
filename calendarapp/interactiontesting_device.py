from tdm.lib.device import EntityRecognizer, DeviceAction, DeviceWHQuery

from calendarapp.device import CalendarAppDevice


class CalendarAppDevice(CalendarAppDevice):

    class ShowCalendarAction(DeviceAction):
        PARAMETERS = ["selected_year.grammar_entry","selected_month.grammar_entry"]
        def perform(self,selected_year,selected_month):
            return True

    class InsertEventAction(DeviceAction):
        PARAMETERS = ["selected_event.grammar_entry","selected_month.grammar_entry","selected_day.grammar_entry","selected_year.grammar_entry"]
        def perform(self,selected_event,selected_month,selected_day,selected_year):
            return True

    class ShowEventAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry","selected_day.grammar_entry","selected_year.grammar_entry"]
        def perform(self,selected_month,selected_day,selected_year):
            return True