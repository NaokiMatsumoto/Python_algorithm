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
        # friends_count 最終的な返り値
        friends_count = 0
        # 0人目から最後の人までループ
        for row in range(len(friends)):
            # row人目の友人、友人の友人の数(friends_count_tmp)を初期化
            friends_count_tmp = 0
            # col を0人目から最後までループ、row人目とcol人目が友人かチェック
            for col in range(len(friends)):
                # row == col 同じ人を探索している場合は、飛ばす
                if row == col:
                    continue
                # 友達の場合は、friends_count_tmpに1加える
                if friends[row][col] == 'Y':
                    friends_count_tmp += 1
                else:
                    # 友達でなかった場合も、index番目の人がお互いの友達の場合は、友達の友達となるためfriends_count_tmpに1加える
                    for index in range(len(friends)):
                        if friends[row][index] == 'Y' and friends[index][col] == 'Y':
                            friends_count_tmp += 1
            #maxをとる。
            friends_count = max(friends_count_tmp, friends_count)
        return friends_count


friends = ["NYNNN",
           "YNYNN",
           "NYNYN",
           "NNYNY",
           "NNNYN"]
print(FriendScore.highest_score(friends))

