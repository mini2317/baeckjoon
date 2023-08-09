for _ in range(int(input())):
    sum_ = 0
    for i in range(1, int(input())+1):
        if (not '3' in str(i)) and (not '6' in str(i)) and (not '9' in str(i)): sum_ += bin(i).count('1')
    print(sum_)