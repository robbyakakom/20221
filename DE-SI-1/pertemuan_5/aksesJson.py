import json 
file = open('mahasiswa.json', 'r') 
dataMhs = json.load(file) 
for rowMhs in dataMhs['mahasiswa'] :
    nim = rowMhs['nim']
    nama = rowMhs['nama']
    prodi = rowMhs['prodi']
    print('{:10} {:10} {:10}'.format(nim,nama,prodi))
