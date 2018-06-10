#Parser for raw EEG data

import csv
from random import shuffle



#For processing raw EEG file into to 5 channel + Event csv file
f = open("push.csv") #raw eeg filename
index = 0
x = [['AF3', 'T7', 'Pz', 'T8', 'AF4','Event']]
for row in csv.reader(f):
    if index == 0:
        index+=1
        continue
    x.append(list(map(float,row[2:7]+[1]))) #Change event 0 or 1, etc
x_new = x[:15001]
with open('parseddata_push.csv', 'w') as myfile: #Name of file you want to write into
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows(x_new)
myfile.close()


#For updating a file with new values (Merging two files)
with open('parseddata.csv','a') as myfile: #Name of file containing data you want to merge new file to
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerows(x_new[1:])
myfile.close()



#For shuffling rows of a preprocessed csv file
#with open('sum_parseddata_neutral.csv', 'r') as myfile:
 # reader = csv.reader(myfile)
  #your_list = list(reader)
  #t = your_list[1:]
  #shuffle(t)
  #x_shuff = [['AF3', 'T7', 'Pz', 'T8', 'AF4','Event']] + t
#myfile.close()
#with open('parseddatashuffled.csv', 'w') as myfile: #Name of file you want to write into
 #   wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
  #  wr.writerows(x_shuff)
#myfile.close()

def truncate(f, n):
#Truncates/pads a float f to n decimal places without rounding
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return float('.'.join([i, (d+'0'*n)[:n]]))

with open('parsed_neutral_data.csv', 'r') as myfile:
  reader = csv.reader(myfile)
  your_list = list(reader)
  your_list = your_list[1:]

  lst = []
  for i in your_list:
      lst.append(list(map(float,i[:5])))

#NEUTRAL


for i in range(len(lst)):
    for j in range(5):
        lst[i][j] = round(truncate(lst[i][j],6) * 10**6)

lst2 = []
for i in range(1,151):
    lst2.append(lst[(i-1)*100:i*100])

n_list = []
for i in lst2:
    n_list.append([i,0])


#PUSH

with open('parsed_push_data.csv', 'r') as myfile:
  reader = csv.reader(myfile)
  your_list = list(reader)
  your_list = your_list[1:]

  your_list2 = []
  for i in your_list:
      your_list2.append(list(map(float,i[:5])))

  plst = your_list2

for i in range(len(plst)):
    for j in range(5):
        plst[i][j] = round(truncate(plst[i][j],6) * 10**6)

plst2 = []
for t in range(1,151):
    plst2.append(plst[(t-1)*100:t*100])

p_list = []
for t in plst2:
    p_list.append([t,1])

#making train test splits

n_list_train = n_list[:120]
n_list_test = n_list[120:]

p_list_train = p_list[:120]
p_list_test = p_list[120:]

list_train = n_list_train + p_list_train
list_test = n_list_test + p_list_test

shuffle(list_test)
shuffle(list_train)


#Making np arrays

import numpy as np

X_train_list = []
Y_train_list = []
X_test_list = []
Y_test_list = []

for j in list_train:
    X_train_list.append(j[0])
    Y_train_list.append(j[1])

for j in list_test:
    X_test_list.append(j[0])
    Y_test_list.append(j[1])

X_train = np.empty(len(X_train_list), dtype = object)
Y_train = np.empty(len(Y_train_list), dtype = object)
X_test = np.empty(len(X_test_list), dtype = object)
Y_test = np.empty(len(Y_test_list), dtype = object)

X_train[:] = X_train_list[:]
Y_train[:] = Y_train_list[:]
X_test[:] = X_test_list[:]
Y_test[:] = Y_test_list[:]

np.save('X_train.npy', X_train)
np.save('Y_train.npy', Y_train)
np.save('X_test.npy', X_test)
np.save('Y_test.npy', Y_test)

'''
f = open("parseddata.csv")
t = x_new[1:]
shuffle(t)
x_shuff = [['AF3', 'T7', 'Pz', 'T8', 'AF4','Event']] + t


with open('parseddata.csv','a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(x_new[1:])
myfile.close()




  index = 0
  for i in range(1,len(x_shuff)):
	x_shuff[i] = list(map(float,x_shuff[i]))


with open('parseddata_neutral.csv', 'r') as myfile:
  reader = csv.reader(myfile)
  new = list(reader)
  for i in range(1,len(new)):
      new[i] = list(map(float,new[i]))

with open('parseddata_neutral2.csv', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows(new)

'''
