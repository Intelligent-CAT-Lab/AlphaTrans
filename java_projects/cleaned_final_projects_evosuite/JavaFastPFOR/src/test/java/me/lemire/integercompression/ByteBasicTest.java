
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

import me.lemire.integercompression.differential.IntegratedVariableByte;

import org.junit.Test;

import static org.junit.Assert.*;


/**
 * Just some basic sanity tests.
 * 
 * @author Daniel Lemire
 */
@SuppressWarnings({ "static-method" })
public class ByteBasicTest {
    ByteIntegerCODEC[] codecs = {
            new VariableByte(),
            new IntegratedVariableByte(),
         };

	/**
     * 
     */
	@Test
	public void saulTest() {
		for (ByteIntegerCODEC C : codecs) {
			for (int x = 0; x < 50 * 4; ++x) {
				int[] a = { 2, 3, 4, 5 };
				byte[] b = new byte[90*4];
				int[] c = new int[a.length];

				IntWrapper aOffset = new IntWrapper(0);
				IntWrapper bOffset = new IntWrapper(x);
				C.compress1(a, aOffset, a.length, b, bOffset);
				int len = bOffset.get() - x;

				bOffset.set(x);
				IntWrapper cOffset = new IntWrapper(0);
				C.uncompress1(b, bOffset, len, c, cOffset);
				if(!Arrays.equals(a, c)) {
					System.out.println("Problem with "+C);
				}
				assertArrayEquals(a, c);
			}
		}
	}
    /**
     * 
     */
    @Test
    public void varyingLengthTest() {
        int N = 4096;
        int[] data = new int[N];
        for (int k = 0; k < N; ++k)
            data[k] = k;
        for (ByteIntegerCODEC c : codecs) {
            for (int L = 1; L <= 128; L++) {
                byte[] comp = TestUtils.compress0(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress1(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug "+c.toString()+" "+k+" "+answer[k]+" "+data[k]);
            }
            for (int L = 128; L <= N; L *= 2) {
                byte[] comp = TestUtils.compress0(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress1(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }

        }
    }

    /**
     * 
     */
    @Test
    public void varyingLengthTest2() {
        int N = 128;
        int[] data = new int[N];
        data[127] = -1;
        for (ByteIntegerCODEC c : codecs) {
            try {
                // CODEC Simple9 is limited to "small" integers.
                if (c.getClass().equals(
                        Class.forName("me.lemire.integercompression.Simple9")))
                    continue;
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            for (int L = 1; L <= 128; L++) {
                byte[] comp = TestUtils.compress0(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress1(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug at k = "+k+" "+answer[k]+" "+data[k]);
            }
            for (int L = 128; L <= N; L *= 2) {
                byte[] comp = TestUtils.compress0(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress1(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }

        }
    }


}
