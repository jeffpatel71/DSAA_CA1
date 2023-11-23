import re
import os


class InputOutputHandler:
    def __init__(self):
        pass

    def check_input(self, options, msg, invalid_msg):
        inp = input(msg)
        while not re.match(options, inp):
            print(invalid_msg)
            inp = input(msg)
        return inp

    def get_key(self):
        return int(
            self.check_input(
                "^-?\d+$",
                "Enter the cipher key: ",
                "Invalid input, please enter a number",
            )
        )

    def get_encrypt(self):
        return self.check_input(
            "^[ED]$",
            "Enter E to encrypt, D to decrypt: ",
            "Invalid input, please enter E or D",
        )

    def get_message(self, text):
        return input(text)

    def get_file_path(self, prompt):
        return self.check_input(
            "^.+\.txt$", prompt, "Invalid input, please enter a valid file path"
        )

    def open_non_empty_file(self, file_path, prompt):
        while True:
            file_contents = self.openfile(file_path, prompt)
            if file_contents != "":
                return file_contents
            else:
                print(f"The file '{file_path}' is empty.")
                file_path = self.get_file_path(prompt)

    def writefile(self, file_path, content_to_write):
        while True:
            try:
                with open(file_path, "w") as file:
                    file.write(content_to_write)
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
    
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
    
    def check_folder(self):
        folder_name = self.check_input(
            "^[a-zA-Z0-9_\-\s]+$",
            "Enter the folder name: ",
            "Invalid input, please enter a valid folder name",
        )
        while True:
            try:
                if os.path.exists(folder_name):
                    break
                else:
                    print(f"The folder '{folder_name}' does not exist.\n")
                    folder_name = self.check_input(
                        "^[a-zA-Z0-9_\-\s]+$",
                        "Enter the folder name: ",
                        "Invalid input, please enter a valid folder name",
                    )
            except Exception as e:
                print(f"An error occurred: {e}")
                print("")
        return folder_name

    def get_files_folder(self, folder_path):
        files_folder = []
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(folder_path, file_name)
                file_contents = self.openfile(file_path, input_message="none")
                if file_contents == "":
                    print(f"The file '{file_path}' is empty, and won't be processed.")
                    continue
                files_folder.append(file_path)
        return files_folder