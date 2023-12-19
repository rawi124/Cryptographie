#include <stdio.h>
#include <string.h>

int pin[16] = {7,3,8,0,1,9,7,6,1,5,7,8,4,4,2,0};
int perm[16] = {4,12,8,1,0,15,9,2,3,14,13,5,7,6,10,11};

int main(int argc, char * argv[])
{
  if ( argc < 1 ){
    printf("usage: %s code\n",argv[0]);
    return -1;
  }
  if  (strlen(argv[1])!=16){
    printf("le code doit avoir 16 chiffres\n");
      return -1;
  }
  int i,j,k=1;
  for (i=0; i<16; i++){
    for (j=0; j<5000000;j++)
      k = k*84561235; 
    if (argv[1][perm[i]]!=(pin[perm[i]]+'0')){
      return -1;
    }
  }
  return 0;   

}

