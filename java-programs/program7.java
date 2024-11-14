interface Rectangle{
    void rect();
}
interface Circle{
    void cir();
}
class Shapes implements Rectangle,Circle{
    public void rect(){
        System.out.println("Rectangle drawn");
    }

    public void cir(){
        System.out.println("circle drawn");
    }
}
public class program7{
    public static void main(String[] args){
        Shapes s=new Shapes();
        s.rect();
        s.cir();
    }
}