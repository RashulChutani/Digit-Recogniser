import csv

#test

with open('train.csv', 'rb') as f:
    reader = csv.reader(f)
    features_train = list(reader)
del features_train[0]
labels_train = list()

for i in range(0,len(features_train)):
    for j in range(0,len(features_train[0])):
        features_train[i][j] = float(features_train[i][j])
        
for i in range(0,len(features_train)):
    labels_train.append(features_train[i][0])
    del features_train[i][0]

with open('test.csv', 'rb') as k:
    reader = csv.reader(k)
    features_test = list(reader)
del features_test[0]

for i in range(0,len(features_test)):
    for j in range(0,len(features_test[0])):
        features_test[i][j] = float(features_test[i][j])
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(features_train,labels_train)
result = list()
pred = features_test[0:999]
for i in range(0,28):
     features = features_test[i*1000:(i+1)*1000]
     #print features
     pred = clf.predict(features)
     result.extend(pred)

print len(result)

#print features_test;
csvData = list()
final = list()
csvData.append("ImageId")
csvData.append("Label")
final.append(csvData)
for i in range(0,len(result)):
    csvData = []
    csvData.append(str(i+1))
    csvData.append(str(result[i]))
    final.append(csvData)

print final
                   
with open('sample_submission.csv', 'w') as csvFile:
    csvwriter = csv.writer(csvFile)
    csvwriter.writerows(final)
    
