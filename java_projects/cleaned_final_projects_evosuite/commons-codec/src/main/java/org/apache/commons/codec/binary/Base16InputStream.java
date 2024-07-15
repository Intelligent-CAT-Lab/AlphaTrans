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

import org.apache.commons.codec.CodecPolicy;

import java.io.InputStream;

/**
 * Provides Base16 encoding and decoding in a streaming fashion (unlimited size).
 *
 * <p>The default behavior of the Base16InputStream is to DECODE, whereas the default behavior of
 * the {@link Base16OutputStream} is to ENCODE, but this behavior can be overridden by using a
 * different constructor.
 *
 * @since 1.15
 */
public class Base16InputStream extends BaseNCodecInputStream {

    /**
     * Creates a Base16InputStream such that all data read is Base16-decoded from the original
     * provided InputStream.
     *
     * @param in InputStream to wrap.
     */
    public Base16InputStream(
            final InputStream in,
            final boolean doEncode,
            final boolean lowerCase,
            final CodecPolicy decodingPolicy) {
        super(in, new Base16(lowerCase, decodingPolicy), doEncode);
    }

    public static Base16InputStream Base16InputStream1(
            final InputStream in, final boolean doEncode, final boolean lowerCase) {
        return new Base16InputStream(in, doEncode, lowerCase, CodecPolicy.LENIENT);
    }

    public static Base16InputStream Base16InputStream2(
            final InputStream in, final boolean doEncode) {
        return Base16InputStream1(in, doEncode, false);
    }

    public static Base16InputStream Base16InputStream3(final InputStream in) {
        return Base16InputStream2(in, false);
    }

    /**
     * Creates a Base16InputStream such that all data read is either Base16-encoded or
     * Base16-decoded from the original provided InputStream.
     *
     * @param in InputStream to wrap.
     * @param doEncode true if we should encode all data read from us, false if we should decode.
     */

    /**
     * Creates a Base16InputStream such that all data read is either Base16-encoded or
     * Base16-decoded from the original provided InputStream.
     *
     * @param in InputStream to wrap.
     * @param doEncode true if we should encode all data read from us, false if we should decode.
     * @param lowerCase if {@code true} then use a lower-case Base16 alphabet.
     */

    /**
     * Creates a Base16InputStream such that all data read is either Base16-encoded or
     * Base16-decoded from the original provided InputStream.
     *
     * @param in InputStream to wrap.
     * @param doEncode true if we should encode all data read from us, false if we should decode.
     * @param lowerCase if {@code true} then use a lower-case Base16 alphabet.
     * @param decodingPolicy Decoding policy.
     */
}
