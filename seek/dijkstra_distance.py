"""
迪杰斯特拉(Dijkstra)算法
典型最短路径算法,用于计算一个节点到其他节点的最短路径
利用广度优先算法搜索
"""


# heapq 模块提供了堆排序算法的实现, 堆的值可以是元组类型，可以实现对带权值的元素进行排序
import heapq
import math


def djskstra(graph, start):
    # 创建堆
    hqueue = []
    # 添加带权重的值入堆
    heapq.heappush(hqueue, (0, start))
    # 创建集合记录已经走过的点
    seen = set(start)
    # 记录当前点的前一个节点
    parent = {}
    # 记录从起始点到当前点的距离
    distance = {start:0}

    while len(hqueue) > 0:
        # 将距离最小的节点从堆中
        dist, node = heapq.heappop(hqueue)
        seen.add(node)
        for i in graph[node].keys():
            if i not in seen:
                # 判断当前节点距离是否比已记录的距离小（如没有记录默认为正无穷），小则加入堆中，并替换距离表
                td = dist + graph[node][i]
                bd = distance[i] if distance.get(i) else math.inf
                if td < bd:
                    heapq.heappush(hqueue, (dist+graph[node][i], i))
                    parent[i] = node
                    distance[i] = dist + graph[node][i]
    return parent, distance


if __name__ == "__main__":
    # 用键值对表示相连点
    graph = {
        "A": {"B": 5, "C": 1},
        "B": {"A": 5, "C": 2, "D": 1},
        "C": {"A": 1, "B": 2, "D": 4, "E": 8},
        "D": {"B": 1, "C": 4, "E": 3, "F": 6},
        "E": {"C": 7, "D": 3},
        "F": {"D": 6},
    }
    parent, distance = djskstra(graph, 'A')
    print(parent)
    print(distance)