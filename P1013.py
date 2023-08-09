import re

def is_pattern_matched(signal):
    pattern = re.compile("(100+1+|01)+")
    return pattern.fullmatch(signal) is not None

T = int(input().strip())
for _ in range(T):
    signal = input().strip()
    print('YNEOS'[not is_pattern_matched(signal)::2])
