/*
Represent a given graph using adjacency matrix / list to perform DFS and using list to perform BFS.
Use the map of the area around the college as the graph.Identify the prominent land marks as nodes
and perform DFS and BFS on that
*/
#include <bits/stdc++.h>
using namespace std;

class DFSGraph
{
    int vertex, edge;
    int **adj;

public:
    DFSGraph(int v, int e);
    void addEdge(int start, int e);
    void DFS(int start, vector<bool> &visited);
};

class BFSGraph
{
    int vertexNo;
    list<int>* adjList;
    bool* visited;
    public:
        BFSGraph(int vertex);
        void addEdge(int src, int dest);
        void BFS(int start);
};


BFSGraph::BFSGraph(int vertex){
    vertexNo = vertex;
    adjList = new list<int>[vertex];
}

void BFSGraph::addEdge(int src, int dest){
    adjList[src].push_back(dest);
    adjList[dest].push_back(src);
}

void BFSGraph::BFS(int start){
    visited = new bool[vertexNo];
    for(int i = 0; i<vertexNo;i++)
        visited[i] = false;

    list<int> queue;

    visited[start] = true;
    queue.push_back(start);

    list<int>::iterator i;

    while (!queue.empty()){
        int currentVertex = queue.front();
        cout<<" Visited "<<currentVertex;
        queue.pop_front();

        for(i = adjList[currentVertex].begin(); i!=adjList[currentVertex].end();++i){
            int adjVertex = *i;
            if(!visited[adjVertex]){
                visited[adjVertex] = true;
                queue.push_back(adjVertex);
            }
        }
    }
}

DFSGraph::DFSGraph(int v, int e)
{
    this->vertex = v;
    this->edge = e;
    adj = new int *[v];
    for (int i = 0; i < v; i++)
    {
        adj[i] = new int[v];
        for (int j = 0; j < v; j++)
            adj[i][j] = 0;
    }
}

void DFSGraph::addEdge(int start, int e)
{
    // if bidirectional edge
    adj[start][e] = 1;
    adj[e][start] = 1;
}

void DFSGraph::DFS(int start, vector<bool> &visited)
{
    cout << start << " "; // Print current node

    visited[start] = true;

    for (int i = 0; i < vertex; i++)
    {
        if(adj[start][i] == 1 && (!visited[i]))
            DFS(i, visited);
    }
}

int main()
{
    int choice;
    int v = 5, e = 4;
    vector<bool> visited(v, false);

    // Create the graph
    DFSGraph G(v, e);
    G.addEdge(0, 3);
    G.addEdge(3, 2);
    G.addEdge(2, 3);
    G.addEdge(1, 4);
    // Perform DFS
    G.DFS(0, visited);
    
    BFSGraph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.BFS(2);
    
    return 0;
}