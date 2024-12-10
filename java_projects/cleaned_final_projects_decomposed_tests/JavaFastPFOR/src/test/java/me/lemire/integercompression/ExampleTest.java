/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.integercompression;

import me.lemire.integercompression.differential.*;
import java.util.*;

import org.junit.Test;

/**
 * 
 *
 */
public class ExampleTest {
	/**
	 * 
	 */
	

	/**
	 * 
	 */
	

	/**
	 * Like the basicExample, but we store the input array size manually.
	 */
	

	/**
	 * This is an example to show you can compress unsorted integers as long as
	 * most are small.
	 */
	

	/**
	 * This is like the basic example, but we show how to process larger arrays
	 * in chunks.
	 *
	 * Some of this code was written by Pavel Klinov.
	 */
	

	/**
	 * Demo of the headless approach where we must supply the array length
	 */

    @Test
    public void superSimpleExample_test0_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
    }

    @Test
    public void superSimpleExample_test1_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        System.out.println("Compressing " + data.length + " integers using friendly interface");
        int[] compressed = iic.compress(data);
    }

    @Test
    public void superSimpleExample_test2_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        System.out.println("Compressing " + data.length + " integers using friendly interface");
        int[] compressed = iic.compress(data);
        int[] recov = iic.uncompress(compressed);
    }

    @Test
    public void superSimpleExample_test3_decomposed()  {
        IntegratedIntCompressor iic = new IntegratedIntCompressor(1, null);
        int[] data = new int[2342351];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        System.out.println("Compressing " + data.length + " integers using friendly interface");
        int[] compressed = iic.compress(data);
        int[] recov = iic.uncompress(compressed);
        System.out
				.println("compressed from " + data.length * 4 / 1024 + "KB to " + compressed.length * 4 / 1024 + "KB");
        if (!Arrays.equals(recov, data))
			throw new RuntimeException("bug");
    }

    @Test
    public void basicExample_test0_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
    }

    @Test
    public void basicExample_test1_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
    }

    @Test
    public void basicExample_test2_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
    }

    @Test
    public void basicExample_test3_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
    }

    @Test
    public void basicExample_test4_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
    }

    @Test
    public void basicExample_test5_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[data.length];
        IntWrapper recoffset = new IntWrapper(0);
    }

    @Test
    public void basicExample_test6_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[data.length];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length, recovered, recoffset);
    }

    @Test
    public void basicExample_test7_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC codec = new IntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[data.length];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length, recovered, recoffset);
        if (Arrays.equals(data, recovered))
			System.out.println("data is recovered without loss");
		else
			throw new RuntimeException("bug");
        System.out.println();
    }

    @Test
    public void basicExampleHeadless_test0_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
    }

    @Test
    public void basicExampleHeadless_test1_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
    }

    @Test
    public void basicExampleHeadless_test2_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
    }

    @Test
    public void basicExampleHeadless_test3_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
        compressed[0] = data.length;
        codec.headlessCompress(data, inputoffset, data.length, compressed, outputoffset, new IntWrapper(0));
    }

    @Test
    public void basicExampleHeadless_test4_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
        compressed[0] = data.length;
        codec.headlessCompress(data, inputoffset, data.length, compressed, outputoffset, new IntWrapper(0));
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
    }

    @Test
    public void basicExampleHeadless_test5_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
        compressed[0] = data.length;
        codec.headlessCompress(data, inputoffset, data.length, compressed, outputoffset, new IntWrapper(0));
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int howmany = compressed[0];
        int[] recovered = new int[howmany];
        IntWrapper recoffset = new IntWrapper(0);
    }

    @Test
    public void basicExampleHeadless_test6_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
        compressed[0] = data.length;
        codec.headlessCompress(data, inputoffset, data.length, compressed, outputoffset, new IntWrapper(0));
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int howmany = compressed[0];
        int[] recovered = new int[howmany];
        IntWrapper recoffset = new IntWrapper(0);
        codec.headlessUncompress(compressed, new IntWrapper(1), compressed.length, recovered, recoffset, howmany, new IntWrapper(0));
    }

    @Test
    public void basicExampleHeadless_test7_decomposed()  {
        int[] data = new int[2342351];
        System.out.println("Compressing " + data.length + " integers in one go using the headless approach");
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        SkippableIntegratedComposition codec = new SkippableIntegratedComposition(new IntegratedBinaryPacking(),
				new IntegratedVariableByte());
        int[] compressed = new int[data.length + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(1);
        compressed[0] = data.length;
        codec.headlessCompress(data, inputoffset, data.length, compressed, outputoffset, new IntWrapper(0));
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int howmany = compressed[0];
        int[] recovered = new int[howmany];
        IntWrapper recoffset = new IntWrapper(0);
        codec.headlessUncompress(compressed, new IntWrapper(1), compressed.length, recovered, recoffset, howmany, new IntWrapper(0));
        if (Arrays.equals(data, recovered))
			System.out.println("data is recovered without loss");
		else
			throw new RuntimeException("bug");
        System.out.println();
    }

    @Test
    public void unsortedExample_test0_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
    }

    @Test
    public void unsortedExample_test1_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
    }

    @Test
    public void unsortedExample_test2_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
    }

    @Test
    public void unsortedExample_test3_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
    }

    @Test
    public void unsortedExample_test4_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println("compressed unsorted integers from " + data.length * 4 / 1024 + "KB to "
				+ outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
    }

    @Test
    public void unsortedExample_test5_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println("compressed unsorted integers from " + data.length * 4 / 1024 + "KB to "
				+ outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[N];
        IntWrapper recoffset = new IntWrapper(0);
    }

    @Test
    public void unsortedExample_test6_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println("compressed unsorted integers from " + data.length * 4 / 1024 + "KB to "
				+ outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[N];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length, recovered, recoffset);
    }

    @Test
    public void unsortedExample_test7_decomposed()  {
        final int N = 1333333;
        int[] data = new int[N];
        for (int k = 0; k < N; k += 1)
			data[k] = 3;
        for (int k = 0; k < N; k += 5)
			data[k] = 100;
        for (int k = 0; k < N; k += 533)
			data[k] = 10000;
        int[] compressed = new int[N + 1024];
        IntegerCODEC codec = new Composition(FastPFOR.FastPFOR1(), new VariableByte());
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        codec.compress0(data, inputoffset, data.length, compressed, outputoffset);
        System.out.println("compressed unsorted integers from " + data.length * 4 / 1024 + "KB to "
				+ outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[N];
        IntWrapper recoffset = new IntWrapper(0);
        codec.uncompress0(compressed, new IntWrapper(0), compressed.length, recovered, recoffset);
        if (Arrays.equals(data, recovered))
			System.out.println("data is recovered without loss");
		else
			throw new RuntimeException("bug");
        System.out.println();
    }

    @Test
    public void advancedExample_test0_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
    }

    @Test
    public void advancedExample_test1_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
    }

    @Test
    public void advancedExample_test2_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
    }

    @Test
    public void advancedExample_test3_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
    }

    @Test
    public void advancedExample_test4_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
    }

    @Test
    public void advancedExample_test5_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        for (int k = 0; k < TotalSize / ChunkSize; ++k)
			regularcodec.compress0(data, inputoffset, ChunkSize, compressed, outputoffset);
        lastcodec.compress0(data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset);
    }

    @Test
    public void advancedExample_test6_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        for (int k = 0; k < TotalSize / ChunkSize; ++k)
			regularcodec.compress0(data, inputoffset, ChunkSize, compressed, outputoffset);
        lastcodec.compress0(data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
    }

    @Test
    public void advancedExample_test7_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        for (int k = 0; k < TotalSize / ChunkSize; ++k)
			regularcodec.compress0(data, inputoffset, ChunkSize, compressed, outputoffset);
        lastcodec.compress0(data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[ChunkSize];
        IntWrapper compoff = new IntWrapper(0);
    }

    @Test
    public void advancedExample_test8_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        for (int k = 0; k < TotalSize / ChunkSize; ++k)
			regularcodec.compress0(data, inputoffset, ChunkSize, compressed, outputoffset);
        lastcodec.compress0(data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[ChunkSize];
        IntWrapper compoff = new IntWrapper(0);
        IntWrapper recoffset;
        int currentpos = 0;
        while (compoff.get() < compressed.length) {
			recoffset = new IntWrapper(0);
			regularcodec.uncompress0(compressed, compoff, compressed.length - compoff.get(), recovered, recoffset);

			if (recoffset.get() < ChunkSize) {// last chunk detected
				ivb.uncompress0(compressed, compoff, compressed.length - compoff.get(), recovered, recoffset);
			}
			for (int i = 0; i < recoffset.get(); ++i) {
				if (data[currentpos + i] != recovered[i])
					throw new RuntimeException("bug"); // could use assert
			}
			currentpos += recoffset.get();
		}
    }

    @Test
    public void advancedExample_test9_decomposed()  {
        int TotalSize = 2342351;
        int ChunkSize = 16384;
        System.out.println("Compressing " + TotalSize + " integers using chunks of " + ChunkSize + " integers ("
				+ ChunkSize * 4 / 1024 + "KB)");
        System.out.println("(It is often better for applications to work in chunks fitting in CPU cache.)");
        int[] data = new int[TotalSize];
        for (int k = 0; k < data.length; ++k)
			data[k] = k;
        IntegratedIntegerCODEC regularcodec = new IntegratedBinaryPacking();
        IntegratedVariableByte ivb = new IntegratedVariableByte();
        IntegratedIntegerCODEC lastcodec = new IntegratedComposition(regularcodec, ivb);
        int[] compressed = new int[TotalSize + 1024];
        IntWrapper inputoffset = new IntWrapper(0);
        IntWrapper outputoffset = new IntWrapper(0);
        for (int k = 0; k < TotalSize / ChunkSize; ++k)
			regularcodec.compress0(data, inputoffset, ChunkSize, compressed, outputoffset);
        lastcodec.compress0(data, inputoffset, TotalSize % ChunkSize, compressed, outputoffset);
        System.out.println(
				"compressed from " + data.length * 4 / 1024 + "KB to " + outputoffset.intValue() * 4 / 1024 + "KB");
        compressed = Arrays.copyOf(compressed, outputoffset.intValue());
        int[] recovered = new int[ChunkSize];
        IntWrapper compoff = new IntWrapper(0);
        IntWrapper recoffset;
        int currentpos = 0;
        while (compoff.get() < compressed.length) {
			recoffset = new IntWrapper(0);
			regularcodec.uncompress0(compressed, compoff, compressed.length - compoff.get(), recovered, recoffset);

			if (recoffset.get() < ChunkSize) {// last chunk detected
				ivb.uncompress0(compressed, compoff, compressed.length - compoff.get(), recovered, recoffset);
			}
			for (int i = 0; i < recoffset.get(); ++i) {
				if (data[currentpos + i] != recovered[i])
					throw new RuntimeException("bug"); // could use assert
			}
			currentpos += recoffset.get();
		}
        System.out.println("data is recovered without loss");
        System.out.println();
    }

    @Test
    public void headlessDemo_test0_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
    }

    @Test
    public void headlessDemo_test1_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
    }

    @Test
    public void headlessDemo_test2_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
    }

    @Test
    public void headlessDemo_test3_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
    }

    @Test
    public void headlessDemo_test4_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
    }

    @Test
    public void headlessDemo_test5_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
    }

    @Test
    public void headlessDemo_test6_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
        int length2 = outPos.get() - previous.get();
    }

    @Test
    public void headlessDemo_test7_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
        int length2 = outPos.get() - previous.get();
        compressed = Arrays.copyOf(compressed, length1 + length2);
        System.out
				.println("compressed unsorted integers from " + uncompressed1.length * 4 + "B to " + length1 * 4 + "B");
        System.out
				.println("compressed unsorted integers from " + uncompressed2.length * 4 + "B to " + length2 * 4 + "B");
        System.out.println("Total compressed output " + compressed.length);
        int[] recovered1 = new int[uncompressed1.length];
        int[] recovered2 = new int[uncompressed1.length];
        IntWrapper inPos = IntWrapper.IntWrapper1();
    }

    @Test
    public void headlessDemo_test8_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
        int length2 = outPos.get() - previous.get();
        compressed = Arrays.copyOf(compressed, length1 + length2);
        System.out
				.println("compressed unsorted integers from " + uncompressed1.length * 4 + "B to " + length1 * 4 + "B");
        System.out
				.println("compressed unsorted integers from " + uncompressed2.length * 4 + "B to " + length2 * 4 + "B");
        System.out.println("Total compressed output " + compressed.length);
        int[] recovered1 = new int[uncompressed1.length];
        int[] recovered2 = new int[uncompressed1.length];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        System.out.println("Decoding first array starting at pos = " + inPos);
        codec.headlessUncompress(compressed, inPos, compressed.length, recovered1, new IntWrapper(0),
				uncompressed1.length);
    }

    @Test
    public void headlessDemo_test9_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
        int length2 = outPos.get() - previous.get();
        compressed = Arrays.copyOf(compressed, length1 + length2);
        System.out
				.println("compressed unsorted integers from " + uncompressed1.length * 4 + "B to " + length1 * 4 + "B");
        System.out
				.println("compressed unsorted integers from " + uncompressed2.length * 4 + "B to " + length2 * 4 + "B");
        System.out.println("Total compressed output " + compressed.length);
        int[] recovered1 = new int[uncompressed1.length];
        int[] recovered2 = new int[uncompressed1.length];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        System.out.println("Decoding first array starting at pos = " + inPos);
        codec.headlessUncompress(compressed, inPos, compressed.length, recovered1, new IntWrapper(0),
				uncompressed1.length);
        System.out.println("Decoding second array starting at pos = " + inPos);
        codec.headlessUncompress(compressed, inPos, compressed.length, recovered2, new IntWrapper(0),
				uncompressed2.length);
    }

    @Test
    public void headlessDemo_test10_decomposed()  {
        System.out.println("Compressing arrays with minimal header...");
        int[] uncompressed1 = { 1, 2, 1, 3, 1 };
        int[] uncompressed2 = { 3, 2, 4, 6, 1 };
        int[] compressed = new int[uncompressed1.length + uncompressed2.length + 1024];
        SkippableIntegerCODEC codec = new SkippableComposition(new BinaryPacking(), new VariableByte());
        IntWrapper outPos = IntWrapper.IntWrapper1();
        IntWrapper previous = IntWrapper.IntWrapper1();
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed1, IntWrapper.IntWrapper1(), uncompressed1.length, compressed, outPos);
        int length1 = outPos.get() - previous.get();
        previous = new IntWrapper(outPos.get());
        IntWrapper.IntWrapper1();
        codec.headlessCompress(uncompressed2, IntWrapper.IntWrapper1(), uncompressed2.length, compressed, outPos);
        int length2 = outPos.get() - previous.get();
        compressed = Arrays.copyOf(compressed, length1 + length2);
        System.out
				.println("compressed unsorted integers from " + uncompressed1.length * 4 + "B to " + length1 * 4 + "B");
        System.out
				.println("compressed unsorted integers from " + uncompressed2.length * 4 + "B to " + length2 * 4 + "B");
        System.out.println("Total compressed output " + compressed.length);
        int[] recovered1 = new int[uncompressed1.length];
        int[] recovered2 = new int[uncompressed1.length];
        IntWrapper inPos = IntWrapper.IntWrapper1();
        System.out.println("Decoding first array starting at pos = " + inPos);
        codec.headlessUncompress(compressed, inPos, compressed.length, recovered1, new IntWrapper(0),
				uncompressed1.length);
        System.out.println("Decoding second array starting at pos = " + inPos);
        codec.headlessUncompress(compressed, inPos, compressed.length, recovered2, new IntWrapper(0),
				uncompressed2.length);
        if (!Arrays.equals(uncompressed1, recovered1))
			throw new RuntimeException("First array does not match.");
        if (!Arrays.equals(uncompressed2, recovered2))
			throw new RuntimeException("Second array does not match.");
        System.out.println("The arrays match, your code is probably ok.");
    }
}