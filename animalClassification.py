class Animalia:
    def __init__(self,name,kelas,ordo):
        self.name = name
        self.kelas = kelas
        self.ordo = ordo
    def informasi(self):
        print (f'{self.name}:\n\t'
              f'kelas = {self.kelas}\n\t'
              f'ordo = {self.ordo}')
class Chordata(Animalia):
    def __init__(self,name,kelas,ordo):
        super().__init__(name,kelas,ordo)
    def informasi(self):
        print (f'{self.name}:\n\t'
              f'filum = Chordata\n\t'
              f'kelas = {self.kelas}\n\t'
              f'ordo = {self.ordo}')
class Porifera(Animalia):
    def __init__(self,name,kelas,ordo):
        super().__init__(name,kelas,ordo)
    def informasi(self):
        print (f'{self.name}:\n\t'
              f'filum = Porfera \n\t'
              f'kelas = {self.kelas}\n\t'
              f'ordo = {self.ordo}')
class Moluska(Animalia):
    def __init__(self,name,kelas,ordo):
        super().__init__(name,kelas,ordo)
    def informasi(self):
        print (f'{self.name}:\n\t'
              f'filum = Moluska \n\t'
              f'kelas = {self.kelas}\n\t'
              f'ordo = {self.ordo}')
class Platyhelmintes(Animalia):
    def __init__(self,name,kelas,ordo,ciri_ciri):
        super().__init__(name,kelas,ordo)
        self.ciri_ciri = ciri_ciri
    def informasi(self):
        super().informasi()
        print(self.ciri_ciri)
        
class Nemathelmintes(Animalia):
    def __init__(self, name, kelas, ordo, jenis):
        super().__init__(name,kelas,ordo)
        self.jenis = jenis
    def informasi(self):
        super().informasi()
        print(self.jenis)

manusia = Chordata('Manusia','Mamalia','Primata')
spongia = Porifera('Spongia','Demospongiae','Dictyoceratida')
octopus = Moluska('Octopus','Sefalopoda','Octopoda')
cacing = Platyhelmintes('cacing','cacing','cacing','tidak punya kaki')
cacing1Nemathelmintes('a','b','c','d',)
manusia.informasi()
