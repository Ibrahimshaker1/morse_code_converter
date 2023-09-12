from morse_code_data import Data
# the Convert class will covert the massage to morse code massage


class Convert:
    def __init__(self, massage: str):
        self.data = Data().morse_code
        self.massage = massage

    def convert_letter_to_code(self):
        massage = self.massage
        coded_massage = massage
        for letter in massage:
            if letter != " ":
                try:
                    coded_massage = coded_massage.replace(letter, self.data[letter])
                except KeyError:
                    pass
        print(coded_massage)
