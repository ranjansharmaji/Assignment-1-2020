#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_blas.h>

int main()
{
  double data[]={1.0,0.67,0.33,
	       0.45,1.0,0.55,
	       0.67,0.33,1.0};
  
  gsl_matrix_view A=gsl_matrix_view_array(data,3,3);

  gsl_permutation *p=gsl_permutation_alloc(3);
  int s;

  gsl_linalg_LU_decomp(&A.matrix,p,&s);

  gsl_matrix_fprintf(stdout,&A.matrix,"%g");

  
  //refrence lu decomposition in gsl documentation
