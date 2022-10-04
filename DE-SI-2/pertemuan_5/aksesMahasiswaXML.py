from xml.dom.minidom import parse 
mahasiswa = parse('mahasiswa.xml')

jumMhs = len(mahasiswa.getElementsByTagName("mahasiswa"))

print("Jumlah Mahasiswa : ", jumMhs)

print("{:10} {:15} {:10} ".format("NIM","Nama Mahasiswa","Prodi"))
i = 0
while i < jumMhs :
    nim = mahasiswa.getElementsByTagName("nim")[i].firstChild.nodeValue 
    nama = mahasiswa.getElementsByTagName("nama")[i].firstChild.nodeValue 
    prodi = mahasiswa.getElementsByTagName("prodi")[i].firstChild.nodeValue 
    i = i + 1
    print("{:10} {:15} {:10} ".format(nim, nama, prodi))
    


