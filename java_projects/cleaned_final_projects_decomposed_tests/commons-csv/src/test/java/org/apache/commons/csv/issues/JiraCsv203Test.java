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
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.QuoteMode;
import org.junit.jupiter.api.Test;

/**
 * JIRA: <a href="https://issues.apache.org/jira/browse/CSV-203">withNullString value is printed
 * without quotes when QuoteMode.ALL is specified</a>
 */
public class JiraCsv203Test {

    @Test
    public void testQuoteModeAll_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testQuoteModeAll_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testQuoteModeAll_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testQuoteModeAll_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testQuoteModeAll_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
    }

    @Test
    public void testQuoteModeAll_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testQuoteModeAll_test6_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals("\"N/A\",\"Hello\",\"N/A\",\"World\"\r\n", buffer.toString());
    }

    @Test
    public void testQuoteModeAllNonNull_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testQuoteModeAllNonNull_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testQuoteModeAllNonNull_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testQuoteModeAllNonNull_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL_NON_NULL);
    }

    @Test
    public void testQuoteModeAllNonNull_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL_NON_NULL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build();
    }

    @Test
    public void testQuoteModeAllNonNull_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL_NON_NULL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testQuoteModeAllNonNull_test6_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL_NON_NULL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals("N/A,\"Hello\",N/A,\"World\"\r\n", buffer.toString());
    }

    @Test
    public void testQuoteModeMinimal_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testQuoteModeMinimal_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testQuoteModeMinimal_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testQuoteModeMinimal_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.MINIMAL);
    }

    @Test
    public void testQuoteModeMinimal_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.MINIMAL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build();
    }

    @Test
    public void testQuoteModeMinimal_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.MINIMAL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testQuoteModeMinimal_test6_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.MINIMAL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals("N/A,Hello,N/A,World\r\n", buffer.toString());
    }

    @Test
    public void testQuoteModeNonNumeric_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testQuoteModeNonNumeric_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testQuoteModeNonNumeric_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testQuoteModeNonNumeric_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testQuoteModeNonNumeric_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.NON_NUMERIC);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build();
    }

    @Test
    public void testQuoteModeNonNumeric_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.NON_NUMERIC);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testQuoteModeNonNumeric_test6_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.NON_NUMERIC);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals("N/A,\"Hello\",N/A,\"World\"\r\n", buffer.toString());
    }

    @Test
    public void testWithEmptyValues_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testWithEmptyValues_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testWithEmptyValues_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testWithEmptyValues_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testWithEmptyValues_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
    }

    @Test
    public void testWithEmptyValues_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1("", "Hello", "", "World");
        }
    }

    @Test
    public void testWithEmptyValues_test6_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1("", "Hello", "", "World");
        }
        assertEquals("\"\",\"Hello\",\"\",\"World\"\r\n", buffer.toString());
    }

    @Test
    public void testWithoutNullString_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testWithoutNullString_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testWithoutNullString_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testWithoutNullString_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
    }

    @Test
    public void testWithoutNullString_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testWithoutNullString_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true);
        CSVFormat.EXCEL.builder().setIgnoreSurroundingSpaces(true).setQuoteMode(QuoteMode.ALL);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setIgnoreSurroundingSpaces(true)
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals(",\"Hello\",,\"World\"\r\n", buffer.toString());
    }

    @Test
    public void testWithoutQuoteMode_test0_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
    }

    @Test
    public void testWithoutQuoteMode_test1_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
    }

    @Test
    public void testWithoutQuoteMode_test2_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
    }

    @Test
    public void testWithoutQuoteMode_test3_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .build();
    }

    @Test
    public void testWithoutQuoteMode_test4_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
    }

    @Test
    public void testWithoutQuoteMode_test5_decomposed() throws Exception {
        CSVFormat.EXCEL.builder();
        CSVFormat.EXCEL.builder().setNullString("N/A");
        CSVFormat.EXCEL.builder().setNullString("N/A").setIgnoreSurroundingSpaces(true);
        final CSVFormat format =
                CSVFormat.EXCEL
                        .builder()
                        .setNullString("N/A")
                        .setIgnoreSurroundingSpaces(true)
                        .build();
        final StringBuilder buffer = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(buffer, format)) {
            printer.printRecord1(null, "Hello", null, "World");
        }
        assertEquals("N/A,Hello,N/A,World\r\n", buffer.toString());
    }
}