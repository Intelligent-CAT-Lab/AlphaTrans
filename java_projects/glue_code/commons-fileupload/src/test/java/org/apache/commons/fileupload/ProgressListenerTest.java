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
package org.apache.commons.fileupload;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

/** Tests the {@link ProgressListener}. */
public class ProgressListenerTest {

    private class ProgressListenerImpl implements ProgressListener {

        private final long expectedContentLength;

        private final int expectedItems;

        private Long bytesRead;

        private Integer items;

        ProgressListenerImpl(long pContentLength, int pItems) {
            expectedContentLength = pContentLength;
            expectedItems = pItems;
        }

        @Override
        public void update(long pBytesRead, long pContentLength, int pItems) {
            assertTrue(pBytesRead >= 0 && pBytesRead <= expectedContentLength);
            assertTrue(pContentLength == -1 || pContentLength == expectedContentLength);
            assertTrue(pItems >= 0 && pItems <= expectedItems);

            assertTrue(bytesRead == null || pBytesRead >= bytesRead.longValue());
            bytesRead = new Long(pBytesRead);
            assertTrue(items == null || pItems >= items.intValue());
            items = new Integer(pItems);
        }

        void checkFinished() {
            assertEquals(expectedContentLength, bytesRead.longValue());
            assertEquals(expectedItems, items.intValue());
        }
    }

    /** Parse a very long file upload by using a progress listener. */
}
