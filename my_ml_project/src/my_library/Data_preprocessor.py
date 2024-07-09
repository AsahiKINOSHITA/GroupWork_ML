import os
import sys
import pickle
import numpy as np
from . import count_polarity_statistics as counter 

class DataPreprocessor:
    def __init__(self, sentence_arrays, d1, d2,length):
        """
        DataPreprocessorクラスのコンストラクタ
        Args:
            sentence_arrays (list of lists): 処理する文章の配列
            d1, d2 (dict): 極性辞書を読み込んだ辞書型変数         
        """
        self.sentence_arrays = sentence_arrays
        self.dictionary1 = d1
        self.dictionary2 = d2
        self.length=length
        self.X = None   #極性の4次元ベクトルを要素に持つnumpy配列を入れる
        self.y = None

    def preprocess_data(self):
        """
        data.txtのデータ形式を前提に前処理を行う
        """
        X_list = []
        """for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i]     # 配列の要素が文章であると想定
            count_vector = counter.count_and_vectorize(self.dictionary1, self.dictionary2, sentence)
            X_list.append(count_vector)"""
        X_list=counter.count_and_vectorize(self.dictionary1,self.dictionary2,self.sentence_arrays,self.length)
        self.X = np.array(X_list)                  # リストをnumpyの多次元配列に変換

    def preprocess_data_and_label(self):
        """
        train.txtのデータ形式を前提に前処理を行う
        """
        X_list, y_list = [], []
        """for i in range(len(self.sentence_arrays)):
            sentence = self.sentence_arrays[i][0]  # Sentenceの列を取得
            count_vector = counter.count_and_vectorize(self.dictionary1, self.dictionary2, sentence)
            X_list.append(count_vector)
            if self.sentence_arrays[i][4] == "0":  # Writer_Joyの列が"0"なら負例とする 
                y_list.append(-1)
            else:                                  # Writer_Joyの列が"0"でないなら正例とする 
                y_list.append(1)
            if len(X_list) < 4:
                print(X_list[-1], y_list[-1])"""
        X_list = counter.count_and_vectorize(self.dictionary1,self.dictionary2,self.sentence_arrays[0],self.length)
        for i in range(len(self.sentence_arrays[1])):
            if self.sentence_arrays[1][i] == 0:
                y_list.append(-1)
            else:
                y_list.append(1)
        
        self.X, self.y = np.array(X_list), np.array(y_list)  # リストをnumpyの多次元配列に変換


    def dump(self, file_path):
        """
        前処理されたデータとラベルをファイルに保存する
        Args:
            file_path (str): 前処理データを保存するファイルのパス
        """
        with open(file_path, "wb") as f:
            pickle.dump((self.X, self.y), f)