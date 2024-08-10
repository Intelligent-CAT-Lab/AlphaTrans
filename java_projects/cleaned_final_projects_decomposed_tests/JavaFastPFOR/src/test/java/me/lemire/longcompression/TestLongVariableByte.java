/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.longcompression;

import java.util.stream.LongStream;

import org.junit.Assert;
import org.junit.Test;

/**
 * Edge-cases having caused issue specifically with LongVariableByte.
 * 
 * @author Benoit Lacelle
 */
public class TestLongVariableByte {
	final LongVariableByte codec = new LongVariableByte();

	private void checkConsistency(LongCODEC codec, long[] array) {
		{
			long[] compressed = LongTestUtils.compress1(codec, array);
			long[] uncompressed = LongTestUtils.uncompress0(codec, compressed, array.length);

			Assert.assertArrayEquals(array, uncompressed);
		}

		if (codec instanceof ByteLongCODEC) {
			byte[] compressed = LongTestUtils.compress0((ByteLongCODEC) codec, array);
			long[] uncompressed = LongTestUtils.uncompress1((ByteLongCODEC) codec, compressed, array.length);

			Assert.assertArrayEquals(array, uncompressed);
		}

		if (codec instanceof SkippableLongCODEC) {
			long[] compressed = LongTestUtils.compressHeadless((SkippableLongCODEC) codec, array);
			long[] uncompressed =
					LongTestUtils.uncompressHeadless((SkippableLongCODEC) codec, compressed, array.length);

			Assert.assertArrayEquals(array, uncompressed);
		}
	}

    @Test
    public void testCodec_ZeroMinus1_test0_decomposed()  {
        checkConsistency(codec, new long[] { -1 });
    }

    @Test
    public void testCodec_ZeroTimes8Minus1_test0_decomposed()  {
        checkConsistency(codec, new long[] { 0, 0, 0, 0, 0, 0, 0, 0, -1 });
    }

    @Test
    public void testCodec_ZeroTimes127Minus1_test0_decomposed()  {
        long[] array = LongStream.concat(LongStream.range(0, 127).map(l -> 0), LongStream.of(-1)).toArray();
        checkConsistency(codec, array);
    }

    @Test
    public void testCodec_ZeroTimes128Minus1_test0_decomposed()  {
        long[] array = LongStream.concat(LongStream.range(0, 128).map(l -> 0), LongStream.of(-1)).toArray();
        checkConsistency(codec, array);
    }

    @Test
    public void testCodec_MinValue_test0_decomposed()  {
        checkConsistency(codec, new long[] { Long.MIN_VALUE });
    }

    @Test
    public void testCodec_ZeroMinValue_test0_decomposed()  {
        checkConsistency(codec, new long[] { 0, Long.MIN_VALUE });
    }

    @Test
    public void testCodec_allPowerOfTwo_test0_decomposed()  {
        checkConsistency(codec, new long[] { 1L << 42 });
        for (int i = 0; i < 64; i++) {
			checkConsistency(codec, new long[] { 1L << i });
		}
    }

    @Test
    public void testCodec_ZeroThenAllPowerOfTwo_test0_decomposed()  {
        for (int i = 0; i < 64; i++) {
			checkConsistency(codec, new long[] { 0, 1L << i });
		}
    }

    @Test
    public void testCodec_intermediateHighPowerOfTwo_test0_decomposed()  {
        Assert.assertEquals(1, LongTestUtils.compress1((LongCODEC) codec, new long[] { 1L << 42 }).length);
    }

    @Test
    public void testCodec_intermediateHighPowerOfTwo_test1_decomposed()  {
        Assert.assertEquals(1, LongTestUtils.compress1((LongCODEC) codec, new long[] { 1L << 42 }).length);
        Assert.assertEquals(7, LongTestUtils.compress0((ByteLongCODEC) codec, new long[] { 1L << 42 }).length);
    }

    @Test
    public void testCodec_intermediateHighPowerOfTwo_test2_decomposed()  {
        Assert.assertEquals(1, LongTestUtils.compress1((LongCODEC) codec, new long[] { 1L << 42 }).length);
        Assert.assertEquals(7, LongTestUtils.compress0((ByteLongCODEC) codec, new long[] { 1L << 42 }).length);
        Assert.assertEquals(1, LongTestUtils.compressHeadless((SkippableLongCODEC) codec, new long[] { 1L << 42 }).length);
    }
}