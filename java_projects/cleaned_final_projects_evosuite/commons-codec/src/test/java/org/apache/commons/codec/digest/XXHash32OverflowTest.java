
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

package org.apache.commons.codec.digest;

import org.junit.Assert;
import org.junit.Assume;
import org.junit.Test;

public class XXHash32OverflowTest {

    /**
     * This test hits an edge case where a very large number of bytes is added to the incremental
     * hash. The data is constructed so that an integer counter of unprocessed bytes will overflow.
     * If this is not handled correctly then the code throws an exception when it copies more data
     * into the unprocessed bytes array.
     */
    @Test
    public void testIncrementalHashWithUnprocessedBytesAndHugeLengthArray() {
        final int bufferSize = 16;
        final int unprocessedSize = bufferSize - 1;
        final int hugeLength = Integer.MAX_VALUE - (unprocessedSize - 1);
        Assert.assertTrue(
                "This should overflow to negative", unprocessedSize + hugeLength < bufferSize);

        byte[] bytes = null;
        try {
            bytes = new byte[hugeLength];
        } catch (final OutOfMemoryError ignore) {
        }
        Assume.assumeTrue("Cannot allocate array of length " + hugeLength, bytes != null);

        final XXHash32 inc = XXHash32.XXHash321();
        inc.update1(bytes, 0, unprocessedSize);
        inc.update1(bytes, 0, hugeLength);
    }
}
