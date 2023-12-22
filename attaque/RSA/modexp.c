#include "modexp.h"
#include <stdio.h>



static void montg_red(mpz_t t, mpz_t T, mpz_t n, int r, mpz_t n1){
  mpz_t temp1, temp2;

  mpz_inits(temp1, temp2,NULL);

  mpz_fdiv_r_2exp(temp1,T,r);
  mpz_mul(temp1,temp1,n1);
  mpz_fdiv_r_2exp(temp1,temp1,r);
  mpz_mul(temp2,temp1,n);
  mpz_add(temp1,T,temp2);
  mpz_fdiv_q_2exp(t,temp1,r);
  if (mpz_cmp(t,n) > 0){
    mpz_sub(t,t,n);
    //extra operation factice pour rendre
    //l'attaque temporelle plus facile
    mpz_mul(temp2,t,n);
  }
  mpz_clears(temp1,temp2,NULL);
}

void modexp(mpz_t y, mpz_t x, mpz_t k, mpz_t n)
{
  int r = mpz_sizeinbase(n,2)+1;
  int len =  mpz_sizeinbase(k,2);
  mpz_t R,n1,X,Y,neg;

  mpz_init_set_ui(R,1);
  mpz_init(n1);
  mpz_init(neg);
  mpz_neg(neg,n);
  mpz_mul_2exp(R,R,r);
  
  mpz_invert(n1,neg,R);
  
  mpz_inits(X,Y,NULL);
  mpz_mul(X,x,R);
  mpz_mod(X,X,n);
  mpz_set(Y,R);
  mpz_mod(Y,Y,n);
  
  for (int i=len-1; i>=0; i--){
    mpz_mul(Y,Y,Y);
    montg_red(Y,Y,n,r,n1);
    if (mpz_tstbit(k,i)){
      mpz_mul(Y,Y,X);
      montg_red(Y,Y,n,r,n1);
    }
  }  
  montg_red(y,Y,n,r,n1);
  mpz_clears(R,n1,X,Y,neg,NULL);
}
