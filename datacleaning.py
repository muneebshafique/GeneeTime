import pandas as pd


class DataCleaning:
    def __init__(self) -> None:    
        self.class_nbr_dict ={}
        self.df = pd.read_csv('Spring 2023 Schedule.csv')

        self.extractingFromDataset()

    def extractingFromDataset(self):
        # Extract the unique values of "Class nbr" and store them in a list
        self.room_list = self.df['Room'].unique().tolist()

        # Count the frequency of each Class nbr and store it in a dictionary
        class_nbr_freq = self.df['Class nbr'].value_counts().to_dict()

        # Loop through each row in the DataFrame and add the "Class nbr" and "Room" values to the dictionary
        for index, row in self.df.iterrows():
            class_nbr = row['Class nbr']
            room = row['Course title']
            instructor = row['Instructor']
            duration = row['Actual Class Duration']
            self.class_nbr_dict[class_nbr] = {'Room': room, 'Instructor': instructor, 'Actual Class Duration':duration, 'Frequency':class_nbr_freq[class_nbr] }
        

dc=DataCleaning()

print("-------- Statistics--------")
print("Number of classrooms: ",len(dc.room_list))
print("Number of Classes (no. of unique class br) at Habib: ",len(dc.class_nbr_dict))
print("Dictionary storing all data")
print(dc.class_nbr_dict)



