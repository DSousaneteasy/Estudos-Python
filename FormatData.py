from FormattedData import FormatData

NewData= [FormatData("Gerge", 65, True),
          FormatData("Sally", 47, False),
          FormatData("Doug", 52, True)]

FormatData.SaveData("TesteFile.csv", NewData)
