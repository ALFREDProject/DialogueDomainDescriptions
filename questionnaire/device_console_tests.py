# -*- coding: utf-8 -*-

from tdm.lib.device import DeviceAction

from questionnaire.device import QuestionnaireDevice


class QuestionnaireDevice(QuestionnaireDevice):

    class GetInfo(DeviceAction):
        PARAMETERS = ["selected_info_type"]

        def perform(self, selected_info_type):
            return True
