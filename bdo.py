class BibliographicDataObject:
    def __init__(self, 
                 author="", 
                 authorName="",
                 authorSurname="",
                 title="", 
                 subtitle="",
                 responsibility="",
                 placeOfPublication="", 
                 publisher="",
                 dateOfPublication="",
                 extent=""):
        self.author = author
        self.authorName = authorName
        self.authorSurname = authorSurname
        self.title = title
        self.subtitle = subtitle
        self.responsibility = responsibility
        self.placeOfPublication = placeOfPublication
        self.publisher = publisher
        self.dateOfPublication = dateOfPublication
        self.extent = extent

    def printMLA(self):
        '''
        Author's Last Name, First Name. Title of Book. Publisher, Publication Year.
        '''
        print(f"{self.authorSurname}, {self.authorName}. {self.title}{': ' + self.subtitle if self.subtitle else ''}. {self.publisher}, {self.dateOfPublication}." if all(x is not None for x in [self.authorSurname, self.authorName, self.title, self.publisher, self.dateOfPublication]) else "")
    
    def printAPA(self):
        '''
        Author's Last Name, First Initial. Second Initial. (Publication Year). Title of work: Capital letter also for subtitle. Publisher.
        '''
        #print(f"{self.authorSurname}, {self.authorName}. ({self.dateOfPublication}). {self.title}. {self.publisher}.")
        return