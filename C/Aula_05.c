#include <stdio.h>

int main() {

    // Operadores matematicos:

    /* Seguindo o padrão, os operadores em C são:
    
    +   | Adição       | 5 + 2 | 7
    -   | Subtração    | 5 - 2 | 3
    *   | Mutiplicação | 5 * 2 | 10
    /   | Divisão      | 5 / 2 | 2
    %   | Resto da div | 5 % 2 | 1
    
    */
    
    int n1, n2, adi, sub, mut, div1, mod;
    double div2, div3;

    n1 = 5;
    n2 = 2;

    adi = n1 + n2;
    sub = n1 - n2;
    mut = n1 * n2;
    mod = n1 % n2;


    /*Sempre que dividimos um número inteiro por outro, a linguagem C nos retorna também um número inteiro.
    independente se declaramos a variavel que receberá o resultado como inteiro ou decimal */
    div1 = n1 / n2;
    div2 = n1 / n2;

    /*Para que o resultado seja gravado como decimal devemos transformar o dividendo em decimal atraves de casting*/
    div3 = (double) n1 / n2;
    return 0;
}