
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

import java.util.Arrays;

import org.junit.Assert;
import org.junit.Test;

import me.lemire.integercompression.differential.IntegratedBinaryPacking;
import me.lemire.integercompression.differential.IntegratedIntCompressor;
import me.lemire.integercompression.differential.IntegratedVariableByte;
import me.lemire.integercompression.differential.SkippableIntegratedComposition;

/**
 * Testing IntCompressor objects.
 */
public class IntCompressorTest {
    IntegratedIntCompressor[] iic = {
            new IntegratedIntCompressor(0, new IntegratedVariableByte()),
            new IntegratedIntCompressor(0, new SkippableIntegratedComposition(
                            new IntegratedBinaryPacking(),
                            new IntegratedVariableByte()))
 };
    IntCompressor[] ic = {
            new IntCompressor(0, new VariableByte()),
            new IntCompressor(0, new SkippableComposition(new BinaryPacking(),
                    new VariableByte())) };

    /**
     * 
     */
    @Test
    public void basicTest() {
        for (int N = 1; N <= 10000; N *= 10) {
            int[] orig = new int[N];
            for (int k = 0; k < N; k++)
                orig[k] = 3 * k + 5;
            for (IntCompressor i : ic) {
                int[] comp = i.compress(orig);
                int[] back = i.uncompress(comp);
                Assert.assertArrayEquals(back, orig);
            }
        }

    }
    /**
     * 
     */
    @Test
    public void superSimpleExample() {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for(int k = 0; k < data.length; ++k)
          data[k] = k;
        System.out.println("Compressing "+data.length+" integers using friendly interface");
        int[] compressed = iic.compress(data);
        int[] recov = iic.uncompress(compressed);
        System.out.println("compressed from "+data.length*4/1024+"KB to "+compressed.length*4/1024+"KB");
        if(!Arrays.equals(recov,data)) throw new RuntimeException("bug");
    }

    /**
     * 
     */
    @Test
    public void basicIntegratedTest() {
        for (int N = 1; N <= 10000; N *= 10) {
            int[] orig = new int[N];
            for (int k = 0; k < N; k++)
                orig[k] = 3 * k + 5;
            for (IntegratedIntCompressor i : iic) {
                int[] comp = i.compress(orig);
                int[] back = i.uncompress(comp);
                Assert.assertArrayEquals(back, orig);
            }
        }
    }
}
