import random
from site import abs_paths
num_all = 10
num_abs = 2
num_challenge = 2
alpha_list = list("QWERTYUIOPASDFGHJKLZXCVBNM")
def shutudai():
    all_chars = random.sample(alpha_list,num_all)
    print("対象文字：", end="")
    for i in sorted(all_chars):
        print(i, end= "")
    print()
    abs_chars = random.sample(all_chars, num_abs)
    print("表示文字：", end="")
    for i in all_chars:
        if i not in abs_chars:
            print(i, end="")
    print()
    print("デバッグ用欠損文字：", abs_chars)
    return abs_chars


def kaito(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？: "))
    if num != num_abs:
        print("不正解！ ")
    else:
        print("正解です.それでは具体的に欠損文字を一つずつ入力してください ")
        for i in range(num):
            c = input(f"{i+1}つ目の文字を入力してください")
            if c in seikai:
                seikai.remove(c)
            else:
                print("不正解です　またチャレンジしてください")
                return False
        else:
            print("完全正解です おめでとうございます！")
            return True



if __name__ == "__main__":
    for i in range(num_challenge):
        abs_chars = shutudai()
        seigo = kaito(abs_chars)
        if seigo:
            break
        else:
            print("-"*20)