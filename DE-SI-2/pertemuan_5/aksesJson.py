import json 
file_json = open('mahasiswa.json', 'r') 
data = json.load(file_json) 

print("{:10} {:15} {:10}".format("NIM","Nama Mahasiswa","Prodi"))
for baris in data["mahasiswa"] :
    print("{:10} {:15} {:10}".format(baris["nim"],baris["nama"],baris["prodi"]))

