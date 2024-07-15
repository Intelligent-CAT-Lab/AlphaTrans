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

import java.util.regex.Pattern;

/**
 * SHA2-based Unix crypt implementation.
 *
 * <p>Based on the C implementation released into the Public Domain by Ulrich Drepper
 * &lt;drepper@redhat.com&gt; http://www.akkadia.org/drepper/SHA-crypt.txt
 *
 * <p>Conversion to Kotlin and from there to Java in 2012 by Christian Hammers
 * &lt;ch@lathspell.de&gt; and likewise put into the Public Domain.
 *
 * <p>This class is immutable and thread-safe.
 *
 * @since 1.7
 */
public class Sha2Crypt {

    /** Default number of rounds if not explicitly specified. */
    private static final int ROUNDS_DEFAULT = 5000;

    /** Maximum number of rounds. */
    private static final int ROUNDS_MAX = 999999999;

    /** Minimum number of rounds. */
    private static final int ROUNDS_MIN = 1000;

    /** Prefix for optional rounds specification. */
    private static final String ROUNDS_PREFIX = "rounds=";

    /** The number of bytes the final hash value will have (SHA-256 variant). */
    private static final int SHA256_BLOCKSIZE = 32;

    /** The prefixes that can be used to identify this crypt() variant (SHA-256). */
    static final String SHA256_PREFIX = "$5$";

    /** The number of bytes the final hash value will have (SHA-512 variant). */
    private static final int SHA512_BLOCKSIZE = 64;

    /** The prefixes that can be used to identify this crypt() variant (SHA-512). */
    static final String SHA512_PREFIX = "$6$";

    /** The pattern to match valid salt values. */
    private static final Pattern SALT_PATTERN =
            Pattern.compile("^\\$([56])\\$(rounds=(\\d+)\\$)?([\\.\\/a-zA-Z0-9]{1,16}).*");

    /**
     * Generates a libc crypt() compatible "$5$" hash value with random salt.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * <p>A salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     * consider using {@link SecureRandom} to generate your own salts and calling {@link
     * #sha256Crypt(byte[], String)}.
     *
     * @param keyBytes plaintext to hash
     * @return complete hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() compatible "$5$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * @param keyBytes plaintext to hash
     * @param salt real salt value without prefix or "rounds=". The salt may be null, in which case
     *     a salt is generated for you using {@link SecureRandom}. If one does not want to use
     *     {@link SecureRandom}, you can pass your own {@link Random} in {@link #sha256Crypt(byte[],
     *     String, Random)}.
     * @return complete hash value including salt
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() compatible "$5$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * @param keyBytes plaintext to hash
     * @param salt real salt value without prefix or "rounds=".
     * @param random the instance of {@link Random} to use for generating the salt. Consider using
     *     {@link SecureRandom} or {@link ThreadLocalRandom}.
     * @return complete hash value including salt
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @since 1.12
     */

    /**
     * Generates a libc6 crypt() compatible "$5$" or "$6$" SHA2 based hash value.
     *
     * <p>This is a nearly line by line conversion of the original C function. The numbered comments
     * are from the algorithm description, the short C-style ones from the original C code and the
     * ones with "Remark" from me.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * @param keyBytes plaintext to hash
     * @param salt real salt value without prefix or "rounds="; may not be null
     * @param saltPrefix either $5$ or $6$
     * @param blocksize a value that differs between $5$ and $6$
     * @param algorithm {@link MessageDigest} algorithm identifier string
     * @return complete hash value including prefix and salt
     * @throws IllegalArgumentException if the given salt is {@code null} or does not match the
     *     allowed pattern
     * @throws IllegalArgumentException when a {@link NoSuchAlgorithmException} is caught
     * @see MessageDigestAlgorithms
     */

    /**
     * Generates a libc crypt() compatible "$6$" hash value with random salt.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * <p>A salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     * consider using {@link SecureRandom} to generate your own salts and calling {@link
     * #sha512Crypt(byte[], String)}.
     *
     * @param keyBytes plaintext to hash
     * @return complete hash value
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() compatible "$6$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * @param keyBytes plaintext to hash
     * @param salt real salt value without prefix or "rounds=". The salt may be null, in which case
     *     a salt is generated for you using {@link SecureRandom}; if you want to use a {@link
     *     Random} object other than {@link SecureRandom} then we suggest you provide it using
     *     {@link #sha512Crypt(byte[], String, Random)}.
     * @return complete hash value including salt
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     */

    /**
     * Generates a libc6 crypt() compatible "$6$" hash value.
     *
     * <p>See {@link Crypt#crypt(String, String)} for details.
     *
     * @param keyBytes plaintext to hash
     * @param salt real salt value without prefix or "rounds=". The salt may be null, in which case
     *     a salt is generated for you using {@link ThreadLocalRandom}; for more secure salts
     *     consider using {@link SecureRandom} to generate your own salts.
     * @param random the instance of {@link Random} to use for generating the salt. Consider using
     *     {@link SecureRandom} or {@link ThreadLocalRandom}.
     * @return complete hash value including salt
     * @throws IllegalArgumentException if the salt does not match the allowed pattern
     * @throws IllegalArgumentException when a {@link java.security.NoSuchAlgorithmException} is
     *     caught.
     * @since 1.12
     */
}
