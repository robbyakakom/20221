class Person :
    def __init__(self,nim,nama) :
        self.nim = nim
        self.nama = nama

    def cetak(self) :
        print(f'{self.nim:15} {self.nama:15}')