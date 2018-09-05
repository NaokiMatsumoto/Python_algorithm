# * クラス名：Palindrome
# * 関数名 : find
# * 内容　： 引数strに右端から文字列を追加して回文となった場合の回文の長さの最小値を返す
# * 引数　：
#    str : 文字列
# * 返値　： 回文の長さ
# example : str = aab
# => return 5(aabaaが最小の回文)


class Palindrome:

    @staticmethod
    def find(str):
        # mid_str : 与えられた文字列(str)の中心
        mid_str = len(str) // 2
        # palindroome_lenは返り値とする。
        palindrome_len = len(str) * 2
        # 与えられた文字列の真ん中から右に移動し、回文を作れるかチェック
        for index in range(mid_str, len(str)):
            is_palindrome = True
            # check_indexは0～indexからstrの右端までの長さ
            for check_index in range(len(str) - index):
                if str[index - check_index] != str[index + check_index]:
                    is_palindrome = False
                    break
            if is_palindrome:
                palindrome_len = min(palindrome_len, index * 2 + 1)
        return palindrome_len


str1 = "abab"
# 回文はababaのため5
print(Palindrome.find(str1))

str1 = "abacaba"
# 回文はabacabaのため7
print(Palindrome.find(str1))

str1 = "qwerty"
# 回文はqwertytrewqのため11
print(Palindrome.find(str1))
