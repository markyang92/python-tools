#include <stdio.h>
char str[100000 + 10];
int Solve(){
    int count=0,sum=0;
    for(int i=0; str[i]; i++){
        if(str[i]=='('){
            count++;
        } else {
            count--;
            if (str[i-1] == '('){
                sum+=count;
            } else {
                sum++;
            }
        }
    }
    return sum;
}

void InputData(){
    scanf("%s", str);
}

int main(void){
    int ans;
    InputData();
    ans=Solve();
    printf("%d\n",ans);
    return 0;
}