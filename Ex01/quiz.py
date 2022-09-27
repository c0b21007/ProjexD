mondai1 = ["サザエの旦那の名前は？",["マスオ","ますお"]]
mondai2 = ["カツオの妹の名前は？",["ワカメ","わかめ"]]
mondai3 = ["タラオはカツオから見てどんな関係？",["甥","おい","甥っ子","おいっこ"]]
mondai_lis = [mondai1,mondai2,mondai3]
from random import randint

def shutudai(num):
    print("問題: " + mondai_lis[num][0])

def kaito(num):
    ans = input("答えよ: ")
    if ans in mondai_lis[num][1]:
        print("正解！ ")
    else:
        print("不正解！ ")


if __name__ == "__main__":
    num = randint(0,2)
    shutudai(num)
    kaito(num)

