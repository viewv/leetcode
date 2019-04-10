#include<stdio.h>
int n;  //n个出租站

int main(){
    scanf("%d",&n); 
    int **r=new int*[n+1];    //多申请了一组空间，解决了下标i和第i个数值不同的问题 
    for(int i=0;i<n+1;i++){
        r[i]=new int[n+1];
    }
    
    for(int i=1;i<n+1;i++){  //有选择性地输入，用不着的都空着 
        for(int j=i+1;j<n+1;j++)
            scanf("%d",&r[i][j]);
    }
    for(int i=1;i<n+1;i++)  //例如：第3站到第三站的价钱为0（数组打底，首先从某一站走到它自己）
        r[i][i]=0;
    
    for(int l=2;l<=n;l++){  //从两个出租站开始，逐步计算每多个出租站之间的最优解
        for(int i=1;i<=n-l+1;i++){
            int j=i+l-1;
            for(int k=i+1;k<j;k++){
                int temp=r[i][k]+r[k][j];
                if(temp<r[i][j])
                    r[i][j]=temp; 
            }   
        }
    }
    printf("%d",r[1][n]);
    return 0;
}