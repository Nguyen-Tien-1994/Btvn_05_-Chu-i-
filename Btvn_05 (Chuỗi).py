# Bài 01:
# Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
# Bài làm:
'''
s = input("nhập kí tự s là:")
n = input("nhập kí tự n là:")
print(s.replace(s[0], n))
'''
# Bài 2:
#Bài 05. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
# Bài làm:
'''
s = input("nhập chuỗi kí tự s là:")
n = 1
max = s[0]
min = s[0]
for n in range(len(s)):
    if s[n] > max:
        max = s[n]
    else:
        if s[n] < min:
            min = s[n]
    n += 1
print(max)
print(min)
'''
# Bài 3:
'''
Bài 02:
 Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
 '''
# Bài làm:
'''s = input("nhập chuỗi kí tự s là:")
m = int(input("nhập m ="))
S1 = s.replace(s[m],"",m)
print(S1)'''
# Bài 4:
'''Bài 03. Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.'''
# Bài làm:
#s = input("nhập chuỗi kí tự s là:")







