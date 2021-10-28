#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main(){
    vector<vector<int>> map;
    int V; // Vertex
    int E; // All nums of Edge
    cin >> V >> E;
    V++;
    map.resize(V);
    map[0].push_back(-1);
    int nowV, nowE;
    for(int i=0; i<E; i++){
        cin >> nowV >> nowE;
        map[nowV].push_back(nowE);
        map[nowE].push_back(nowV);
    }

    vector<int> q;
    q.push_back({1});
    vector<bool> visited;
    visited.resize(V,false);
    visited[1]=true;
    while (q.size()!=0){
        int now_node=q[0];
        printf("%d ",now_node);
        q.erase(q.begin());
        for(int i=0; i<map[now_node].size(); i++){
            if(visited[map[now_node][i]] == true)
                continue;
            visited[map[now_node][i]]=true;
            q.push_back({map[now_node][i]});
        }
    }


    return 0; 

}