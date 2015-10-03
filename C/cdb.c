/* * * * * * * * * * * * * * * * * * * * * * * * * * * *
* Author: Eduardo Frazão ( http://github.com/fr4z40 )  *
* * * * * * * * * * * * * * * * * * * * * * * * * * * */
/*   Trabalho de Avaliação                             *
*                                                      *
*   Diciplina: Organização de Computadores.            *
*                                                      *
*   Conversão de Bases Numericas                       *
* * * * * * * * * * * * * * * * * * * * * * * * * * * */

#include <stdio.h>
#include <stdlib.h>

///////////////////////////////////////////////////////////////////////////////////////////////


/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Decimal para Binario                     *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
void dec_to_bin()
  {
    int a;
    char b[8];

    printf ("Valor de Entrada: ");
    scanf("%d",&a);
    itoa(a,b,2);
    printf("Convertido em binario: %s",b);
  }



/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Binario para Decimal                     *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
int bin_to_dec(int bin)
  {
    int total = 0;
    int potenc = 1;
    while(bin > 0)
      {
        total += bin % 10 * potenc;
        bin = bin / 10;
        potenc = potenc * 2;
      }
    return total;
  }

void bin_f_dec()
  {
    int vlr;
    printf("\n\n");
    printf ("Valor de Entrada: ");
    scanf("%d",&vlr);
    printf("\n\n");
    printf ("Convertido em decimal: %d", bin_to_dec(vlr));
  }



/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Decimal Para hexadecimal                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
void dec_to_hex()
  {
    int vlr;
    printf("\n\n");
    printf ("Valor de Entrada: ");
    scanf("%d",&vlr);
    printf("\n\n");
    printf ("Convertido em hexadecimal: %X", vlr);
  }



/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Hexadecimal para Decimal                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
void hex_to_dec()
  {
    printf("\n\n");
    int vlr;
    printf ("Valor de Entrada: ");
    scanf("%X",&vlr);
    printf("\n\n");
    printf ("Convertido em decimal: %d", vlr);
  }



/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Binario para Hexa                        *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
void bin_to_hex()
  {
    printf("\n\n");
    int vlr;
    printf ("Valor de Entrada: ");
    scanf("%d",&vlr);
    printf("\n\n");
    printf ("Convertido em hexadecimal: %X", bin_to_dec(vlr));
  }



/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*                         Hexadecimal Para Binario                 *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */
void hex_to_bin()
  {
    printf("\n\n");
    int vlr;
    char b[8];
    printf ("Valor de Entrada: ");
    scanf("%x",&vlr);
    vlr = ("%d",vlr);
    itoa(vlr,b,2);
    printf("\n\n");
    printf ("Convertido em binario: %s", b);
  }

///////////////////////////////////////////////////////////////////////////////////////////////


void menu();

void menu_reset(int * op)
  {
    printf("\nDeseja voltar ao menu? (1-sim / 2-nao) ");
    scanf ("%d", op);
    if (*op==1)
      {
        system ("cls");
        menu();
      }
  }


void menu()
  {
    int opc;
    printf("\n\tConversao de Bases\n\n");
    printf("Escolha a conversao:\n\n");
    printf("1-Decimal para binario  ");
    printf("2-Binario para decimal\n");
    printf("3-Decimal para hexadecimal  ");
    printf("4-Hexadecimal para decimal\n");
    printf("5-Binario para hexadecimal  ");
    printf("6-Hexadecimal para binario\n");
    printf("7-Sair\n\n");
    printf("Opcao: ");
    scanf("%d", &opc);
    switch (opc)
      {
        case 1:
          dec_to_bin();
          menu_reset(&opc);
          break;
        case 2:
          bin_f_dec();
          menu_reset(&opc);
          break;
        case 3:
          dec_to_hex();
          menu_reset(&opc);
          break;
        case 4:
          hex_to_dec();
          menu_reset(&opc);
          break;
        case 5:
          bin_to_hex();
          menu_reset(&opc);
          break;
        case 6:
          hex_to_bin();
          menu_reset(&opc);
          break;
        case 7:
          exit(1);
        default:
          system ("cls");
          menu();
      }
  }


int main(void)
  {
    menu();
    return 0;
  }
