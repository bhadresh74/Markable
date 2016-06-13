package markable.controller;

import markable.Number;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.lang.*;
import java.util.HashSet;

/**
 * Created by Bhadresh on 6/08/2016.
 */
@RestController
public class Controller {

    @Autowired
    Number num;
    HashSet<Integer> h= new HashSet<>();
    @RequestMapping(value = "/message",method = RequestMethod.POST, consumes = ("application/json"),produces = ("application/json"))
    public ResponseEntity<?> getSum(@RequestBody Input ip)
    {
        Integer answer;
        if(!h.contains(ip.getMid())) {
            h.add(ip.getMid());
            answer = num.findAmicable(ip.getSeed());
            return new ResponseEntity(answer, HttpStatus.OK);
        }
        else{
            return new ResponseEntity(null, HttpStatus.CONFLICT);
        }
    }
}
