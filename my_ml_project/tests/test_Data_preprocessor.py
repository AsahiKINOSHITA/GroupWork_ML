import os,sys
import pytest
import pickle
import numpy as np
from unittest.mock import mock_open, patch

project_root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
sys.path.append(os.path.join(project_root_path, "src", "my_library"))

import src.my_library.Data_preprocessor as DataPreprocessor


# モックデータとモック辞書を用意
mock_sentences1 = [["This",0,1],
                  ["is",0,1],
                  ["a",0,1],
                  ["test",0,1],
                  ["sentence",0,1],
                  ["Another",1,1],
                  ["test",1,1],
                  ["sentence",1,1]]
"""mock_sentences1 = ["This is a test sentence", "Another test sentence"]"""
mock_sentences1.sort()
mock_sentences2 = [
    [
        ["This",0,1],
        ["is",0,1],
        ["a",0,1],
        ["test",0,1],
        ["sentence",0,1],
        ["Another",1,1],
        ["test",1,1],
        ["sentence",1,1]
    ],
    [
        1,0
    ]

]
"""mock_sentence2 = [
    ("This is a test sentence.", "1"),
    ("Another test sentence.","0")

    ]"""

mock_sentences2[0].sort()

mock_dictionary1 = [["test", 1], ["sentence", 0], ["This", -1]]
mock_dictionary1.sort()
mock_dictionary2 = []

mock_count_vectors = [[1, 1, 1, 3], [0, 1, 1, 2]]

def test_preprocess_data():
    dp = DataPreprocessor.DataPreprocessor( mock_sentences1, mock_dictionary1,mock_dictionary2,2)
    dp.preprocess_data()
    assert np.array_equal(dp.X, np.array(mock_count_vectors))

def test_dump(tmp_path):
    dp = DataPreprocessor.DataPreprocessor(mock_sentences2, mock_dictionary1,mock_dictionary2,2)
    dp.preprocess_data_and_label()
    file_path = os.path.join(tmp_path , "preprocessed_data.pkl")
    dp.dump(file_path)
    
    with open(file_path, "rb") as f:
        X, y = pickle.load(f)
    os.remove(file_path)
    
    assert np.array_equal(X, np.array(mock_count_vectors))
    assert np.array_equal(y, np.array([1, -1]))
def test_preprocess_data_and_label():
    dp = DataPreprocessor.DataPreprocessor(mock_sentences2, mock_dictionary1,mock_dictionary2,2)
    dp.preprocess_data_and_label()
    assert np.array_equal(dp.X, np.array(mock_count_vectors))
    assert np.array_equal(dp.y, np.array([1, -1]))
