//problema 1 laborator 3
import javax.swing.JOptionPane;

public class java {
        public static int suma(int a, int b) {
                return a + b;
        }public static int diferenta(int a, int b) {
                return a - b;
        }public static int produs(int a, int b) {
                return a * b;
        }public static int maxim(int a,int b){
            return (int) Math.max(a,b);}
        public static int minim(int a,int b){
            if(a<b)
            return a;
            return b;
        }
        public static void main(String[] args){
            String s1=JOptionPane.showInputDialog("Introduceti primul numar");
            String s2=JOptionPane.showInputDialog("Introduce al doilea numar");
            int n1=Integer.parseInt(s1);
            int n2=Integer.parseInt(s2);
            JOptionPane.showMessageDialog(null,"Suma este "+suma(n1,n2)+"\nProdusul este "+produs(n1,n2)+"\nDiferenta este "+diferenta(n1,n2)+"\nMaximul este "+maxim(n1,n2)+"\nMinimul este "+minim(n1,n2));
            
        }
        }
        