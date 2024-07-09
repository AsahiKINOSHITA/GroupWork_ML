from janome.tokenizer import Tokenizer

def count_and_vectorize(d1, d2, sentence,length):
    """ PN_table = [0, 0, 0, 0] #陰性、中性、陽性, 極性持ち語数
    t = Tokenizer()
    words = []
    for token in t.tokenize(sentence):
        words.append(token.base_form)

    for i in range(len(words)):
        if words[i] in d1:
            if d1[words[i]] == -1:
                PN_table[0] += 1
            elif d1[words[i]] == 0:
                PN_table[1] += 1
            elif d1[words[i]] == 1:
                PN_table[2] += 1
            PN_table[3] += 1
        elif words[i] in d2:
            if d2[words[i]] == -1:
                PN_table[0] += 1
            elif d2[words[i]] == 1:
                PN_table[2] += 1
            PN_table[3] += 1
    return PN_table
    """
    PN_tables=[[0,0,0,0] for _ in range(length)]
    index1,index2 = 0,0
    for w in sentence:
        while index1 < len(d1) and d1[index1][0] < w[0]:
            index1 += 1
        while index2 < len(d2) and d2[index2][0] < w[0]:
            index2 += 1
        if index1 < len(d1) and w[0] == d1[index1][0]:
            PN_tables[w[1]][3] += 1
            if d1[index1][1] == -1:
                PN_tables[w[1]][0] += 1
            elif d1[index1][1] == 0:
                PN_tables[w[1]][1] += 1
            elif d1[index1][1] == 1:
                PN_tables[w[1]][2] += 1
         
        if index2 < len(d2) and w[0] == d2[index2][0]:
            PN_tables[w[1]][3] += 1
            if d2[index2][1] == -1:
                PN_tables[w[1]][0] += 1
            elif d2[index2][1] == 0:
                PN_tables[w[1]][1] += 1
            elif d2[index2][1] == 1:
                PN_tables[w[1]][2] += 1
    return PN_tables
         