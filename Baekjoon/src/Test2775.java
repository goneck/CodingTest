import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;


public class Test2775 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf=new BufferedReader(new InputStreamReader((System.in)));
        int count=Integer.parseInt(bf.readLine());
        
        ArrayList<Integer> k_list=new ArrayList<>();
        ArrayList<Integer> n_list=new ArrayList<>(); 

        for (int i=0;i<count;i++){
            int k=Integer.parseInt(bf.readLine());
            int n=Integer.parseInt(bf.readLine());

            k_list.add(k);
            n_list.add(n);
        }

        int max_k=Collections.max(k_list);
        int max_n=Collections.max(n_list);

        int[][] arr= new int[max_k+1][max_n];

        for (int j=0;j<max_n;j++){
            arr[0][j]=j+1;
        }

        for (int i=1;i<max_k+1;i++){
            for (int j=0;j<max_n;j++){

                if(j==0){
                    arr[i][j]=1;
                }

                else{
                    //System.out.println(i+" "+j);
                    arr[i][j]=arr[i][j-1]+arr[i-1][j];
                }
            }
        }
        // for (int i=0; i<max_k;i++){
        //     System.out.println(Arrays.toString(arr[i]));
        // }

        Integer[] kIndex=k_list.toArray(new Integer[count]);
        Integer[] nIndex=n_list.toArray(new Integer[count]);
        for(int i=0;i<count;i++){
            //System.out.println(kIndex[i]+ ","+(nIndex[i]-1));
            System.out.println(arr[(kIndex[i])][(nIndex[i]-1)]);
        }
            
    }
}