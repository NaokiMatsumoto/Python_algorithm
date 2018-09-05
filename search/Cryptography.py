# * クラス名：Cryptography
# * 関数名 : encrypt
# * 内容　：与えられたnumbersリストのうち任意の一つに1加算したときの
#           リストの全ての値の積のうち、最も大きい値を返す
# * 引数　：
#    numbers  : 数値のリスト(各要素の値は1～1000)
# * 返値　： numbersのうち一つに1加算した場合の積の最大値
# example : numbers = [1,3,2,1,1,3}
# => return 36


class Cryptography:

    @staticmethod
    def encrypt(numbers):
        # 答えとして返す値(multiply_max)を初期化します。各要素の値は1~1000なので、最低でも1となります。
        multiply_max = 1
        multiply = 1
        # multiplyを数値のリスト(numbers)に含まれる数の積にします。
        for number in numbers:
            multiply *= number
        for number in numbers:
            # multiplyはnumbersのすべての積のため、multiply // number * (number + 1)は数値のひとつに1加算したものの積となります。ループの中で各数値に1加えていきmax関数で最大値を取ります。
            multiply_max = max(multiply_max, multiply // number * (number + 1))
        return multiply_max


numbers = [1, 2, 3]
# 1 => 2 にして積は12
print(Cryptography.encrypt(numbers))

numbers = [1000, 999, 998, 997, 996, 995]
# 986074810223904000
print(Cryptography.encrypt(numbers))
