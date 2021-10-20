#include <stdio.h>

int R;

void InputData(){
    scanf("%d",&R);
}
int Solve(){
    int count=0;
    for(int a=1; a<= R; a++){
        for(int b=1;b<=R;b++){
            if(a*a+b*b<=R*R){
                count++;
            }
        }
    }
    return count*4;
}

int main(void){
    int ans;
    InputData();
    ans=Solve();
    printf("%d\n",ans);
    return 0;
}