namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {


            Console.WriteLine("Sisesta esimene arv:");
            double num1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Sisesta tehe (+, -, *, /):");
            char operation = Convert.ToChar(Console.ReadLine());

            Console.WriteLine("Sisesta teine arv:");
            double num2 = Convert.ToDouble(Console.ReadLine());

            double result = 0;

            if (operation == '+')
            {
                result = num1 + num2;
            }
            else if (operation == '-')
            {
                result = num1 - num2;
            }
            else if (operation == '*')
            {
                result = num1 * num2;
            }
            else if (operation == '/')
            {
                if (num2 != 0)
                {
                    result = num1 / num2;
                }
                else
                {
                    Console.WriteLine("Tegemist on jagamisega nulliga, mis pole lubatud.");
                    return;
                }
            }
            else
            {
                Console.WriteLine("Vigane tehe, palun kasuta +, -, * või /.");
                return;
            }

            Console.WriteLine("Tulemus: " + result);
        }
    }


}

