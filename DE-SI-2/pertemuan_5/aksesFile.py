file = open("data.txt","a")
file.write("\ntambah baris baru 2")
file.close()

bukaFile = open("data.txt","r")
isiFile = bukaFile.read()
print(isiFile)