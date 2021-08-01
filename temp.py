import pandas as pd

frame = pd.read_csv('ShopperPlanningstuff.csv')
print(frame)

# frame['Initiatives/Project'] = frame['Initiatives/Project'] + ' // ' + frame['Features'].astype("str")

# frame = frame.drop(['Features'], axis = 1)

# frame.to_csv('ShopperPlanningStuff.csv', index = False, header=True)