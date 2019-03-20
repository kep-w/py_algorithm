"""
广度优先遍历，Breadth First Search
原理类似队列的结构(先进先出), 消除父节点(出队列,顺便打印), 添加子节点(进队列),当队列内元素个数为零, 完成遍历
"""

def bfs(graph, start):
    """
    :param graph: 搜索的图
    :param start: 开始节点
    :return:
    """
    queue = []
    queue.append(start)
    s = set(start)
    while len(queue)>0:
        node = queue.pop(0)
        next_nodes = graph[node]
        for n in next_nodes:
            if n not in s:
                queue.append(n)
                s.add(n)
        print(node)


if __name__ == "__main__":
    # 用键值对表示相连点
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "E"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"],
    }
    bfs(graph, 'A')