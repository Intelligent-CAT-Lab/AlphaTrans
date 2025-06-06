
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


package me.lemire.longcompression;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;

import me.lemire.integercompression.IntWrapper;

/**
 * Static utility methods for test.
 */
public class LongTestUtils {
    
    protected static void dumpIntArray(long[] data, String label) {
        System.out.print(label);
        for (int i = 0; i < data.length; ++i) {
            if (i % 6 == 0) {
                System.out.println();
            }
            System.out.format(" %1$11d", data[i]);
        }
        System.out.println();
    }

    protected static void dumpIntArrayAsHex(long[] data, String label) {
        System.out.print(label);
        for (int i = 0; i < data.length; ++i) {
            if (i % 8 == 0) {
                System.out.println();
            }
            System.out.format(" %1$08X", data[i]);
        }
        System.out.println();
    }

    /**
     * Check that compress and uncompress keep original array.
     *
     * @param codec CODEC to test.
     * @param orig  original integers
     */
    public static void assertSymmetry(LongCODEC codec, long... orig) {
        // There are some cases that compressed array is bigger than original
        // array.  So output array for compress must be larger.
        //
        // Example:
        //  - VariableByte compresses an array like [ -1 ].
        //  - Composition compresses a short array.
        final int EXTEND = 1;

        long[] compressed = new long[orig.length + EXTEND];
        IntWrapper c_inpos = new IntWrapper(0);
        IntWrapper c_outpos = new IntWrapper(0);
        codec.compress0(orig, c_inpos, orig.length, compressed,
                c_outpos);

        assertTrue(c_outpos.get() <= orig.length + EXTEND);

        // Uncompress an array.
        long[] uncompressed = new long[orig.length];
        IntWrapper u_inpos = new IntWrapper(0);
        IntWrapper u_outpos = new IntWrapper(0);
        codec.uncompress1(compressed, u_inpos, c_outpos.get(),
                uncompressed, u_outpos);

        // Compare between uncompressed and orig arrays.
        long[] target = Arrays.copyOf(uncompressed, u_outpos.get());
        assertArrayEquals(orig, target);
    }

    protected static long[] compress1(LongCODEC codec, long[] data) {
        long[] outBuf = new long[data.length * 8];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.compress0(data, inPos, data.length, outBuf, outPos);
        return Arrays.copyOf(outBuf, outPos.get());
    }

    protected static long[] uncompress0(LongCODEC codec, long[] data, int len) {
        long[] outBuf = new long[len + 1024];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.uncompress1(data, inPos, data.length, outBuf, outPos);
        return Arrays.copyOf(outBuf, outPos.get());
    }



    protected static byte[] compress0(ByteLongCODEC codec, long[] data) {
        byte[] outBuf = new byte[data.length * 4 * 4];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.compress1(data, inPos, data.length, outBuf, outPos);
        return Arrays.copyOf(outBuf, outPos.get());
    }

    protected static long[] uncompress1(ByteLongCODEC codec, byte[] data, int len) {
        long[] outBuf = new long[len + 1024];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.uncompress1(data, inPos, data.length, outBuf, outPos);
        return Arrays.copyOf(outBuf, outPos.get());
    }

    protected static long[] compressHeadless(SkippableLongCODEC codec, long[] data) {
        long[] outBuf = new long[data.length * 4];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.headlessCompress(data, inPos, data.length, outBuf, outPos);
        return Arrays.copyOf(outBuf, outPos.get());
    }

    protected static long[] uncompressHeadless(SkippableLongCODEC codec, long[] data, int len) {
        long[] outBuf = new long[len + 1024];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        IntWrapper outPos = IntWrapper.IntWrapper1();
        codec.headlessUncompress(data, inPos, data.length, outBuf, outPos,len);
        if(outPos.get() < len) throw new RuntimeException("Insufficient output.");
        return Arrays.copyOf(outBuf, outPos.get());
    }

	public static String longToBinaryWithLeading(long l) {
		return String.format("%64s", Long.toBinaryString(l)).replace(' ', '0');
	}
}
