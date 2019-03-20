"""
深度优先遍历，Deepth First Search
原理类似堆栈的结构(先进后出), 添加父&子节点(进堆栈),消除子节点(出堆栈,顺便打印), 当堆栈内元素个数为零, 完成遍历
"""

def dfs(graph, start):
    """
    :param graph: 搜索的图
    :param start: 开始节点
    :return:
    """
    stack = []
    stack.append(start)
    # 通过集合保存遍历过的节点，避免重复
    s = set(start)
    while len(stack)>0:
        node = stack.pop()
        next_nodes = graph[node]
        for n in next_nodes:
            if n not in s:
                stack.append(n)
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
    dfs(graph, 'A')