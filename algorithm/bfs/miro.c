#include <stdio.h>

int X,Y;
int sx,sy,ex,ey;
char map[102][102];
int visited[102][102];

struct QUEUE{
	int y,x,time;
};

struct QUEUE queue[10000];
int wp,rp;

void Enqueue(int y, int x,int time){
	queue[wp].y=y;
	queue[wp].x=x;
	queue[wp].time=time;
	wp++;
}

struct QUEUE Dequeue(){
	return queue[rp++];
}

int Empty(){
	return wp == rp;
}

int main(void){
	scanf("%d %d", &X, &Y);
	scanf("%d %d %d %d", &sx, &sy, &ex, &ey);
	for(int i=1; i<=Y; i++){
		scanf("%s", &map[i][1]);
	}
	int dx[]={0,0,1,-1};
	int dy[]={1,-1,0,0};

	Enqueue(sy, sx,0);
	visited[sy][sx]=1;
	while(!Empty()){
		struct QUEUE cur=Dequeue();
		if((cur.y==ey)&&(cur.x==ex)){
			printf("%d",cur.time);
		}
		for(int i=0; i<4;i++){
			int ny=cur.y+dy[i];
			int nx=cur.x+dx[i];
			if((ny<1)||(ny>Y)) continue;
			if((nx<1)||(nx>X)) continue;
			if(visited[ny][nx]==1) continue;
			if(map[ny][nx] != '0') continue;
			Enqueue(ny,nx,cur.time+1);
			visited[ny][nx]=1;
		}
	}
	return -1;
}
