// Variaveis

#include <stdio.h>

int main() {
    
    // Em C, as variaveis podem ser declaradas sem valor, e atribui-lo em outro momento:
    int numero;
    numero = 5;

    // Sendo que dessa maneira, pode-se declarar mais de uma variavel do mesmo tipo na mesma linha:
    int n1, n2, soma;

    n1 = 10;
    n2 = 50;
    soma = n1 + n2;

    // Ou já declara-la com um valor:
    int numero_2 = 5;

    /* 
    Para ambos os casos, é necessário indicar o tipo de dados que será atribuido. Eles são basicamente:
    int     | Números inteiros                                           | %d ou %i
    float   | Numeros decimais simples (6-7 casas)                       | %f ou %F
    double  | Números decimais copostos (15 casas)                       | %lf
    char    | 1 unico caracter (usar aspas simples)                      | %c
    char [] | tratado como um array, recebe um texto (usar aspas duplas) | %s
    
    Esses formatos são utilizados para definir o espaço em que o valor de uma variavel
    será incluido na hora de printa-lo com o printf()
    
    */

    // Diferente do python, onde podemos usar print(f'Numero: {numero}'), no C devemos escrever essa forma:
    printf("Numero: %d \n", numero);

    // Para imprimir mais de uma variavel no mesmo printf, devemos incluir um formato para cada um:
    printf("Soma: %d + %d = %d", n1,n2,soma);

    // É possivel alterar o valor de uma variavel dps de te-la criado:
    numero_2 = 10;

    // É possivel criar uma cópia de uma variavel atribuindo a ela o valor de uma outra variavel
    int copia_numero_2 = numero_2;
    
    // Há outras maneiras de se declarar mais de uma varival na mesma linha:
    
    // Já informando seus valores:
    int v_1 = 10, v_2 = 15, v_3 = 20;

    // Ou deixando para informa-los posteriormente:
    int v_4, v_5, v_6;

    // Sendo que dessa maneira, podemos atribuir o mesmo valor a todas elas em uma unica linha:
    v_4 = v_5 = v_6 = 25;
    
    return 0;
}