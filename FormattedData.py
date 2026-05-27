import csv

class FormatData:
    def __init__(self, Name= "", Age = 0, Married=False):
        self.Name = Name
        self.Age = Age
        self.Married = Married

    def __str__(self):
        OutString = "'{0}', {1}, {2}".format(
            self.Name,
            self.Age,
            self.Married)
        return OutString
    
    def SaveData(Filename = "", DataList = []):
        with open(Filename,
                  "w", newline = '\n') as csvfile:
            DataWriter = csv.writer(
                csvfile,
                delimiter= ',',
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)

            for Entry in DataList:
                DataWriter.writerow([str(Entry)])
            
            print("Data saved!")
    
    def ReadData(Filename = ""):
        with open(Filename,
                  "r", newline='') as csvfile:
            DataReader = csv.reader(
                csvfile,
                delimiter=',',
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)

            Output = []
            for Item in DataReader:
                Output.append(Item[0])

            csvfile.close()
            print("Data Read!")
            return Output
