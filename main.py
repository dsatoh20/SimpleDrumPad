from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from pydub import AudioSegment
import simpleaudio as sa

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
        self.playbacks = {}
    
    def load_sound(self, filepath):
        return AudioSegment.from_wav(filepath)
        
    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        
        button_symbols = ('Empty', 'Empty', 'Snare', 'O-Hi-Hat', 'Crush',
                          'Kick', 'Kick', 'Snare', 'C-Hi-Hat', 'C-Hi-Hat')
        
        button_grid = GridLayout(cols=5, size_hint_y=2)
        for symbol in button_symbols:
            button = Button(text=symbol)
            button.bind(on_press=self.play)
            button_grid.add_widget(button)

        root_widget.add_widget(button_grid)
        
        return root_widget
    
    def play_sound(self, symbol):
        if symbol in self.sounds and self.sounds[symbol]:
            if symbol == "C-Hi-Hat" and 'O-Hi-Hat' in self.playbacks:
                self.playbacks['O-Hi-Hat'].stop()
            sound = self.sounds[symbol]
            playback = sa.play_buffer(
                sound.raw_data,
                num_channels=sound.channels,
                bytes_per_sample=sound.sample_width,
                sample_rate=sound.frame_rate
            )
            print(f"Playing sound: {symbol}")
    
    def play(self, instance):
        self.play_sound(instance.text)
        
if __name__ == '__main__':
    PadApp().run()
