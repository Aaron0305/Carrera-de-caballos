package carreracaballos403;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
public class Caballo implements Runnable {
    private JLabel etiqueta;
    private Caballos403 carrera;
    private int millis = 0;
    private static boolean carreraFinalizada = false;

    public Caballo(JLabel etiqueta, Caballos403 carrera) {
        this.etiqueta = etiqueta;
        this.carrera = carrera;
    }

    @Override
    public void run() {
        while (true) {
            if (carreraFinalizada) {
                break;
            }

            try {
                Thread.sleep(millis);
                millis = (int) (Math.random() * 100);
                etiqueta.setLocation(etiqueta.getLocation().x + 10, etiqueta.getLocation().y);
                etiqueta.repaint();
                
                if (etiqueta.getLocation().x >= carrera.getMeta().getLocation().x - 5 && !carreraFinalizada) {
                    carreraFinalizada = true;
                    JOptionPane.showMessageDialog(null, etiqueta.getText() + " ha ganado en: " + millis + " milisegundos");
                    break;
                }
            } catch (Exception e) {
                System.out.println("Error en la ejecución: " + e.getMessage());
            }
        }
    }

    public static void resetCarrera() {
        carreraFinalizada = false;
    }
}
