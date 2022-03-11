# 종합문제
# 문제1
# a="a:b:c:d"
# print("#".join(a.split(":")))

# 문제2
# a={'A':90, 'B':80}
# try: a['C']
# except: print('70')

# 문제4
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum=0
# for n in range(len(A)):
#     if A[n]>=50:
#         sum+=A[n]
# print(sum)

# 문제5
# k=int(input("정수"))
# A=[0,1]
# while ((A[len(A)-2]+A[len(A)-1]) <= k) :
#     A.append(A[len(A)-2]+A[len(A)-1])
# print(A)

문제6
a=input().split(',')
sum=0
for n in range(len(a)):
    sum+=int(a[n])
print(sum)

문제7
a=int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))
for n in range (8):
    print(a*(n+1),end=' ')