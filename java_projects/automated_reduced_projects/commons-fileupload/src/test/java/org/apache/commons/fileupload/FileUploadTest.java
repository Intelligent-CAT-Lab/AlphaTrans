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
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.List;

import org.apache.commons.fileupload.servlet.ServletFileUploadTest;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameter;
import org.junit.runners.Parameterized.Parameters;

/**
 * Common tests for implementations of {@link FileUpload}. This is a parameterized test.
 * Tests must be valid and common to all implementations of FileUpload added as parameter
 * in this class.
 *
 * @see ServletFileUploadTest
 * @see PortletFileUploadTest
 * @since 1.4
 */
public class FileUploadTest {

    /**
     * @return {@link FileUpload} classes under test.
     */

    /**
     * Current parameterized FileUpload.
     */
    @Parameter
    public FileUpload upload;

    // --- Test methods common to all implementations of a FileUpload



    /**
     * This is what the browser does if you submit the form without choosing a file.
     */

    /**
     * Internet Explorer 5 for the Mac has a bug where the carriage
     * return is missing on any boundary line immediately preceding
     * an input with type=image. (type=submit does not have the bug.)
     */

    /**
     * Test for <a href="http://issues.apache.org/jira/browse/FILEUPLOAD-62">FILEUPLOAD-62</a>
     */

    /**
     * Test for <a href="http://issues.apache.org/jira/browse/FILEUPLOAD-111">FILEUPLOAD-111</a>
     */

    /**
     * Test case for <a href="http://issues.apache.org/jira/browse/FILEUPLOAD-130">
     */

    /**
     * Test for <a href="http://issues.apache.org/jira/browse/FILEUPLOAD-239">FILEUPLOAD-239</a>
     */

    private void assertHeaders(String[] pHeaderNames, String[] pHeaderValues,
            FileItem pItem, int pIndex) {
        for (int i = 0; i < pHeaderNames.length; i++) {
            final String value = pItem.getHeaders().getHeader(pHeaderNames[i]);
            if (i == pIndex) {
                assertEquals(pHeaderValues[i], value);
            } else {
                assertNull(value);
            }
        }
    }
}
