from tdm.lib.device import DeviceAction

from meetingapp.device import MeetingAppDevice


class MeetingAppDevice(MeetingAppDevice):

    class CreateMeetingAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject.grammar_entry", "selected_location.grammar_entry"]

        def perform(self, selected_month, selected_day, selected_year, selected_subject, selected_location):
            return True

    class CreateAppointmentAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_appointment.grammar_entry", "selected_location_appointment.grammar_entry"]

        def perform(self, selected_month, selected_day, selected_year, selected_subject_appointment, selected_location_appointment):
            return True

    class CreateConferenceAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_conference.grammar_entry", "selected_location_conference.grammar_entry"]

        def perform(self, selected_month, selected_day, selected_year, selected_subject_conference, selected_location_conference):
            return True

    class CreateInvitationAction(DeviceAction):
        PARAMETERS = ["selected_month.grammar_entry", "selected_day.grammar_entry",
                      "selected_year.grammar_entry", "selected_subject_invitation.grammar_entry", "selected_location_invitation.grammar_entry"]

        def perform(self, selected_month, selected_day, selected_year, selected_subject_invitation, selected_location_invitation):
            return True
