/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
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
    
    /**
     * 
     */
    

    /**
     * 
     */

    @Test
    public void basicTest_test0_decomposed()  {
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

    @Test
    public void superSimpleExample_test0_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
    }

    @Test
    public void superSimpleExample_test1_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for(int k = 0; k < data.length; ++k)
          data[k] = k;
        System.out.println("Compressing "+data.length+" integers using friendly interface");
        int[] compressed = iic.compress(data);
    }

    @Test
    public void superSimpleExample_test2_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for(int k = 0; k < data.length; ++k)
          data[k] = k;
        System.out.println("Compressing "+data.length+" integers using friendly interface");
        int[] compressed = iic.compress(data);
        int[] recov = iic.uncompress(compressed);
    }

    @Test
    public void superSimpleExample_test3_decomposed()  {
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

    @Test
    public void basicIntegratedTest_test0_decomposed()  {
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