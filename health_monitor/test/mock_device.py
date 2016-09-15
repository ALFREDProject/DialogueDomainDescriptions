from tdm.lib.device import DeviceWHQuery

from health_monitor.device import HealthMonitorDevice

class HealthMonitorDevice(HealthMonitorDevice):

    class value_of_vital_parameter(DeviceWHQuery):
        PARAMETERS = ["selected_vital_parameter.grammar_entry"]
        def perform(self, selected_vital_parameter):
            entity = {
                "grammar_entry": "100"
            }
            return [entity]
