import java.util.*;
public class Fibonacci {
    // Versão recursiva simples (O(2^n))
    public static long fibonacciRecursivo(int n) {
        if (n <= 1) return n;
        return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2);
    }

    // Versão iterativa otimizada (O(n))
    public static long fibonacciIterativo(int n) {
        if (n <= 1) return n;
        long a = 0, b = 1, c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args) {
        int[] valores = {5, 10, 15, 20, 25, 30, 35};

        System.out.printf("%-10s %-20s %-20s%n", "n", "Tempo Recursivo (ms)", "Tempo Iterativo (ms)");

        for (int n : valores) {
            long inicio = System.nanoTime();
            fibonacciRecursivo(n);
            long fim = System.nanoTime();
            long tempoRecursivo = (fim - inicio) / 1_000_000;

            inicio = System.nanoTime();
            fibonacciIterativo(n);
            fim = System.nanoTime();
            long tempoIterativo = (fim - inicio) / 1_000_000;

            System.out.printf("%-10d %-20d %-20d%n", n, tempoRecursivo, tempoIterativo);
        }
    }
}
