class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kasvatuskoko = int(kasvatuskoko)
        self.vasen_jono = [0] 
        self.alkioiden_lukumaara = 0

    def kuuluu(self, luku):
        if luku in self.vasen_jono:
            return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.vasen_jono[self.alkioiden_lukumaara] = luku
            self.alkioiden_lukumaara += 1

            if self.alkioiden_lukumaara == len(self.vasen_jono):
                self.vasen_jono += [0] * self.kasvatuskoko
            return True
        return False

    def poista(self, poistettava: int):
        for i, luku in enumerate(self.vasen_jono):
            if poistettava == luku:
                self.vasen_jono.pop(i)
                self.vasen_jono.append(0)
                self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
                return True
        return False


    def mahtavuus(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        return self.vasen_jono[:self.alkioiden_lukumaara]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for luku in a_taulu + b_taulu:
            x.lisaa(luku)

        return x

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for a_luku in a_taulu:
            for b_luku in b_taulu:
                if a_luku == b_luku:
                    leikkaus.lisaa(a_luku)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for luku in a_taulu:
            if luku not in b_taulu:
                erotus.lisaa(luku)        
        return erotus

    def __str__(self):
        return f"{{{', '.join(list(map(lambda x: str(x), self.to_int_list())))}}}"
