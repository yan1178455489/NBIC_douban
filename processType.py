import csv

typename_map={}
typename_map['music']='0'
typename_map['course']='1'
typename_map['travel']='2'
typename_map['drama']='3'
typename_map['film']='4'
typename_map['exhibition']='5'
typename_map['salon']='6'
typename_map['party']='7'
typename_map['kids']='8'
typename_map['commonweal']='9'
typename_map['sports']='10'
typename_map['competition']='11'
typename_map['others']='12'

emap = open('eventmap.txt', 'r')
e_map = {}
for line in emap:
    edata=line.split(' ')
    e_map[edata[0]]=edata[1].replace("\n", "")
emap.close()

event_file = csv.reader(open('events_meta.csv','r'))
eid_type = {}
flag = 1
for line in event_file:
    if flag == 1:
        flag = 0
        continue
    if line[0] in e_map:
        eid_type[e_map[line[0]]] = typename_map[line[1]]

et_file = open('eid_type.txt', 'w')
for key,value in eid_type.items():
    et_file.writelines(key+' ' + value + '\n')
et_file.close()
