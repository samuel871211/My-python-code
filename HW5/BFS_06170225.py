from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):     
        q1 = self.graph[s]
        q2 = [s]
        while len(q1) != 0:
            q2.append(q1[0])
            q1.pop(0)
            for i in range(len(self.graph[q2[-1]])):
                if self.graph[q2[-1]][i] not in q1 and self.graph[q2[-1]][i] not in q2:
                    q1.append(self.graph[q2[-1]][i])
        return q2
    
    def DFS(self,s):
        s1 = self.graph[s]
        s2 = [s]
        while len(s1) != 0:
            s2.append(s1[-1])
            s1.pop(-1)
            for i in range(len(self.graph[s2[-1]])):
                if self.graph[s2[-1]][i] not in s1 and self.graph[s2[-1]][i] not in s2:
                    s1.append(self.graph[s2[-1]][i])
        return s2

# 參考資料：

# https://www.programiz.com/dsa/graph-bfs

# https://www.javatpoint.com/breadth-first-search-algorithm

# http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

# https://www.javatpoint.com/breadth-first-search-algorithm

# https://www.accelebrate.com/blog/using-defaultdict-python

# https://ithelp.ithome.com.tw/articles/10193094

# http://szteven3.logdown.com/posts/205697-algorithm-notes-time-complexity
