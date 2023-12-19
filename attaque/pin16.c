#include <stdio.h>
#include <string.h>

int pin[16] = {5,0,0,2,1,4,9,6,3,1,5,8,4,9,9,0};

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
    if (argv[1][i]!=(pin[i]+'0')){
      return -1;
    }
  }
  return 0;   

}

