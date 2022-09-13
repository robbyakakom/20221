## penggunaan perulangan
# x = 0
# while x <= 5 :
#     x = x + 1
#     if x == 3 :
#         continue 
#     print(x)
    
for x in range(1,6) : # [1,2,3,4,5]
    if x == 3 :
        continue 
    print(x)

list = ["amir","budi","cici","dedi"]
no = 1
for n in list :
    print(str(no) + " " + n)
    no = no + 1