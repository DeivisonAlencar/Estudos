#include <stdio.h>

int main(){

    /*Condicionais*/

    int num = 10;
    int posicao = 2;

    /*A declaração if serve basicamente para validar se uma determinada condição é verdadeira*/

    /*Nesse caso estamos validando se o valor contido na variavel num é maior do que 5m
    e a função printf só será executada se a condição for verdadeira*/
    if (num > 5) {
        printf("O número é maior que 5\n");
    }
    

    /*Podemos validar hipoteses diferentes com (else if) e (else) */

    if (posicao == 1) {
        printf("Medalha de ouro\n");
    }
    else if (posicao == 2) {
        printf("Medalha de Prata\n");
    }
    else if (posicao == 3) {
        printf("Medalha de Bronze\n");
    }
    else {
        printf("Não entrou no pódio\n");
    }



    return 0;
}