import re
### Name : Hazem Bin Ryaz Patel
### Admission Number : 2200550
### Class : DAAA/FT/2B/07

class View:
    def __init__(self):
        self.selection = None

    def display_menu(self):
        while True:
            print("""Please select your choice: (1,2,3,4,5,6,7,8):
                            1. Encrypt/Decrypt Message
                            2. Encrypt/Decrypt File
                            3. Analyze letter frequency distribution
                            4. Infer Caesar cipher key from file
                            5. Analyze and sort encrypted files
                            6. Batch Encrypt/Decrypt Files
                            7. Compare frequency distribution with English language # on hold, not sure if we need this/makes sense
                            8. Exit program""")
            self.selection = input("Enter choice: ")
            if self.selection in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                return self.selection
            else:
                print("Invalid choice. Please enter a valid option (1-8).\n")
    
    def display_encryption(self, message, encrypted):
        print("Original message: ", message)
        print("Encrypted message: ", encrypted)
    
    def display_key(self, key):
        print("The Inferred key is: ", key)
    
    def display_analyze_frequency(self, frequency):

        index_frequency_pairs = [(i, freq) for i, freq in enumerate(frequency)]
        top5 = sorted(index_frequency_pairs, key=lambda x:x[1], reverse=True)[:5]
        
        for i in range(26, 0, -1):
            line = ''.join('*  ' if freq > (100 * i / 26) else '   ' for freq in frequency)
            # Add the frequency percentage for the current character
            
            if i > 0:
                line += f'  | {chr(91-i)}- {frequency[26 - i]}%'
            # Add the top 5 frequencies
            if i == 17:
                line += '   TOP 5 FREQ'
            if i == 16: 
                line += '   ----------'

            if 10 < i < 16:
                index, freq = top5[15 - i]
                if freq >= 10:
                    line += f'   | {chr(65 + index)}-{freq}%' # double digits
                else:
                    line += f'   | {chr(65 + index)}- {freq}%' # single digits
                

            print(line)
        print("________________________________________________________________________________|")
        print("  ".join(chr(65 + i) for i in range(26)))
    
    def display_frequency(self, frequency_diff, percentage_similarity):

        print("The difference between the text's frequency distribution and the English language frequency distribution is:", frequency_diff)
        print("The text's frequency distribution is", percentage_similarity, "% similar to the English language frequency distribution.")