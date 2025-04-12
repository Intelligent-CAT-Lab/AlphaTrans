
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
