#include <stdio.h>

int main() {

    /* Recebendo entrada de dados*/

    /*Para recebermos uma entrada de dados, começamos declarando uma varivael do tipo que queremos receber*/
    int num;

    /*Utilizamos a função scanf para solicitar algo pro usuario e guardamos na variavel que criamos antes*/
    
    /*Incluimos o timpo de dado entre aspas duplas, da mesma forma que no printf
    e separado por uma virgula o nome da variavel onde queremos guardar o resultado logo após o sinal de &*/
    scanf("%d", &num);

    printf("Voce digitou o numero %d", num);

    return 0;
}