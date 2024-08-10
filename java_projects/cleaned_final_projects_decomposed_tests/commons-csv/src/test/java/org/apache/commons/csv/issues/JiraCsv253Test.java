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
package org.apache.commons.csv.issues;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.csv.QuoteMode;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.StringReader;
import java.util.Iterator;

/**
 * Setting QuoteMode:ALL_NON_NULL or NON_NUMERIC can distinguish between empty string columns and
 * absent value columns.
 */
public class JiraCsv253Test {

    private void assertArrayEqual(final String[] expected, final CSVRecord actual) {
        for (int i = 0; i < expected.length; i++) {
            assertEquals(expected[i], actual.get1(i));
        }
    }

    @Test
    public void testHandleAbsentValues_test0_decomposed() throws IOException {
        final String source =
                "\"John\",,\"Doe\"\n" + ",\"AA\",123\n" + "\"John\",90,\n" + "\"\",,90";
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testHandleAbsentValues_test1_decomposed() throws IOException {
        final String source =
                "\"John\",,\"Doe\"\n" + ",\"AA\",123\n" + "\"John\",90,\n" + "\"\",,90";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testHandleAbsentValues_test2_decomposed() throws IOException {
        final String source =
                "\"John\",,\"Doe\"\n" + ",\"AA\",123\n" + "\"John\",90,\n" + "\"\",,90";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build();
    }

    @Test
    public void testHandleAbsentValues_test3_decomposed() throws IOException {
        final String source =
                "\"John\",,\"Doe\"\n" + ",\"AA\",123\n" + "\"John\",90,\n" + "\"\",,90";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build();
        try (final CSVParser parser = csvFormat.parse(new StringReader(source))) {
            final Iterator<CSVRecord> csvRecords = parser.iterator();
            assertArrayEqual(new String[] {"John", null, "Doe"}, csvRecords.next());
            assertArrayEqual(new String[] {null, "AA", "123"}, csvRecords.next());
            assertArrayEqual(new String[] {"John", "90", null}, csvRecords.next());
            assertArrayEqual(new String[] {"", null, "90"}, csvRecords.next());
        }
    }
}