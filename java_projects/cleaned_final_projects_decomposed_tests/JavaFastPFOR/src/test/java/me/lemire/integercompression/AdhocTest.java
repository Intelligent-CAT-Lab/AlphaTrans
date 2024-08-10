/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
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
    
    
    /**
     * 
     */
    
    

    /**
     * 
     */
    
 
    /**
     * a test
     */
    

    /**
     * a test
     */
    

    /**
     * a test
     */

    @Test
    public void testIssue29_test0_decomposed()  {
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

    @Test
    public void testIssue29b_test0_decomposed()  {
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

    @Test
    public void testIssue41_test0_decomposed()  {
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

    @Test
    public void biggerCompressedArray0_test0_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
    }

    @Test
    public void biggerCompressedArray0_test1_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 0, 16384);
    }

    @Test
    public void biggerCompressedArray0_test2_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 0, 16384);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
    }

    @Test
    public void biggerCompressedArray0_test3_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 0, 16384);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        assertSymmetry(c, 0, 16384);
    }

    @Test
    public void biggerCompressedArray1_test0_decomposed()  {
        IntegerCODEC c = new VariableByte();
    }

    @Test
    public void biggerCompressedArray1_test1_decomposed()  {
        IntegerCODEC c = new VariableByte();
        assertSymmetry(c, -1);
    }

    @Test
    public void biggerCompressedArray2_test0_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
    }

    @Test
    public void biggerCompressedArray2_test1_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
    }

    @Test
    public void biggerCompressedArray2_test2_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
    }

    @Test
    public void biggerCompressedArray2_test3_decomposed()  {
        IntegerCODEC c = new Composition(FastPFOR128.FastPFOR1281(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
        c = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        assertSymmetry(c, 65535, 65535);
    }
}