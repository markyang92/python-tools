#include <iostream>
#include <vector>

using namespace std;
int N=0;
int cnt=0;
vector<int> map;

bool check(int idx, int value){
    for(int i=0;i<idx;i++){
        if(map[i]==value){
            return false;
        }
    }

    for(int i=0;i<idx;i++){
        int std=map[i];
        if ((std+(idx-i))==value){
            return false;
        }
        if ((std-(idx-i))==value){
            return false;
        }
    }
    return true;
}

void permute(int idx, int value){
    if(idx == N-1){
        cnt++;
        return;
    }
    map[idx]=value;
    for(int i=0;i<N;i++){
        if(check(idx+1,i)){
            permute(idx+1,i);
        }
    }
}

void solve(){
    for(int i=0;i<N;i++){
        permute(0,i);
    }
}

int main(){
    scanf("%d",&N);
    map.resize(N);
    solve();
    printf("%d",cnt);

    return 0;
}