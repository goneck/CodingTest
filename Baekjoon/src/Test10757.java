import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test10757 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st=new StringTokenizer(bf.readLine()," ");

        String num1=st.nextToken();
        String num2=st.nextToken();

        int max_length=Math.max(num1.length(), num2.length());

        int[] A=new int[max_length+1];

        int[] B=new int[max_length+1];

        for (int i=num1.length()-1,idx=0;i>=0;i--,idx++){
            A[idx]=num1.charAt(i)-'0';  // 1의 아스키코드는 49, 0의 아스키코드는 48이라 0을 빼주면 원래의 int값을 얻게 된다.
        }

        for (int i=num2.length()-1,idx=0;i>=0;i--,idx++){
            B[idx]=num2.charAt(i)-'0';
        }

        for (int i=0;i<max_length;i++){
            int sum=A[i]+B[i];
            A[i]=sum%10;
            A[i+1]+=(sum/10);
        }

        StringBuilder sb=new StringBuilder();
        if(A[max_length]!=0){
            sb.append(A[max_length]);
        }

        for (int i=max_length-1;i>=0;i--){
            sb.append(A[i]);
        }

        System.out.println(sb);

    }

}
