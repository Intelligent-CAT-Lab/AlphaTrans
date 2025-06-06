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

/** Unit tests for {@link org.apache.commons.fileupload.DefaultFileItem}. */
@SuppressWarnings({"deprecation", "javadoc"}) // unit tests for deprecated class
public class DefaultFileItemTest {

    /** Content type for regular form items. */
    private static final String textContentType = "text/plain";

    /** Content type for file uploads. */
    private static final String fileContentType = "application/octet-stream";

    /** Very low threshold for testing memory versus disk options. */
    private static final int threshold = 16;

    /** Test construction of a regular text field. */

    /** Test construction of a file field. */

    /**
     * Test creation of a field for which the amount of data falls below the configured threshold.
     */

    /**
     * Test creation of a field for which the amount of data falls above the configured threshold,
     * where no specific repository is configured.
     */

    /**
     * Test creation of a field for which the amount of data falls above the configured threshold,
     * where a specific repository is configured.
     */

    /**
     * Common code for cases where the amount of data is above the configured threshold, but the
     * ultimate destination of the data has not yet been determined.
     *
     * @param repository The directory within which temporary files will be created.
     */

    /**
     * Creates a new <code>FileItemFactory</code> and returns it, obscuring from the caller the
     * underlying implementation of this interface.
     *
     * @param repository The directory within which temporary files will be created.
     * @return the new <code>FileItemFactory</code> instance.
     */
    static final String CHARSET_ISO88591 = "ISO-8859-1";

    static final String CHARSET_ASCII = "US-ASCII";

    static final String CHARSET_UTF8 = "UTF-8";

    static final String CHARSET_KOI8_R = "KOI8_R";

    static final String CHARSET_WIN1251 = "Cp1251";

    static final int SWISS_GERMAN_STUFF_UNICODE[] = {
        0x47, 0x72, 0xFC, 0x65, 0x7A, 0x69, 0x5F, 0x7A, 0xE4, 0x6D, 0xE4
    };

    static final int SWISS_GERMAN_STUFF_ISO8859_1[] = {
        0x47, 0x72, 0xFC, 0x65, 0x7A, 0x69, 0x5F, 0x7A, 0xE4, 0x6D, 0xE4
    };

    static final int SWISS_GERMAN_STUFF_UTF8[] = {
        0x47, 0x72, 0xC3, 0xBC, 0x65, 0x7A, 0x69, 0x5F, 0x7A, 0xC3, 0xA4, 0x6D, 0xC3, 0xA4
    };

    static final int RUSSIAN_STUFF_UNICODE[] = {
        0x412, 0x441, 0x435, 0x43C, 0x5F, 0x43F, 0x440, 0x438, 0x432, 0x435, 0x442
    };

    static final int RUSSIAN_STUFF_UTF8[] = {
        0xD0, 0x92, 0xD1, 0x81, 0xD0, 0xB5, 0xD0, 0xBC, 0x5F,
        0xD0, 0xBF, 0xD1, 0x80, 0xD0, 0xB8, 0xD0, 0xB2, 0xD0,
        0xB5, 0xD1, 0x82
    };

    static final int RUSSIAN_STUFF_KOI8R[] = {
        0xF7, 0xD3, 0xC5, 0xCD, 0x5F, 0xD0, 0xD2, 0xC9, 0xD7, 0xC5, 0xD4
    };

    static final int RUSSIAN_STUFF_WIN1251[] = {
        0xC2, 0xF1, 0xE5, 0xEC, 0x5F, 0xEF, 0xF0, 0xE8, 0xE2, 0xE5, 0xF2
    };

    private static String constructString(int[] unicodeChars) {
        StringBuilder buffer = new StringBuilder();
        if (unicodeChars != null) {
            for (int unicodeChar : unicodeChars) {
                buffer.append((char) unicodeChar);
            }
        }
        return buffer.toString();
    }

    /** Test construction of content charset. */
}
