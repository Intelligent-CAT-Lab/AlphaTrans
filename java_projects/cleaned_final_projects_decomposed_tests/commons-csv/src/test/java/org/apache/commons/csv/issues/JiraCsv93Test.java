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

/**
 * Add more tests about null value.
 *
 * <p>QuoteMode:ALL_NON_NULL (Quotes all non-null fields, null will not be quoted but not null will
 * be quoted). when withNullString("NULL"), NULL String value ("NULL") and null value (null) will be
 * formatted as '"NULL",NULL'. So it also should be parsed as NULL String value and null value
 * (["NULL", null]), It should be distinguish in parsing. And when don't set nullString in
 * CSVFormat, String '"",' should be parsed as "" and null (["", null]) according to null will not
 * be quoted but not null will be quoted. QuoteMode:NON_NUMERIC, same as ALL_NON_NULL.
 *
 * <p>This can solve the problem of distinguishing between empty string columns and absent value
 * columns which just like Jira CSV-253 to a certain extent.
 */
public class JiraCsv93Test {
    private static Object[] objects1 = {"abc", "", null, "a,b,c", 123};

    private static Object[] objects2 = {"abc", "NULL", null, "a,b,c", 123};

    private void every(
            final CSVFormat csvFormat,
            final Object[] objects,
            final String format,
            final String[] data)
            throws IOException {
        final String source = csvFormat.format(objects);
        assertEquals(format, csvFormat.format(objects));
        try (final CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            final CSVRecord csvRecord = csvParser.iterator().next();
            for (int i = 0; i < data.length; i++) {
                assertEquals(csvRecord.get1(i), data[i]);
            }
        }
    }

    @Test
    public void testWithNotSetNullString_test0_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
    }

    @Test
    public void testWithNotSetNullString_test1_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithNotSetNullString_test2_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testWithNotSetNullString_test3_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
    }

    @Test
    public void testWithNotSetNullString_test4_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
    }

    @Test
    public void testWithNotSetNullString_test5_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithNotSetNullString_test6_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
    }

    @Test
    public void testWithNotSetNullString_test7_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
    }

    @Test
    public void testWithNotSetNullString_test8_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
    }

    @Test
    public void testWithNotSetNullString_test9_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithNotSetNullString_test10_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
    }

    @Test
    public void testWithNotSetNullString_test11_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
    }

    @Test
    public void testWithNotSetNullString_test12_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
    }

    @Test
    public void testWithNotSetNullString_test13_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithNotSetNullString_test14_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
    }

    @Test
    public void testWithNotSetNullString_test15_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
    }

    @Test
    public void testWithNotSetNullString_test16_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
    }

    @Test
    public void testWithNotSetNullString_test17_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", "", "", "a,b,c", "123"});
    }

    @Test
    public void testWithNotSetNullString_test18_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithNotSetNullString_test19_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testWithNotSetNullString_test20_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build();
    }

    @Test
    public void testWithNotSetNullString_test21_decomposed() throws IOException {
        every(
                CSVFormat.DEFAULT,
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.ALL_NON_NULL).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.MINIMAL).build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setEscape0('?');
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT.builder().setEscape0('?').setQuoteMode(QuoteMode.NONE).build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", "", "", "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build();
        every(
                CSVFormat.DEFAULT.builder().setQuoteMode(QuoteMode.NON_NUMERIC).build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",123",
                new String[] {"abc", "", null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test0_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test1_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test2_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test3_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test4_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test5_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test6_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testWithSetNullStringEmptyString_test7_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test8_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test9_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test10_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test11_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
    }

    @Test
    public void testWithSetNullStringEmptyString_test12_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test13_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test14_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test15_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test16_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
    }

    @Test
    public void testWithSetNullStringEmptyString_test17_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test18_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test19_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test20_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test21_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
    }

    @Test
    public void testWithSetNullStringEmptyString_test22_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
    }

    @Test
    public void testWithSetNullStringEmptyString_test23_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test24_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringEmptyString_test25_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringEmptyString_test26_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
    }

    @Test
    public void testWithSetNullStringEmptyString_test27_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testWithSetNullStringEmptyString_test28_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC).build();
    }

    @Test
    public void testWithSetNullStringEmptyString_test29_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL).build(),
                objects1,
                "\"abc\",\"\",\"\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",\"123\"",
                new String[] {"abc", "", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects1,
                "abc,,,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects1,
                "abc,,,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("");
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setNullString("").setQuoteMode(QuoteMode.NON_NUMERIC).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("")
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build(),
                objects1,
                "\"abc\",\"\",,\"a,b,c\",123",
                new String[] {"abc", "", null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test0_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test1_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test2_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
    }

    @Test
    public void testWithSetNullStringNULL_test3_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test4_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test5_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test6_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
    }

    @Test
    public void testWithSetNullStringNULL_test7_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
    }

    @Test
    public void testWithSetNullStringNULL_test8_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test9_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test10_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test11_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
    }

    @Test
    public void testWithSetNullStringNULL_test12_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
    }

    @Test
    public void testWithSetNullStringNULL_test13_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test14_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test15_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test16_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
    }

    @Test
    public void testWithSetNullStringNULL_test17_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
    }

    @Test
    public void testWithSetNullStringNULL_test18_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test19_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test20_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test21_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
    }

    @Test
    public void testWithSetNullStringNULL_test22_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
    }

    @Test
    public void testWithSetNullStringNULL_test23_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
    }

    @Test
    public void testWithSetNullStringNULL_test24_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
    }

    @Test
    public void testWithSetNullStringNULL_test25_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testWithSetNullStringNULL_test26_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
    }

    @Test
    public void testWithSetNullStringNULL_test27_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testWithSetNullStringNULL_test28_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC).build();
    }

    @Test
    public void testWithSetNullStringNULL_test29_decomposed() throws IOException {
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").build();
        every(
                CSVFormat.DEFAULT.builder().setNullString("NULL").build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",\"NULL\",\"a,b,c\",\"123\"",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.ALL_NON_NULL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.ALL_NON_NULL)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",\"123\"",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.MINIMAL).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.MINIMAL)
                        .build(),
                objects2,
                "abc,NULL,NULL,\"a,b,c\",123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?');
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setEscape0('?').setQuoteMode(QuoteMode.NONE).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setEscape0('?')
                        .setQuoteMode(QuoteMode.NONE)
                        .build(),
                objects2,
                "abc,NULL,NULL,a?,b?,c,123",
                new String[] {"abc", null, null, "a,b,c", "123"});
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setNullString("NULL");
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC);
        CSVFormat.DEFAULT.builder().setNullString("NULL").setQuoteMode(QuoteMode.NON_NUMERIC).build();
        every(
                CSVFormat.DEFAULT
                        .builder()
                        .setNullString("NULL")
                        .setQuoteMode(QuoteMode.NON_NUMERIC)
                        .build(),
                objects2,
                "\"abc\",\"NULL\",NULL,\"a,b,c\",123",
                new String[] {"abc", "NULL", null, "a,b,c", "123"});
    }
}