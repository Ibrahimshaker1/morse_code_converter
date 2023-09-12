# import libraries
import string
# filter the massage remove anything is not a letter or number like(!, ?, / .....)


class Filter:
    def __init__(self, path):
        self.path = path
        self.alpha_bet_list = list(string.ascii_lowercase)
        self.number_list = list(string.digits)

    # to make the file path valid to open
    def valid_path(self):
        path = self.path
        new_path = ""
        if "\\" in path:
            new_path = path.replace("\\", "/")
            return new_path
        else:
            new_path = path
            return new_path

    # this function read the file and filter it (remove anything is not a letter or number)
    def read(self, valid_path: str):
        with open(valid_path, "r") as mf:
            massage = mf.readlines()
            filtered_line = ''
            for lines in massage:
                remove_letter = ""
                for letter in lines.lower():
                    if letter not in self.alpha_bet_list and letter != " ":
                        if letter not in self.number_list and letter != "\n":
                            remove_letter += letter
                new_line = lines
                for rl in remove_letter:
                    new_line = new_line.replace(rl, "")
                filtered_line += new_line.lower()
            return filtered_line


