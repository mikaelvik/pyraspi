import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

/**
 * @author Mikael Vik (BEKK) - mikael.vik@bekk.no
 */
public class MyPi4j {

    public static void main(String[] args) {
        System.out.println("hoi" + args.length);
        GpioController gpioController = GpioFactory.getInstance();
        PinState ps = args.length > 0 ? PinState.HIGH : PinState.LOW;
        gpioController.provisionDigitalOutputPin(RaspiPin.GPIO_00, "gpio0", ps);
        System.out.println("bai");
    }

}





