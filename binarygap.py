def solution(N):
    binary = tobinary(N)
    count = 0
    temp = 0
    for i in range(len(binary)):
        if binary[i] == 0:
            temp += 1
        else:
            count = max(count,temp)
            temp = 0
    return count
    
def tobinary(N):
    binary = []
    while N != 0:
        binary.append(N%2)
        N = N//2
    binary.reverse()
    return binary

