
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


package me.lemire.integercompression.differential;

/**
 * Generic class to compute differential coding.
 * 
 * @author Daniel Lemire
 * 
 */
public final class Delta {

        /**
         * Apply differential coding (in-place).
         * 
         * @param data
         *                data to be modified
         */
        public static void delta0(int[] data) {
                for (int i = data.length - 1; i > 0; --i) {
                        data[i] -= data[i - 1];
                }
        }

        /**
         * Apply differential coding (in-place) given an initial value.
         * 
         * @param data
         *                data to be modified
         * @param start
         *                starting index
         * @param length
         *                number of integers to process
         * @param init
         *                initial value
         * @return next initial vale
         */
        public static int delta1(int[] data, int start, int length, int init) {
                final int nextinit = data[start + length - 1];
                for (int i = length - 1; i > 0; --i) {
                        data[start + i] -= data[start + i - 1];
                }
                data[start] -= init;
                return nextinit;
        }

        /**
         * Compute differential coding given an initial value. Output is written
         * to a provided array: must have length "length" or better.
         * 
         * @param data
         *                data to be modified
         * @param start
         *                starting index
         * @param length
         *                number of integers to process
         * @param init
         *                initial value
         * @param out
         *                output array
         * @return next initial vale
         */
        public static int delta2(int[] data, int start, int length, int init,
                                 int[] out) {
                for (int i = length - 1; i > 0; --i) {
                        out[i] = data[start + i] - data[start + i - 1];
                }
                out[0] = data[start] - init;
                return data[start + length - 1];
        }

        /**
         * Undo differential coding (in-place). Effectively computes a prefix
         * sum.
         * 
         * @param data
         *                to be modified.
         */
        public static void inverseDelta(int[] data) {
                for (int i = 1; i < data.length; ++i) {
                        data[i] += data[i - 1];
                }
        }

        /**
         * Undo differential coding (in-place). Effectively computes a prefix
         * sum. Like inverseDelta, only faster.
         * 
         * @param data
         *                to be modified
         */
        public static void fastinverseDelta0(int[] data) {
                int sz0 = data.length / 4 * 4;
                int i = 1;
                if (sz0 >= 4) {
                        int a = data[0];
                        for (; i < sz0 - 4; i += 4) {
                                a = data[i] += a;
                                a = data[i + 1] += a;
                                a = data[i + 2] += a;
                                a = data[i + 3] += a;
                        }
                }

                for (; i != data.length; ++i) {
                        data[i] += data[i - 1];
                }
        }

        /**
         * Undo differential coding (in-place). Effectively computes a prefix
         * sum. Like inverseDelta, only faster. Uses an initial value.
         * 
         * @param data
         *                to be modified
         * @param start
         *                starting index
         * @param length
         *                number of integers to process
         * @param init
         *                initial value
         * @return next initial value
         */
        public static int fastinverseDelta1(int[] data, int start, int length,
                                            int init) {
                data[start] += init;
                int sz0 = length / 4 * 4;
                int i = 1;
                if (sz0 >= 4) {
                        int a = data[start];
                        for (; i < sz0 - 4; i += 4) {
                                a = data[start + i] += a;
                                a = data[start + i + 1] += a;
                                a = data[start + i + 2] += a;
                                a = data[start + i + 3] += a;
                        }
                }

                for (; i != length; ++i) {
                        data[start + i] += data[start + i - 1];
                }
                return data[start + length - 1];
        }

}
