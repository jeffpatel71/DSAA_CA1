# Name: Hazem Bin Ryaz Patel
# Admission Number: 2200550
# Class: DAAA/FT/2B/07

from CaesarCipherAnalyzer import CaesarCipherAnalyzer
from View import View
import re
import os
import os



class Controller:
    def __init__(self, view, analyzer):
        self.__view = view
        self.__analyzer = analyzer
        self.__choices = {
            "1": self.selection1,
            "2": self.selection2,
            "3": self.selection3,
            "4": self.selection4,
            "5": self.selection5,
            "6": self.selection6,
            "7": self.selection7,
            "8": self.goodbye,
        }

    def run(self):
        while True:
            selection = self.__view.display_menu()
            self.__choices[selection]()

            if selection == "8":
                break

    def selection1(self):
        encrypt = self.get_encrypt()
        print("Please type text you want to encrypt: ")
        message = input()
        print("")
        key = self.get_key()
        encrypted = self.__analyzer.encrypt(message, key if encrypt == "E" else -key)
        self.__view.display_encryption(message, encrypted)

    def selection2(self):
        print("Option 2 is selected\n")
        user_option = self.get_encrypt()
        print("")

        while True:
            optionchosen = ("encrypt: " if user_option == "E" else "decrypt: ")
            file_path = self.get_file_path(f"Enter the file you want to {optionchosen}")
            file_contents = self.open_non_empty_file(file_path, f"Enter the file you want to {optionchosen}")

            key = self.get_key()
            new_file_path = self.get_file_path("Enter the output file: ")

            file_encrypted = self.__analyzer.encrypt(
                file_contents, key if user_option == "E" else -key
            )

            self.__analyzer.writefile(new_file_path, file_encrypted)
            break
        continuemsg = input("Press any key to continue...")

    def selection3(self):
        text_filepath = self.get_file_path("Please enter the file you want to analyze: ")
        text = self.open_non_empty_file(text_filepath, "Please enter the file you want to analyze: ")

        letter_frequency = self.__analyzer.get_frequency(text)
        self.__view.display_analyze_frequency(letter_frequency)
        print("Option 3 Selected")

    def selection4(self):
        # Get file path & content
        file_path = self.get_file_path("Please enter the file you want to analyze: ")
        file_content = self.open_non_empty_file(file_path, f"Please enter the file you want to analyze: ")

        # Get Reference File & content  
        reference_file_path = self.get_file_path("Please enter the reference file: ")
        reference_file_content = self.open_non_empty_file(reference_file_path, f"Please enter the reference file: ")
        
        # Can't put this inside infer_caesar_cipher_key() because of Option 5
        reference_file = reference_file_content.replace("\n", ",").split(",")
        letterfrequency = [float(x) for x in reference_file[1::2]]

        key = self.__analyzer.infer_caesar_cipher_key(file_content, letterfrequency)
        self.__view.display_key(key) # Display Key

        user_option = self.check_input(
            "^[yn]$",
            "Would you want to decrypt this file using this key? y/n: ",
            "Invalid input, please enter y or n",
        )


        if user_option == "y":
            new_file_path = self.get_file_path("Enter the output file: ")
            decrypted_contents = self.__analyzer.encrypt(file_content, -key)
            self.__analyzer.writefile(new_file_path, decrypted_contents)

    def selection5(self):
        print("")
        # folder_name = self.check_folder()
        # ? = self.analyzer.process_folder(folder_name, encrypt=None, infer=True, key=None)
    
        # write to files
        # save to database
        # print to console
        # do nothing about it?

    def selection6(self):
        print("Option 6 Selected")

        folder_name = self.check_folder()
        enc = self.get_encrypt()
        key = self.get_key()

        self.__kanalyzer.process_folder(folder_name, key, encrypt=enc, infer=None)

    def selection7(self):
        print("Option 7 Selected")
        analyze_message = self.check_input(
            "^[1-2]$",
            "Would you like to analyze a file(1) or a message(2) ",
            "Invalid input, please enter 1 or 2",
        )

        if analyze_message == "1":
            input_message = "Please enter the file you want to analyze: "
            file_path = self.check_input(
                "^.+\.txt$",
                (input_message),
                "Invalid input, please enter a valid file path",
            )
            message = self.analyzer.openfile(file_path, input_message)

        if analyze_message == "2":
            print("Please type text you want to encrypt: ")
            message = input()

        (
            percentage_similarity,
            frequency_diff,
        ) = self.analyzer.compare_frequency_distribution(message)
        self.view.display_frequency(frequency_diff, percentage_similarity)

    def goodbye(self):
        print(
            "\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer"
        )
    
    def get_encrypt(self):
        return self.check_input("^[ED]$", "Enter E to encrypt, D to decrypt: ", "Invalid input, please enter E or D")
    
    def get_key(self):
        return int(self.check_input("^-?\d+$", "Enter the cipher key: ", "Invalid input, please enter a number"))
    
    def check_input(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp

    def check_folder(self):
        folder_name = self.check_input("^[a-zA-Z0-9_\-\s]+$", "Enter the folder name: ", "Invalid input, please enter a valid folder name")
        while True:
            try:
                if os.path.exists(folder_name):
                    break
                else:
                    print(f"The folder '{folder_name}' does not exist.\n")
                    folder_name = self.check_input("^[a-zA-Z0-9_\-\s]+$", "Enter the folder name: ", "Invalid input, please enter a valid folder name")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("")
        return folder_name
    
    def get_file_path(self, prompt):
        return self.check_input("^.+\.txt$", prompt, "Invalid input, please enter a valid file path")
    
    def open_non_empty_file(self, file_path, prompt):
        while True:
            file_contents = self.analyzer.openfile(file_path, prompt)
            if file_contents != "":
                return file_contents
            else:
                print(f"The file '{file_path}' is empty.")
                file_path = self.get_file_path(prompt)

if __name__ == "__main__":
    print(
        """
*********************************************************
* ST1507 DSAA: Welcome to:                              *
*                                                       *
*      ~ Caesar Cipher Encrypted Message Analyzer ~     *
*-------------------------------------------------------*
*                                                       *
*  - Done by: Hazem Bin Ryaz Patel(2200550)             *
*  - Class DAAA/2B/07                                   *
*********************************************************
Press enter key to continue..."""
    )
    input()
    view = View()
    analyzer = CaesarCipherAnalyzer()
    Controller(view, analyzer).run()

