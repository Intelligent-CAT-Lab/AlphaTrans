/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.integercompression;

import java.util.Arrays;
import java.util.Random;

import me.lemire.integercompression.differential.Delta;
import me.lemire.integercompression.differential.IntegratedBinaryPacking;
import me.lemire.integercompression.differential.IntegratedComposition;
import me.lemire.integercompression.differential.IntegratedIntegerCODEC;
import me.lemire.integercompression.differential.IntegratedVariableByte;
import me.lemire.integercompression.differential.XorBinaryPacking;
import me.lemire.integercompression.synth.ClusteredDataGenerator;

import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Just some basic sanity tests.
 * 
 * @author Daniel Lemire
 */
@SuppressWarnings({ "static-method" })
public class BasicTest {
    final IntegerCODEC[] codecs = {
            new IntegratedComposition(new IntegratedBinaryPacking(),
                    new IntegratedVariableByte()),
            new JustCopy(),
            new VariableByte(),
            new GroupSimple9(),
            new IntegratedVariableByte(),
            new Composition(new BinaryPacking(), new VariableByte()),
            new Composition(new NewPFD(), new VariableByte()),
            new Composition(new NewPFDS16(), new VariableByte()),
            new Composition(new OptPFDS9(), new VariableByte()),
            new Composition(new OptPFDS16(), new VariableByte()),
            new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()),
            new Composition(FastPFOR.FastPFOR1(), new VariableByte()),
            new Simple9(),
            new Simple16(),
            new GroupSimple9(),
            new Composition(new XorBinaryPacking(), new VariableByte()),
            new Composition(new DeltaZigzagBinaryPacking(),
					new DeltaZigzagVariableByte()) };

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
     * Verify bitpacking.
     */
    

    /**
     * Verify bitpacking without mask.
     */
    

    /**
     * @param array
     *            some array
     * @param mask
     *            provided mask
     */
    public static void maskArray(int[] array, int mask) {
        for (int i = 0, end = array.length; i < end; ++i) {
            array[i] &= mask;
        }
    }

    /**
     * Verify bitpacking with exception.
     */
    

    /**
     * check that the codecs can be inverted.
     */
    

    /**
     * check that there is no spurious output.
     */
    

    /**
     * check that an empty array generates an empty array after compression.
     */
    

    private static void testSpurious(IntegerCODEC c) {
        int[] x = new int[1024];
        int[] y = new int[0];
        IntWrapper i0 = new IntWrapper(0);
        IntWrapper i1 = new IntWrapper(0);
        for (int inlength = 0; inlength < 32; ++inlength) {
            c.compress0(x, i0, inlength, y, i1);
            assertEquals(0, i1.intValue());
        }
    }

    private static void testZeroInZeroOut(IntegerCODEC c) {
        int[] x = new int[0];
        int[] y = new int[0];
        IntWrapper i0 = new IntWrapper(0);
        IntWrapper i1 = new IntWrapper(0);
        c.compress0(x, i0, 0, y, i1);
        assertEquals(0, i1.intValue());

        int[] out = new int[0];
        IntWrapper outpos = new IntWrapper(0);
        c.uncompress0(y, i1, 0, out, outpos);
        assertEquals(0, outpos.intValue());
    }

    private static void test0(IntegerCODEC c, IntegerCODEC co, int N, int nbr) {
        ClusteredDataGenerator cdg = new ClusteredDataGenerator();
        for (int sparsity = 1; sparsity < 31 - nbr; sparsity += 4) {
            int[][] data = new int[N][];
            int max = (1 << (nbr + sparsity));
            for (int k = 0; k < N; ++k) {
                data[k] = cdg.generateClustered((1 << nbr), max);
            }
            testCodec(c, co, data, max);
        }
    }

    private static void test1(int N, int nbr) {
        ClusteredDataGenerator cdg = new ClusteredDataGenerator();
        System.out.println("[BasicTest.test] N = " + N + " " + nbr);
        for (int sparsity = 1; sparsity < 31 - nbr; sparsity += 4) {
            int[][] data = new int[N][];
            int max = (1 << (nbr + sparsity));
            for (int k = 0; k < N; ++k) {
                data[k] = cdg.generateClustered((1 << nbr), max);
            }

            testCodec(new IntegratedComposition(new IntegratedBinaryPacking(),
                    new IntegratedVariableByte()),
                    new IntegratedComposition(new IntegratedBinaryPacking(),
                            new IntegratedVariableByte()), data, max);
            testCodec(new JustCopy(), new JustCopy(), data, max);
            testCodec(new VariableByte(), new VariableByte(), data, max);
            testCodec(new IntegratedVariableByte(),
                    new IntegratedVariableByte(), data, max);
            testCodec(new Composition(new BinaryPacking(), new VariableByte()),
                    new Composition(new BinaryPacking(), new VariableByte()),
                    data, max);
            testCodec(new Composition(new NewPFD(), new VariableByte()),
                    new Composition(new NewPFD(), new VariableByte()), data,
                    max);
            testCodec(new Composition(new NewPFDS9(), new VariableByte()),
                    new Composition(new NewPFDS9(), new VariableByte()), data,
                    max);
            testCodec(new Composition(new NewPFDS16(), new VariableByte()),
                    new Composition(new NewPFDS16(), new VariableByte()), data,
                    max);
            testCodec(new Composition(new OptPFD(), new VariableByte()),
                    new Composition(new OptPFD(), new VariableByte()), data,
                    max);
            testCodec(new Composition(new OptPFDS9(), new VariableByte()),
                    new Composition(new OptPFDS9(), new VariableByte()), data,
                    max);
            testCodec(new Composition(new OptPFDS16(), new VariableByte()),
                    new Composition(new OptPFDS16(), new VariableByte()), data,
                    max);
            testCodec(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()),
                    new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()),
                    data, max);
            testCodec(new Composition(FastPFOR.FastPFOR1(), new VariableByte()),
                    new Composition(FastPFOR.FastPFOR1(), new VariableByte()),
                    data, max);
            testCodec(new Simple9(), new Simple9(), data, max);
        }
    }

    private static void testCodec(IntegerCODEC c, IntegerCODEC co,
            int[][] data, int max) {
        int N = data.length;
        int maxlength = 0;
        for (int k = 0; k < N; ++k) {
            if (data[k].length > maxlength)
                maxlength = data[k].length;
        }
        int[] buffer = new int[maxlength + 1024];
        int[] dataout = new int[4 * maxlength + 1024];
        // 4x + 1024 to account for the possibility of some negative
        // compression.
        IntWrapper inpos = IntWrapper.IntWrapper1();
        IntWrapper outpos = IntWrapper.IntWrapper1();
        for (int k = 0; k < N; ++k) {
            int[] backupdata = Arrays.copyOf(data[k], data[k].length);

            inpos.set(1);
            outpos.set(0);
            if (!(c instanceof IntegratedIntegerCODEC)) {
                Delta.delta0(backupdata);
            }
            c.compress0(backupdata, inpos, backupdata.length - inpos.get(),
                    dataout, outpos);
            final int thiscompsize = outpos.get() + 1;
            inpos.set(0);
            outpos.set(1);
            buffer[0] = backupdata[0];
            co.uncompress0(dataout, inpos, thiscompsize - 1, buffer, outpos);
            if (!(c instanceof IntegratedIntegerCODEC))
                Delta.fastinverseDelta0(buffer);

            // Check assertions.
            assertEquals("length is not match", outpos.get(), data[k].length);
            int[] bufferCutout = Arrays.copyOf(buffer, outpos.get());
            assertArrayEquals("failed to reconstruct original data", data[k],
                    bufferCutout);
        }
    }

    /**
     * Test for unsorted array.
     */
    

    /**
     * @param codec
     *            provided codec
     */
    public void testUnsorted(IntegerCODEC codec) {
        int[] lengths = { 133, 1026, 1333333 };
        for (int N : lengths) {
            int[] data = new int[N];
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
            int[] compressed = new int[(int) Math.ceil(N * 1.01) + 1024];
            IntWrapper inputoffset = new IntWrapper(0);
            IntWrapper outputoffset = new IntWrapper(0);
            codec.compress0(data, inputoffset, data.length, compressed,
                    outputoffset);
            // we can repack the data: (optional)
            compressed = Arrays.copyOf(compressed, outputoffset.intValue());

            int[] recovered = new int[N];
            IntWrapper recoffset = new IntWrapper(0);
            codec.uncompress0(compressed, new IntWrapper(0), compressed.length,
                    recovered, recoffset);
            assertArrayEquals(data, recovered);
        }
    }

    private void testUnsorted2(IntegerCODEC codec) {
        int[] data = new int[128];
        data[5] = -1;
        int[] compressed = new int[1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        // we can repack the data: (optional)
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());

        int[] recovered = new int[128];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length,
                recovered, recoffset);
        assertArrayEquals(data, recovered);
    }

    private void testUnsorted3(IntegerCODEC codec) {
        int[] data = new int[128];
        data[127] = -1;
        int[] compressed = new int[1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        // we can repack the data: (optional)
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());

        int[] recovered = new int[128];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length,
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
        for (IntegerCODEC C : codecs) {
			for (int x = 0; x < 50; ++x) {
				int[] a = { 2, 3, 4, 5 };
				int[] b = new int[90];
				int[] c = new int[a.length];

				IntWrapper aOffset = new IntWrapper(0);
				IntWrapper bOffset = new IntWrapper(x);
				C.compress0(a, aOffset, a.length, b, bOffset);
				int len = bOffset.get() - x;

				bOffset.set(x);
				IntWrapper cOffset = new IntWrapper(0);
				C.uncompress0(b, bOffset, len, c, cOffset);
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
        int[] data = new int[N];
        for (int k = 0; k < N; ++k)
            data[k] = k;
        for (IntegerCODEC c : codecs) {
            System.out.println("[BasicTest.varyingLengthTest] codec = " + c);
            for (int L = 1; L <= 128; L++) {
                int[] comp = TestUtils.compress1(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }
            for (int L = 128; L <= N; L *= 2) {
                int[] comp = TestUtils.compress1(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress0(c, comp, L);
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
        int[] data = new int[N];
        data[127] = -1;
        for (IntegerCODEC c : codecs) {
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
                int[] comp = TestUtils.compress1(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }
            for (int L = 128; L <= N; L *= 2) {
                int[] comp = TestUtils.compress1(c, Arrays.copyOf(data, L));
                int[] answer = TestUtils.uncompress0(c, comp, L);
                for (int k = 0; k < L; ++k)
                    if (answer[k] != data[k])
                        throw new RuntimeException("bug");
            }

        }
    }

    @Test
    public void checkDeltaZigzagVB_test0_decomposed()  {
        DeltaZigzagVariableByte codec = new DeltaZigzagVariableByte();
    }

    @Test
    public void checkDeltaZigzagVB_test1_decomposed()  {
        DeltaZigzagVariableByte codec = new DeltaZigzagVariableByte();
        DeltaZigzagVariableByte codeco = new DeltaZigzagVariableByte();
    }

    @Test
    public void checkDeltaZigzagVB_test2_decomposed()  {
        DeltaZigzagVariableByte codec = new DeltaZigzagVariableByte();
        DeltaZigzagVariableByte codeco = new DeltaZigzagVariableByte();
        testZeroInZeroOut(codec);
    }

    @Test
    public void checkDeltaZigzagVB_test3_decomposed()  {
        DeltaZigzagVariableByte codec = new DeltaZigzagVariableByte();
        DeltaZigzagVariableByte codeco = new DeltaZigzagVariableByte();
        testZeroInZeroOut(codec);
        test0(codec, codeco, 5, 10);
        test0(codec, codeco, 5, 14);
        test0(codec, codeco, 2, 18);
    }

    @Test
    public void checkDeltaZigzagPacking_test0_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
    }

    @Test
    public void checkDeltaZigzagPacking_test1_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
    }

    @Test
    public void checkDeltaZigzagPacking_test2_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
    }

    @Test
    public void checkDeltaZigzagPacking_test3_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
        IntegerCODEC compo = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
    }

    @Test
    public void checkDeltaZigzagPacking_test4_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
        IntegerCODEC compo = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        IntegerCODEC compo2 = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
    }

    @Test
    public void checkDeltaZigzagPacking_test5_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
        IntegerCODEC compo = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        IntegerCODEC compo2 = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        testZeroInZeroOut(compo);
    }

    @Test
    public void checkDeltaZigzagPacking_test6_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
        IntegerCODEC compo = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        IntegerCODEC compo2 = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        testZeroInZeroOut(compo);
        testUnsorted(compo);
    }

    @Test
    public void checkDeltaZigzagPacking_test7_decomposed()  {
        DeltaZigzagBinaryPacking codec = new DeltaZigzagBinaryPacking();
        testZeroInZeroOut(codec);
        testSpurious(codec);
        IntegerCODEC compo = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        IntegerCODEC compo2 = new Composition(new DeltaZigzagBinaryPacking(),
                new VariableByte());
        testZeroInZeroOut(compo);
        testUnsorted(compo);
        test0(compo, compo2, 5, 10);
        test0(compo, compo2, 5, 14);
        test0(compo, compo2, 2, 18);
    }

    @Test
    public void checkXorBinaryPacking_test0_decomposed()  {
        testZeroInZeroOut(new XorBinaryPacking());
    }

    @Test
    public void checkXorBinaryPacking_test1_decomposed()  {
        testZeroInZeroOut(new XorBinaryPacking());
        testSpurious(new XorBinaryPacking());
    }

    @Test
    public void checkXorBinaryPacking1_test0_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
    }

    @Test
    public void checkXorBinaryPacking1_test1_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
        testZeroInZeroOut(c);
    }

    @Test
    public void checkXorBinaryPacking2_test0_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
    }

    @Test
    public void checkXorBinaryPacking2_test1_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
        testUnsorted(c);
    }

    @Test
    public void checkXorBinaryPacking3_test0_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
    }

    @Test
    public void checkXorBinaryPacking3_test1_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
        IntegerCODEC co = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
    }

    @Test
    public void checkXorBinaryPacking3_test2_decomposed()  {
        IntegerCODEC c = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
        IntegerCODEC co = new IntegratedComposition(new XorBinaryPacking(),
                new IntegratedVariableByte());
        test0(c, co, 5, 10);
        test0(c, co, 5, 14);
        test0(c, co, 2, 18);
    }

    @Test
    public void verifyBitPacking_test0_decomposed()  {
        final int N = 32;
        final int TIMES = 1000;
        Random r = new Random();
        int[] data = new int[N];
        int[] compressed = new int[N];
        int[] uncompressed = new int[N];
        for (int bit = 0; bit < 31; ++bit) {
            for (int t = 0; t < TIMES; ++t) {
                for (int k = 0; k < N; ++k) {
                    data[k] = r.nextInt(1 << bit);
                }
                BitPacking.fastpack(data, 0, compressed, 0, bit);
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit);
                assertArrayEquals(uncompressed, data);
            }
        }
    }

    @Test
    public void verifyWithoutMask_test0_decomposed()  {
        final int N = 32;
        final int TIMES = 1000;
        Random r = new Random();
        int[] data = new int[N];
        int[] compressed = new int[N];
        int[] uncompressed = new int[N];
        for (int bit = 0; bit < 31; ++bit) {
            for (int t = 0; t < TIMES; ++t) {
                for (int k = 0; k < N; ++k) {
                    data[k] = r.nextInt(1 << bit);
                }
                BitPacking.fastpackwithoutmask(data, 0, compressed, 0, bit);
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit);
                assertArrayEquals(uncompressed, data);
            }
        }
    }

    @Test
    public void verifyWithExceptions_test0_decomposed()  {
        final int N = 32;
        final int TIMES = 1000;
        Random r = new Random();
        int[] data = new int[N];
        int[] compressed = new int[N];
        int[] uncompressed = new int[N];
        for (int bit = 0; bit < 31; ++bit) {
            for (int t = 0; t < TIMES; ++t) {
                for (int k = 0; k < N; ++k) {
                    data[k] = r.nextInt();
                }
                BitPacking.fastpack(data, 0, compressed, 0, bit);
                BitPacking.fastunpack(compressed, 0, uncompressed, 0, bit);

                // Check assertions.
                maskArray(data, ((1 << bit) - 1));
                assertArrayEquals(data, uncompressed);
            }
        }
    }

    @Test
    public void basictest_test0_decomposed()  {
        test1(5, 10);
        test1(5, 14);
        test1(2, 18);
    }

    @Test
    public void spuriousouttest_test0_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
    }

    @Test
    public void spuriousouttest_test1_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
    }

    @Test
    public void spuriousouttest_test2_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
    }

    @Test
    public void spuriousouttest_test3_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
    }

    @Test
    public void spuriousouttest_test4_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
    }

    @Test
    public void spuriousouttest_test5_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
    }

    @Test
    public void spuriousouttest_test6_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
    }

    @Test
    public void spuriousouttest_test7_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
        testSpurious(new OptPFDS16());
    }

    @Test
    public void spuriousouttest_test8_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
        testSpurious(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void spuriousouttest_test9_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
        testSpurious(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testSpurious(FastPFOR128.FastPFOR1281());
    }

    @Test
    public void spuriousouttest_test10_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
        testSpurious(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testSpurious(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
    }

    @Test
    public void spuriousouttest_test11_decomposed()  {
        testSpurious(new IntegratedBinaryPacking());
        testSpurious(new BinaryPacking());
        testSpurious(new NewPFD());
        testSpurious(new NewPFDS9());
        testSpurious(new NewPFDS16());
        testSpurious(new OptPFD());
        testSpurious(new OptPFDS9());
        testSpurious(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testSpurious(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testSpurious(FastPFOR.FastPFOR1());
    }

    @Test
    public void zeroinzerouttest_test0_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
    }

    @Test
    public void zeroinzerouttest_test1_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
    }

    @Test
    public void zeroinzerouttest_test2_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
    }

    @Test
    public void zeroinzerouttest_test3_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
    }

    @Test
    public void zeroinzerouttest_test4_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
    }

    @Test
    public void zeroinzerouttest_test5_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
    }

    @Test
    public void zeroinzerouttest_test6_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
    }

    @Test
    public void zeroinzerouttest_test7_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
    }

    @Test
    public void zeroinzerouttest_test8_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
    }

    @Test
    public void zeroinzerouttest_test9_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void zeroinzerouttest_test10_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
    }

    @Test
    public void zeroinzerouttest_test11_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
    }

    @Test
    public void zeroinzerouttest_test12_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
    }

    @Test
    public void zeroinzerouttest_test13_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
    }

    @Test
    public void zeroinzerouttest_test14_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test15_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test16_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test17_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test18_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test19_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test20_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test21_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test22_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void zeroinzerouttest_test23_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test24_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
    }

    @Test
    public void zeroinzerouttest_test25_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
    }

    @Test
    public void zeroinzerouttest_test26_decomposed()  {
        testZeroInZeroOut(new IntegratedBinaryPacking());
        testZeroInZeroOut(new IntegratedVariableByte());
        testZeroInZeroOut(new BinaryPacking());
        testZeroInZeroOut(new NewPFD());
        testZeroInZeroOut(new NewPFDS9());
        testZeroInZeroOut(new NewPFDS16());
        testZeroInZeroOut(new OptPFD());
        testZeroInZeroOut(new OptPFDS9());
        testZeroInZeroOut(new OptPFDS16());
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(FastPFOR128.FastPFOR1281());
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(FastPFOR.FastPFOR1());
        testZeroInZeroOut(new VariableByte());
        testZeroInZeroOut(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new BinaryPacking(),
                new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new NewPFDS16(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFD(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS9(), new VariableByte()));
        testZeroInZeroOut(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testZeroInZeroOut(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testZeroInZeroOut(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testZeroInZeroOut(new IntegratedComposition(
                new IntegratedBinaryPacking(), new IntegratedVariableByte()));
    }

    @Test
    public void testUnsortedExample_test0_decomposed()  {
        testUnsorted(new VariableByte());
    }

    @Test
    public void testUnsortedExample_test1_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
    }

    @Test
    public void testUnsortedExample_test2_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test3_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test4_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test5_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test6_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test7_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test8_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test9_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void testUnsortedExample_test10_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test11_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
    }

    @Test
    public void testUnsortedExample_test12_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test13_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
    }

    @Test
    public void testUnsortedExample_test14_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test15_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
    }

    @Test
    public void testUnsortedExample_test16_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
    }

    @Test
    public void testUnsortedExample_test17_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test18_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test19_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test20_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test21_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test22_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test23_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test24_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void testUnsortedExample_test25_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test26_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
    }

    @Test
    public void testUnsortedExample_test27_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test28_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
    }

    @Test
    public void testUnsortedExample_test29_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test30_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
    }

    @Test
    public void testUnsortedExample_test31_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
    }

    @Test
    public void testUnsortedExample_test32_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test33_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test34_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test35_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test36_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test37_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test38_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test39_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
    }

    @Test
    public void testUnsortedExample_test40_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted3(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test41_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted3(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
    }

    @Test
    public void testUnsortedExample_test42_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted3(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted3(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
    }

    @Test
    public void testUnsortedExample_test43_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted3(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted3(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted2(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
    }

    @Test
    public void testUnsortedExample_test44_decomposed()  {
        testUnsorted(new VariableByte());
        testUnsorted(new IntegratedVariableByte());
        testUnsorted(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted2(new VariableByte());
        testUnsorted2(new IntegratedVariableByte());
        testUnsorted2(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted2(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted2(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted2(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted3(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted3(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
        testUnsorted3(new VariableByte());
        testUnsorted3(new IntegratedVariableByte());
        testUnsorted3(new Composition(new BinaryPacking(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFD(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new NewPFDS16(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFD(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS9(), new VariableByte()));
        testUnsorted3(new Composition(new OptPFDS16(), new VariableByte()));
        FastPFOR128.FastPFOR1281();
        testUnsorted3(new Composition(FastPFOR128.FastPFOR1281(), new VariableByte()));
        FastPFOR.FastPFOR1();
        testUnsorted3(new Composition(FastPFOR.FastPFOR1(), new VariableByte()));
        testUnsorted2(new IntegratedComposition(new IntegratedBinaryPacking(),
                new IntegratedVariableByte()));
        testUnsorted2(new Composition(new IntegratedBinaryPacking(),
                new VariableByte()));
    }

    @Test
    public void fastPforTest_test0_decomposed()  {
        FastPFOR codec1 = FastPFOR.FastPFOR1();
        FastPFOR codec2 = FastPFOR.FastPFOR1();
    }

    @Test
    public void fastPforTest_test1_decomposed()  {
        FastPFOR codec1 = FastPFOR.FastPFOR1();
        FastPFOR codec2 = FastPFOR.FastPFOR1();
        int N = FastPFOR.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
    }

    @Test
    public void fastPforTest_test2_decomposed()  {
        FastPFOR codec1 = FastPFOR.FastPFOR1();
        FastPFOR codec2 = FastPFOR.FastPFOR1();
        int N = FastPFOR.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
        int[] answer = TestUtils.uncompress0(codec2, comp, N);
    }

    @Test
    public void fastPforTest_test3_decomposed()  {
        FastPFOR codec1 = FastPFOR.FastPFOR1();
        FastPFOR codec2 = FastPFOR.FastPFOR1();
        int N = FastPFOR.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
        int[] answer = TestUtils.uncompress0(codec2, comp, N);
        for (int k = 0; k < N; ++k)
            if (answer[k] != data[k])
                throw new RuntimeException("bug " + k + " " + answer[k]
                        + " != " + data[k]);
    }

    @Test
    public void fastPfor128Test_test0_decomposed()  {
        FastPFOR128 codec1 = FastPFOR128.FastPFOR1281();
        FastPFOR128 codec2 = FastPFOR128.FastPFOR1281();
    }

    @Test
    public void fastPfor128Test_test1_decomposed()  {
        FastPFOR128 codec1 = FastPFOR128.FastPFOR1281();
        FastPFOR128 codec2 = FastPFOR128.FastPFOR1281();
        int N = FastPFOR128.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
    }

    @Test
    public void fastPfor128Test_test2_decomposed()  {
        FastPFOR128 codec1 = FastPFOR128.FastPFOR1281();
        FastPFOR128 codec2 = FastPFOR128.FastPFOR1281();
        int N = FastPFOR128.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
        int[] answer = TestUtils.uncompress0(codec2, comp, N);
    }

    @Test
    public void fastPfor128Test_test3_decomposed()  {
        FastPFOR128 codec1 = FastPFOR128.FastPFOR1281();
        FastPFOR128 codec2 = FastPFOR128.FastPFOR1281();
        int N = FastPFOR128.BLOCK_SIZE;
        int[] data = new int[N];
        for (int i = 0; i < N; i++)
            data[i] = 0;
        data[126] = -1;
        int[] comp = TestUtils.compress1(codec1, Arrays.copyOf(data, N));
        int[] answer = TestUtils.uncompress0(codec2, comp, N);
        for (int k = 0; k < N; ++k)
            if (answer[k] != data[k])
                throw new RuntimeException("bug " + k + " " + answer[k]
                        + " != " + data[k]);
    }
}