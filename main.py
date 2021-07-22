import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang.builder import Builder
import webbrowser
import json
import time
import kivy.uix.widget
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from kivy.clock import Clock
from functools import partial
# ------------------------------------------------------------------------------------------story storage system ----------------------------------------------------------------------------------------------------------------

class story_speicher():

    dictionary = {}
    schlüssel = {}
    dictlänge = 0
    data = None
    counter = 0
    neuepos = 0
    update = False
    change_screen_data = ""

class story_storage_system():

    def suche_schluessel(self, value):
        for schluessel, wert in story_speicher.schlüssel.items():
            if value == wert:
                return schluessel
        return None

    def aktualisieren(self):
        with open("./Story/storage.json", "w") as file:
            json.dump(story_speicher.dictionary, file, indent=4)

        with open("./Story/storage.json", "r") as myfile:
            story_speicher.data = myfile.read()
            story_speicher.dictionary = json.loads(story_speicher.data)
            story_speicher.dictlänge = len(story_speicher.dictionary)

        with open("./Story/key_names.json", "w") as file:
            json.dump(story_speicher.schlüssel, file, indent=4)

        with open("./Story/key_names.json", "r") as file:
            story_speicher.data = file.read()
            story_speicher.schlüssel = json.loads(story_speicher.data)

        story_speicher.update = True

    def add(self, eingabe1, eingabe2):
        story_speicher.dictlänge += 1
        story_speicher.dictionary[str(
            story_speicher.dictlänge)] = str(eingabe1)
        story_speicher.schlüssel[str(story_speicher.dictlänge)] = str(eingabe2)
        story_storage_system.aktualisieren(self)

    def loeschen(self, eingabe_zahl, eingabe_name):
        try:
            story_speicher.counter = int(
                story_storage_system.suche_schluessel(self, eingabe_name))
        except:
            story_speicher.counter = int(eingabe_zahl)

        try:
            if story_speicher.counter and story_speicher.dictlänge == 1 or story_speicher.counter == story_speicher.dictlänge:
                story_speicher.schlüssel.pop(str(story_speicher.counter))
                story_speicher.dictionary.pop(str(story_speicher.counter))
                story_storage_system.aktualisieren(self)
            elif story_speicher.counter <= story_speicher.dictlänge:
                while story_speicher.counter <= story_speicher.dictlänge:
                    story_speicher.dictlänge = len(story_speicher.dictionary)
                    story_speicher.neuepos = story_speicher.counter
                    story_speicher.counter += 1
                    story_speicher.schlüssel[str(story_speicher.neuepos)] = story_speicher.schlüssel.pop(
                        str(story_speicher.counter))
                    story_speicher.dictionary[str(story_speicher.neuepos)] = story_speicher.dictionary.pop(
                        str(story_speicher.counter))
                    story_storage_system.aktualisieren(self)
        except:
            story_speicher.dictlänge = len(story_speicher.dictionary)

# ------------------------------------------------------------------------------------------character storage system ----------------------------------------------------------------------------------------------------------------

class character_speicher():

    dictionary = {}
    schlüssel = {}
    dictlänge = 0
    data = None
    counter = 0
    neuepos = 0
    update = False
    change_screen_data = ""

class character_storage_system():

    def suche_schluessel(self, value):
        for schluessel, wert in character_speicher.schlüssel.items():
            if value == wert:
                return schluessel
        return None

    def aktualisieren(self):
        with open("./Charaktere/storage.json", "w") as file:
            json.dump(character_speicher.dictionary, file, indent=4)

        with open("./Charaktere/storage.json", "r") as myfile:
            character_speicher.data = myfile.read()
            character_speicher.dictionary = json.loads(character_speicher.data)
            character_speicher.dictlänge = len(character_speicher.dictionary)

        with open("./Charaktere/key_names.json", "w") as file:
            json.dump(character_speicher.schlüssel, file, indent=4)

        with open("./Charaktere/key_names.json", "r") as file:
            character_speicher.data = file.read()
            character_speicher.schlüssel = json.loads(character_speicher.data)

        character_speicher.update = True

    def add(self, eingabe1, eingabe2):
        character_speicher.dictlänge += 1
        character_speicher.dictionary[str(
            character_speicher.dictlänge)] = str(eingabe1)
        character_speicher.schlüssel[str(
            character_speicher.dictlänge)] = str(eingabe2)
        character_storage_system.aktualisieren(self)

    def loeschen(self, eingabe_zahl, eingabe_name):
        try:
            character_speicher.counter = int(
                character_storage_system.suche_schluessel(self, eingabe_name))
        except:
            character_speicher.counter = int(eingabe_zahl)

        try:
            if character_speicher.counter and character_speicher.dictlänge == 1 or character_speicher.counter == character_speicher.dictlänge:
                character_speicher.schlüssel.pop(
                    str(character_speicher.counter))
                character_speicher.dictionary.pop(
                    str(character_speicher.counter))
                character_storage_system.aktualisieren(self)
            elif character_speicher.counter <= character_speicher.dictlänge:
                while character_speicher.counter <= character_speicher.dictlänge:
                    character_speicher.dictlänge = len(
                        character_speicher.dictionary)
                    character_speicher.neuepos = character_speicher.counter
                    character_speicher.counter += 1
                    character_speicher.schlüssel[str(character_speicher.neuepos)] = character_speicher.schlüssel.pop(
                        str(character_speicher.counter))
                    character_speicher.dictionary[str(character_speicher.neuepos)] = character_speicher.dictionary.pop(
                        str(character_speicher.counter))
                    character_storage_system.aktualisieren(self)
        except:
            character_speicher.dictlänge = len(character_speicher.dictionary)

# -------------------------------------------------------------------------story system insert ----------------------------------------------------------------------------------------------
with open("./Story/storage.json", "r") as myfile:
    story_speicher.data = myfile.read()
    story_speicher.dictionary = json.loads(story_speicher.data)
    if len(story_speicher.dictionary) > 0:
        story_speicher.dictlänge = len(story_speicher.dictionary)
    elif len(story_speicher.dictionary) == 0:
        story_speicher.dictlänge = 0

with open("./Story/key_names.json", "r") as keyfile:
    story_speicher.data = keyfile.read()
    story_speicher.schlüssel = json.loads(story_speicher.data)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------character system insert ----------------------------------------------------------------------------------------------
with open("./Charaktere/storage.json", "r") as myfile:
    character_speicher.data = myfile.read()
    character_speicher.dictionary = json.loads(character_speicher.data)
    if len(character_speicher.dictionary) > 0:
        character_speicher.dictlänge = len(character_speicher.dictionary)
    elif len(character_speicher.dictionary) == 0:
        character_speicher.dictlänge = 0

with open("./Charaktere/key_names.json", "r") as keyfile:
    character_speicher.data = keyfile.read()
    character_speicher.schlüssel = json.loads(character_speicher.data)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Story_RV(RecycleView):
    def __init__(self, **kwargs):
        super(Story_RV, self).__init__(**kwargs)
        Clock.schedule_interval(self.prüfen, 1.2)
        if story_speicher.dictlänge == 0:
            self.data = []
        elif story_speicher.dictlänge > 0:
            self.data = [{'text': str(x) + ": " + str(story_speicher.schlüssel[str(x)]), 'on_release': partial(
                self.oeffnen, x)} for x in range(1, story_speicher.dictlänge+1)]

    def prüfen(self, no_need):
        if story_speicher.update == True:
            self.erneuern()
            story_speicher.update = False

    def erneuern(self):
        self.data = [{'text': str(x) + ": " + str(story_speicher.schlüssel[str(x)]), 'on_release': partial(self.oeffnen, x)} for x in range(1, story_speicher.dictlänge+1)]

    def oeffnen(self, x):
        try:
            story_speicher.change_screen_data = "{0}".format(x)
        except:
            story_speicher.change_screen_data = ""

class Character_RV(RecycleView):
    def __init__(self, **kwargs):
        super(Character_RV, self).__init__(**kwargs)
        Clock.schedule_interval(self.prüfen, 1.2)
        if character_speicher.dictlänge == 0:
            self.data = []
        elif character_speicher.dictlänge > 0:
            self.data = [{'text': str(x) + ": " + str(character_speicher.schlüssel[str(x)]), 'on_release': partial(
                self.oeffnen, x)} for x in range(1, character_speicher.dictlänge+1)]

    def prüfen(self, no_need):
        if character_speicher.update == True:
            self.erneuern()
            character_speicher.update = False

    def erneuern(self):
        self.data = [{'text': str(x) + ": " + str(character_speicher.schlüssel[str(x)]),
                      'on_release': partial(self.oeffnen, x)} for x in range(1, character_speicher.dictlänge+1)]

    def oeffnen(self, x):
        try:
            character_speicher.change_screen_data = "{0}".format(x)
        except:
            character_speicher.change_screen_data = ""


class Startscreen(Screen):

    def change_to_mainscreen(self, *args):
        self.manager.current = "mainscreen"
        self.ids.starten.background_color = (1, 1, 1, 0.05)

    def end_screen(self, *args):
        Pen_and_Paper().stop()

    def starten(self):
        # Erste Animation
        animate = Animation(background_color=(1, 1, 1, 1), duration=0.5)
        # Zweite Animation
        animate += Animation(background_color=(0, 0, 0, 0), duration=0.5)
        # Binden von Methode
        animate.bind(on_complete=self.change_to_mainscreen)
        # Starte Animation
        animate.start(self.ids.starten)

    def beenden(self):
        # Erste Animation
        animate = Animation(background_color=(1, 1, 1, 1), duration=0.5)
        # Zweite Animation
        animate += Animation(background_color=(0, 0, 0, 0), duration=0.5)
        # Binden von Methode
        animate.bind(on_complete=self.end_screen)
        # Starte Animation
        animate.start(self.ids.beenden)


class Mainscreen(Screen):
    pass

class Story_Mainscreen(Screen):
    pass

class Story_Addscreen(Screen):

    def add(self):
        if self.ids.story_inhalt.text != "":
            try:
                story_storage_system.add(
                    self, self.ids.story_inhalt.text, self.ids.titel_story.text)
                self.ids.titel_story.text = ""
                self.ids.story_inhalt.text = ""
            except:
                self.ids.titel_story.text = "Fehler"
                self.ids.story_inhalt.text = "Fehler"
                time.sleep(1.5)
                self.ids.titel_story.text = ""
                self.ids.story_inhalt.text = ""
            
class Story_Show_Change_Screen(Screen):
    
    def data_loading(self):
        if story_speicher.change_screen_data != "":
            try:
                self.ids.story_inhalt.text = story_speicher.dictionary[story_speicher.change_screen_data]
                self.ids.story_titel_show.text = story_speicher.schlüssel[story_speicher.change_screen_data]
            except: 
                self.ids.story_inhalt.text = "Fehler"
                self.ids.story_titel_show.text = "Fehler"
                time.sleep(1)
                self.manager.current = "storyMainscreen"
                
    
    def back(self):
        self.ids.story_titel_show.text  = ""
        self.ids.story_inhalt.text = ""
        story_speicher.change_screen_data = ""
        
    def save_change(self):
        if self.ids.story_inhalt.text != "":
            try:
                story_speicher.dictionary[story_speicher.change_screen_data] = self.ids.story_inhalt.text
                story_speicher.schlüssel[story_speicher.change_screen_data] = self.ids.story_titel_show.text
                story_storage_system.aktualisieren(self)
                story_speicher.change_screen_data = ""
                self.ids.story_titel_show.text  = ""
                self.ids.story_inhalt.text = ""
            except:
                story_speicher.change_screen_data = ""
                self.manager.current = "storyMainscreen"
        
    def delete(self):
        try:
            story_storage_system.loeschen(self,story_speicher.change_screen_data, story_speicher.schlüssel[story_speicher.change_screen_data])
            self.ids.story_titel_show.text  = ""
            self.ids.story_inhalt.text = ""
            story_speicher.change_screen_data = ""
        except:
            self.ids.story_titel_show.text  = ""
            self.ids.story_inhalt.text = ""
            story_speicher.change_screen_data = ""

class Character_Mainscreen(Screen):
    pass

class Character_Addscreen(Screen):

    def add(self):
        if self.ids.character_inhalt.text != "":
            try:
                character_storage_system.add(
                    self, self.ids.character_inhalt.text, self.ids.character_titel.text)
                self.ids.character_titel.text = ""
                self.ids.character_inhalt.text = ""
            except:
                self.ids.character_titel.text = "Fehler"
                self.ids.character_inhalt.text = "Fehler"
                time.sleep(1.5)
                self.ids.character_titel.text = ""
                self.ids.character_inhalt.text = ""
        else:
            self.ids.character_inhalt.text = ""
            self.ids.character_titel.text = ""
            
class Character_Show_Change_Screen(Screen):
    
    def data_loading(self):
        if character_speicher.change_screen_data != "":
            try:
                self.ids.character_inhalt.text = character_speicher.dictionary[character_speicher.change_screen_data]
                self.ids.character_titel_show.text = character_speicher.schlüssel[character_speicher.change_screen_data]
            except: 
                self.ids.character_inhalt.text = "Fehler"
                self.ids.character_titel_show.text = "Fehler"
                time.sleep(1)
                self.manager.current = "characterMainscreen"
                
    
    def back(self):
        self.ids.character_titel_show.text  = ""
        self.ids.character_inhalt.text = ""
        character_speicher.change_screen_data = ""
        
    def save_change(self):
        if self.ids.character_inhalt.text != "":
            try:
                character_speicher.dictionary[character_speicher.change_screen_data] = self.ids.character_inhalt.text
                character_speicher.schlüssel[character_speicher.change_screen_data] = self.ids.character_titel_show.text
                character_storage_system.aktualisieren(self)
                character_speicher.change_screen_data = ""
                self.ids.character_titel_show.text  = ""
                self.ids.character_inhalt.text = ""
            except:
                character_speicher.change_screen_data = ""
                self.manager.current = "characterMainscreen"
        
    def delete(self):
        try:
            character_storage_system.loeschen(self,character_speicher.change_screen_data, character_speicher.schlüssel[character_speicher.change_screen_data])
            self.ids.character_titel_show.text  = ""
            self.ids.character_inhalt.text = ""
            character_speicher.change_screen_data = ""
        except:
            self.ids.character_titel_show.text  = ""
            self.ids.character_inhalt.text = ""
            character_speicher.change_screen_data = ""
            
class Wmanager(ScreenManager):
    pass

class Pen_and_Paper(App):
    def build(self):
        with open("./guicode.kv", encoding="utf8") as file:
            guidesign = Builder.load_string(file.read())
            return guidesign


if __name__ == "__main__":

   Pen_and_Paper().run()