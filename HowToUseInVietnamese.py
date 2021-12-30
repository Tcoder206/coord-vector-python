from coord import * # Import thư viện coord (Coordinate: Tọa độ)

### coord.create(a,b) ###
a = (5,2) # Tọa độ của vector a
b = (6,7) # Tọa độ của vector b
AB = coord.create(a,b) # Tính tọa độ vector AB
CD = coord.create((1,1),(3,5)) # Tính tọa độ vector CD
# -> Trong đó tọa độ vector C là (1,1), tọa độ vector D là (3,5) 
print(f'Vector AB = {AB}') # Output: Vector AB = (1,5)
print(f'Vector CD = {CD}') # Output: Vector CD = (2,4)

### coord.add(a,b,c,...,n) ###
add = coord.add(AB,CD) # Tính phép cộng giữa 2 vector AB và CD 
print(f'AB{AB} + CD{CD} = {add}') # Output: AB(1,5) + CD(2,4) = (3,9)

### coord.subtract(a,b,c,...,n) ###
subtract = coord.subtract(AB,CD) # Tính phép trừ giữa 2 vector AB và CD
print(f'AB{AB} - CD{CD} = {subtract}') # Output: AB(1,5) - CD(2,4) = (-1,1)

### coord.multi(k,a,b,c,...,n) ###
# -> k là số nguyên. a,b,c,...n là tọa độ của vector
multi1 = coord.multi(3,AB) # Tính tích của 3 lần vector AB
print(f'2 * vector AB = {multi1}') # Output: 2 * vector AB = (3,15)
multi2 = coord.multi(5,AB,CD) # Tính tích của 5 lần vector AB và 5 lần vector CD
print(multi2) # Output: [(5,25),(10,20)]
# -> (5,25) là tích của 5 lần vector AB. (10,20) là tích của 5 lần vector CD.

### coord.co_exp(a,b) ###
# -> Biểu thức tọa độ của 2 vector (Coordinate Expression)
co_exp = coord.co_exp(AB,CD) # Tính tích vô hướng của tọa độ AB(1,5) và CD(2,4)
print(f'vector AB * vector CD = {co_exp}') # Output: vector AB * vector CD = 22
# -> # Hoành * hoành + tung * tung = 1 * 2 + 5 * 4 = 2 + 20 = 22

### coord.average(a,b,c,...,n) ###
# -> Tính tọa độ của trung điểm, trọng tâm của vector
c = (1,1) # Tọa độ của vector c
d = (3,5) # Tọa độ của vector d
# Tọa độ vector a và vector b đã đc khai báo ở trên
AC = coord.create(a,c) # => vector AC = (-4,-1)
BC = coord.create(b,c) # => vector BC = (-5,-6)
trungdiem = coord.average(AB,AC) # Tính trung điểm của 2 vector AB và CD
print(trungdiem) # Output: (-1.5,2) hoặc (-3/2,2)
trongtam = coord.average(AB,AC,BC) # Tính trọng tâm của tam giác ABC
print(trongtam) # Output: (-2.6666666666666665,-0.6666666666666666) hoặc (-8/3,-2/3)

### coord.size(vec,compact) ###
# -> Tính kích thước, độ dài của vector
# -> Trong đó vec là tọa độ của vector, compact là kiểu bool và mặc định là False
ABlength = coord.size(AB,compact=False) # Tính độ dài của vector AB
print(ABlength) # Output: 5.0990195135927845
# -> Để độ dài của vector chuyển từ số thập phân sang căn bậc 2 thì đổi compact=True
ABsize = coord.size(AB,compact=True)
print(ABsize) # Output: √26 (Căn bậc 2 của 26)

## coord.mid_angle(a,b) ###
# -> Tính góc giữa của 2 vector bất kỳ
EF = (2,-3) # Tọa độ của vector EF là (2,-3)
GH = (6,4) # Tọa độ của vector EF là (6,4)
middle = coord.mid_angle(EF,GH) # Tính góc giữa 2 vector EF và GH
print(f'(a,b) = {middle}') # Output: (a,b) = 90 (Góc giữa là 90 độ)