from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.array = []
        self.roots = {}
    
    def addEdge(self,u,v,w): 
        if not self.array:
            self.array.append([u,v,w])
        else:
            det = True
            for i in range(len(self.array)):
                if self.array[i][2] > w:
                    self.array.insert(i,[u,v,w])
                    det = False
                    break
            if det:
                self.array.append([u,v,w])

    def K_helper(self,final):
        
        pivot = self.array[0]

        while self.roots[pivot[0]] != None and self.roots[pivot[1]] != None and self.roots[pivot[0]] == self.roots[pivot[1]]:
            self.array.pop(0)
            pivot = self.array[0]
        
        self.array.remove(pivot)
        
        small = min(pivot[0],pivot[1])
        large = max(pivot[0],pivot[1])

        if self.roots[large] == None and self.roots[small] == None:
            self.roots[large] , self.roots[small] = small , small

        elif self.roots[large] == None and self.roots[small] != None:
            self.roots[large] = self.roots[small]          

        else:
            for i in range(self.V):
                if i != large and self.roots[i] == self.roots[large]:
                    self.roots[i] = small
            self.roots[large] , self.roots[small] = small , small

        final[str(str(pivot[0])+"-"+str(pivot[1]))] = pivot[2]

        if len(final) != self.V-1:
            self.K_helper(final)
        
        return final
    
    def Kruskal(self):
        for j in range(self.V): 
            self.roots[j] = None
        final = {}
        return self.K_helper(final)
    
    def Dijkstra(self, s):
        visited = [s]
        final = dict()
        parent = dict()
        temp = []
        for i in range(self.V):
            final[i] = None
            parent[i] = None
        final[s] = 0
        for i in range(self.V-1):
            for j in range(len(self.graph[visited[-1]])):
                if self.graph[visited[-1]][j] != 0 and j not in visited:
                    
                    val = self.graph[visited[-1]][j] + final[visited[-1]]
                    
                    if not final[j]:
                        final[j] = val
                        parent[j] = visited[-1]
                    else:
                        if val < final[j]:
                            final[j] = val
                            parent[j] = visited[-1]
                    
                    if not temp:
                        temp.append([j,final[j]])
                    else:
                        det = True
                        for k in range(len(temp)):
                            if temp[k][1] > final[j]:
                                temp.insert(k,[j,final[j]])
                                det = False
                                break
                        if det:
                            temp.append([j,final[j]])
            
            while temp[0][0] in visited:
                temp.pop(0)
            visited.append(temp[0][0])
            temp.pop(0)
        
        last = {}
        for i in range(self.V):
            last[str(i)] = final[i]

        return last
    
# 參考資料：

# https://ithelp.ithome.com.tw/articles/10209593

# http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html

# http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html

# https://www.youtube.com/watch?v=9wV1VxlfBlI

# https://www.youtube.com/watch?v=pVfj6mxhdMw&t

# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

# https://www.youtube.com/watch?v=71UQH7Pr9kU

# http://alrightchiu.github.io/SecondRound/minimum-spanning-treeintrojian-jie.html
