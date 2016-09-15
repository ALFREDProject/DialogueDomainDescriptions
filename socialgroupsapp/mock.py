from tdm.lib.device import DeviceAction

from socialgroupsapp.device import SocialGroupsAppDevice


class SocialGroupsAppDevice(SocialGroupsAppDevice):

    class CreateSocialGroupAction(DeviceAction):
        PARAMETERS = ["selected_groupname.grammar_entry",
                      "selected_groupdescription.grammar_entry"]

        def perform(self, selected_groupname, selected_groupdescription):
            return True

    class CreateDiscussionAction(DeviceAction):
        PARAMETERS = ["selected_discussionname.grammar_entry",
                      "selected_discussiondescription.grammar_entry"]

        def perform(self, selected_discussionname, selected_discussiondescription):
            return True
