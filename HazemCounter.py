### Name : Hazem Bin Ryaz Patel
### Admission Number : 2200550
### Class : DAAA/FT/2B/07

class LetterFrequency:
    def __init__(self, input_string=None):
        self.letter_counts = [0] * 26
        if input_string is not None:
            self.update(input_string)

    def update(self, input_string):
        total_letters = 0
        for char in input_string.lower():
            if 'a' <= char <= 'z':
                total_letters += 1
        self.letter_counts = [100 *count / total_letters for count in self.letter_counts]
        
    def get_frequencies(self):
        return self.letter_counts
