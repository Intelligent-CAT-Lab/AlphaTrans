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
package org.apache.commons.codec.cli;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.MessageDigestAlgorithms;

import java.io.IOException;
import java.util.Arrays;

/**
 * A minimal command line to run digest over files, directories or a string
 *
 * @see #main(String[])
 * @since 1.11
 */
public class Digest {

    /**
     * Runs the digest algorithm in {@code args[0]} on the file in {@code args[1]}. If there is no
     * {@code args[1]}, use standard input.
     *
     * <p>The algorithm can also be {@code ALL} or {@code *} to output one line for each known
     * algorithm.
     *
     * @param args {@code args[0]} is one of {@link MessageDigestAlgorithms} name, {@link
     *     MessageDigest} name, {@code ALL}, or {@code *}. {@code args[1+]} is a
     *     FILE/DIRECTORY/String.
     * @throws IOException if an error occurs
     */
    private final String algorithm;

    private final String[] args;
    private final String[] inputs;

    private Digest(final String[] args) {
        if (args == null) {
            throw new IllegalArgumentException("args");
        }
        final int argsLength = args.length;
        if (argsLength == 0) {
            throw new IllegalArgumentException(
                    String.format(
                            "Usage: java %s [algorithm] [FILE|DIRECTORY|string] ...",
                            Digest.class.getName()));
        }
        this.args = args;
        algorithm = args[0];
        if (argsLength <= 1) {
            inputs = null;
        } else {
            inputs = new String[argsLength - 1];
            System.arraycopy(args, 1, inputs, 0, inputs.length);
        }
    }

    private void println0(final String prefix, final byte[] digest) {
        println1(prefix, digest, null);
    }

    private void println1(final String prefix, final byte[] digest, final String fileName) {
        System.out.println(
                prefix + Hex.encodeHexString0(digest) + (fileName != null ? "  " + fileName : ""));
    }

    @Override
    public String toString() {
        return String.format("%s %s", super.toString(), Arrays.toString(args));
    }
}
