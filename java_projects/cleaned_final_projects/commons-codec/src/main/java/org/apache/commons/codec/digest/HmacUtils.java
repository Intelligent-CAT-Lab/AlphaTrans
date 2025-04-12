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

package org.apache.commons.codec.digest;

/**
 * Simplifies common {@link javax.crypto.Mac} tasks. This class is immutable and thread-safe.
 * However the Mac may not be.
 *
 * <p><strong>Note: Not all JCE implementations support all algorithms. If not supported, an
 * IllegalArgumentException is thrown.</strong>
 *
 * <p>Sample usage:
 *
 * <pre>
 * import static HmacAlgorithms.*;
 * byte[] key = {1,2,3,4}; // don't use this actual key!
 * String valueToDigest = "The quick brown fox jumps over the lazy dog";
 * byte[] hmac = new HmacUtils(HMAC_SHA_224, key).hmac(valueToDigest);
 * // Mac re-use
 * HmacUtils hm1 = new HmacUtils("HmacAlgoName", key); // use a valid name here!
 * String hexPom = hm1.hmacHex(new File("pom.xml"));
 * String hexNot = hm1.hmacHex(new File("NOTICE.txt"));
 * </pre>
 *
 * @since 1.10
 */
public final class HmacUtils {

    private static final int STREAM_BUFFER_LENGTH = 1024;

    /**
     * Returns whether this algorithm is available
     *
     * @param name the name to check
     * @return whether this algorithm is available
     * @since 1.11
     */

    /**
     * Returns whether this algorithm is available
     *
     * @param name the name to check
     * @return whether this algorithm is available
     * @since 1.11
     */

    /**
     * Returns an initialized {@code Mac} for the HmacMD5 algorithm.
     *
     * <p>Every implementation of the Java platform is required to support this standard Mac
     * algorithm.
     *
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code getInitializedMac(HmacAlgorithms.HMAC_MD5, byte[])}
     */

    /**
     * Returns an initialized {@code Mac} for the HmacSHA1 algorithm.
     *
     * <p>Every implementation of the Java platform is required to support this standard Mac
     * algorithm.
     *
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code getInitializedMac(HmacAlgorithms.HMAC_SHA_1, byte[])}
     */

    /**
     * Returns an initialized {@code Mac} for the HmacSHA256 algorithm.
     *
     * <p>Every implementation of the Java platform is required to support this standard Mac
     * algorithm.
     *
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code getInitializedMac(HmacAlgorithms.HMAC_SHA_256, byte[])}
     */

    /**
     * Returns an initialized {@code Mac} for the HmacSHA384 algorithm.
     *
     * <p>Every implementation of the Java platform is <em>not</em> required to support this Mac
     * algorithm.
     *
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code getInitializedMac(HmacAlgorithms.HMAC_SHA_384, byte[])}
     */

    /**
     * Returns an initialized {@code Mac} for the HmacSHA512 algorithm.
     *
     * <p>Every implementation of the Java platform is <em>not</em> required to support this Mac
     * algorithm.
     *
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code getInitializedMac(HmacAlgorithms.HMAC_SHA_512, byte[])}
     */

    /**
     * Returns an initialized {@code Mac} for the given {@code algorithm}.
     *
     * @param algorithm the name of the algorithm requested. See <a href=
     *     "http://docs.oracle.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA"
     *     >Appendix A in the Java Cryptography Architecture Reference Guide</a> for information
     *     about standard algorithm names.
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     */

    /**
     * Returns an initialized {@code Mac} for the given {@code algorithm}.
     *
     * @param algorithm the name of the algorithm requested. See <a href=
     *     "http://docs.oracle.com/javase/6/docs/technotes/guides/security/crypto/CryptoSpec.html#AppA"
     *     >Appendix A in the Java Cryptography Architecture Reference Guide</a> for information
     *     about standard algorithm names.
     * @param key The key for the keyed digest (must not be null)
     * @return A Mac instance initialized with the given key.
     * @see Mac#getInstance(String)
     * @see Mac#init(Key)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacMD5 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5, byte[]).hmac(byte[])}
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacMD5 MAC for the given key and value
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5,
     *     byte[]).hmac(InputStream)}
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacMD5 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5, String).hmac(String)}
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) as a hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacMD5 MAC for the given key and value as a hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5, byte[]).hmacHex(byte[])}
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) as a hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacMD5 MAC for the given key and value as a hex string (lowercase)
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5,
     *     byte[]).hmacHex(InputStream)}
     */

    /**
     * Returns a HmacMD5 Message Authentication Code (MAC) as a hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacMD5 MAC for the given key and value as a hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_MD5, String).hmacHex(String)}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA1 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1, byte[]).hmac(byte[])}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA1 MAC for the given key and value
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1,
     *     byte[]).hmac(InputStream)}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA1 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1, String).hmac(String)}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) as hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA1 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1,
     *     byte[]).hmacHex(byte[])}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) as hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA1 MAC for the given key and value as hex string (lowercase)
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1,
     *     byte[]).hmacHex(InputStream)}
     */

    /**
     * Returns a HmacSHA1 Message Authentication Code (MAC) as hex string (lowercase) for the given
     * key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA1 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_1,
     *     String).hmacHex(String)}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA256 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     byte[]).hmac(byte[])}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA256 MAC for the given key and value
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     byte[]).hmac(InputStream)}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA256 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     String).hmac(String)}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA256 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     byte[]).hmacHex(byte[])}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA256 MAC for the given key and value as hex string (lowercase)
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     byte[]).hmacHex(InputStream)}
     */

    /**
     * Returns a HmacSHA256 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA256 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_256,
     *     String).hmacHex(String)}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA384 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     byte[]).hmac(byte[])}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA384 MAC for the given key and value
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     byte[]).hmac(InputStream)}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA384 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     String).hmac(String)}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA384 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     byte[]).hmacHex(byte[])}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA384 MAC for the given key and value as hex string (lowercase)
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     byte[]).hmacHex(InputStream)}
     */

    /**
     * Returns a HmacSHA384 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA384 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_384,
     *     String).hmacHex(String)}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA512 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     byte[]).hmac(byte[])}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA512 MAC for the given key and value
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     byte[]).hmac(InputStream)}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) for the given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA512 MAC for the given key and value
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     String).hmac(String)}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA512 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     byte[]).hmacHex(byte[])}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest
     *     <p>The InputStream must not be null and will not be closed
     * @return HmacSHA512 MAC for the given key and value as hex string (lowercase)
     * @throws IOException If an I/O error occurs.
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     byte[]).hmacHex(InputStream)}
     */

    /**
     * Returns a HmacSHA512 Message Authentication Code (MAC) as hex string (lowercase) for the
     * given key and value.
     *
     * @param key The key for the keyed digest (must not be null)
     * @param valueToDigest The value (data) which should to digest (maybe empty or null)
     * @return HmacSHA512 MAC for the given key and value as hex string (lowercase)
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @deprecated (1.11) Use {@code new HmacUtils(HmacAlgorithms.HMAC_SHA_512,
     *     String).hmacHex(String)}
     */

    /**
     * Resets and then updates the given {@link Mac} with the value.
     *
     * @param mac the initialized {@link Mac} to update
     * @param valueToDigest the value to update the {@link Mac} with (maybe null or empty)
     * @return the updated {@link Mac}
     * @throws IllegalStateException if the Mac was not initialized
     */

    /**
     * Resets and then updates the given {@link Mac} with the value.
     *
     * @param mac the initialized {@link Mac} to update
     * @param valueToDigest the value to update the {@link Mac} with
     *     <p>The InputStream must not be null and will not be closed
     * @return the updated {@link Mac}
     * @throws IOException If an I/O error occurs.
     * @throws IllegalStateException If the Mac was not initialized
     */

    /**
     * Resets and then updates the given {@link Mac} with the value.
     *
     * @param mac the initialized {@link Mac} to update
     * @param valueToDigest the value to update the {@link Mac} with (maybe null or empty)
     * @return the updated {@link Mac}
     * @throws IllegalStateException if the Mac was not initialized
     */

    /**
     * Preserves binary compatibility only. As for previous versions does not provide useful
     * behavior
     *
     * @deprecated since 1.11; only useful to preserve binary compatibility
     */

    /**
     * Creates an instance using the provided algorithm type.
     *
     * @param algorithm to use
     * @param key the key to use
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @since 1.11
     */

    /**
     * Creates an instance using the provided algorithm type.
     *
     * @param algorithm to use
     * @param key the key to use
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @since 1.11
     */

    /**
     * Creates an instance using the provided algorithm type.
     *
     * @param algorithm to use
     * @param key the key to use
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @since 1.11
     */

    /**
     * Creates an instance using the provided algorithm type.
     *
     * @param algorithm to use.
     * @param key the key to use
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught or key is
     *     null or key is invalid.
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use
     * @return the digest as a byte[]
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use
     * @return the digest as a hex String
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use, treated as UTF-8
     * @return the digest as a byte[]
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use, treated as UTF-8
     * @return the digest as a hex String
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use
     * @return the digest as a byte[]
     * @since 1.11
     */

    /**
     * Returns the digest for the input data.
     *
     * @param valueToDigest the input to use
     * @return the digest as a hex String
     * @since 1.11
     */

    /**
     * Returns the digest for the stream.
     *
     * @param valueToDigest the data to use
     *     <p>The InputStream must not be null and will not be closed
     * @return the digest
     * @throws IOException If an I/O error occurs.
     * @since 1.11
     */

    /**
     * Returns the digest for the stream.
     *
     * @param valueToDigest the data to use
     *     <p>The InputStream must not be null and will not be closed
     * @return the digest as a hex String
     * @throws IOException If an I/O error occurs.
     * @since 1.11
     */

    /**
     * Returns the digest for the file.
     *
     * @param valueToDigest the file to use
     * @return the digest
     * @throws IOException If an I/O error occurs.
     * @since 1.11
     */

    /**
     * Returns the digest for the file.
     *
     * @param valueToDigest the file to use
     * @return the digest as a hex String
     * @throws IOException If an I/O error occurs.
     * @since 1.11
     */
}
