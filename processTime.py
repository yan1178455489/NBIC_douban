import csv
from datetime import datetime

emap = open('eventmap.txt', 'r')
e_map = {}
for line in emap:
    edata=line.split(' ')
    e_map[edata[0]]=edata[1].replace("\n", "")
emap.close()

location_dict = dict()
with open('events_meta.csv', 'r') as f:
    train_csv = csv.DictReader(f)
    event_count = 0
    locat_count = 0
    wf0 = open('douban/location_event.csv', 'w')
    wf1 = open('douban/time_event.csv', 'w')
    for row in train_csv:
        eid = row['id']
        lid = row['geo']
        time = row['begin_time'].split(' ')
        weekday = datetime.strptime(time[0], '%Y-%m-%d').weekday()
        real_time = int(time[1].split(':')[0])
        date = time[0].split('/')
        if real_time >= 0 and real_time <= 5:
            real_time = 1
        elif real_time >= 6 and real_time <= 11:
            real_time = 2
        elif real_time >= 12 and real_time <= 17:
            real_time = 3
        else:
            real_time = 4
        wp = 4*weekday+real_time
        if lid not in location_dict:
            location_dict[lid] = str(locat_count)
            locat_count += 1
        if eid in e_map:
            wf0.writelines(location_dict[lid] + ',' + e_map[eid] + '\n')
            wf1.writelines(str(wp) + ',' + e_map[eid] + '\n')
    wf0.close()
    wf1.close()
