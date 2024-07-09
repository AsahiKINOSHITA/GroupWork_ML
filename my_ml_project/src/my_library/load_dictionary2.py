def load(input_path):

    dictionary = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                array = line.split("\t") #arrayは左から評価基準・P/Nを持つリスト
                if array[0] == "ネガ（経験）" or array[0] == "ネガ（評価）":
                    array[0] = -1
                elif array[0] == "ポジ（経験）" or array[0] == "ポジ（評価）":
                    array[0] = 1
                #以下の処理で、連語の対策をする
                if " " in array[1]: #例えば「キリ が ない」が該当する
                    if "悪い" in array[1]:  #「間 が 悪い」などは前半の名詞ではなく、「悪い」(dictionary2収録済み)が連語の極性を決定づけている
                        continue
                    elif "ない" in array[1]:
                        array[0] *= -1 #極性を反転
                    else:
                        pass
                    array[1] = (array[1].split())[0]    #「キリ が ない」なら、大胆にはじめの「キリ」のみ辞書に登録
                dictionary.append((array[1].rstrip('\n'),array[0]))#[array[1].rstrip('\n')] = array[0]
            else:
                pass
    dictionary.sort()
    return dictionary