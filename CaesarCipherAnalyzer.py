# Name: Hazem Bin Ryaz Patel
# Admission Number: 2200550
# Class: DAAA/FT/2B/07

# model.py


import re
import math
from HazemCounter import LetterFrequency
import os


class CaesarCipherAnalyzer:
    def __init__(self):
        self.selection = None

    def check_input(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp

    def get_frequency(self, text):
        return LetterFrequency(text).get_frequencies()

    def infer_caesar_cipher_key(self, text, reference_frequencies):
        lowest_acc = math.inf
        closest_acc = 0
        
        for key in range(26):
            frequency_diff = [
                abs(float(a - b))
                for a, b in zip(
                    reference_frequencies,
                    LetterFrequency(self.encrypt(text, -key)).get_frequencies()
                )
            ]
            current_acc =  sum(frequency_diff)
            if current_acc < lowest_acc:
                lowest_acc = current_acc
                closest_acc = key
        return closest_acc

    def encrypt(self, text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    shifted_char = chr(
                        ((ord(char) - ord("a") + shift_amount) % 26) + ord("a")
                    )
                else:
                    shifted_char = chr(
                        ((ord(char) - ord("A") + shift_amount) % 26) + ord("A")
                    )
                encrypted_text += shifted_char
            else:
                encrypted_text += char
        return encrypted_text

    def openfile(self, file_path, input_message):
        while True: 
            try:
                with open(file_path, "r") as file:
                    file_contents = file.read()
                    
                    break
            except FileNotFoundError:
                print(f"The file '{file_path}' was not found.")
                print("")
                file_path = self.check_input(
                "^.+\.txt$",
                (input_message),
                "Invalid input, please enter a valid file path",
            )
            except Exception as e:
                print(f"An error occurred: {e}")
        return file_contents
    
    def writefile(self, file_path, content_to_write):
        while True:  
            try:
                with open(file_path, "w") as file:
                    file.write(content_to_write)
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def process_folder(self, folder_path,encrypt = None, key= None,infer= None):
        letterfrequency = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0,
                           0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 
                           0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 
                           0.15, 2.0, 0.074]
        file_keys = []
        # Iterate through all files in the folder
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):

                file_path = os.path.join(folder_path, file_name)
                file_contents = self.openfile(file_path, input_message="none")
                if file_contents == "":
                    print(f"The file '{file_path}' is empty, and won't be processed.")
                    continue
                
                # Infer the Caesar cipher key for the file
                if infer == True:
                    inferred_key = self.infer_caesar_cipher_key(
                        file_contents, letterfrequency
                    )
                    file_keys.append((file_name, inferred_key))
                    # Add the file name and key to a list of tuples
                elif encrypt != None:
                    file_keys.append((file_name,key))

            
        # Sort the list of tuples by key
        if infer == True:
            file_keys.sort(key=lambda x: x[1])

        file_keys_log = ""
        file_number = 1

        # Iterate through the list of tuples and decrypt each file
        for file_name, key in file_keys:
            file_contents = self.openfile(os.path.join(folder_path, file_name), input_message="none")
            file_contents = self.encrypt(file_contents, -key if encrypt == "D" or infer==True else key)

            # Write the decrypted contents to a new file
            file_no = f"file{file_number}.txt"
            self.writefile(os.path.join(folder_path, file_no ), file_contents)

            enc = "Encrypted" if encrypt == "E" else "Decrypted"
            # Print a message indicating the file has been decrypted
            print(f"{enc} : {file_name} with key {key} as :{file_no}.txt\n")

            # Add the file name and key to a log string
            file_keys_log += f"{enc} : {file_name} with key {key} as :{file_no}.txt\n"
            file_number += 1
        
        self.writefile(os.path.join(folder_path, "log.txt" ), file_keys_log)

    def compare_frequency_distribution(self,text):
        text_frequencies = LetterFrequency(text).get_frequencies()
        reference_frequencies = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4, 6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]
        
        frequency_diff = [abs(a - b) for a, b in zip(reference_frequencies, text_frequencies)]
        max_diff = sum(reference_frequencies) + 100

        percentage = (sum(frequency_diff) / max_diff) * 100
        percentage_similarity = 100 - percentage

        return percentage_similarity, sum(frequency_diff)    