# * 関数名：InteretingParty
# * 内容　：各メンバーの趣味としてfirst,secondという引数として与えられます。
#           同じ趣味を持つ人の数を返します
# * 引数　：
#    first   : リスト、first[i]はi番目の人の1つ目の趣味
#    second  : リスト、second[i]はi番目の人の2つ目の趣味
#    firstとsecondは同じ数とする
# * 返値　： 同じ趣味の人の数


class InterestingParty:
#aaaa
    @staticmethod
    def best_invitation(first, second):
        hobby_dict = {}
        # first secondをそれぞれ、hobby_dict内に挿入する、キーが存在しない場合は1で初期化し、キーが存在する場合、1プラスする
        for index in range(len(first)):
            hobby_dict[first[index]] = 1 if first[index] not in hobby_dict else hobby_dict[first[index]] + 1
            hobby_dict[second[index]] = 1 if second[index] not in hobby_dict else hobby_dict[second[index]] + 1
        # 配列の値で最も多いものが最も多い趣味となる
        return max(hobby_dict.values())


first = ["fishing", "gardening", "swimming", "fishing"]
second = ["hunting", "fishing", "fishing", "biting"]

# 趣味fishingとする人の数が最も多く4となる
print(InterestingParty.best_invitation(first, second))

first = ["snakes", "programming", "cobra", "monti"]
second = ["python", "python", "anaconda", "python"]

# 趣味pythonとする人の数が最も多く3となる
print(InterestingParty.best_invitation(first, second))
