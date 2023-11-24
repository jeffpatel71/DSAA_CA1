# Name: Hazem Bin Ryaz Patel
# Admission Number: 2200550
# Class: DAAA/FT/2B/07

from CaesarCipherAnalyzer import CaesarCipherAnalyzer
from View import View
from InputOutputHandler import InputOutputHandler
import re
import os


class Controller:
    def __init__(self, view, analyzer, input_output_handler):
        self.__input_output_handler = input_output_handler
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
        print("")
        encrypt = self.__input_output_handler.get_encrypt()
        message = self.__input_output_handler.get_message(
            "Please type text you want to encrypt: \n"
        )

        key = self.__input_output_handler.get_key()
        encrypted = self.__analyzer.encrypt(message, key if encrypt == "E" else -key)
        self.__view.display_encryption(message, encrypted)
        self.__input_output_handler.enter_message()

    def selection2(self):
        print("")
        user_option = self.__input_output_handler.get_encrypt()
        while True:
            optionchosen = "encrypt: " if user_option == "E" else "decrypt: "
            file_path = self.__input_output_handler.get_file_path(f"Enter the file you want to {optionchosen}")
            file_contents = self.__input_output_handler.open_non_empty_file(file_path, f"Enter the file you want to {optionchosen}")

            key = self.__input_output_handler.get_key()
            new_file_path = self.__input_output_handler.get_file_path(
                "Enter the output file: "
            )

            file_encrypted = self.__analyzer.encrypt(
                file_contents, key if user_option == "E" else -key
            )

            self.__input_output_handler.writefile(new_file_path, file_encrypted)
            break
        self.__input_output_handler.enter_message()

    def selection3(self):
        print()
        text_filepath = self.__input_output_handler.get_file_path(
            "Please enter the file you want to analyze: "
        )
        text = self.__input_output_handler.open_non_empty_file(
            text_filepath, "Please enter the file you want to analyze: "
        )
        letter_frequency = self.__analyzer.get_frequency(text)
        self.__view.display_analyze_frequency(letter_frequency)

    def selection4(self):
        print()
        # Get file path & content
        file_path = self.__input_output_handler.get_file_path("Please enter the file you want to analyze: ")
        file_content = self.__input_output_handler.open_non_empty_file(file_path, f"Please enter the file you want to analyze: ")

        # Get Reference File & content
        reference_file_path = self.__input_output_handler.get_file_path("Please enter the reference file: ", nospacing=True)
        reference_file_content = self.__input_output_handler.open_non_empty_file(reference_file_path, f"Please enter the reference file: ")

        # Can't put this inside infer_caesar_cipher_key() because of Option 5
        reference_file = reference_file_content.replace("\n", ",").split(",")
        letterfrequency = [float(x) for x in reference_file[1::2]]

        key = self.__analyzer.infer_caesar_cipher_key(file_content, letterfrequency)
        self.__view.display_key(key)  # Display Key

        user_option = self.__input_output_handler.check_input(
            "^[yn]$",
            "Would you want to decrypt this file using this key? y/n: ",
            "Invalid input, please enter y or n",
        )
        print()

        if user_option == "y":
            new_file_path = self.__input_output_handler.get_file_path(
                "Enter the output file: "
            )
            decrypted_contents = self.__analyzer.encrypt(file_content, -key)
            self.__input_output_handler.writefile(new_file_path, decrypted_contents)
        self.__input_output_handler.enter_message()

    def selection5(self):
        print()
        letterfrequency = [8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,0.15,0.77,4.0,2.4,
                           6.7,7.5,1.9,0.095,6.0,6.3,9.1,2.8,0.98,2.4,0.15,2.0,0.074,]
        
        folder_path = self.__input_output_handler.check_folder()
        # retrieve all file paths inside that folder_path
        files_folder = self.__input_output_handler.get_files_folder(folder_path)
        file_keys = []

        for files in files_folder:
            content = self.__input_output_handler.openfile(
                os.path.join(folder_path, files), input_message="none"
            )
            if content == "":
                print(f"The file '{files}' is empty, and won't be processed.")
                continue
            inferred_key = self.__analyzer.infer_caesar_cipher_key(
                content, letterfrequency
            )
            file_keys.append((files, inferred_key))

        file_keys.sort(key=lambda x: x[1])
        file_keys_log = ""
        file_number = 1

        for file_name, key in file_keys:
            file_contents = self.__input_output_handler.openfile(os.path.join(folder_path, file_name), input_message="none")
            file_contents = self.__analyzer.encrypt(file_contents, -key)

            # Write the decrypted contents to a new file
            file_no = f"file{file_number}.txt"
            self.__input_output_handler.writefile(os.path.join(folder_path, file_no), file_contents)
            print(f"Decrypting: {file_name} with key: {key} as: {file_no}\n")

            # Add the file name and key to a log string
            file_keys_log += f"Decrypted : {file_name} with key {key} as: {file_no}\n"
            file_number += 1
        self.__input_output_handler.writefile(os.path.join(folder_path, "log.txt"), file_keys_log)
        print("\n")
        self.__input_output_handler.enter_message()

    def selection6(self): # Batch Encrypt Files
        print()
        folder_name = self.__input_output_handler.check_folder()
        files_folder = self.__input_output_handler.get_files_folder(folder_name)
        key = self.__input_output_handler.get_key()

        for file_name in files_folder:
            filepath = os.path.join(folder_name, file_name)
            file_contents = self.__input_output_handler.openfile(filepath, input_message="none")
            if file_contents == "":
                print(f"The file '{file_name}' is empty, and won't be encrypted.")
                continue
            file_contents = self.__analyzer.encrypt(file_contents, key)
            file_encrypted = f"{file_name}_encrypted.txt"
            self.__input_output_handler.writefile(os.path.join(folder_name, file_encrypted), file_contents)

        print(f"Encrypted files are saved in {folder_name}")
        print("\n")
        self.__input_output_handler.enter_message()
    
    def selection7(self):
        print()
        analyze_message = self.__input_output_handler.check_input(
            "^[1-2]$",
            "Would you like to analyze a file(1) or a message(2) ",
            "Invalid input, please enter 1 or 2",
        )

        if analyze_message == "1":
            file_path = self.__input_output_handler.get_file_path("Please enter the file you want to analyze: ")
            message = self.__input_output_handler.openfile(file_path, input_message="Please enter the file you want to analyze: ")

        if analyze_message == "2":
            message = self.__input_output_handler.get_message("Please enter the message you want to analyze: \n")

        percentage_similarity, frequency_diff = self.__analyzer.compare_frequency_distribution(message)
        self.__view.display_frequency(frequency_diff, percentage_similarity)
        self.__input_output_handler.enter_message()

    def goodbye(self):
        print(
            "\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer"
        )


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
*********************************************************"""
    )
    input("Press enter key, to continue...")
    view = View()
    analyzer = CaesarCipherAnalyzer()
    io = InputOutputHandler()
    Controller(view, analyzer, io).run()
