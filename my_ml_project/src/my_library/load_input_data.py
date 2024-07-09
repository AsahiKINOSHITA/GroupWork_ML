from janome.tokenizer import Tokenizer
import time

def load(input_path):   #train.txtの情報を要素に持つリストを要素に持つリスト
    words_and_value_arrays = [[],[]]
    cnt=0
    t=Tokenizer()
    is_first_line = True
    with open(input_path) as f:
        for line in f:
            if line != "":
                line = line.rstrip("\n")
                if "\t" in line:
                    line_arrays = line.split("\t")
                else:
                    pass
                if is_first_line:
                    is_first_line = False
                    continue
                for token in t.tokenize(line_arrays[0]):
                    words_and_value_arrays[0].append((token.base_form,cnt))
                    print(f"\r loaded {cnt} lines",end="")
            else:
                print("\r")
                pass
            cnt+=1
            words_and_value_arrays[1].append(line_arrays[4])
    words_and_value_arrays[0].sort()
    return words_and_value_arrays

def load_raw_data(input_path):  #data.txtの一文を要素に持つリストを返す
    words_array = []
    t=Tokenizer()
    cnt=0
    with open(input_path) as f:
        for line in f:
            if line != "":
                line = line.rstrip("\n")
                for token in t.tokenize(line):
                    words_array.append((token.base_form,cnt))
                    print(f"\r loaded {cnt} lines",end="")
            else:
                print("\r")
                pass
            cnt+=1
    words_array.sort()
    return words_array