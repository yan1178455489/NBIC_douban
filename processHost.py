import csv
from numpy import *

def process():
    ehfile = csv.reader(open('events_host.csv','r'))
    eh_map = {}
    event_map = {}
    host_map = {}
    hcount = 0
    em = open('eventmap.txt','r')
    for line in em:
        eid,index = line.split(' ')
        index = index.strip('\n')
        event_map[eid] = index
    for line in ehfile:
        if line[0]=='eid':
            continue
        if line[0] in event_map:
            if line[1] in host_map:
                eh_map[event_map[line[0]]] = host_map[line[1]]
            else:
                eh_map[event_map[line[0]]] = host_map[line[1]] = hcount
                hcount += 1

    return eh_map

eh_map = process()
file = open('events_host.txt','w')
for key in eh_map:
    file.writelines(str(key)+' '+str(eh_map[key])+'\n')
file.close()