import pandas as pd

print("!!! Note: XL- 12 + Sprints, L- 6- 12 Sprints, M- 6 Sprints, S- 3-5 Sprints, Xs – 2 Sprints !!!\n")

def readCSV(file):
    return pd.read_csv(file)

def selectColumns(dataframe, teamName):
    dataframe.dropna(how='all', axis=1, inplace=True)
    dataframe = dataframe[["Initiatives/Project", "Customer/Business Problem Statement", "Driving Team", teamName]]
    return dataframe

def locateTeamColumn(dataframe, teamName):
    dataframe = dataframe.loc[(dataframe[teamName] == "X") | (dataframe[teamName] == "x")]
    return dataframe

def askTeamName():
    name = input("Enter team name here: ") 
    return name

def toCSV(dataframe):
    # dataframe.to_csv(r'C:\Users\srikardevarakonda\Downloads\ItemsToEdit.csv', index = False, header=True)
    dataframe.to_csv('ItemsToEdit2.csv', index = False, header=True)

def main():
    df = readCSV("ShopperPlanningStuff.csv")
    name = askTeamName()
    cleanDf = selectColumns(df, name)
    rowsToEdit = locateTeamColumn(cleanDf, name)
    toCSV(rowsToEdit)
    print('done')

if __name__ == "__main__":
    main()

### only show the important columns (done)