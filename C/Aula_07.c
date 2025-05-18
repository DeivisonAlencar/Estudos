#include <stdio.h>

int main() {

    /*Recebendo strings*/
    
    /*Também é possivel receber strings com scanf
    Basta declarar a variavel antes com o numero de caracteres que se espera*/

    char nome[50];
    char nome_completo[50];

    // Uma vez que a varivael nome é na verdade um array de char, não é necessário o simbolo de &
    scanf("%s", nome);

    printf("O nome digitado foi: %s", nome);

    /*Um problema de utilizar scanf para receber strings, é no entanto a impossibilidade de receber espaços.
    Se tentarmos incluir nome e sobrenome, a variavel receberá apenas o texto antes do primeiro espaço*/

    // Para contornar isso utilizamos outra função: fgets:

    /*Ela utiliza o nome da varivael, seu tamanho(igual a declaração)
     e a inscrição "stdin" que indica para pegar a entrada do usuario */
    fgets(nome_completo, 50, stdin);

    printf("O nome completo digitado foi: %s", nome_completo);

    return 0;
}