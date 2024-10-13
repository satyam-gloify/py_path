from typing import List
# def solution(a: [int]) -> [int]:
def solution(a: List[int]) -> List[int]:
# write your solution here
    for i in range(a.__len__):
        a[i]= a[i]*a[i]
        
    res = a.sort(reverse=True)
    return res
# DO NOT • CHANGE the code below, we use it to grade your submission.
# changed your submission will be failed
if __name__ == '__main ':
    line = input ( )
    a = line.strip().split()
    output = solution(a)
    if output == []:
        print('[]')
    else:
        print(' [%s]' % ', '.join(map(str, output) ))