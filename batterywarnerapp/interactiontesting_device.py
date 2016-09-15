from tdm.lib.device import EntityRecognizer, DeviceAction, Validity, DeviceWHQuery

from batterywarnerapp.device import BatteryWarnerAppDevice


class BatteryWarnerAppDevice(BatteryWarnerAppDevice):

    class selected_battery_status(DeviceWHQuery):
        def perform(self):
            status_entity = {
                "grammar_entry": "50",
            }
            return [status_entity]
