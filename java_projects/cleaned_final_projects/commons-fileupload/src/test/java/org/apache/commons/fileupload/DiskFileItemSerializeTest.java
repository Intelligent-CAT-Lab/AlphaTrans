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
import static org.junit.Assert.assertNotNull;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

/** Serialization Unit tests for {@link org.apache.commons.fileupload.disk.DiskFileItem}. */
public class DiskFileItemSerializeTest {

    private static final File REPO =
            new File(System.getProperty("java.io.tmpdir"), "diskfileitemrepo");

    /** Content type for regular form items. */
    private static final String textContentType = "text/plain";

    /** Very low threshold for testing memory versus disk options. */
    private static final int threshold = 16;

    /** Helper method to test creation of a field when a repository is used. */

    /** Helper method to test creation of a field. */

    /**
     * Test creation of a field for which the amount of data falls below the configured threshold.
     */

    /** Test creation of a field for which the amount of data equals the configured threshold. */

    /**
     * Test creation of a field for which the amount of data falls above the configured threshold.
     */

    /** Test serialization and deserialization when repository is not null. */

    /** Test deserialization fails when repository is not valid. */

    /** Test deserialization fails when repository contains a null character. */

    /** Compare content bytes. */
    private void compareBytes(String text, byte[] origBytes, byte[] newBytes) {
        assertNotNull("origBytes must not be null", origBytes);
        assertNotNull("newBytes must not be null", newBytes);
        assertEquals(text + " byte[] length", origBytes.length, newBytes.length);
        for (int i = 0; i < origBytes.length; i++) {
            assertEquals(text + " byte[" + i + "]", origBytes[i], newBytes[i]);
        }
    }

    /** Create content bytes of a specified size. */
    private byte[] createContentBytes(int size) {
        StringBuilder buffer = new StringBuilder(size);
        byte count = 0;
        for (int i = 0; i < size; i++) {
            buffer.append(count + "");
            count++;
            if (count > 9) {
                count = 0;
            }
        }
        return buffer.toString().getBytes();
    }

    /** Create a FileItem with the specfied content bytes and repository. */

    /** Create a FileItem with the specfied content bytes. */

    /** Do serialization */
    private ByteArrayOutputStream serialize(Object target) throws Exception {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(target);
        oos.flush();
        oos.close();
        return baos;
    }

    /** Do deserialization */
    private Object deserialize(ByteArrayOutputStream baos) throws Exception {
        Object result = null;
        ByteArrayInputStream bais = new ByteArrayInputStream(baos.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bais);
        result = ois.readObject();
        bais.close();

        return result;
    }
}
