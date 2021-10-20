#include <stdio.h>
int N;
struct POLE{
    int L,H
};
struct POLE pole[1000 + 10];
void InputData(){
    scanf("%d", &N);
    for (int i=0; i<N; i++){
        scanf("%d %d",&pole[i].L, &pole[i].H);
    }
}
void sort(int s, int e){
    for (int i=s; i<e; i++){
        for (int j=i+1;j<=e;j++){
            if(pole[i].L>pole[j].L){
                struct POLE temp=pole[i];
                pole[i]=pole[j];
                pole[j]=temp;
            }
        }
    }
}
int Solve(){
    int area=0, preL,preH;
    int maxindex=0;
    sort(0,N-1);
    for(int i=1;i<N;i++){
        if (pole[maxindex].H < pole[i].H){
            maxindex=i;
        }
    }
    preL=pole[0].L;
    preH=pole[0].H;
    for(int i=1;i<=maxindex;i++){
        if (preH<=pole[i].H){
            area+=(pole[i].L-preL)*preH;
            preL=pole[i].L;
            preH=pole[i].H;
        }
    }
    area+=pole[maxindex].H;
    preL=pole[N-1].L;
    preH=pole[N-1].H;
    for(int i=N-2;i>=maxindex;i--){
        if(preH<=pole[i].H){
            area+=(preL-pole[i].L)*preH;
            preL=pole[i].L;
            preH=pole[i].H;
        }
    }
    return area;
}

int main(){
    int ans;
    InputData();
    ans=Solve();
    printf("%d\n",ans);
    return 0;
}
