#include <stdio.h>

    // Função print

int main() {
    
    printf("A função printf, exibe uma mensagem na tela \n");
    printf("Toda linha de execução deve conter ; no final! \n");
    printf("A função de printar texto, funciona com aspas duplas \n");
    printf("O escape contra_barra+n serve para pular uma linha, uma vez que o C não faz isso automaticamente \n");
    printf("Para criar uma linha em branco entre uma mensagem e outra, utiliza-se dois contra_barra+n \n\n");
    printf("Para criar um espaço em branco lateral \t");
    printf("Utilizamos o contra_barra+t \n");
    printf("Se precisarmos de uma contra_barra no nosso texto, utilizar \\ retornará apenas 1 contra_barra \n");
    printf("Já se quisermos que uma aspas duplas apareça no noss texto devemos incluir \"Dessa forma\". ");
    
    return 0;
}