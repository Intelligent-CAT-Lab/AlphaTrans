/**
 * This code is released under the
 * Apache License Version 2.0 http://www.apache.org/licenses/.
 *
 * (c) Daniel Lemire, http://lemire.me/en/
 */

package me.lemire.integercompression;

import java.util.ArrayList;
import me.lemire.integercompression.differential.IntegratedIntCompressor;
import me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC;

import java.io.BufferedReader;
import java.io.File;
import org.junit.Assert;
import java.io.FileReader;
import java.io.IOException;

import org.junit.Test;

/**
 * Tests with resources
 *
 */
public class ResourcedTest {
	SkippableIntegerCODEC[] codecs = { new JustCopy(), new VariableByte(),
			new SkippableComposition(new BinaryPacking(), new VariableByte()),
			new SkippableComposition(new NewPFD(), new VariableByte()),
			new SkippableComposition(new NewPFDS9(), new VariableByte()),
			new SkippableComposition(new NewPFDS16(), new VariableByte()),
			new SkippableComposition(new OptPFD(), new VariableByte()),
			new SkippableComposition(new OptPFDS9(), new VariableByte()),
			new SkippableComposition(new OptPFDS16(), new VariableByte()),
			new SkippableComposition(FastPFOR128.FastPFOR1281(), new VariableByte()),
			new SkippableComposition(FastPFOR.FastPFOR1(), new VariableByte()), new Simple9(), new Simple16() };

	/**
	 * @throws IOException
	 *             if the resource cannot be accessed (should be considered a
	 *             bug)
	 * 
	 */

    @Test
    public void IntCompressorTest_test0_decomposed() throws IOException {
        File f = new File("src/test/resources/integers.txt");
        System.out.println("loading test data from "+ f.getAbsolutePath());
        BufferedReader bfr = new BufferedReader(new FileReader(f));
        String line;
        ArrayList<Integer> ai = new ArrayList<Integer>();
        while ((line = bfr.readLine()) != null) {
			ai.add(Integer.parseInt(line));
		}
    }

    @Test
    public void IntCompressorTest_test1_decomposed() throws IOException {
        File f = new File("src/test/resources/integers.txt");
        System.out.println("loading test data from "+ f.getAbsolutePath());
        BufferedReader bfr = new BufferedReader(new FileReader(f));
        String line;
        ArrayList<Integer> ai = new ArrayList<Integer>();
        while ((line = bfr.readLine()) != null) {
			ai.add(Integer.parseInt(line));
		}
        bfr.close();
        int[] data = new int[ai.size()];
        for (int k = 0; k < data.length; ++k)
			data[k] = ai.get(k).intValue();
    }

    @Test
    public void IntCompressorTest_test2_decomposed() throws IOException {
        File f = new File("src/test/resources/integers.txt");
        System.out.println("loading test data from "+ f.getAbsolutePath());
        BufferedReader bfr = new BufferedReader(new FileReader(f));
        String line;
        ArrayList<Integer> ai = new ArrayList<Integer>();
        while ((line = bfr.readLine()) != null) {
			ai.add(Integer.parseInt(line));
		}
        bfr.close();
        int[] data = new int[ai.size()];
        for (int k = 0; k < data.length; ++k)
			data[k] = ai.get(k).intValue();
        ai = null;
        for (SkippableIntegerCODEC C : codecs) {
			IntCompressor iic = new IntCompressor(0, C);
			int[] compressed = iic.compress(data);
			int[] recovered = iic.uncompress(compressed);
			Assert.assertArrayEquals(recovered, data);

		}
    }

    @Test
    public void IntCompressorTest_test3_decomposed() throws IOException {
        File f = new File("src/test/resources/integers.txt");
        System.out.println("loading test data from "+ f.getAbsolutePath());
        BufferedReader bfr = new BufferedReader(new FileReader(f));
        String line;
        ArrayList<Integer> ai = new ArrayList<Integer>();
        while ((line = bfr.readLine()) != null) {
			ai.add(Integer.parseInt(line));
		}
        bfr.close();
        int[] data = new int[ai.size()];
        for (int k = 0; k < data.length; ++k)
			data[k] = ai.get(k).intValue();
        ai = null;
        for (SkippableIntegerCODEC C : codecs) {
			IntCompressor iic = new IntCompressor(0, C);
			int[] compressed = iic.compress(data);
			int[] recovered = iic.uncompress(compressed);
			Assert.assertArrayEquals(recovered, data);

		}
        for (SkippableIntegerCODEC C : codecs) {
			if (C instanceof SkippableIntegratedIntegerCODEC) {
				IntegratedIntCompressor iic = new IntegratedIntCompressor(0, (SkippableIntegratedIntegerCODEC) C);
				int[] compressed = iic.compress(data);
				int[] recovered = iic.uncompress(compressed);
				Assert.assertArrayEquals(recovered, data);
			}

		}
    }
}