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
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.CSVRecord;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;

public class JiraCsv288Test {

    private void print(final CSVRecord csvRecord, final CSVPrinter csvPrinter) throws IOException {
        for (final String value : csvRecord) {
            csvPrinter.print(value);
        }
    }

    @Test
    public void testParseWithABADelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a|~|b|~|c|~|d|~||~|f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser parser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("|~|").build())) {
            for (final CSVRecord csvRecord : parser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithDoublePipeDelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a||b||c||d||||f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("||").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithDoublePipeDelimiterDoubleCharValue_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a||bb||cc||dd||f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("||").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,bb,cc,dd,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithDoublePipeDelimiterEndsWithDelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a||b||c||d||||f||");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("||").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f,", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithDoublePipeDelimiterQuoted_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a||\"b||c\"||d||||f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("||").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b||c,d,,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithSinglePipeDelimiterEndsWithDelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a|b|c|d||f|");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f,", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTriplePipeDelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a|||b|||c|||d||||||f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("|||").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTwoCharDelimiter1_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a~|b~|c~|d~|~|f");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("~|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTwoCharDelimiter2_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a~|b~|c~|d~|~|f~");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("~|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f~", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTwoCharDelimiter3_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a~|b~|c~|d~|~|f|");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("~|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f|", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTwoCharDelimiter4_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a~|b~|c~|d~|~|f~~||g");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("~|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f~,|g", stringBuilder.toString());
            }
        }
    }

    @Test
    public void testParseWithTwoCharDelimiterEndsWithDelimiter_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a~|b~|c~|d~|~|f~|");
        final StringBuilder stringBuilder = new StringBuilder();
        try (CSVPrinter csvPrinter = new CSVPrinter(stringBuilder, CSVFormat.EXCEL);
                CSVParser csvParser =
                        CSVParser.parse3(
                                in, CSVFormat.Builder.create0().setDelimiter1("~|").build())) {
            for (final CSVRecord csvRecord : csvParser) {
                print(csvRecord, csvPrinter);
                assertEquals("a,b,c,d,,f,", stringBuilder.toString());
            }
        }
    }
}