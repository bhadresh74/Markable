package markable;

import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Bhadresh on 6/08/2016.
 */
@Component
public class Number {

    public Integer findAmicable(int seed){
        Number obj = new Number();
        Integer sumAmicable = 0;
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=2;i<=seed;i++){
            map.put(i,obj.findSumdivisors(i));
        }

        for(int i=2;i<=seed;i++) {
            int value = map.get(i);
            if (value != 0 && value != 1 && value <= seed) {
                int sumValue = map.get(value);
                if (sumValue == i && sumValue != value) {
                    sumAmicable = sumAmicable + value + sumValue;
                    map.put(i, 0);
                    map.put(value, 0);
                }
            }
        }
        return sumAmicable;
    }

    public Integer findSumdivisors(int div) {
        int sum = 1;
        for (int i = 2; i <= (int) Math.sqrt(div); i++) {
            if (div % i == 0) {
                sum += i;
                int quo = div / i;
                if (quo != i)
                    sum += quo;
            }
        }
        return sum;
    }

    }

