import hashlib
import random


def md5(s):
    """
    Calculates the md5 hash of a string
    :param s: input string
    :return: md5 of the given string, as `str`
    """
    d = hashlib.md5()
    d.update(s.encode("utf-8"))
    return d.hexdigest()


def clamp(value, min_, max_):
    """
    Clamps `value` between `min_` and `max_`
    :param value: input value
    :param min_: minimum
    :param max_: maximum
    :return: clamped value
    """
    return max(min_, min(value, max_))


def aestheticize(s, spaced=False, symbols=True):
    """
    A E S T H E T I C I Z E S  a string
    :param s: input string
    :param spaced: if `True`, put additional spaces between each letter
    :param symbols: if `True`, append some aesthetic symbols to the string
    :return: aestheticized string
    """
    aesthetic_letters = {
        " ": "　", "`": "`", "1": "１", "2": "２", "3": "３", "4": "４", "5": "５", "6": "６", "7": "７",
        "8": "８", "9": "９", "0": "０", "-": "－", "=": "＝", "~": "~", "!": "！", "@": "＠", "#": "＃",
        "$": "＄", "%": "％", "^": "^", "&": "＆", "*": "＊", "(": "（", ")": "）", "_": "_", "+": "＋",
        "q": "ｑ", "w": "ｗ", "e": "ｅ", "r": "ｒ", "t": "ｔ", "y": "ｙ", "u": "ｕ", "i": "ｉ", "o": "ｏ",
        "p": "ｐ", "[": "[", "]": "]", "\\": "\\", "Q": "Ｑ", "W": "Ｗ", "E": "Ｅ", "R": "Ｒ", "T": "Ｔ",
        "Y": "Ｙ", "U": "Ｕ", "I": "Ｉ", "O": "Ｏ", "P": "Ｐ", "{": "{", "}": "}", "|": "|", "a": "ａ",
        "s": "ｓ", "d": "ｄ", "f": "ｆ", "g": "ｇ", "h": "ｈ", "j": "ｊ", "k": "ｋ", "l": "ｌ", ";": "；",
        "'": "＇", "A": "Ａ", "S": "Ｓ", "D": "Ｄ", "F": "Ｆ", "G": "Ｇ", "H": "Ｈ", "J": "Ｊ", "K": "Ｋ",
        "L": "Ｌ", ":": "：", "\"": "\"", "z": "ｚ", "x": "ｘ", "c": "ｃ", "v": "ｖ", "b": "ｂ", "n": "ｎ",
        "m": "ｍ", ",": "，", ".": "．", "/": "／", "Z": "Ｚ", "X": "Ｘ", "C": "Ｃ", "V": "Ｖ", "B": "Ｂ",
        "N": "Ｎ", "M": "Ｍ", "<": "<", ">": ">", "?": "？"
    }
    aesthetic_symbols = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひ" \
                        "びぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔアイウエオカキクケコキャキュキョ" \
                        "サシスセソシャシュショタチツテトチャチュチョナニヌネノニャニュニョハヒフヘホヒャヒュヒョマミムメモミ" \
                        "ャミュミョヤユヨラリルレロリャリュリョワンガギグゲゴギャギュギョザジズゼゾジャジュジョダヂヅデドバビ" \
                        "ブベボビャビュビョパピプペポピャピュピョファフィフェフォツァティトゥウェウォ日一大年中会人本月長国出上" \
                        "十生子分東三行同今高金時手見市力米自前円合立内二事社者地京間田体学下目五後新明方部.女八心四民対主正代" \
                        "言九小思七山実入回場野開万全定家北六問話文動度県水安氏和政保表道相意発不党"
    joiner = " " if spaced else ""
    final_string = joiner.join(aesthetic_letters[x] if x in aesthetic_letters else x for x in s)
    if symbols:
        final_string += "  " * (2 if spaced else 1 if s else 0)
        final_string += joiner.join(random.choice(aesthetic_symbols) for _ in range(clamp(len(s) // 5, min_=3, max_=7)))
    return final_string
