/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.codec.language.bm;

import org.junit.Test;

public class CacheSubSequencePerformanceTest {

    

    private void test1(final CharSequence input, final int times) {
        final long beginTimeMillis = System.currentTimeMillis();
        for (int i = 0; i < times; i++) {
            test2(input);
        }
        System.out.println(System.currentTimeMillis() - beginTimeMillis + " millis");
    }

    private void test2(final CharSequence input) {
        for (int i = 0; i < input.length(); i++) {
            for (int j = i; j <= input.length(); j++) {
                input.subSequence(i, j);
            }
        }
    }

    private CharSequence cacheSubSequence(final CharSequence cached) {
        final CharSequence[][] cache = new CharSequence[cached.length()][cached.length()];
        return new CharSequence() {
            @Override
            public char charAt(final int index) {
                return cached.charAt(index);
            }

            @Override
            public int length() {
                return cached.length();
            }

            @Override
            public CharSequence subSequence(final int start, final int end) {
                if (start == end) {
                    return "";
                }
                CharSequence res = cache[start][end - 1];
                if (res == null) {
                    res = cached.subSequence(start, end);
                    cache[start][end - 1] = res;
                }
                return res;
            }
        };
    }

    @Test
    public void test0_test0_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
    }

    @Test
    public void test0_test1_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
        System.out.print("Test with StringBuilder : ");
        test1(new StringBuilder("Angelo"), times);
    }

    @Test
    public void test0_test2_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
        System.out.print("Test with StringBuilder : ");
        test1(new StringBuilder("Angelo"), times);
        System.out.print("Test with cached String : ");
        cacheSubSequence("Angelo");
    }

    @Test
    public void test0_test3_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
        System.out.print("Test with StringBuilder : ");
        test1(new StringBuilder("Angelo"), times);
        System.out.print("Test with cached String : ");
        cacheSubSequence("Angelo");
        test1(cacheSubSequence("Angelo"), times);
    }

    @Test
    public void test0_test4_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
        System.out.print("Test with StringBuilder : ");
        test1(new StringBuilder("Angelo"), times);
        System.out.print("Test with cached String : ");
        cacheSubSequence("Angelo");
        test1(cacheSubSequence("Angelo"), times);
        System.out.print("Test with cached StringBuilder : ");
        cacheSubSequence(new StringBuilder("Angelo"));
    }

    @Test
    public void test0_test5_decomposed()  {
        final int times = 10000000;
        System.out.print("Test with String : ");
        test1("Angelo", times);
        System.out.print("Test with StringBuilder : ");
        test1(new StringBuilder("Angelo"), times);
        System.out.print("Test with cached String : ");
        cacheSubSequence("Angelo");
        test1(cacheSubSequence("Angelo"), times);
        System.out.print("Test with cached StringBuilder : ");
        cacheSubSequence(new StringBuilder("Angelo"));
        test1(cacheSubSequence(new StringBuilder("Angelo")), times);
    }
}