
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

import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Random;
import java.util.Set;


import me.lemire.integercompression.synth.UniformDataGenerator;

/**
 * This class will generate "uniform" lists of random longs.
 * 
 * @author Benoit Lacelle
 * @see UniformDataGenerator
 */
public class LongUniformDataGenerator {
        /**
         * construct generator of random arrays.
         */
public LongUniformDataGenerator(int constructorId, final int seed) {
    if (constructorId == 0) {

                this.rand = new Random(seed);
            }
    else {

                this.rand = new Random();
            }
}
//         public LongUniformDataGenerator() {
//                 this.rand = new Random();
//         }

        /**
         * @param seed
         *                random seed
         */
//         public LongUniformDataGenerator(final int seed) {
//                 this.rand = new Random(seed);
//         }

        /**
         * generates randomly N distinct longs from 0 to Max.
         */
        long[] generateUniformHash(int N, long Max) {
                if (N > Max)
                        throw new RuntimeException("not possible");
                long[] ans = new long[N];
                Set<Long> s = new HashSet<>();
                while (s.size() < N)
                        s.add((long) (this.rand.nextDouble() * Max));
                Iterator<Long> i = s.iterator();
                for (int k = 0; k < N; ++k)
                        ans[k] = i.next().longValue();
                Arrays.sort(ans);
                return ans;
        }

        /**
         * output all longs from the range [0,Max) that are not in the array
         */
        static long[] negate(long[] x, long Max) {
        	int newLength = saturatedCast(Max - x.length);
        	long[] ans = new long[newLength];
                int i = 0;
                int c = 0;
                for (int j = 0; j < x.length; ++j) {
                	long v = x[j];
                        for (; i < v; ++i)
                                ans[c++] = i;
                        ++i;
                }
                while (c < ans.length)
                        ans[c++] = i++;
                return ans;
        }

		private static int saturatedCast(long toInt) {
        	if (toInt > Integer.MAX_VALUE) {
        		return Integer.MAX_VALUE;
        	} else {
        		return (int) toInt;
        	}
		}

        /**
         * generates randomly N distinct longs from 0 to Max.
         * 
         * @param N
         *                number of longs to generate
         * @param Max
         *                bound on the value of longs
         * @return an array containing randomly selected longs
         */

        /**
         * generates randomly N distinct longs from 0 to Max.
         */

        Random rand = new Random();

}