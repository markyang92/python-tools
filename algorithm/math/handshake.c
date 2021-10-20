#include <stdio.h>
int R,C;
char map[50+5][50+5];

void InputData(){
    scanf("%d %d", &R, &C);
    for (int i=0; i<R; i++){
        scanf("%s",map[i]);
    }
}

int handshake(int r,int c){
    int dr[]={-1,-1,-1,0,1,1,1,0};
    int dc[]={-1,0,1,1,1,0,-1,-1};
    int count=0;
    for(int i=0;i<8;i++){
        int nr=r+dr[i];
        int nc=c+dc[i];
        if ((nr<0)||(nr>=R)||(nc<0)||(nc>=C)) continue;
        if (map[nr][nc]=='o') count++;
    }
    return count;
}

int Solve(){
    int count=0;
    for (int i=0;i<R;i++){
        for (int j=0; j<C;j++){
            if(map[i][j]!='o') continue;
            count+=handshake(i,j);
        }
    }
    count /= 2;

    int max=0;
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(map[i][j]!='.') continue;
            int temp=handshake(i,j);
            if (max<temp) max=temp;
        }
    }
    return count+max;
}

int main(void){
    int ans;
    InputData();
    ans=Solve();
    printf("%d\n", ans);
    return 0;
}