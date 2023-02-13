#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    int m=0;
    int mi=0;
    int mit=0;
    
  for (int a=1;a<n;a++){
      for(int b=2;b<=n;b++){
          if(a==b){
              continue;
            }
          else{
              int x=a&b;
              int y=a|b;
              int z=a^b;
               m=k>x && x>m?x:m;
               mi=k>y && y>mi?y:mi;
               mit=k>z && z>mit?z:mit;
            }
        }
    }
    printf("%d\n",m);
    printf("%d\n",mi);
    printf("%d\n",mit);

}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
