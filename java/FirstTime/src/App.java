import javax.swing.JOptionPane;

public class App {
    public static double transformainGradeCelsius(int f){
        return (f - 32) * 5 / 9;
    }public static double transformareingradeFahrenheit(int c){
        return (c * 9 / 5) + 32;
    }
    public static void main(String[] args) throws Exception {
        String s1 = JOptionPane.showInputDialog("Introduceti temperatura in grade Fahrenheit");
        int n1 = Integer.parseInt(s1);
        JOptionPane.showMessageDialog(null, "Temperatura in grade Celsius este " + transformainGradeCelsius(n1));
        String s2 = JOptionPane.showInputDialog("Introduceti temperatura in grade Celsius");
        int n2 = Integer.parseInt(s2);
        JOptionPane.showMessageDialog(null, "Temperatura in grade Fahrenheit este " + transformareingradeFahrenheit(n2));
    }
}


