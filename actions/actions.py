import sqlite3
from pathlib import Path
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCheckKnowledge(Action):
    knowledge = Path("data/obat.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_obat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Obat':
                Obat = x['value'].lower()
                if Obat in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, obat {Obat} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf obat {Obat} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeMata(Action):
    knowledge = Path("data/mata.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_perawatan_mata"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Perawatan_Mata':
                Perawatan_Mata = x['value'].lower()
                if Perawatan_Mata in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, perawatan mata {Perawatan_Mata} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf perawatan mata {Perawatan_Mata} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgePenyakitDalam(Action):
    knowledge = Path("data/penyakit_dalam.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_penyakit_dalam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Penyakit_Dalam':
                Penyakit_Dalam = x['value'].lower()
                if Penyakit_Dalam in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan penyakit dalam {Penyakit_Dalam} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan penyakit dalam {Penyakit_Dalam} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeGigi(Action):
    knowledge = Path("data/Gigi.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_gigi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Gigi':
                Gigi = x['value'].lower()
                if Gigi in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan untuk {Gigi} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan {Gigi} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeJiwa(Action):
    knowledge = Path("data/jiwa.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_jiwa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Jiwa':
                Jiwa = x['value'].lower()
                if Jiwa in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan untuk {Jiwa} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan {Jiwa} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeTHT(Action):
    knowledge = Path("data/THT.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_THT"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'THT':
                THT = x['value'].lower()
                if THT in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan untuk {THT} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan {THT} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeAnak(Action):
    knowledge = Path("data/anak.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_anak"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Anak':
                Anak = x['value'].lower()
                if Anak in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan untuk {Anak} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan {Anak} tidak ada, coba cek lagi pengejaan yang benar.")
        return []


class ActionCheckKnowledgeFisioterapi(Action):
    knowledge = Path("data/fisioterapi.txt").read_text().lower().split("\n")

    def name(self) -> Text:
        return "action_check_fisioterapi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for x in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if x['entity'] == 'Fisioterapi':
                Fisioterapi = x['value'].lower()
                if Fisioterapi in self.knowledge:
                    dispatcher.utter_message(
                        text=f"Ya, penanganan untuk {Fisioterapi} ini ada.")
                else:
                    dispatcher.utter_message(
                        text=f"Maaf penanganan {Fisioterapi} tidak ada, coba cek lagi pengejaan yang benar.")
        return []
