from domain.Entities import Balla

class RepoError(Exception):
    pass
class RepoBalla(object):

    def __init__(self):
        self._ballaList = []
    
    
    def add(self , song):
        if song in self._ballaList :
            raise RepoError("Existing element")
        self._ballaList.append(song)
        
    def getAll (self):
        return self._ballaList[:]

class FileRepoBalla(RepoBalla):
    
    def __init__(self,filename):
        RepoBalla.__init__(self)
        self.__filename = filename
        self.__readAllFromFile()
        
    def __readAllFromFile(self):
        try:
            with open(self.__filename) as f:
                
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        words = line.strip().split(",")
                        ident = int(words[0].strip())
                        name = words[1].strip()
                        value = float(words[2])
                        basketballer = Balla(ident,name,value)
                        self._ballaList.append(basketballer)
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
    
    def __writeAllToFile(self):
        try:
            with open(self.__filename,"w") as f:
                for elem in self._ballaList:
                    f.write(str(elem)+"\n")
        except FileNotFoundError :
            print("Inexistent file : "+self.__filename)
        

    def add(self, song):
        RepoBalla.add(self, song)
        self.__writeAllToFile()
    
    
        
    def print_all(self):
        for t in RepoBalla.getAll(self):
            print(t)


        
repo = FileRepoBalla("gigi.csv")
repo.add(Balla(34,"LeBum James",-100))

repo.print_all()

#writeAllToFile("gigiout.csv", elems)