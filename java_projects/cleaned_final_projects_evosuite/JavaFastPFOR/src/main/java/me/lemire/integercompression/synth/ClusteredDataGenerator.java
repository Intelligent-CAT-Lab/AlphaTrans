
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */

package me.lemire.integercompression.synth;

/**
 * This class will generate lists of random integers based on the clustered
 * model:
 * 
 * Reference: Vo Ngoc Anh and Alistair Moffat. 2010. Index compression using
 * 64-bit words. Softw. Pract. Exper.40, 2 (February 2010), 131-147.
 * 
 * @author Daniel Lemire
 */
public class ClusteredDataGenerator {

        UniformDataGenerator unidg = new UniformDataGenerator(1, 0);

        /**
         * Creating random array generator.
         */
        public ClusteredDataGenerator() {
        }

        void fillUniform(int[] array, int offset, int length, int Min, int Max) {
                int[] v = this.unidg.generateUniform(length, Max - Min);
                for (int k = 0; k < v.length; ++k)
                        array[k + offset] = Min + v[k];
        }

        void fillClustered(int[] array, int offset, int length, int Min, int Max) {
                final int range = Max - Min;
                if ((range == length) || (length <= 10)) {
                        fillUniform(array, offset, length, Min, Max);
                        return;
                }
                final int cut = length
                        / 2
                        + ((range - length - 1 > 0) ? this.unidg.rand
                                .nextInt(range - length - 1) : 0);
                final double p = this.unidg.rand.nextDouble();
                if (p < 0.25) {
                        fillUniform(array, offset, length / 2, Min, Min + cut);
                        fillClustered(array, offset + length / 2, length
                                - length / 2, Min + cut, Max);
                } else if (p < 0.5) {
                        fillClustered(array, offset, length / 2, Min, Min + cut);
                        fillUniform(array, offset + length / 2, length - length
                                / 2, Min + cut, Max);
                } else {
                        fillClustered(array, offset, length / 2, Min, Min + cut);
                        fillClustered(array, offset + length / 2, length
                                - length / 2, Min + cut, Max);
                }
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
        public int[] generateClustered(int N, int Max) {
                int[] array = new int[N];
                fillClustered(array, 0, N, 0, Max);
                return array;
        }

        /**
         * Little test program.
         * 
         * @param args
         *                arguments are ignored
         */
        public static void main(final String[] args) {
                int[] example = (new ClusteredDataGenerator())
                        .generateClustered(20, 1000);
                for (int k = 0; k < example.length; ++k)
                        System.out.println(example[k]);
        }

}
