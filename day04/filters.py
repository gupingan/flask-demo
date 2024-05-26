"""
自定义过滤器
注意：函数名需要以 do_ 开头
比如:
    def do_xxx():
        pass
星号分隔线下方的代码请不要动!
"""


def do_fixed(value: str, length: int = 2):
    return f'{value: .{length}f}'


def do_suffix(value: str, suffix: str = '元'):
    return f'{value}{suffix}'


def do_hide_phone(value: str, length: int = 4, dot: str = '*'):
    value_length = len(value)
    if value_length - 1 <= length:
        return value

    first_index = (value_length - length) // 2
    second_index = first_index + length
    return f'{value[:first_index]}{dot * length}{value[second_index:]}'


# **************************************************************************************
# 以下代码无需变动，上方增加过滤器即可
# **************************************************************************************


filters = {}

for variable in locals().copy().keys():
    if isinstance(variable, str) and variable.startswith('do_'):
        use_name = variable.lower().split('_', 1)[-1]
        if not use_name:
            continue
        filters[use_name] = locals().get(variable)
