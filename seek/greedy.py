# -*- coding:utf-8 -*-

"""
贪婪算法，在对问题求解时，总是做出在当前看来是最好的选择。实现步骤：
（1）找到局部最优解
（2）到一个新的局部，重复上一步
"""


# 要覆盖的州
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
# 广播台清单
stations = dict()
stations['KONE'] = {'id', 'nv', 'ut'}
stations['KTWO'] = {'wa', 'id', 'mt'}
stations['KTHREE'] = {'or', 'nv', 'ca'}
stations['KFOUR'] = {'nv', 'ut'}
stations['KFIVE'] = {'ca', 'az'}


def greedy(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = set()
        station_covered = set()
        for k, v in stations.items():
            if len(v & states_needed) > len(station_covered):
                station_covered = v
                best_station = k
        states_needed -= station_covered
        final_stations.add(best_station)

    return final_stations


final_stations = greedy(states_needed, stations)

print(final_stations)