using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


// 1 El usuario ingresará valores positivos, cuando no tenga más valores ingresará 0 (cero) El sistema deberá informar la suma de los ingresados

namespace Ejercicio_While
{
    internal class Class1
    {
        static void Main(string[] args)
        {
            Console.WriteLine("ingrese un valor mayor a 0");
            int num = 1;
            double suma;
            double promedio;
            List<double> positivos = new List<double>();
            while (num != 0)
            {
                num = Convert.ToInt32(Console.ReadLine());
                if (num > 0)
                {
                    positivos.Add(num);
                }
                else if (num == 0)
                {
                    suma = positivos.Sum();
                    promedio = suma / positivos.Count();
                    Console.WriteLine("El resultado de la suma es " + suma);
                }
            }
        }
    }
}
// 3 El usuario ingresará una lista de nombre de persona, cuando se ingresé un nombre vacío, sin datos; el sistema informará cuántos nombres de han ingresado.



class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Ingresa la lista de nombres de persona:");

        int count = 0;
        string name = Console.ReadLine();

        while (name != "")
        {
            count++;
            name = Console.ReadLine();
        }

        Console.WriteLine("\nSe ingresaron " + count + " nombres de personas.");
    }
}

// 4 Para calcular el total de una factura , el usuario ingresará pares de datos Costo y Total ; cuando se ingrese costo 0 finaliza el ingreso de datos; informar el total adeudado.


class Program
{
    static void Main()
    {
        double totalAdeudado = 0;
        Console.Write("Ingrese un costo: ");
        double costo = double.Parse(Console.ReadLine());
        while (costo != 0)
        {
            Console.Write("Ingrese el total: ");
            double total = double.Parse(Console.ReadLine());
            totalAdeudado += total;
            Console.Write("Ingrese otro costo (o 0 para finalizar): ");
            costo = double.Parse(Console.ReadLine());
        }

        Console.WriteLine("El total adeudado es: " + totalAdeudado);
    }
}
//5 Para calcular el consumo total de un cliente, el usuario primero ingresará cuántos productos compró; luego el sistema solicitará que ingrese el total y costo de cada uno de esos productos consumidos; al terminar informará el total adeudado por el cliente. 

class Program
{
    static void Main()
    {
        double totalAdeudado = 0;
        Console.Write("¿Cuántos productos compró el cliente? ");
        int cantidadProductos = int.Parse(Console.ReadLine());
        int i = 1;

        while (i <= cantidadProductos)
        {
            Console.Write("Ingrese el costo del producto " + i + ": ");
            double costo = double.Parse(Console.ReadLine());
            Console.Write("Ingrese el total del producto " + i + ": ");
            double total = double.Parse(Console.ReadLine());
            totalAdeudado += total;
            i++;
        }

        Console.WriteLine("El total adeudado es: " + totalAdeudado);
    }
}