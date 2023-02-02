from kivy.app import App

# Grafiske komponenter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Properties til interaktion mellem python og kv
from kivy.properties import StringProperty, NumericProperty

# Kivys interne clock til timing og framerate .
from kivy.clock import Clock

# Python standard biblioteker
import math

class TimerLayout(BoxLayout):
    # Tekst paa knappen. Bundet via .kv. Bliver aendret i update.
    timerText = StringProperty('Set time')
    buttonText = StringProperty('Start timer')
    running = False        # Nedtaellingen koerer hvis sand
    expired = False
    startTime = 5 #int(input('Hvor mange sekunder skal der være? '))          # Antal sekunder timeren starter på
    timeLeft = startTime   # Antal sekunder tilbage i nedtaellingen

    # Skifter running til modsatte boolske vaerdi
    def toggle(self):
        if self.expired and not self.running:
            self.timeLeft = self.startTime
            self.expired = False
        else:
            self.running = not self.running

    # Taeller ned hvis running. Opdaterer buttonText ved hvert kald
    def update(self, dt):

        self.ids.yearpicker.update()
        self.ids.monthpicker.update()
        self.ids.daypicker.update()
        self.ids.hourpicker.update()
        self.ids.minutepicker.update()

        """year = int(self.ids.yearpicker.value)
        month = int(input('Vælg måned '))
        day = int(input('vælg dag '))
        hour = int(input('Vælg time '))
        minute = int(input('Vælg minut '))

        targetDate = datetime(year, month, day, hour, minute)

        today = datetime.today()
        """
        if self.running:
            self.timeLeft = self.timeLeft - dt
        if self.timeLeft <= 0 and self.running:
            self.toggle()
            self.expired = True

        self.timerText = str(int(math.ceil(self.timeLeft)))

        if self.running and not self.expired:
            self.buttonText = 'Stop'
        elif not self.running and not self.expired:
            self.buttonText = 'Start'
        else:
            self.buttonText = 'Reset'



class Picker(BoxLayout):
    maxValue = NumericProperty()
    minValue = NumericProperty()
    value = NumericProperty()
    displayText = StringProperty()


    def update(self):
        self.displayText = str(self.value)


    def add(self):
        if self.value < self.maxValue:
            self.value+=1

    def sub(self):
        if self.value > self.minValue:
            self.value-=1

class BasicTimerApp(App):

    def build(self):
        # Initialiser knappen
        layout = TimerLayout()

        # Bed Kivy om at kalde update() 30 gange pr. sekund
        Clock.schedule_interval(layout.update, 1.0/30.0)

        return layout

if __name__ in ('__main__', '__android__'):
    BasicTimerApp().run()
