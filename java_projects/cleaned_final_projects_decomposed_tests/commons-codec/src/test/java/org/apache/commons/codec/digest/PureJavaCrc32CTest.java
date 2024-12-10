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

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;

/**
 * Test class for PureJavaCrc32C. Test data was derived from
 * https://tools.ietf.org/html/rfc3720#appendix-B.4
 */
public class PureJavaCrc32CTest {

    private final PureJavaCrc32C crc = new PureJavaCrc32C();

    private final byte[] data = new byte[32];

    

    

    

    

    private void check(final int expected) {
        crc.reset();
        crc.update0(data, 0, data.length);
        final int actual = (int) crc.getValue();
        Assert.assertEquals(Integer.toHexString(expected), Integer.toHexString(actual));
    }

    @Test
    public void testZeros_test0_decomposed()  {
        Arrays.fill(data, (byte) 0);
    }

    @Test
    public void testZeros_test1_decomposed()  {
        Arrays.fill(data, (byte) 0);
        check(0x8a9136aa);
    }

    @Test
    public void testOnes_test0_decomposed()  {
        Arrays.fill(data, (byte) 0xFF);
    }

    @Test
    public void testOnes_test1_decomposed()  {
        Arrays.fill(data, (byte) 0xFF);
        check(0x62a8ab43);
    }

    @Test
    public void testIncreasing_test0_decomposed()  {
        for (int i = 0; i < data.length; i++) {
            data[i] = (byte) i;
        }
        check(0x46dd794e);
    }

    @Test
    public void testDecreasing_test0_decomposed()  {
        for (int i = 0; i < data.length; i++) {
            data[i] = (byte) (31 - i);
        }
        check(0x113fdb5c);
    }
}