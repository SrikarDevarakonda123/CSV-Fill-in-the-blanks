import pandas as pd

def readCSV(file):
    return pd.read_csv(file)

def sameNumRowsCols(givenDF, originalDF):
    if givenDF.shape[1] == originalDF.shape[1]:
        if givenDF.shape[0] == originalDF.shape[0]:
            return True
        else:
            return 'there is an interference with the num of rows'
    else:
        if givenDF.shape[0] == originalDF.shape[0]:
            return 'there is an interference with the num of columns'
        else:
            return 'there is an interference with the num of rows & columns'

def askTeamName(): 
    name = input("Enter team name here: ") 
    return name

# def checkX(dataframe, name):
#     possVals = ['XL', 'L', 'M', 'S', 'XS']
#     # if "x" not in dataframe[name] or 'X' not in dataframe[name]:
#     upperDataframe = dataframe[name].str.upper().astype('str')
#     for item in upperDataframe:
#         if item != "X" and item != 'nan':
#             if item not in possVals:
#                 print(item.index)
#                 return 'false item entered'
#             else:
#                 continue
#         else:
#             itemsToFill = dataframe.loc[(dataframe[name] == "X") | (dataframe[name] == "x")].index
#             print('items to fill are at row number: ', list(itemsToFill))
#             return 'not fully edited'
#     return True

def checkX(dataframe, name):
    possVals = ['XL', 'L', 'M', 'S', 'XS']
    upperDataframe = dataframe[name].str.upper().astype('str')
    itemsToFill = list(dataframe.loc[(dataframe[name] == "X") | (dataframe[name] == "x")].index)
    if itemsToFill != False:
        for item in itemsToFill:
            print('row num', item + 2, "has to be edited.")
        arrOfErrors = [False]

    for item in upperDataframe:
        if (item not in possVals and item != 'X') and item != 'nan':
            print(item, "was entered but is not a possible option")
            arrOfErrors.append(False)
        else:
            continue

    if arrOfErrors.__contains__(False):
        return False

    return

def checkFullDataFrame(givenDf, originalDf, name):
    if originalDf.drop([name], axis = 1).equals(givenDf.drop([name], axis = 1)):
        return True
    else:
        print('Parts that were not supposed to be modified were modified')
        return False

# def locIndex(givenFrame, originalFrame, teamName):
#     #print(givenFrame['OSS'])
#     originalFrame = originalFrame.loc[(originalFrame[teamName] == "X") | (originalFrame[teamName] == "x")]
#     return originalFrame[teamName]
#     # return givenFrame['OSS']

def main():
    givenFrame = readCSV("ItemsToEdit2.csv")
    originalFrame = readCSV("ItemsToEdit.csv")
    name = askTeamName()
    # print(locIndex(givenFrame, originalFrame, name))
    # return 
    # sameShape = sameNumRowsCols(givenFrame, originalFrame)
    checkedX = checkX(givenFrame, name)
    # fullFrameCheck = checkFullDataFrame(givenFrame, originalFrame, name)
    # if sameShape != True:
    #     print(sameShape)
    if checkedX != True:
        print('Edit the file correctly and then come back')
    else:
        print("good job")
    # if fullFrameCheck != True:
    #     print(fullFrameCheck)



if __name__ == "__main__":
    main()

### Note down project names, index values of the rows that are not fully edited