namespace ConsoleApp2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //if ja else rakenduses tuleb teha 
            //kontrollib sinu vanust 
            //1. kui oled alla 18, siis konsool annab vastuseks, 
            //et oled alealine

            //2. Kui oled 19 kuni 65 aastat vana, siis 
            //konsool vastab, et oled ule 65 a vana, siis pensionaar 
            // YN KALKULAATOR 

            Console.WriteLine("mis su vanus on nigga?");
            int vanus = int.Parse (Console.ReadLine());


            if (vanus > 18)
                Console.WriteLine("Oled alaealine cuh");


            else if (vanus >= 19 && vanus <= 65)
                Console.WriteLine("Taiskasvanu oled gng");

            else if (vanus >= 65)
                Console.WriteLine("oi blya nigga ong liiga vana oled unc");






            



            













        }
    }
}
