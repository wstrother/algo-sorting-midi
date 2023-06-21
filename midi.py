"""
This file will provide a method that takes 
    - a list of numbers (correpsonding to the index of array accesses generated by a sorting algorithm)
    - general parameters for the style of output (rhythmic guidelines, note mapping)

and generate a MIDI file as output.
"""

from midiutil import MIDIFile


class NoteGenerator:
    def __init__(self, *params) -> None:
        self.current_time = 0
        self.midi = MIDIFile(1)
        self.midi.addTempo(0, 0, 120)

    def get_pitch(self, value, step_number) -> float:
        return value
    
    def get_duration(self, value, step_number) -> float:
        return 1
    
    def get_volume(self, value, step_number) -> float:
        return 50

    def get_delta_t(self, value, step_number) -> float:
        return 1

    def process_step(self, value, step_number):
        # set defaults
        pitch, duration, volume = 0, 0, 0
        
        # if there is no index value in the step, consider it a rest
        rest = value is None
        
        # increment current time
        self.current_time += self.get_delta_t(value, step_number) or 1
        
        if not rest:
            # apply transformations
            pitch = self.get_pitch(value, step_number) or pitch
            duration = self.get_duration(value, step_number) or duration
            volume = self.get_volume(value, step_number) or volume
            
            # write midi note
            self.midi.addNote(0, 0, pitch, self.current_time, duration, volume)
    
    def write_file(self, file_name):
        with open(file_name, "wb") as output_file:
            self.midi.writeFile(output_file)
    
    @staticmethod
    def create_midi(values, file_name, *params):
        generator = NoteGenerator(*params)        
        
        for (step_number, value) in enumerate(values):
            generator.process_step(value, step_number)
        
        generator.write_file(file_name)

