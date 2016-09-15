# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice, DeviceWHQuery

from tdm.device_handler import send_to_frontend_device


class SocialGroupsAppDevice(DddDevice):

    def __init__(self):
        self.should_recognize_name = False
        self.should_recognize_description = False
        self.should_recognize_name_disc = False
        self.should_recognize_description_disc = False

    class CreateSocialGroupAction(DeviceAction):
        PARAMETERS = ["selected_groupname.grammar_entry",
                      "selected_groupdescription.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_groupname, selected_groupdescription):
            return True

    class CreateDiscussionAction(DeviceAction):
        PARAMETERS = ["selected_discussionname.grammar_entry",
                      "selected_discussiondescription.grammar_entry"]

        @send_to_frontend_device
        def perform(self, selected_discussionname, selected_discussiondescription):
            return True

    class OnInitializedPlan(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = True
            self.device.should_recognize_name_disc = False
            self.device.should_recognize_description = False
            self.device.should_recognize_description_disc = False
            return True

    class OnInitializedPlanDisc(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_name_disc = True
            self.device.should_recognize_description = False
            self.device.should_recognize_description_disc = False
            return True

    class OnRecognizedName(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_description = True
            self.device.should_recognize_name_disc = False
            self.device.should_recognize_description_disc = False
            return True

    class OnRecognizedNameDisc(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_description = False
            self.device.should_recognize_name_disc = False
            self.device.should_recognize_description_disc = True
            return True

    class OnRecognizedDescription(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_name_disc = False
            self.device.should_recognize_description = False
            self.device.should_recognize_description_disc = False
            return True

    class OnRecognizedDescriptionDisc(DeviceAction):

        def perform(self):
            self.device.should_recognize_name = False
            self.device.should_recognize_name_disc = False
            self.device.should_recognize_description = False
            self.device.should_recognize_description_disc = False
            return True

    class SocialgroupsRecognizer(EntityRecognizer):

        def recognize_entity(self, string):
            result = []
            words = string.lower().split()
            if self.device.should_recognize_name:
                recognized_entity = {
                    "sort": "groupname",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
            if self.device.should_recognize_name_disc:
                recognized_entity = {
                    "sort": "groupname",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
            if self.device.should_recognize_description:
                recognized_entity = {
                    "sort": "groupdescription",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
            if self.device.should_recognize_description_disc:
                recognized_entity = {
                    "sort": "groupdescription",
                    "grammar_entry": string
                }
                result.append(recognized_entity)
            return result
