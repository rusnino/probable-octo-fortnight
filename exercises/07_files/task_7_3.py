# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt таким образом чтобы:
- считывались строки, в которых указаны MAC-адреса
- каждая строка, где есть MAC-адрес, должна обрабатываться таким образом,
  чтобы на стандартный поток вывода была выведена таблица вида:

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
template = " {0:<7}{1:<17}{2:<}"
count = 0
table = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if count >= 6:
        	table.append(line.rstrip().split())
        count += 1

# print(table)
# for line in table:
    # print(template.format(line[0], line[1], line[3]))
for vlan, mac, _, intf in table:
	print(vlan, mac, intf)