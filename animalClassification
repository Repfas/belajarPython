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
breakpoint()
manusia = Chordata('Manusia','Mamalia','Primata')
spongia = Porifera('Spongia','Demospongiae','Dictyoceratida')
octopus = Moluska('Octopus','Sefalopoda','Octopoda')

manusia.informasi()
