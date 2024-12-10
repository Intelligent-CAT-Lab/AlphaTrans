/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */
package me.lemire.longcompression.synth;

import me.lemire.integercompression.synth.ClusteredDataGenerator;

/**
 * This class will generate lists of random longs based on the clustered
 * model:
 * 
 * Reference: Vo Ngoc Anh and Alistair Moffat. 2010. Index compression using
 * 64-bit words. Softw. Pract. Exper.40, 2 (February 2010), 131-147.
 * 
 * @author Benoit Lacelle
 * @see ClusteredDataGenerator
 */
public class LongClusteredDataGenerator {

        final LongUniformDataGenerator unidg = new LongUniformDataGenerator(1, 0);

        /**
         * Creating random array generator.
         */
        public LongClusteredDataGenerator() {
        }

        /**
         * generates randomly N distinct integers from 0 to Max.
         * 
         * @param N
         *                number of integers to generate
         * @param Max
         *                maximal value of the integers
         * @return array containing the integers
         */

        /**
         * Little test program.
         * 
         * @param args
         *                arguments are ignored
         */

    
}
