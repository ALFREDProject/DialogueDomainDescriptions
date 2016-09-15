# -*- coding: utf-8 -*-

from tdm.lib.device import DddDevice, DeviceAction, EntityRecognizer
from tdm.device_handler import send_to_frontend_device


class GameManagerDevice(DddDevice):

    GAMES = [
        "spine game",
        "balance bike",
        "dance game",
        "city explorer",
        "puzzle arena"
    ]

    class StartGame(DeviceAction):
        PARAMETERS = ["game_to_start.grammar_entry"]

        @send_to_frontend_device
        def perform(self, game_to_start):
            return True

    class StopGame(DeviceAction):
        
        @send_to_frontend_device
        def perform(self):
            return True

    class ResumeGame(DeviceAction):

        @send_to_frontend_device
        def perform(self):
            return True

    class PauseGame(DeviceAction):

        @send_to_frontend_device
        def perform(self):
            return True

    class GameRecognizer(EntityRecognizer):

        def recognize_entity(self, string):
            result = []
            for game in self.device.GAMES:
                if game.lower() in string:
                    recognized_entity = {
                        "sort": "game",
                        "grammar_entry": game
                    }
                    result.append(recognized_entity)
            return result
