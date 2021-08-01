import pandas as pd
import numpy as np

def readCSV(file):
    return pd.read_csv(file)

def locateTeamColumn(dataframe, teamName):
    # print(dataframe, teamName)
    dataframe = dataframe.loc[(dataframe[teamName] == "X") | (dataframe[teamName] == "x")]
    return dataframe.index

def askTeamName():
    name = input("Enter team name here: ") 
    return name

# def replaceRows(masterFrame, index, updatedFrame):
#     pass

# def matchAndReplace(masterFrame, updatedFrame, teamName):
#     updatedSeries = updatedFrame[teamName].tolist()
#     masterSeries = masterFrame[teamName].tolist()
#     # print(masterSeries)
#     for item in masterSeries:
#         if updatedSeries == []:
#             break
#         if (item == "x") | (item == "X"):
#             print(int(item.index))
#             continue
#             masterFrame.at[item.index, 'AvgBill'] = updatedSeries[0]
#             # item = updatedSeries[0]
#             updatedSeries.pop(0)
#     # print(masterFrame[teamName].tolist())
#     # masterFrame[teamName] = masterSeries
#     return masterFrame

def matchAndReplace(masterFrame, updatedFrame, teamName, arrOfIndexes):
    updatedSeries = updatedFrame[teamName].tolist()
    for i in arrOfIndexes:
        masterFrame.at[i, teamName] = updatedSeries[0]
        updatedSeries.pop(0)
    return masterFrame
    # print(masterFrame[teamName].tolist())
    # print(masterFrame.loc[masterFrame[teamName] == 'L'])
    # print(masterFrame.loc[(masterFrame[teamName] == 'X') | (masterFrame[teamName] == 'x')])

def toCSV(dataframe):
    # dataframe.to_csv(r'C:\Users\srikardevarakonda\Downloads\ItemsToEdit.csv', index = False, header=True)
    dataframe.to_csv('ShopperPlanningstuff.csv', index = False, header=True)

def main():
    updatedFrame = readCSV('ItemsToEdit2.csv')
    masterFrame = readCSV('ShopperPlanningstuff.csv')
    name = askTeamName()
    indexes = locateTeamColumn(masterFrame, name)
    masterFrame = matchAndReplace(masterFrame, updatedFrame, name, indexes)
    toCSV(masterFrame)
    print('done')
    # print(masterFrame.loc[masterFrame[name] == "x"])
    # print(updatedFrame[name])
    # print(indexes)
    # print(updatedFrame[name].iloc[0])
    # for index in indexes:
    #     replaceRows(masterFrame, index, updatedFrame)







if __name__ == "__main__":
    main()