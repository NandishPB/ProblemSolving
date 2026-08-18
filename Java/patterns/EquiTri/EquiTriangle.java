public class EquiTriangle{
    public static void main(String[] args){
        int n = 5;
        int i;
    for(int M=1; M<=n; M++){
        for(i=1; i<=n-M; i++){
            System.out.print(" ");
        }

        for(int j=0; j<2*M-1; j++){
            System.out.print("*");
        }

        for(int k=1; k<=n-M; k++){
            System.out.print(" ");
        }
        System.out.println();
    }
    }
}