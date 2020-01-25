
import pandas as pd
import numpy as np
import speech_recognition as sr


# Importing the dataset
path= 'Speech_Recognition_Dataset.csv'
dataset = pd.read_csv(path, header=0)
X = dataset.iloc[:, 1].values
Y = dataset.iloc[:, 2].values
#print(dataset)
        
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    text = r.recognize_google(audio)

for row in X:
   if(text.format()==row):
       search=dataset.loc[dataset['speech_input']==row]
       final=search.iloc[:, 2].values
       print (','.join(final))
       break
else:
    print(" you said :{} ".format(text))       