public class App {
    public static void main(String[] args) throws Exception {
        Arvore<Integer> arvore = new Arvore<Integer>();
        arvore.adicionar(10);
        arvore.adicionar(8);
        arvore.adicionar(5);
        arvore.adicionar(9);
        arvore.adicionar(13);
        arvore.adicionar(18);
        arvore.adicionar(7);
        arvore.adicionar(20);

        System.out.println("\n\nEm-ordem");
        arvore.emOrdem(arvore.getRaiz());

    }
}
