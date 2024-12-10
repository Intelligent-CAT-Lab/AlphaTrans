/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.longcompression;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.Test;

import me.lemire.integercompression.FastPFOR;
import me.lemire.integercompression.FastPFOR128;
import me.lemire.integercompression.IntWrapper;
import me.lemire.longcompression.differential.LongDelta;

/**
 * Just some basic sanity tests.
 * 
 * @author Benoit Lacelle
 */
@SuppressWarnings({ "static-method" })
public class LongBasicTest {
    final LongCODEC[] codecs = {
            new LongJustCopy(),
            new LongVariableByte(),
            LongAs2IntsCodec.LongAs2IntsCodec1()};

	/**
     * This tests with a compressed array with various offset
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
     * check that the codecs can be inverted.
     */

    private static void testSpurious(LongCODEC c) {
        long[] x = new long[1024];
        long[] y = new long[0];
        IntWrapper i0 = new IntWrapper(0);
        IntWrapper i1 = new IntWrapper(0);
        for (int inlength = 0; inlength < 32; ++inlength) {
            c.compress0(x, i0, inlength, y, i1);
            assertEquals(0, i1.intValue());
        }
    }

    private static void testZeroInZeroOut(LongCODEC c) {
        long[] x = new long[0];
        long[] y = new long[0];
        IntWrapper i0 = new IntWrapper(0);
        IntWrapper i1 = new IntWrapper(0);
        c.compress0(x, i0, 0, y, i1);
        assertEquals(0, i1.intValue());

        long[] out = new long[0];
        IntWrapper outpos = new IntWrapper(0);
        c.uncompress1(y, i1, 0, out, outpos);
        assertEquals(0, outpos.intValue());
    }

    private static void testCodec(LongCODEC c, LongCODEC co,
            long[][] data, long max) {
        int N = data.length;
        int maxlength = 0;
        for (int k = 0; k < N; ++k) {
            if (data[k].length > maxlength)
                maxlength = data[k].length;
        }
        long[] buffer = new long[maxlength + 1024];
        long[] dataout = new long[4 * maxlength + 1024];
        // 4x + 1024 to account for the possibility of some negative
        // compression.
        IntWrapper inpos = IntWrapper.IntWrapper1();
        IntWrapper outpos = IntWrapper.IntWrapper1();
        for (int k = 0; k < N; ++k) {
            long[] backupdata = Arrays.copyOf(data[k], data[k].length);

            inpos.set(1);
            outpos.set(0);
            if (!(c instanceof IntegratedLongCODEC)) {
                LongDelta.delta0(backupdata);
            }
            c.compress0(backupdata, inpos, backupdata.length - inpos.get(),
                    dataout, outpos);
            final int thiscompsize = outpos.get() + 1;
            inpos.set(0);
            outpos.set(1);
            buffer[0] = backupdata[0];
            co.uncompress1(dataout, inpos, thiscompsize - 1, buffer, outpos);
            if (!(c instanceof IntegratedLongCODEC))
            	LongDelta.fastinverseDelta0(buffer);

            // Check assertions.
            assertEquals("length is not match", outpos.get(), data[k].length);
            long[] bufferCutout = Arrays.copyOf(buffer, outpos.get());
            assertArrayEquals("failed to reconstruct original data", data[k],
                    bufferCutout);
        }
    }

    /**
     * @param codec
     *            provided codec
     */
    public void testUnsorted(LongCODEC codec) {
        int[] lengths = { 133, 1026, 1333333 };
        for (int N : lengths) {
            long[] data = new long[N];
            // initialize the data (most will be small)
            for (int k = 0; k < N; k += 1)
                data[k] = 3;
            // throw some larger values
            for (int k = 0; k < N; k += 5)
                data[k] = 100;
            for (int k = 0; k < N; k += 533)
                data[k] = 10000;
            data[5] = -311;
            // could need more compressing
            long[] compressed = new long[(int) Math.ceil(N * 1.01) + 1024];
            IntWrapper inputoffset = new IntWrapper(0);
            IntWrapper outputoffset = new IntWrapper(0);
            codec.compress0(data, inputoffset, data.length, compressed,
                    outputoffset);
            // we can repack the data: (optional)
            compressed = Arrays.copyOf(compressed, outputoffset.intValue());

            long[] recovered = new long[N];
            IntWrapper recoffset = new IntWrapper(0);
            codec.uncompress1(compressed, new IntWrapper(0), compressed.length,
                    recovered, recoffset);
            assertArrayEquals(data, recovered);
        }
    }

    private void testUnsorted2(LongCODEC codec) {
        long[] data = new long[128];
        data[5] = -1;
        long[] compressed = new long[1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        // we can repack the data: (optional)
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());

        long[] recovered = new long[128];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress1(compressed, new IntWrapper(0), compressed.length,
                recovered, recoffset);
        assertArrayEquals(data, recovered);
    }

    private void testUnsorted3(LongCODEC codec) {
        long[] data = new long[128];
        data[127] = -1;
        long[] compressed = new long[1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        // we can repack the data: (optional)
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());

        long[] recovered = new long[128];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress1(compressed, new IntWrapper(0), compressed.length,
                recovered, recoffset);
        assertArrayEquals(data, recovered);
    }

    /**
         * 
         */
    

    /**
     * 
     */

    @Test
    public void saulTest_test0_decomposed()  {
        for (LongCODEC C : codecs) {
			for (int x = 0; x < 50; ++x) {
				long[] a = { 2, 3, 4, 5 };
				long[] b = new long[90];
				long[] c = new long[a.length];

				IntWrapper aOffset = new IntWrapper(0);
				IntWrapper bOffset = new IntWrapper(x);
				C.compress0(a, aOffset, a.length, b, bOffset);
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

    @Test
    public void varyingLengthTest_test0_decomposed()  {
        int N = 4096;
        long[] data = new long[N];
        for (int k = 0; k < N; ++k)
            data[k] = k;
        for (LongCODEC c : codecs) {
            System.out.println("[BasicTest.varyingLengthTest] codec = " + c);
            for (int L = 1; L <= 128; L++) {
                long[] comp = LongTestUtils.compress1(c, Arrays.copyOf(data, L));
                long[] answer = LongTestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }
            for (int L = 128; L <= N; L *= 2) {
                long[] comp = LongTestUtils.compress1(c, Arrays.copyOf(data, L));
                long[] answer = LongTestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k]) {
                        System.out.println(Arrays.toString(Arrays.copyOf(
                                answer, L)));
                        System.out.println(Arrays.toString(Arrays.copyOf(data,
                                L)));
                        throw new RuntimeException("bug");
                    }
            }

        }
    }

    @Test
    public void varyingLengthTest2_test0_decomposed()  {
        int N = 128;
        long[] data = new long[N];
        data[127] = -1;
        for (LongCODEC c : codecs) {
            System.out.println("[BasicTest.varyingLengthTest2] codec = " + c);
            try {
                // CODEC Simple9 is limited to "small" integers.
                if (c.getClass().equals(
                        Class.forName("me.lemire.integercompression.Simple9")))
                    continue;
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            try {
                // CODEC Simple16 is limited to "small" integers.
                if (c.getClass().equals(
                        Class.forName("me.lemire.integercompression.Simple16")))
                    continue;
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }
            try {
                // CODEC GroupSimple9 is limited to "small" integers.
                if (c.getClass().equals(
                        Class.forName("me.lemire.integercompression.GroupSimple9")))
                    continue;
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }

            for (int L = 1; L <= 128; L++) {
                long[] comp = LongTestUtils.compress1(c, Arrays.copyOf(data, L));
                long[] answer = LongTestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }
            for (int L = 128; L <= N; L *= 2) {
                long[] comp = LongTestUtils.compress1(c, Arrays.copyOf(data, L));
                long[] answer = LongTestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }

        }
    }

    @Test
    public void fastPforTest_test0_decomposed()  {
        for (LongCODEC codec : codecs) {
	        int N = FastPFOR.BLOCK_SIZE;
	        long[] data = new long[N];
	        for (int i = 0; i < N; i++)
	            data[i] = 0;
	        data[126] = -1;
	        long[] comp = LongTestUtils.compress1(codec, Arrays.copyOf(data, N));
	        long[] answer = LongTestUtils.uncompress0(codec, comp, N);
	        for (int k = 0; k < N; ++k)
	            if (answer[k] != data[k])
	                throw new RuntimeException("bug " + k + " " + answer[k]
	                        + " != " + data[k]);
    	}
    }

    @Test
    public void fastPfor128Test_test0_decomposed()  {
        for (LongCODEC codec : codecs) {
	        int N = FastPFOR128.BLOCK_SIZE;
	        long[] data = new long[N];
	        for (int i = 0; i < N; i++)
	            data[i] = 0;
	        data[126] = -1;
	        long[] comp = LongTestUtils.compress1(codec, Arrays.copyOf(data, N));
	        long[] answer = LongTestUtils.uncompress0(codec, comp, N);
	        for (int k = 0; k < N; ++k)
	            if (answer[k] != data[k])
	                throw new RuntimeException("bug " + k + " " + answer[k]
	                        + " != " + data[k]);
    	}
    }
}