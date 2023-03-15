public class Produs{
    private String denumire;
    private int pret;
    public Produs(String Denumire, int Pret){
        this.denumire = Denumire;
        this.pret = Pret;
    }
    public void setDenumire(String Denumire){
        System.out.print(denumire+"   "+pret);
    }
    public double getPret(){
        return pret;
    }
    public void setPret(int Pret){
        this.pret = Pret;
    }
    public void aplicaReducere(double procent){
        this.pret = (int)(pret - (pret * procent / 100));
    }
    public static void main(String args[])
    {
        Produs p1 = new Produs("Lapte", 10);
        p1.setDenumire("Lapte");
        p1.setPret(10);
        p1.aplicaReducere(10);
        System.out.print(p1.getPret());
    }
}