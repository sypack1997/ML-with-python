# One - hot Encoding : 단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고, 다른 인덱스에는 0을 부여하는 단어의 벡터 표현 방식 (모든 무나열 값들을 숫자형으로 인코딩 하는 전처리 작업 후 머신러닝 모델에 학습시켜야 한다.)

# Bag of Words : 단어들의 순서는 전혀 고려하지 않고, 단어들의 출현 빈도에만 집중하는 텍스트 데이터의 수치화 표현 방법

# corpus : 머신러닝을 하기 위해서는 기계에 학습시켜야 할 데이터가 필요하다. 자연어 처리의 경우, 자연어 데이터를 corpus라고 부르며, 조사나 연구 목적에 의해서 특정 도메인으로부터 수집된 텍스트 집합을 말한다. (ex. txt파일, csv파일, 음성데이터, 영화리뷰 등등)

import os

def get_file_list(dir_name):
    return os.listdir(dir_name)

if __name__ == "__main__":
    dir_name = "news_data"
    file_list = get_file_list(dir_name)
    file_list == [os.path.join(dir_name, file_name) for file_name in file_list] # os.path.join 다시 확인해보기

def get_contents(file_list):
    y_class = []
    X_text = []
    class_dict = {
        1:"0", 2:"0", 3:"0", 4:"0", 5:"1", 6:"1", 7:"1", 8:"1"
    } # 0 = "야구", 1 = "축구"
    for file_name in file_list:
        try:
            f = open(file_name, "r", encoding = "cp949")
            category = int(file_name.split(os.sep)[1].split("_")[0]) # 다시 확인하기
            y_class.append(class_dict[category]) # y_class = category의 값
            X_text.append(f.read()) # X_text = 문서
            f.close()
        except UnicodeDecodeError as e:
            print(e)
            print(file_name)
        return X_text, y_class

def get_cleaned_text(text):
    import re
    text = re.sub('\W+', '', text.lower()) # 의미없는 문장부호 등은 제거
    return text

def get_corpus_dict(text): #text안의 word들을 통해 index값을 만들어줌 (각각의 word가 몇번째 index에 속하는지 선언)
    text = [sentence.split() for sentence in text]
    cleaned_words = [get_cleaned_text(word) for words in text for word in words] # 1 Dimential로 바꿔줌, 동일한 단어들은 모두 합쳐짐

    from collections import OrderedDict # word들이 key 값이 됨
    corpus_dict = OrderedDict()
    for i, v in enumerate(set(cleaned_words)):
        corpus_dict[v] = i
    return corpus_dict

def get_count_vector(text, corpus):
    text = [sentence.split() for sentence in text]
    word_number_list = [[corpus[get_cleaned_text(word)] for word in words] for words in text] # 2 Dimential 형태로 바꿔줌
    X_vector = [[0 for _ in range(len(corpus))] for x in range(len(text))] # 파이썬에서 _는 변수를 두지 않는다는 의미 

    for i, text in enumerate(word_number_list):
        for word_number in text:
            X_vector[i][word_number] += 1
        return X_vector

import math
def get_cosine_similarity(v1, v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2) / {||v1|| * ||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy / math.sqrt(sumxx * sumyy)

def get_similarity_score(X_vector, source): # source = 찾고자 하는 문서
    source_vector = X_vector[source]
    similarity_list = []
    for target_vector in X_vector:
        similarity_list.append(get_cosine_similarity(source_vector, target_vector))
    return similarity_list

def get_top_n_similaritiy_news(similarity_score, n):
    import operator
    x = {i:v for i, v in enumerate(similarity_score)}
    sorted_x = sorted(x.items(), key = operator.itemgetter(1))

    return list(reversed(sorted_x))[1:n+1]