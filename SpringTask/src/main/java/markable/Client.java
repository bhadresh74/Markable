package markable;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

/**
 * Created by Bhadresh on 6/08/2016.
 */
@SpringBootApplication
@EnableScheduling
public class Client {
    public static void main(String args[]){
       SpringApplication.run(Client.class,args);
    }
}
