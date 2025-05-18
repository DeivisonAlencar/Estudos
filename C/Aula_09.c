#include <stdio.h>

int main(){

    /*Condições com switch case*/

    int posicao = 2;
    
    /*Para validarmos mais de uma hiposete, sem precisar criar varios ifs, podemos utilizar o switch case*/

    // Cada case precisa contar com um break, para que o código se encerre caso aquela hipotese seja verdadeira
    
    /*Ao final, temos a declaração default, para quando nenhuma das hiposetes for verdadeira,
    essa declaração não precisa de break*/
    switch (posicao){
        case 1:
            printf("Medalha de Ouro\n");
            break;
        case 2:
            printf("Medalha de Prata\n");
            break;
        case 3:
            printf("Medalha de Bronze\n");
            break;
        default:
            printf("Não entrou no pódio\n");
    }


    return 0;
}