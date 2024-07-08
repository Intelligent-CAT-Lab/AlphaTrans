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

import static org.apache.commons.codec.binary.StringUtils.getBytesUtf8;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;

import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Locale;
import java.util.Random;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.binary.StringUtils;
import org.junit.After;
import org.junit.Assume;
import org.junit.Before;
import org.junit.Test;

/**
 * Tests DigestUtils methods.
 *
 */
public class DigestUtilsTest {

    private static final String EMPTY_STRING = "";

    private final byte[] testData = new byte[1024 * 1024];

    private File testFile;

    private File testRandomAccessFile;

    private RandomAccessFile testRandomAccessFileWrapper;

    byte[] getTestData() {
        return testData;
    }

    File getTestFile() {
        return testFile;
    }

    Path getTestPath() {
        return testFile.toPath();
    }

    RandomAccessFile getTestRandomAccessFile() {
        return testRandomAccessFileWrapper;
    }

    @Before
    public void setUp() throws Exception {
        new Random().nextBytes(testData);
        testFile = File.createTempFile(DigestUtilsTest.class.getName(), ".dat");
        try (final FileOutputStream fos = new FileOutputStream(testFile)) {
            fos.write(testData);
        }

        testRandomAccessFile = File.createTempFile(DigestUtilsTest.class.getName(), ".dat");
        try (final FileOutputStream fos = new FileOutputStream(testRandomAccessFile)) {
            fos.write(testData);
        }
        testRandomAccessFileWrapper = new RandomAccessFile(testRandomAccessFile, "rw");
    }

    @After
    public void tearDown() {
        if (!testFile.delete()) {
            testFile.deleteOnExit();
        }

        if (!testRandomAccessFile.delete()) {
            testRandomAccessFile.deleteOnExit();
        }
    }






    /**
     * An MD2 hash converted to hex should always be 32 characters.
     */

    /**
     * An MD2 hash should always be a 16 element byte[].
     */


    /**
     * An MD5 hash converted to hex should always be 32 characters.
     */

    /**
     * An MD5 hash should always be a 16 element byte[].
     */



























}
