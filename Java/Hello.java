class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
}

public class Hello {

    public static void main(String a[]) {
        int num1 = 2;
        double num2 = 3.2;
        double res = num1 + num2;
        boolean boo = true;

        System.out.print(res);
        System.out.print(boo);

        if (num1 > num2) {
            System.out.print("num1 is greater than num2");
        } else {
            System.out.print("num1 is less than num2");
        }

        Calculator calc = new Calculator();
        int sum = calc.add(5, 3);
        System.out.println("Sum: " + sum);
    }
}