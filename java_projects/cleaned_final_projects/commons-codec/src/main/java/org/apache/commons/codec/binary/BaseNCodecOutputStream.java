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

import static org.apache.commons.codec.binary.BaseNCodec.EOF;

import org.apache.commons.codec.binary.BaseNCodec.Context;

import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Objects;

/**
 * Abstract superclass for Base-N output streams.
 *
 * <p>To write the EOF marker without closing the stream, call {@link #eof()} or use an <a
 * href="https://commons.apache.org/proper/commons-io/">Apache Commons IO</a> <a href=
 * "https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/output/CloseShieldOutputStream.html"
 * >CloseShieldOutputStream</a>.
 *
 * @since 1.5
 */
public class BaseNCodecOutputStream extends FilterOutputStream {

    private final boolean doEncode;

    private final BaseNCodec baseNCodec;

    private final byte[] singleByte = new byte[1];

    private final Context context = new Context();

    /**
     * TODO should this be protected?
     *
     * @param output the underlying output or null.
     * @param basedCodec a BaseNCodec.
     * @param doEncode true to encode, false to decode, TODO should be an enum?
     */
    public BaseNCodecOutputStream(
            final OutputStream output, final BaseNCodec basedCodec, final boolean doEncode) {
        super(output);
        this.baseNCodec = basedCodec;
        this.doEncode = doEncode;
    }

    /**
     * Closes this output stream and releases any system resources associated with the stream.
     *
     * <p>To write the EOF marker without closing the stream, call {@link #eof()} or use an <a
     * href="https://commons.apache.org/proper/commons-io/">Apache Commons IO</a> <a href=
     * "https://commons.apache.org/proper/commons-io/apidocs/org/apache/commons/io/output/CloseShieldOutputStream.html"
     * >CloseShieldOutputStream</a>.
     *
     * @throws IOException if an I/O error occurs.
     */
    @Override
    public void close() throws IOException {
        eof();
        flush0();
        out.close();
    }

    /**
     * Writes EOF.
     *
     * @throws IOException if an I/O error occurs.
     * @since 1.11
     */
    public void eof() throws IOException {
        if (doEncode) {
            baseNCodec.encode2(singleByte, 0, EOF, context);
        } else {
            baseNCodec.decode1(singleByte, 0, EOF, context);
        }
    }

    /**
     * Flushes this output stream and forces any buffered output bytes to be written out to the
     * stream.
     *
     * @throws IOException if an I/O error occurs.
     */
    public void flush0() throws IOException {
        flush1(true);
    }

    /**
     * Flushes this output stream and forces any buffered output bytes to be written out to the
     * stream. If propagate is true, the wrapped stream will also be flushed.
     *
     * @param propagate boolean flag to indicate whether the wrapped OutputStream should also be
     *     flushed.
     * @throws IOException if an I/O error occurs.
     */
    private void flush1(final boolean propagate) throws IOException {
        final int avail = baseNCodec.available(context);
        if (avail > 0) {
            final byte[] buf = new byte[avail];
            final int c = baseNCodec.readResults(buf, 0, avail, context);
            if (c > 0) {
                out.write(buf, 0, c);
            }
        }
        if (propagate) {
            out.flush();
        }
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
     * Writes {@code len} bytes from the specified {@code b} array starting at {@code offset} to
     * this output stream.
     *
     * @param array source byte array
     * @param offset where to start reading the bytes
     * @param len maximum number of bytes to write
     * @throws IOException if an I/O error occurs.
     * @throws NullPointerException if the byte array parameter is null
     * @throws IndexOutOfBoundsException if offset, len or buffer size are invalid
     */
    public void write0(final byte array[], final int offset, final int len) throws IOException {
        Objects.requireNonNull(array, "array");
        if (offset < 0 || len < 0) {
            throw new IndexOutOfBoundsException();
        }
        if (offset > array.length || offset + len > array.length) {
            throw new IndexOutOfBoundsException();
        }
        if (len > 0) {
            if (doEncode) {
                baseNCodec.encode2(array, offset, len, context);
            } else {
                baseNCodec.decode1(array, offset, len, context);
            }
            flush1(false);
        }
    }

    /**
     * Writes the specified {@code byte} to this output stream.
     *
     * @param i source byte
     * @throws IOException if an I/O error occurs.
     */
    @Override
    public void write(final int i) throws IOException {
        write1(i);
    }

    public void write1(final int i) throws IOException {
        singleByte[0] = (byte) i;
        write0(singleByte, 0, 1);
    }
}
