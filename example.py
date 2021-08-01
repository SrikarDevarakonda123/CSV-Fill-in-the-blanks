import pandas as pd

def readCSV(file):
    # print(file)
    return pd.read_csv(file)

def changeFrame(frame):
    frame['Team C'] ='nice'
    return frame

def toCSV(frame):
    frame.to_csv('Example.csv', index = False, header=True)

def main():
    masterFrame = readCSV('Example.csv')
    frame = changeFrame(masterFrame)
    toCSV(frame)
    print('done')

if __name__ == "__main__":
    main()
