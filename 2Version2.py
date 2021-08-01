import pandas as pd

def readCSV(file):
    return pd.read_csv(file)

def askTeamName(): 
    name = input("Enter team name here: ") 
    return name

def checkX(dataframe, name):
    noError = True
    possVals = ['XL', 'L', 'M', 'S', 'XS']
    upperDataframe = dataframe[name].str.upper().astype('str').tolist()

    for i in range(0, len(upperDataframe)):
        item = upperDataframe[i]
        if item == "X":
            print('did not fill in at row number', i+2, '; project name:', dataframe.at[i, 'Initiatives/Project'])
            noError = False
        elif item not in possVals and item != "X" and item != 'nan':
            print('incorrect value entered at row number', i+2, '; project name:', dataframe.at[i, 'Initiatives/Project'])
            noError = False

    return noError

def main():
    name = askTeamName()
    givenFrame = readCSV("ItemsToEdit2.csv")
    checkedX = checkX(givenFrame, name)
    if checkedX:
        print("good job")
    else:
        print('Edit the file correctly and then come back')

if __name__ == "__main__":
    main()

### Note down project names, index values of the rows that are not fully edited (done)
### Note down project names, index values of the rows that have false values (done)