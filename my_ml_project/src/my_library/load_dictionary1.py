def load(input_path):
    dictionary = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                array = line.split("\t") #arrayは左から語句・P/N・評価基準を持つリスト
                if array[1] == "p":
                    array[1] = 1
                elif array[1] == "n":
                    array[1] = -1
                else:
                    array[1] = 0
                dictionary.append((array[0],int(array[1])))
            else:
                pass
    dictionary.sort()
    return dictionary