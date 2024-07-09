import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)   
import time
import my_library.load_input_data as input_loader
import my_library.load_dictionary1 as dictionary1_loader
import my_library.load_dictionary2 as dictionary2_loader
from my_library.Data_preprocessor import DataPreprocessor

data_path = input("Enter the path for the data file: ")
dictionary1_path = "data/dictionary1.txt"
dictionary2_path = "data/dictionary2.txt"
preprocessed_data_path = input("Enter the path to save the preprocessed data: ")
data_length = int(input("Enter the number of lines of the data:"))
labeled = input("Enter if the data is labeled (Y/N):")

dictionary1 = dictionary1_loader.load(dictionary1_path)
dictionary2 = dictionary2_loader.load(dictionary2_path)
start = time.time()
if labeled == "Y":
    sentence_arrays = input_loader.load(data_path)
    print(len(sentence_arrays[1]))
    data_preprocessor = DataPreprocessor(sentence_arrays, dictionary1, dictionary2,data_length) #train.txtの見出しの行を削除する
    data_preprocessor.preprocess_data_and_label()
else:
    sentence_arrays = input_loader.load_raw_data(data_path)
    data_preprocessor = DataPreprocessor(sentence_arrays, dictionary1, dictionary2,data_length)
    data_preprocessor.preprocess_data()
end = time.time()
print(end - start)
data_preprocessor.dump(preprocessed_data_path)