/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.codec.binary;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import org.apache.commons.codec.binary.BaseNCodec.Context;
import org.junit.Assert;
import org.junit.Assume;
import org.junit.Before;
import org.junit.Test;

public class BaseNCodecTest {

    BaseNCodec codec;

    @Before
    public void setUp() {
        codec =
                new BaseNCodec(0, 0, 0, 0, 0, (byte) 0, null) {
                    @Override
                    protected boolean isInAlphabet0(final byte b) {
                        return b == 'O' || b == 'K'; // allow OK
                    }

                    @Override
                    void encode2(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}

                    @Override
                    void decode1(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}
                };
    }

    /**
     * Test the Context string representation has debugging info. This is not part of the API and
     * the test should be changed if the string format is updated.
     */
    

    

    

    

    

    

    

    

    

    /** Test to expand to the max buffer size. */
    

    /**
     * Test to expand to beyond the max buffer size.
     *
     * <p>Note: If the buffer is required to expand to above the max buffer size it may not work on
     * all VMs and may have to be annotated with @Ignore.
     */
    

    private static void assertEnsureBufferSizeExpandsToMaxBufferSize(
            final boolean exceedMaxBufferSize) {

        final int length = 0;

        final long presumableFreeMemory = getPresumableFreeMemory();
        final long estimatedMemory = (1L << 31) + 32 * 1024 + length;
        Assume.assumeTrue(
                "Not enough free memory for the test", presumableFreeMemory > estimatedMemory);

        final int max = Integer.MAX_VALUE - 8;

        if (exceedMaxBufferSize) {
            assumeCanAllocateBufferSize(max + 1);
            System.gc();
        }

        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();

        context.buffer = new byte[length];
        context.pos = length;
        int extra = max - length;
        if (exceedMaxBufferSize) {
            extra++;
        }
        ncodec.ensureBufferSize(extra, context);
        Assert.assertTrue(context.buffer.length >= length + extra);
    }

    /** Verify this VM can allocate the given size byte array. Otherwise skip the test. */
    private static void assumeCanAllocateBufferSize(final int size) {
        byte[] bytes = null;
        try {
            bytes = new byte[size];
        } catch (final OutOfMemoryError ignore) {
        }
        Assume.assumeTrue("Cannot allocate array of size: " + size, bytes != null);
    }

    /**
     * Gets the presumable free memory; an estimate of the amount of memory that could be allocated.
     *
     * <p>This performs a garbage clean-up and the obtains the presumed amount of free memory that
     * can be allocated in this VM. This is computed as:
     *
     * <p>
     *
     * <pre>
     * System.gc();
     * long allocatedMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
     * long presumableFreeMemory = Runtime.getRuntime().maxMemory() - allocatedMemory;
     * </pre>
     *
     * @return the presumable free memory
     * @see <a href="https://stackoverflow.com/a/18366283">Christian Fries StackOverflow answer on
     *     Java available memory</a>
     */
    static long getPresumableFreeMemory() {
        System.gc();
        final long allocatedMemory =
                Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
        return Runtime.getRuntime().maxMemory() - allocatedMemory;
    }

    

    /**
     * Extend BaseNCodec without implementation (no operations = NoOp). Used for testing the memory
     * allocation in {@link BaseNCodec#ensureBufferSize(int, Context)}.
     */
    private static class NoOpBaseNCodec extends BaseNCodec {
        NoOpBaseNCodec() {
            super(0, 0, 0, 0, 0, (byte) 0, null);
        }

        @Override
        void encode2(final byte[] pArray, final int i, final int length, final Context context) {}

        @Override
        void decode1(final byte[] pArray, final int i, final int length, final Context context) {}

        @Override
        protected boolean isInAlphabet0(final byte value) {
            return false;
        }
    }

    @Test
    public void testContextToString_test0_decomposed()  {
        final Context context = new Context();
    }

    @Test
    public void testContextToString_test1_decomposed()  {
        final Context context = new Context();
        context.buffer = new byte[3];
        context.currentLinePos = 13;
        context.eof = true;
        context.ibitWorkArea = 777;
        context.lbitWorkArea = 999;
        context.modulus = 5;
        context.pos = 42;
        context.readPos = 981;
        final String text = context.toString();
    }

    @Test
    public void testContextToString_test2_decomposed()  {
        final Context context = new Context();
        context.buffer = new byte[3];
        context.currentLinePos = 13;
        context.eof = true;
        context.ibitWorkArea = 777;
        context.lbitWorkArea = 999;
        context.modulus = 5;
        context.pos = 42;
        context.readPos = 981;
        final String text = context.toString();
        Assert.assertTrue(text.contains("[0, 0, 0]"));
        Assert.assertTrue(text.contains("13"));
        Assert.assertTrue(text.contains("true"));
        Assert.assertTrue(text.contains("777"));
        Assert.assertTrue(text.contains("999"));
        Assert.assertTrue(text.contains("5"));
        Assert.assertTrue(text.contains("42"));
        Assert.assertTrue(text.contains("981"));
    }

    @Test
    public void testBaseNCodec_test0_decomposed()  {
        assertNotNull(codec);
    }

    @Test
    public void testIsWhiteSpace_test0_decomposed()  {
        assertTrue(BaseNCodec.isWhiteSpace((byte) ' '));
        assertTrue(BaseNCodec.isWhiteSpace((byte) '\n'));
        assertTrue(BaseNCodec.isWhiteSpace((byte) '\r'));
        assertTrue(BaseNCodec.isWhiteSpace((byte) '\t'));
    }

    @Test
    public void testIsInAlphabetByte_test0_decomposed()  {
        assertFalse(codec.isInAlphabet0((byte) 0));
        assertFalse(codec.isInAlphabet0((byte) 'a'));
        assertTrue(codec.isInAlphabet0((byte) 'O'));
        assertTrue(codec.isInAlphabet0((byte) 'K'));
    }

    @Test
    public void testIsInAlphabetByteArrayBoolean_test0_decomposed()  {
        assertTrue(codec.isInAlphabet1(new byte[] {}, false));
        assertTrue(codec.isInAlphabet1(new byte[] {'O'}, false));
        assertFalse(codec.isInAlphabet1(new byte[] {'O', ' '}, false));
        assertFalse(codec.isInAlphabet1(new byte[] {' '}, false));
        assertTrue(codec.isInAlphabet1(new byte[] {}, true));
        assertTrue(codec.isInAlphabet1(new byte[] {'O'}, true));
        assertTrue(codec.isInAlphabet1(new byte[] {'O', ' '}, true));
        assertTrue(codec.isInAlphabet1(new byte[] {' '}, true));
    }

    @Test
    public void testIsInAlphabetString_test0_decomposed()  {
        assertTrue(codec.isInAlphabet2("OK"));
        assertTrue(codec.isInAlphabet2("O=K= \t\n\r"));
    }

    @Test
    public void testContainsAlphabetOrPad_test0_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
    }

    @Test
    public void testContainsAlphabetOrPad_test1_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
    }

    @Test
    public void testContainsAlphabetOrPad_test2_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
    }

    @Test
    public void testContainsAlphabetOrPad_test3_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
        "OK ".getBytes();
    }

    @Test
    public void testContainsAlphabetOrPad_test4_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
        "OK ".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK ".getBytes()));
    }

    @Test
    public void testContainsAlphabetOrPad_test5_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
        "OK ".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK ".getBytes()));
        "ok ".getBytes();
    }

    @Test
    public void testContainsAlphabetOrPad_test6_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
        "OK ".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK ".getBytes()));
        "ok ".getBytes();
        assertFalse(codec.containsAlphabetOrPad("ok ".getBytes()));
    }

    @Test
    public void testContainsAlphabetOrPad_test7_decomposed()  {
        assertFalse(codec.containsAlphabetOrPad(null));
        assertFalse(codec.containsAlphabetOrPad(new byte[] {}));
        "OK".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK".getBytes()));
        "OK ".getBytes();
        assertTrue(codec.containsAlphabetOrPad("OK ".getBytes()));
        "ok ".getBytes();
        assertFalse(codec.containsAlphabetOrPad("ok ".getBytes()));
        assertTrue(codec.containsAlphabetOrPad(new byte[] {codec.pad}));
    }

    @Test
    public void testProvidePaddingByte_test0_decomposed()  {
        codec =
                new BaseNCodec(1, 0, 0, 0, 0, (byte) 0x25, null) {
                    @Override
                    protected boolean isInAlphabet0(final byte b) {
                        return b == 'O' || b == 'K'; // allow OK
                    }

                    @Override
                    void encode2(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}

                    @Override
                    void decode1(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}
                };
    }

    @Test
    public void testProvidePaddingByte_test1_decomposed()  {
        codec =
                new BaseNCodec(1, 0, 0, 0, 0, (byte) 0x25, null) {
                    @Override
                    protected boolean isInAlphabet0(final byte b) {
                        return b == 'O' || b == 'K'; // allow OK
                    }

                    @Override
                    void encode2(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}

                    @Override
                    void decode1(
                            final byte[] pArray,
                            final int i,
                            final int length,
                            final Context context) {}
                };
        final byte actualPaddingByte = codec.pad;
        assertEquals(0x25, actualPaddingByte);
    }

    @Test
    public void testEnsureBufferSize_test0_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
    }

    @Test
    public void testEnsureBufferSize_test1_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
    }

    @Test
    public void testEnsureBufferSize_test2_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
    }

    @Test
    public void testEnsureBufferSize_test3_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
    }

    @Test
    public void testEnsureBufferSize_test4_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
    }

    @Test
    public void testEnsureBufferSize_test5_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
        ncodec.ensureBufferSize(1, context);
    }

    @Test
    public void testEnsureBufferSize_test6_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
        ncodec.ensureBufferSize(1, context);
        Assert.assertEquals(
                "buffer should not expand unless required",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
    }

    @Test
    public void testEnsureBufferSize_test7_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
        ncodec.ensureBufferSize(1, context);
        Assert.assertEquals(
                "buffer should not expand unless required",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        int length = context.buffer.length;
        context.pos = length;
        int extra = 1;
        ncodec.ensureBufferSize(extra, context);
    }

    @Test
    public void testEnsureBufferSize_test8_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
        ncodec.ensureBufferSize(1, context);
        Assert.assertEquals(
                "buffer should not expand unless required",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        int length = context.buffer.length;
        context.pos = length;
        int extra = 1;
        ncodec.ensureBufferSize(extra, context);
        Assert.assertTrue("buffer should expand", context.buffer.length >= length + extra);
        length = context.buffer.length;
        context.pos = length;
        extra = length * 10;
        ncodec.ensureBufferSize(extra, context);
    }

    @Test
    public void testEnsureBufferSize_test9_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        Assert.assertNull("Initial buffer should be null", context.buffer);
        context.pos = 76979;
        context.readPos = 273;
        ncodec.ensureBufferSize(0, context);
        Assert.assertNotNull("buffer should be initialized", context.buffer);
        Assert.assertEquals(
                "buffer should be initialized to default size",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        Assert.assertEquals("context position", 0, context.pos);
        Assert.assertEquals("context read position", 0, context.readPos);
        ncodec.ensureBufferSize(1, context);
        Assert.assertEquals(
                "buffer should not expand unless required",
                ncodec.getDefaultBufferSize(),
                context.buffer.length);
        int length = context.buffer.length;
        context.pos = length;
        int extra = 1;
        ncodec.ensureBufferSize(extra, context);
        Assert.assertTrue("buffer should expand", context.buffer.length >= length + extra);
        length = context.buffer.length;
        context.pos = length;
        extra = length * 10;
        ncodec.ensureBufferSize(extra, context);
        Assert.assertTrue(
                "buffer should expand beyond double capacity",
                context.buffer.length >= length + extra);
    }

    @Test
    public void testEnsureBufferSizeExpandsToMaxBufferSize_test0_decomposed()  {
        assertEnsureBufferSizeExpandsToMaxBufferSize(false);
    }

    @Test
    public void testEnsureBufferSizeExpandsToBeyondMaxBufferSize_test0_decomposed()  {
        assertEnsureBufferSizeExpandsToMaxBufferSize(true);
    }

    @Test
    public void testEnsureBufferSizeThrowsOnOverflow_test0_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
    }

    @Test
    public void testEnsureBufferSizeThrowsOnOverflow_test1_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
    }

    @Test(expected = OutOfMemoryError.class)
    public void testEnsureBufferSizeThrowsOnOverflow_test2_decomposed()  {
        final BaseNCodec ncodec = new NoOpBaseNCodec();
        final Context context = new Context();
        final int length = 10;
        context.buffer = new byte[length];
        context.pos = length;
        final int extra = Integer.MAX_VALUE;
        ncodec.ensureBufferSize(extra, context);
    }
}