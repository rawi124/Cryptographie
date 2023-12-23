#include <stdio.h>
#include <gmp.h>
#include "modexp.h"

#define P_RSA  "115792089237316195423570985008687907853269984665640564039457584007913129640233"
#define Q_RSA "115792089237316195423570985008687907853269984665640564039457584007913129640237"
#define E_RSA "2953368932708806040079805629905253705968323820573068368533655818096373816879109354558131974193128687083690589285456933635781170289436955716741611815288627"
#define D_RSA "7139332137211430074462967288742749785777233770320015824474232828917641887182993711699924646585050322197822989620144868160814670144728736961704230654774363"

int main(int argc , char *argv[])
{
  mpz_t n,p,q,d,x,y;

  if (argc < 1){
    printf("usage: %s <message>", argv[0]);
    return 1;
  }
  
  mpz_init(n);
  mpz_init(p);
  mpz_init(q);
  mpz_init(d);

  mpz_set_str(p,P_RSA,10);
  mpz_set_str(q,Q_RSA,10);
  mpz_set_str(d,D_RSA,10);
  mpz_mul(n,p,q);
  
  mpz_init(x);
  mpz_init(y);

  mpz_set_str(x, argv[1], 10);
  modexp(y,x,d,n);

  gmp_printf("%Zd\n", y);
  return 0;
}
