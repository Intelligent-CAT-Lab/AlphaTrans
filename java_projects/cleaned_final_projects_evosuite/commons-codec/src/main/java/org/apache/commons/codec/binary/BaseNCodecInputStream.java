
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


package org.apache.commons.codec.binary;

import static org.apache.commons.codec.binary.BaseNCodec.EOF;

import org.apache.commons.codec.binary.BaseNCodec.Context;

import java.io.FilterInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Objects;

/**
 * Abstract superclass for Base-N input streams.
 *
 * @since 1.5
 */
public class BaseNCodecInputStream extends FilterInputStream {

    private final BaseNCodec baseNCodec;

    private final boolean doEncode;

    private final byte[] singleByte = new byte[1];

    private final byte[] buf;

    private final Context context = new Context();

    protected BaseNCodecInputStream(
            final InputStream input, final BaseNCodec baseNCodec, final boolean doEncode) {
        super(input);
        this.doEncode = doEncode;
        this.baseNCodec = baseNCodec;
        this.buf = new byte[doEncode ? 4096 : 8192];
    }

    /**
     * {@inheritDoc}
     *
     * @return {@code 0} if the {@link InputStream} has reached {@code EOF}, {@code 1} otherwise
     * @since 1.7
     */
    @Override
    public int available() throws IOException {

        return context.eof ? 0 : 1;
    }

    /**
     * Returns true if decoding behavior is strict. Decoding will raise an {@link
     * IllegalArgumentException} if trailing bits are not part of a valid encoding.
     *
     * <p>The default is false for lenient encoding. Decoding will compose trailing bits into 8-bit
     * bytes and discard the remainder.
     *
     * @return true if using strict decoding
     * @since 1.15
     */
    public boolean isStrictDecoding() {
        return baseNCodec.isStrictDecoding();
    }

    /**
     * Marks the current position in this input stream.
     *
     * <p>The {@link #mark} method of {@link BaseNCodecInputStream} does nothing.
     *
     * @param readLimit the maximum limit of bytes that can be read before the mark position becomes
     *     invalid.
     * @see #markSupported()
     * @since 1.7
     */
    @Override
    public synchronized void mark(final int readLimit) {}

    /**
     * {@inheritDoc}
     *
     * @return Always returns {@code false}
     */
    @Override
    public boolean markSupported() {
        return false; // not an easy job to support marks
    }

    /**
     * Reads one {@code byte} from this input stream.
     *
     * @return the byte as an integer in the range 0 to 255. Returns -1 if EOF has been reached.
     * @throws IOException if an I/O error occurs.
     */
    public int read0() throws IOException {
        int r = read1(singleByte, 0, 1);
        while (r == 0) {
            r = read1(singleByte, 0, 1);
        }
        if (r > 0) {
            final byte b = singleByte[0];
            return b < 0 ? 256 + b : b;
        }
        return EOF;
    }

    /**
     * Attempts to read {@code len} bytes into the specified {@code b} array starting at {@code
     * offset} from this InputStream.
     *
     * @param array destination byte array
     * @param offset where to start writing the bytes
     * @param len maximum number of bytes to read
     * @return number of bytes read
     * @throws IOException if an I/O error occurs.
     * @throws NullPointerException if the byte array parameter is null
     * @throws IndexOutOfBoundsException if offset, len or buffer size are invalid
     */
    public int read1(final byte array[], final int offset, final int len) throws IOException {
        Objects.requireNonNull(array, "array");
        if (offset < 0 || len < 0) {
            throw new IndexOutOfBoundsException();
        }
        if (offset > array.length || offset + len > array.length) {
            throw new IndexOutOfBoundsException();
        }
        if (len == 0) {
            return 0;
        }
        int readLen = 0;
        /*
         Rationale for while-loop on (readLen == 0):
         -----
         Base32.readResults() usually returns > 0 or EOF (-1).  In the
         rare case where it returns 0, we just keep trying.

         This is essentially an undocumented contract for InputStream
         implementors that want their code to work properly with
         java.io.InputStreamReader, since the latter hates it when
         InputStream.read(byte[]) returns a zero.  Unfortunately our
         readResults() call must return 0 if a large amount of the data
         being decoded was non-base32, so this while-loop enables proper
         interop with InputStreamReader for that scenario.
         -----
         This is a fix for CODEC-101
        */
        while (readLen < len) {
            if (!baseNCodec.hasData(context)) {
                final int c = in.read(buf);
                if (doEncode) {
                    baseNCodec.encode2(buf, 0, c, context);
                } else {
                    baseNCodec.decode1(buf, 0, c, context);
                }
            }
            final int read =
                    baseNCodec.readResults(array, offset + readLen, len - readLen, context);
            if (read < 0) {
                return readLen != 0 ? readLen : -1;
            }
            readLen += read;
        }
        return readLen;
    }

    /**
     * Repositions this stream to the position at the time the mark method was last called on this
     * input stream.
     *
     * <p>The {@link #reset} method of {@link BaseNCodecInputStream} does nothing except throw an
     * {@link IOException}.
     *
     * @throws IOException if this method is invoked
     * @since 1.7
     */
    @Override
    public synchronized void reset() throws IOException {
        throw new IOException("mark/reset not supported");
    }

    /**
     * {@inheritDoc}
     *
     * @throws IllegalArgumentException if the provided skip length is negative
     * @since 1.7
     */
    @Override
    public long skip(final long n) throws IOException {
        if (n < 0) {
            throw new IllegalArgumentException("Negative skip length: " + n);
        }

        final byte[] b = new byte[512];
        long todo = n;

        while (todo > 0) {
            int len = (int) Math.min(b.length, todo);
            len = this.read1(b, 0, len);
            if (len == EOF) {
                break;
            }
            todo -= len;
        }

        return n - todo;
    }
}
