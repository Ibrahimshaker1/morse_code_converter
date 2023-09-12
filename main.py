from filter import Filter
from converter import Convert
path = input("please paste your txt file path here: ")
my_filter = Filter(path)
path = my_filter.valid_path()
filter_massage = my_filter.read(path)
covert = Convert(filter_massage)
covert.convert_letter_to_code()

