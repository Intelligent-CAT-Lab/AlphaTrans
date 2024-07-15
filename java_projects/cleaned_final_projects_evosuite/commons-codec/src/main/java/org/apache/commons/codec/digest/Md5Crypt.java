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
 * The libc crypt() "$1$" and Apache "$apr1$" MD5-based hash algorithm.
 *
 * <p>Based on the public domain ("beer-ware") C implementation from Poul-Henning Kamp which was
 * found at: <a
 * href="http://www.freebsd.org/cgi/cvsweb.cgi/src/lib/libcrypt/crypt-md5.c?rev=1.1;content-type=text%2Fplain">
 * crypt-md5.c @ freebsd.org</a>
 *
 * <p>Source:
 *
 * <pre>
 * $FreeBSD: src/lib/libcrypt/crypt-md5.c,v 1.1 1999/01/21 13:50:09 brandon Exp $
 * </pre>
 *
 * <p>Conversion to Kotlin and from there to Java in 2012.
 *
 * <p>The C style comments are from the original C code, the ones with "//" from the port.
 *
 * <p>This class is immutable and thread-safe.
 *
 * @since 1.7
 */
public class Md5Crypt {

    /** The Identifier of the Apache variant. */
    static final String APR1_PREFIX = "$apr1$";

    /** The number of bytes of the final hash. */
    private static final int BLOCKSIZE = 16;

    /** The Identifier of this crypt() variant. */
    static final String MD5_PREFIX = "$1$";

    /** The number of rounds of the big loop. */
    private static final int ROUNDS = 1000;

    /**
     * See {@link #apr1Crypt(byte[], String)} for details.
     *
     * <p>A salt is generated for you using {@link SecureRandom}; your own {@link Random} in {@link
     * #apr1Crypt(byte[], Random)}.
     *
     * @param keyBytes plaintext string to hash.
     * @return the hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught. *
     * @see #apr1Crypt(byte[], String)
     */

    /**
     * See {@link #apr1Crypt(byte[], String)} for details.
     *
     * <p>A salt is generated for you using the user provided {@link Random}.
     *
     * @param keyBytes plaintext string to hash.
     * @param random the instance of {@link Random} to use for generating the salt. Consider using
     *     {@link SecureRandom} or {@link ThreadLocalRandom}.
     * @return the hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught. *
     * @see #apr1Crypt(byte[], String)
     * @since 1.12
     */

    /**
     * See {@link #apr1Crypt(String, String)} for details.
     *
     * <p>A salt is generated for you using {@link SecureRandom}
     *
     * @param keyBytes plaintext string to hash.
     * @param salt An APR1 salt. The salt may be null, in which case a salt is generated for you
     *     using {@link ThreadLocalRandom}; for more secure salts consider using {@link
     *     SecureRandom} to generate your own salts.
     * @return the hash value
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * See {@link #apr1Crypt(String, String)} for details.
     *
     * <p>A salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     * consider using {@link SecureRandom} to generate your own salts and calling {@link
     * #apr1Crypt(byte[], String)}.
     *
     * @param keyBytes plaintext string to hash.
     * @return the hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @see #apr1Crypt(byte[], String)
     */

    /**
     * Generates an Apache htpasswd compatible "$apr1$" MD5 based hash value.
     *
     * <p>The algorithm is identical to the crypt(3) "$1$" one but produces different outputs due to
     * the different salt prefix.
     *
     * @param keyBytes plaintext string to hash.
     * @param salt salt string including the prefix and optionally garbage at the end. The salt may
     *     be null, in which case a salt is generated for you using {@link ThreadLocalRandom}; for
     *     more secure salts consider using {@link SecureRandom} to generate your own salts.
     * @return the hash value
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() compatible "$1$" hash value.
     *
     * <p>See {@link #md5Crypt(byte[], String)} for details.
     *
     * <p>A salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     * consider using {@link SecureRandom} to generate your own salts and calling {@link
     * #md5Crypt(byte[], String)}.
     *
     * @param keyBytes plaintext string to hash.
     * @return the hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @see #md5Crypt(byte[], String)
     */

    /**
     * Generates a libc6 crypt() compatible "$1$" hash value.
     *
     * <p>See {@link #md5Crypt(byte[], String)} for details.
     *
     * <p>A salt is generated for you using the instance of {@link Random} you supply.
     *
     * @param keyBytes plaintext string to hash.
     * @param random the instance of {@link Random} to use for generating the salt. Consider using
     *     {@link SecureRandom} or {@link ThreadLocalRandom}.
     * @return the hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @see #md5Crypt(byte[], String)
     * @since 1.12
     */

    /**
     * Generates a libc crypt() compatible "$1$" MD5 based hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details. We use {@link SecureRandom} for seed
     * generation by default.
     *
     * @param keyBytes plaintext string to hash.
     * @param salt salt string including the prefix and optionally garbage at the end. The salt may
     *     be null, in which case a salt is generated for you using {@link ThreadLocalRandom}; for
     *     more secure salts consider using {@link SecureRandom} to generate your own salts.
     * @return the hash value
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() "$1$" or Apache htpasswd "$apr1$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} or {@link #apr1Crypt(String, String)} for details.
     * We use {@link SecureRandom by default}.
     *
     * @param keyBytes plaintext string to hash.
     * @param salt real salt value without prefix or "rounds=". The salt may be null, in which case
     *     a salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     *     consider using {@link SecureRandom} to generate your own salts.
     * @param prefix salt prefix
     * @return the hash value
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() "$1$" or Apache htpasswd "$apr1$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} or {@link #apr1Crypt(String, String)} for details.
     *
     * @param keyBytes plaintext string to hash.
     * @param salt real salt value without prefix or "rounds=". The salt may be null, in which case
     *     a salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     *     consider using {@link SecureRandom} to generate your own salts.
     * @param prefix salt prefix
     * @param random the instance of {@link Random} to use for generating the salt. Consider using
     *     {@link SecureRandom} or {@link ThreadLocalRandom}.
     * @return the hash value
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @since 1.12
     */
}
