class BibliographicDataObject:
    def __init__(self, 
                 author="", 
                 authorName="",
                 authorSurname="",
                 title="", 
                 placeOfPublication="", 
                 publisher="",
                 dateOfPublication="",
                 edition="",
                 extent="",
                 isbn=""):
        self.author = author
        self.authorName = authorName
        self.authorSurname = authorSurname
        self.title = title
        self.placeOfPublication = placeOfPublication
        self.publisher = publisher
        self.dateOfPublication = dateOfPublication
        self.edition = edition
        self.extent = extent
        self.isbn = isbn

    def printMLA(self):
        '''
        Author's Last Name, First Name. Title of Book. Publisher, Publication Year.
        '''
        print(f"{self.authorSurname}, {self.authorName}. {self.title}. {self.publisher}, {self.dateOfPublication}.")

    def printAPA(self):
        '''
        Author's Last Name, First Initial. Second Initial. (Publication Year). Title of work: Capital letter also for subtitle. Publisher.
        '''
        print(f"{self.authorSurname}, {self.authorName}. ({self.dateOfPublication}). {self.title}. {self.publisher}.")