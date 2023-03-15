public class App {
    public double raza;
    public App(double raza) {
        this.raza = raza;
    }
    public double getArie() {
        return Math.PI * raza * raza;
    }
    public double getcircumferinta() {
        return 2 * Math.PI * raza;
    }
    public static void main(String[] args){
        App cerc = new App(5);
        System.out.println("Aria cercului este: " + cerc.getArie());
        System.out.println("Circumferinta cercului este: " + cerc.getcircumferinta());
    }
}
