from kivy.app import App
# from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
from kivy.core.audio import SoundLoader


class PadApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.sounds = {
            'Kick': self.load_sound('source/reggaeton-style-kick-bassy-converted.wav'),
            'Snare': self.load_sound('source/boom-bap-snare-converted.wav'),
            'C-Hi-Hat': self.load_sound('source/hi-hat-one-shot-closed-thin_130bpm_D_major-converted.wav'),
            'O-Hi-Hat': self.load_sound('source/hi-hat-one-shot-open-decay_130bpm_D_major-converted.wav'),
            'Crush': self.load_sound('source/punchy-cymbal-crash-drum-hit-converted.wav'),
        }
    
    def load_sound(self, filepath):
        sound = SoundLoader.load(filepath)
        if sound:
            sound.load()
            return sound
        else:
            print(f"Error loading sound: {filepath}")
            return None
        
    def build(self):
        
        root_widget = BoxLayout(orientation='vertical')
        
        button_symbols = ('Empty', 'Empty', 'Snare', 'O-Hi-Hat', 'Crush',
                          'Kick', 'Kick', 'Snare', 'C-Hi-Hat','C-Hi-Hat')
        
        button_grid = (GridLayout(cols=5, size_hint_y=2))
        for symbol in button_symbols:
            button = Button(text=symbol)
            button.bind(on_press=self.play)
            button_grid.add_widget(button)

        root_widget.add_widget(button_grid)
        
        return root_widget
    def play_sound(self, symbol):
        if symbol in self.sounds and self.sounds[symbol]:
            sound = self.sounds[symbol]
            if symbol == "C-Hi-Hat" and self.sounds["O-Hi-Hat"].state == 'play':
                self.sounds["O-Hi-Hat"].stop()
            sound.play()
            print(self.sounds[symbol])
            
    def play(self, instance):
        self.play_sound(instance.text)
        
        
if __name__ == '__main__':
    PadApp().run()