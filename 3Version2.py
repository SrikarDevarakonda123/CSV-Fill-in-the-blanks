import pandas as pd

def readCSV(file):
    return pd.read_csv(file)

def locateTeamColumn(dataframe, teamName):
    dataframe = dataframe.loc[(dataframe[teamName] == "X") | (dataframe[teamName] == "x")]
    return dataframe.index

def askTeamName():
    name = input("Enter team name here: ") 
    return name

def matchAndReplace(masterFrame, updatedFrame, teamName, arrOfIndexes):
    updatedSeries = updatedFrame[teamName].tolist()
    for i in arrOfIndexes:
        masterFrame.at[i, teamName] = updatedSeries[0]
        updatedSeries.pop(0)
    return masterFrame

def toCSV(dataframe):
    dataframe.to_csv('ShopperPlanningstuff.csv', index = False, header=True)
    return

def main():
    name = askTeamName()
    updatedFrame = readCSV('ItemsToEdit2.csv')
    masterFrame = readCSV('ShopperPlanningstuff.csv')
    indexes = locateTeamColumn(masterFrame, name)
    masterFrame = matchAndReplace(masterFrame, updatedFrame, name, indexes)
    toCSV(masterFrame)
    print('done')


if __name__ == "__main__":
    main()