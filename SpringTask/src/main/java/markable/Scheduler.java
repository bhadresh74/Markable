package markable;

import markable.controller.Input;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

/**
 * Created by Bhadresh on 6/08/2016.
 */
@Component
public class Scheduler {
    Input ip = new Input();
    private String url = "http://localhost:8080/message";
    private  static int mid = 0;
    @Scheduled(fixedRate = 3000)
    public void requestSeed()
    {
        String resp = null;
        ResponseEntity<String> entity = null;
        HttpStatus status = null;
        Integer seed = (int) (Math.random() * ((20000 - 1000) + 1)) + 1000;
        mid =(int) (Math.random() * ((2147483647 - 1) + 1)) + 1;
        ip.setSeed(seed);
        ip.setMid(mid);
        RestTemplate callTemp = new RestTemplate();


        try {
            entity = callTemp.postForEntity(url, ip, String.class);
            resp = entity.getBody();
            status = entity.getStatusCode();
            if (status.equals(HttpStatus.OK)) {
                System.out.println("HttpStatus: " + status);
                System.out.println("ResponseContent: " + resp.toString());
            }
        }
        catch (HttpClientErrorException e)
        {
            System.out.println("HttpStatus: "+e.getStatusCode());
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}
