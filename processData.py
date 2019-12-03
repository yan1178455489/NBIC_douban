import csv
from numpy import *

def split_rating_data(data,ratio=0.2):
    train_data=[]
    test_data=[]
    for line in data:
        num=random.random()
        if num < 0.2:
            test_data.append(line)
        else:
            train_data.append(line)
    train_data=array(train_data)
    test_data=array(test_data)
    return train_data,test_data

def process():
    uefile = csv.reader(open('user_events.csv','r'))

    user_map = {}
    event_map = {}
    user_events = []

    ucount = 0
    ecount = 0
    um = open('usermap.txt', 'w')
    em = open('eventmap.txt','w')

    for line in uefile:
        if line[0] == 'uid':
            continue
        if line[0] in user_map:
            if line[1] in event_map:
                uid = user_map[line[0]]
                eid = event_map[line[1]]
                user_events.append([uid,eid,'5'])
            else:
                uid = user_map[line[0]]
                eid = event_map[line[1]] = ecount
                em.writelines(line[1]+' '+str(eid)+'\n')
                ecount += 1
                user_events.append([uid, eid, '5'])
        else:
            if line[1] in event_map:
                uid = user_map[line[0]] = ucount
                um.writelines(line[0] + ' ' + str(uid)+'\n')
                ucount += 1
                eid = event_map[line[1]]
                user_events.append([uid,eid,'5'])
            else:
                uid = user_map[line[0]] = ucount
                um.writelines(line[0] + ' ' + str(uid)+'\n')
                ucount += 1
                eid = event_map[line[1]] = ecount
                em.writelines(line[1] + ' ' + str(eid)+'\n')
                ecount += 1
                user_events.append([uid, eid, '5'])
    # user_events = array(user_events)
    um.close()
    em.close()
    return user_events

data = process()
file = open('u.data','w')
for line in data:
    file.writelines(str(line[0])+' '+str(line[1])+' '+line[2]+'\n')
file.close()

train_data,test_data = split_rating_data(data)
file = open('u1.base','w')
for line in train_data:
    file.writelines(line[0]+' '+line[1]+' '+line[2]+'\n')
file.close()

file = open('u1.test','w')
for line in test_data:
    file.writelines(line[0]+' '+line[1]+' '+line[2]+'\n')
file.close()