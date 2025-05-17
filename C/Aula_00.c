#include <stdio.h>

int main() {

    // Estrutura básica

    /*
    
        Em C, as funções de saída ficam na biblioteca <stdio.h>
        por isso devemos importa-la logo no inicio do código através do #include
    
    */

    
    // Já o código deve ser escrito no "entrepoint", a estrutura chamada main(){}
    
    printf("Hello World!\n");
    
    /* Por ultimo, ddamos um "return 0", pois em C, caso tenhamos algum erro é nos retonado seu número
    mas se tudo ocorrer bem, queremos que seja retornado 0*/
    return 0;
}