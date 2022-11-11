import pandas as pd
#import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("/mnt/d/OneDrive/Arquivos TCC/dataset_treino_rspamd.csv")

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state = 101)
X, y = smote.fit_resample(df[['xforce', 'idade', 'resolveip', 'httpstatus', 'textonlp', 'anexo']], df['status'])

df_example = df[['xforce', 'idade', 'resolveip', 'httpstatus', 'textonlp', 'anexo', 'status']]

#Creating a new Oversampling Data Frame
df_oversampler = pd.DataFrame(X, columns = ['xforce', 'idade', 'resolveip', 'httpstatus', 'textonlp', 'anexo'])



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_example[['xforce', 'idade', 'resolveip', 'httpstatus', 'textonlp', 'anexo']], df['status'], test_size = 0.01, stratify = df['status'], random_state = 101)

smote = SMOTE(random_state = 101)
X_oversample, y_oversample = smote.fit_resample(X_train, y_train)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

classifier = DecisionTreeClassifier()
classifier.fit(X_oversample, y_oversample)
y_pred = classifier.predict(X_test)

print(df_oversampler.shape)
#print(df_oversampler.head)
#
#print(classification_report(y_test, classifier.predict(X_test)))
#print(confusion_matrix(y_test, y_pred))

####################################

filename = '/mnt/d/OneDrive/Arquivos TCC/pickle_rspamd.sav'
pickle.dump(classifier, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)