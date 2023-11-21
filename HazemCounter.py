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
                self.letter_counts[ord(char) - ord('a')] += 1
                # so it takes the ascii value of the char and subtracts the ascii value of a
                # so if char is a, then ord(char) - ord('a') = 0
                # if char is b, then ord(char) - ord('a') = 1
                # so on... so it's basically just a way to get the index of the letter in the alphabet
                total_letters += 1

        self.letter_counts = [100 *count / total_letters for count in self.letter_counts]

    def get_frequencies(self):
        return self.letter_counts
