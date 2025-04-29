using System;

class Program
{
    static void Main()
    {
        bool continuar = true;

        while (continuar)
        {
            Console.WriteLine("\n=== CALCULADORA SIMPLES ===");
            Console.WriteLine("1. Soma");
            Console.WriteLine("2. Subtração");
            Console.WriteLine("3. Multiplicação");
            Console.WriteLine("4. Divisão");
            Console.WriteLine("0. Sair");
            Console.Write("Escolha uma opção: ");
            string opcao = Console.ReadLine();

            if (opcao == "0")
            {
                Console.WriteLine("Encerrando...");
                break;
            }

            Console.Write("Digite o primeiro número: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double resultado = 0;
            bool operacaoValida = true;

            if (opcao == "1")
            {
                resultado = num1 + num2;
                Console.WriteLine("Resultado da soma: " + resultado);
            }
            else if (opcao == "2")
            {
                resultado = num1 - num2;
                Console.WriteLine("Resultado da subtração: " + resultado);
            }
            else if (opcao == "3")
            {
                resultado = num1 * num2;
                Console.WriteLine("Resultado da multiplicação: " + resultado);
            }
            else if (opcao == "4")
            {
                if (num2 != 0)
                {
                    resultado = num1 / num2;
                    Console.WriteLine("Resultado da divisão: " + resultado);
                }
                else
                {
                    Console.WriteLine("Erro: divisão por zero!");
                }
            }
            else
            {
                Console.WriteLine("Opção inválida.");
                operacaoValida = false;
            }

            if (operacaoValida)
            {
                Console.Write("Deseja fazer outra operação? (s/n): ");
                string resposta = Console.ReadLine().ToLower();
                if (resposta != "s")
                {
                    continuar = false;
                    Console.WriteLine("Programa encerrado.");
                }
            }
        }
    }
}
