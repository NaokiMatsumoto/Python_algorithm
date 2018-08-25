# * クラス名：FriendScore
# * 関数名 : highest_score
# * 内容　：与えられた文字列のリストfriendsから友人の友人まで数えた
#           値の最大値を求める
# * 引数　：
#    friends  : Yは友人を表し、Nは友人でない
# * 返値　： 友人と友人の友人の合計の最大値
# example : friends ={"NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"}
# 0番目と4番目の人の友人と友人の友人の数は2,1番目と3番目の人の友人と友人の友人の数は3
# 2番目の人の友人と友人の友人の数は4
# => return 4


class FriendScore:

    @staticmethod
    def highest_score(friends):
        friends_count = 0
        for row in range(len(friends)):
            friends_count_tmp = 0
            for col in range(len(friends)):
                if row == col:
                    continue
                if friends[row][col] == 'Y':
                    friends_count_tmp += 1
                else:
                    for index in range(len(friends)):
                        if friends[row][index] == 'Y' and friends[index][col] == 'Y':
                            friends_count_tmp += 1
            friends_count = max(friends_count_tmp, friends_count)
        return friends_count


friends = ["NYNNN",
           "YNYNN",
           "NYNYN",
           "NNYNY",
           "NNNYN"]
print(FriendScore.highest_score(friends))

