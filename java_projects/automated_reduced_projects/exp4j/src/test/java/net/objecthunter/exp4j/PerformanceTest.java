/*
 * Copyright 2014 Frank Asseg
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package net.objecthunter.exp4j;

import org.junit.Test;

import java.util.Formatter;
import java.util.Random;

public class PerformanceTest {

    private static final long BENCH_TIME = 2L;
    private static final String EXPRESSION = "log(x) - y * (sqrt(x^cos(y)))";


    private int benchDouble() {
        final Expression expression = new ExpressionBuilder(EXPRESSION)
                .variables("x", "y")
                .build();
        double val;
        Random rnd = new Random();
        long timeout = BENCH_TIME;
        long time = System.currentTimeMillis() + (1000 * timeout);
        int count = 0;
        while (time > System.currentTimeMillis()) {
            expression.setVariable("x", rnd.nextDouble());
            expression.setVariable("y", rnd.nextDouble());
            val = expression.evaluate();
            count++;
        }
        double rate = count / timeout;
        return count;
    }

    private int benchJavaMath() {
        long time = System.currentTimeMillis() + (1000 * BENCH_TIME);
        double x, y, val, rate;
        int count = 0;
        Random rnd = new Random();
        while (time > System.currentTimeMillis()) {
            x = rnd.nextDouble();
            y = rnd.nextDouble();
            val = Math.log(x) - y * (Math.sqrt(Math.pow(x, Math.cos(y))));
            count++;
        }
        return count;
    }

}
