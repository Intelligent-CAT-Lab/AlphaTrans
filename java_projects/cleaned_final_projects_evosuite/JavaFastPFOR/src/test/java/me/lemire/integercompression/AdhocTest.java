
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

import org.junit.Assert;
import org.junit.Test;

import me.lemire.integercompression.differential.*;

import static me.lemire.integercompression.TestUtils.*;

import java.util.Arrays;

/**
 * Collection of adhoc tests.
 */
@SuppressWarnings({  "static-method" })
public class AdhocTest {

    
    /**
     * 
     */
    @Test
    public void testIssue29() {
    	    for(int x = 0; x < 64; x++) {
          int[] a = {2, 3, 4, 5};
          int[] b = new int[90];
          int[] c = new int[a.length];
          IntegerCODEC codec = new Composition(new BinaryPacking(), new VariableByte());

          IntWrapper aOffset = new IntWrapper(0);
          IntWrapper bOffset = new IntWrapper(x);
          codec.compress0(a, aOffset, a.length, b, bOffset);
          int len = bOffset.get() - x;
          bOffset.set(x);
          IntWrapper cOffset = new IntWrapper(0);
          codec.uncompress0(b, bOffset, len, c, cOffset);
          Assert.assertArrayEquals(a,c);
    	    }
    }
    
    /**
     * 
     */
    @Test
    public void testIssue29b() {
    	    for(int x = 0; x < 64; x++) {
          int[] a = {2, 3, 4, 5};
          int[] b = new int[90];
          int[] c = new int[a.length];
          SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
          IntWrapper aOffset = new IntWrapper(0);
          IntWrapper bOffset = new IntWrapper(x);
          codec.headlessCompress(a, aOffset, a.length, b, bOffset);
          int len = bOffset.get() - x;
          bOffset.set(x);
          IntWrapper cOffset = new IntWrapper(0);
          codec.headlessUncompress(b, bOffset, len, c, cOffset, a.length);
          Assert.assertArrayEquals(a,c);
    	    }
    }
    

    /**
     * 
     */
    @Test
	public void testIssue41() {
		for (int x = 0; x < 64; x++) {
			int[] a = { 2, 3, 4, 5 };
			int[] b = new int[90];
			int[] c = new int[a.length];
			SkippableIntegratedIntegerCODEC codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
					new IntegratedVariableByte());
			IntWrapper aOffset = new IntWrapper(0);
			IntWrapper bOffset = new IntWrapper(x);
			IntWrapper initValue = new IntWrapper(0);

			codec.headlessCompress(a, aOffset, a.length, b, bOffset, initValue);
			int len = bOffset.get() - x;
			bOffset.set(x);
			IntWrapper cOffset = new IntWrapper(0);
			initValue = new IntWrapper(0);
			codec.headlessUncompress(b, bOffset, len, c, cOffset, a.length, initValue);
			Assert.assertArrayEquals(a, c);
		}
	}
 
    /**
     * a test
     */
    @Test
    public void biggerCompressedArray0() {
        // No problem: for comparison.
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 0, 16384);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        assertSymmetry(c, 0, 16384);

    }

    /**
     * a test
     */
    @Test
    public void biggerCompressedArray1() {
        // Compressed array is bigger than original, because of VariableByte.
        IntegerCODEC c = new VariableByte();
        assertSymmetry(c, -1);
    }

    /**
     * a test
     */
    @Test
    public void biggerCompressedArray2() {
        // Compressed array is bigger than original, because of Composition.
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
    }

 
}
