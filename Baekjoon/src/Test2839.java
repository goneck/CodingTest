import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2839 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));

        int num=Integer.parseInt(bf.readLine());

        int five=num/5;
        int three=0;
        int sum=-1;
        while(true){
            if((num-five*5)%3!=0){
                if(num/5!=0){
                    five--;
                }
            }
            else{
                three=(num-five*5)/3;
                sum=five+three;
                //System.out.println("second else");
                break;
            }
            
            if(five==0 && num%3!=0){
                //System.out.println("third if");
                break;
            }
        }
        
        System.out.println(sum);
    }
}
