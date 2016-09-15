# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceWHQuery, DddDevice


class AlarmClockDevice(DddDevice):
    RESPONSES_TO_FEELINGS_ENGLISH = {
        "excited": "that's great",
        "joyful": "that's fantastic",

        "cheerful": "that's ok",
        "happy": "that's good",
        "glad": "good to hear this. Have a great day!",
        "good": "that's OK",
        "proud": "that's good",
        "content": "do you want me to suggest and event?",
        "comfortable": "good to hear this. Have a great day!",

        "calm": "I can help you. Do you want me to suggest an event?",
        "indifferent": "do you want me to suggest a game?",
        "quiet": "do you want listen to music?",
        "normal": "I can help you. Do you want me to suggest an event?",
        "fine": "do you want me to suggest a game?",
        "OK": "do you want listen to music?",
        "insecure": "I can help you. Do you want me to suggest an event?",
        "surprised": "do you want me to suggest a game?",
        "serious": "do you want listen to music?",
        "thoughtful": "I can help you. Do you want me to suggest an event?",


        "preoccupied": "do you want me to suggest an event that helps you feel better?",
        "worried": "do you want me to make a call?",
        "nervous": "do you want me to suggest an event that helps you feel better?",
        "confused": "do you want me to make a call?",
        "anxious": "do you want me to suggest an event that helps you feel better?",
        "afraid": "do you want me to make a call?",
        "scared": "do you want me to suggest an event that helps you feel better?",
        "tense": "do you want me to make a call?",
        "bad": "do you want me to suggest an event that helps you feel better?",
        "bored": "do you want me to make a call?",
        "disappointed": "do you want me to suggest an event that helps you feel better?",
        "tired": "do you want me to make a call?",
        "melancholic": "do you want me to suggest an event that helps you feel better?",
        "displeased": "do you want me to make a call?",

        "angry": "that sounds bad. Do you want me to make a call?",
        "irritated": "do you need help? Do you want me to make a call?",
        "annoyed": "that sounds bad. Do you want me to make a call?",
        "disgusted": "do you need help? Do you want me to make a call?",
        "upset": "that sounds bad. Do you want me to make a call?",
        "pain": "do you need help? Do you want me to make a call?",
        "cold": "that sounds bad. Do you want me to make a call?",
        "sick": "that sounds bad. Do you want me to make a call?",
        "sad": "do you need help? Do you want me to make a call?",
        "depressed": "that sounds bad. Do you want me to make a call?",
        "gloomy": "do you need help? Do you want me to make a call?",
        "frustrated": "that sounds bad. Do you want me to make a call?",
    }

    RESPONSES_TO_FEELINGS_FRENCH = {
        u"joyeux": u"c'est fantastique",
        u"gai": u"je suis heureux de l'entendre. Voulez-vous que je vous suggère un événement?",

        u"comblé": u"ça va bien",
        u"efficace": u"voulez-vous que je vous suggère un événement?",
        u"fier": u"ravi de l'entendre. Passez une belle journée! Voulez-vous que je vous suggère un événement?",
        u"ravi": u"ça va",


        u"calme": u"je peux vous aider",
        u"indifférent": u"voulez-vous que je vous suggère un jeu?",
        u"détendu": u"voulez-vous écouter de la musique?",
        u"normal": u"je peux vous aider",
        u"bien": u"voulez-vous que je vous suggère un jeu?",
        u"fragile": u"je peux vous aider",
        u"surpris": u"voulez-vous que je vous suggère un jeu?",
        u"sérieux": u"voulez-vous écouter de la musique?",
        u"pensif": u"je peux vous aider",

        u"préoccupé": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"inquiet": u"voulez-vous que je passe un appel?",
        u"nerveux": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"troublé": u"voulez-vous que je passe un appel?",
        u"anxieux": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"effrayé": u"voulez-vous que je passe un appel?",
        u"apeuré": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"tendu": u"voulez-vous que je passe un appel?",
        u"ennuyé": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"triste": u"voulez-vous que je passe un appel?",
        u"mal": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"déçu": u"voulez-vous que je passe un appel?",
        u"fatigué": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",
        u"mélancolique": u"voulez-vous que je passe un appel?",
        u"mécontent": u"voulez-vous que je vous suggère un événement qui vous aiderait à vous sentir mieux?",

        u"colère": u"ca sé presente mal. Voulez-vous que je passe un appel?",
        u"irrité": u"avez-vous besoin d'aide? Voulez-vous que je passe un appel?",
        u"contrarié": u"ca sé presente mal. Voulez-vous que je passe un appel?",
        u"dégoëfté": u"avez-vous besoin d'aide? Voulez-vous que je passe un appel?",
        u"fâché": u"ca sé presente mal. Voulez-vous que je passe un appel?",
        u"froid": u"avez-vous besoin d'aide? Voulez-vous que je passe un appel?",
        u"malade": u"ca sé presente mal. Voulez-vous que j e passe un appel?",
        u"déprimé": u"avez-vous besoin d'aide? Voulez-vous que je passe un appel?",
        u"maussade": u"ca sé presente mal. Voulez-vous que je passe un appel?",
        u"frustré": u"avez-vous besoin d'aide? Voulez-vous que je passe un appel?",
    }

    RESPONSES_TO_FEELINGS_DUTCH = {
        "enthousiast": "dat is geweldig",
        "blij": "dat is fantastisch",

        "vrolijk": "dat is oke",
        "fijn": "dat is goed",
        "goed": "wilt u dat ik een activiteit voorstel?",
        "trots": "goed om te horen. Nog een fijne dag toegewenst!",
        "tevreden": "dat is oke",
        "comfortabel": "dat is goed",

        "kalm": "ik kan u helpen. Wilt u dat ik een activiteit voorstel?",
        "onverschillig": "wilt u een suggestie voor een spelletje?",
        "rustig": "wilt u naar muziek luisteren",
        "normaal": "ik kan u helpen. Wilt u dat ik een activiteit voorstel?",
        "oke": "wilt u een suggestie voor een spelletje?",
        "onzeker": "ik kan u helpen. Wilt u dat ik een activiteit voorstel?",
        "ernstig": "wilt u een suggestie voor een spelletje?",
        "bedachtzaam": "ik kan u helpen. Wilt u dat ik een activiteit voorstel?",


        "zorgen": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "nerveus": "wilt u dat ik iemand bel?",
        "verward": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "verontrust": "wilt u dat ik iemand bel?",
        "angstig": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "bang": "wilt u dat ik iemand bel?",
        "gespannen": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "slecht": "wilt u dat ik iemand bel?",
        "verveeld": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "verdrietig": "wilt u dat ik iemand bel?",
        "teleurgesteld": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "moe": "wilt u dat ik iemand bel?",
        "melancholisch": "wilt u dat ik een activiteit voorstel waardoor u zich beter gaat voelen?",
        "misnoegd": "wilt u dat ik iemand bel?",

        "kwaad": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "geirriteerd": "heeft u hulp nodig? Wilt u dat ik iemand bel?",
        "geergerd": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "afkerig": "heeft u hulp nodig? Wilt u dat ik iemand bel?",
        "ontdaan": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "pijnlijk": "heeft u hulp nodig? Wilt u dat ik iemand bel?",
        "koud": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "misselijk": "heeft u hulp nodig? Wilt u dat ik iemand bel?",
        "droevig": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "depressief": "heeft u hulp nodig? Wilt u dat ik iemand bel?",
        "somber": "dat klinkt niet goed. Wilt u dat ik iemand bel?",
        "gefrustreerd": "heeft u hulp nodig? Wilt u dat ik iemand bel?",

    }

    class FeelingRecognizer(EntityRecognizer):
        def recognize(self, string, language):
            if language == "eng":
                return self._recognize_response(string, self.device.RESPONSES_TO_FEELINGS_ENGLISH)
            if language == "dut":
                return self._recognize_response(string, self.device.RESPONSES_TO_FEELINGS_DUTCH)
            if language == "fre":
                return self._recognize_response(string, self.device.RESPONSES_TO_FEELINGS_FRENCH)
            return []

        def _recognize_response(self, string, responses):
            result = []
            words = string.lower().split()
            for feeling in responses.keys():
                if feeling.lower() in words:
                    recognized_entity = {
                        "sort": "feeling",
                        "grammar_entry": feeling
                    }
                    result.append(recognized_entity)
            return result

    class response_to_feeling(DeviceWHQuery):
        PARAMETERS = ["selected_feeling.grammar_entry"]
        def perform(self, selected_feeling):
            responses = self._all_responses()
            response = responses.get(selected_feeling)
            entity = {
                "grammar_entry": response
            }
            return [entity]

        def _all_responses(self):
            responses = self.device.RESPONSES_TO_FEELINGS_ENGLISH.copy()
            responses.update(self.device.RESPONSES_TO_FEELINGS_FRENCH)
            responses.update(self.device.RESPONSES_TO_FEELINGS_DUTCH)
            return responses
