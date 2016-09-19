import java.util.Random;
import java.util.Scanner;

/**
 * @author wangjunwei
 */
public class PrngSequenceGuessing {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        while (n-- > 0) {
            long from = in.nextLong();
            long to = in.nextLong();
            int[] arr = new int[10];
            for (int i = 0; i < arr.length; i++) {
                arr[i] = in.nextInt();
            }
            solve(from, to, arr);
        }
    }

    static void solve(long from, long to, int[] arr) {
        Random random = new Random();

        for (long l = from; l < to; l++) {
            random.setSeed(l);
            boolean flag = true;
            for (int i = 0; i < arr.length; i++) {
                if (random.nextInt(1000) != arr[i]) {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                System.out.print(l);
                for (int i = 0; i < 10; i++) {
                    System.out.print(' ');
                    System.out.print(random.nextInt(1000));
                }
                System.out.println();
                break;
            }
        }
    }
}
