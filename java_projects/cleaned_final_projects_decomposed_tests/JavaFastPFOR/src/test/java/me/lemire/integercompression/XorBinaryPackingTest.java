/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.integercompression;

import java.util.Arrays;

import me.lemire.integercompression.differential.XorBinaryPacking;

import org.junit.Test;

import static org.junit.Assert.*;

/**
 * @author lemire
 *
 */
@SuppressWarnings({ "static-method" })
public final class XorBinaryPackingTest
{






    private static void checkCompressAndUncompress(String label, int[] data) {
        XorBinaryPacking codec = new XorBinaryPacking();
        int[] compBuf = TestUtils.compress1(codec, data);
        int[] decompBuf = TestUtils.uncompress0(codec, compBuf, data.length);
        assertArrayEquals(data, decompBuf);
    }

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
     * 
     */
    

    /**
     * 
     */
    

    /**
     * 
     */

    @Test
    public void compressAndUncompress0_test0_decomposed()  {
        int[] data = new int[128];
        Arrays.fill(data,  0,  31, 1);
        Arrays.fill(data, 32,  63, 2);
        Arrays.fill(data, 64,  95, 4);
        Arrays.fill(data, 96, 127, 8);
        checkCompressAndUncompress("compressAndUncompress0", data);
    }

    @Test
    public void compressAndUncompress1_test0_decomposed()  {
        int[] data = new int[128];
        for (int i = 0; i < data.length; ++i) {
            data[i] = i;
        }
        checkCompressAndUncompress("compressAndUncompress1", data);
    }

    @Test
    public void compressAndUncompress2_test0_decomposed()  {
        int[] data = new int[128];
        for (int i = 0; i < data.length; ++i) {
            data[i] = i * (i + 1) / 2;
        }
        checkCompressAndUncompress("compressAndUncompress2", data);
    }

    @Test
    public void compressAndUncompress3_test0_decomposed()  {
        int[] data = new int[256];
        Arrays.fill(data,   0, 127, 2);
        Arrays.fill(data, 128, 255, 3);
        checkCompressAndUncompress("compressAndUncompress3", data);
    }

    @Test
    public void compressAndUncompress4_test0_decomposed()  {
        int[] data = new int[256];
        Arrays.fill(data,   0, 127, 3);
        Arrays.fill(data, 128, 255, 2);
        checkCompressAndUncompress("compressAndUncompress4", data);
    }

    @Test
    public void compressAndUncompress5_test0_decomposed()  {
        int[] data = new int[256];
        for (int i = 0; i < data.length; ++i) {
            data[i] = i;
        }
        checkCompressAndUncompress("compressAndUncompress5", data);
    }
}