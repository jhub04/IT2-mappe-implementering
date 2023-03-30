class Bruker:
    """ Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
    
    """
    def __init__(self, epost, fornavn, etternavn):
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget in")

    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker):
    """ Superklasse for lærere i skolesystemet. Skal ikke brukes direkte

        Attributes:
            epost: En string med lærers epost
            fornavn: En string med lærers fornavn
            etternavn: En string med lærers etternavn
            lønnskonto: En integer med lærers lønnskonto
    
    """
    def __init__(self, epost, fornavn, etternavn ,lønnskonto):
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto

class Kontaktlærer(Lærer):
    """ Subklasse for kontaktlærere i skolesystemet. Ment for å brukes direkte

    Attributes:
            epost: En string med lærers epost
            fornavn: En string med lærers fornavn
            etternavn: En string med lærers etternavn
            lønnskonto: En integer med lærers lønnskonto
            klasse: En string med lærers kontaktklasse
            trinn: En int med lærers kontaktklassetrinn
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto, klasse, trinn):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.klasse = klasse
        self.trinn = trinn

class Faglærer(Lærer):
    """ Subklasse for faglærere i skolesystemet. Ment for å brukes direkte

    Attributes:
            epost: En string med lærers epost
            fornavn: En string med lærers fornavn
            etternavn: En string med lærers etternavn
            lønnskonto: En integer med lærers lønnskonto
            kompetanse: En liste med strings med faglærer er kompetent i
            klasser: En liste med strings med klasser faglærer har
            
    
    """
    def __init__(self, epost, fornavn, etternavn, lønnskonto):
        super().__init__(epost, fornavn, etternavn, lønnskonto)
        self.kompetanse = []
        self.klasser = []

class Elev(Bruker):
    """ En subklasse for brukere i skolesystemet. Ment for å brukes direkte

    Attributes:
        epost: En string med brukers epost
        fornavn: En string med brukers fornavn
        etternavn: En string med brukers etternavn
        trinn: En int med brukers trinn
        klasse: en string med brukers klasse
        fag: en liste med strings med brukers fag
    
    """
    def __init__(self, epost, fornavn, etternavn, trinn, klasse, fag):
        super().__init__(epost, fornavn, etternavn)
        self.trinn = trinn
        self.klasse = klasse
        self.fag = fag
        
# Denne brukes for testing, betyr at koden inne i if-setningen kun kjøres   # hvis vi trykker play på denne fila, eller kjører denne fila i terminalen
if __name__ == "__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
    ravi.logg_inn()

    jonathan = Elev("jonathansh@viken.no", "Jonathan", "Hubertz", "VG3", "3STF", ["R2", "Fys2", "IT2"])
    jonathan.logg_inn()

