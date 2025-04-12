
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


package me.lemire.integercompression;

/**
 * Essentially a mutable wrapper around an integer.
 * 
 * @author dwu
 */
public final class IntWrapper extends Number {
        private static final long serialVersionUID = 1L;
        private int value;

        /**
         * Constructor: value set to 0.
         */
        public IntWrapper(final int v) {
                this.value = v;
        }
        public static IntWrapper IntWrapper1() {
                return new IntWrapper(0);
        }
//         public IntWrapper() {
//                 this(0);
//         }

        /**
         * Construction: value set to provided argument.
         * 
         * @param v
         *                value to wrap
         */
//         public IntWrapper(final int v) {
//                 this.value = v;
//         }

        /**
         * add the provided value to the integer
         * @param v value to add
         */
        public void add(int v) {
                this.value += v;
        }

        @Override
        public double doubleValue() {
                return this.value;
        }

        @Override
        public float floatValue() {
                return this.value;
        }

        /**
         * @return the integer value
         */
        public int get() {
                return this.value;
        }

        /**
         * add 1 to the integer value
         */
        public void increment() {
                this.value++;
        }

        @Override
        public int intValue() {
                return this.value;
        }

        @Override
        public long longValue() {
                return this.value;
        }

        /**
         * Set the value to that of the specified integer.
         * 
         * @param value
         *                specified integer value
         */
        public void set(final int value) {
                this.value = value;
        }

        @Override
        public String toString() {
                return Integer.toString(this.value);
        }
}
