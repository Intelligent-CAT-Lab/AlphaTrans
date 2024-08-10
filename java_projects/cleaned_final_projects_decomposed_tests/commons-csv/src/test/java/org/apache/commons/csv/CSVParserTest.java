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

package org.apache.commons.csv;

import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.CRLF;
import static org.apache.commons.csv.Constants.LF;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.IOException;
import java.io.PipedReader;
import java.io.PipedWriter;
import java.io.Reader;
import java.io.StringReader;
import java.io.StringWriter;
import java.net.URL;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.stream.Collectors;

/**
 * CSVParserTest
 *
 * <p>The test are organized in three different sections: The 'setter/getter' section, the lexer
 * section and finally the parser section. In case a test fails, you should follow a top-down
 * approach for fixing a potential bug (its likely that the parser itself fails if the lexer has
 * problems...).
 */
public class CSVParserTest {

    private static final Charset UTF_8 = StandardCharsets.UTF_8;

    private static final String UTF_8_NAME = UTF_8.name();

    private static final String CSV_INPUT =
            "a,b,c,d\n"
                    + " a , b , 1 2 \n"
                    + "\"foo baar\", b,\n"
                    + "   \"foo\n,,\n\"\",,\n\"\"\",d,e\n"; // changed to use standard CSV escaping

    private static final String CSV_INPUT_1 = "a,b,c,d";

    private static final String CSV_INPUT_2 = "a,b,1 2";

    private static final String[][] RESULT = {
        {"a", "b", "c", "d"},
        {"a", "b", "1 2"},
        {"foo baar", "b", ""},
        {"foo\n,,\n\",,\n\"", "d", "e"}
    };

    private static final String CSV_INPUT_NO_COMMENT = "A,B" + CRLF + "1,2" + CRLF;

    private static final String CSV_INPUT_HEADER_COMMENT =
            "# header comment" + CRLF + "A,B" + CRLF + "1,2" + CRLF;

    private static final String CSV_INPUT_HEADER_TRAILER_COMMENT =
            "# header comment" + CRLF + "A,B" + CRLF + "1,2" + CRLF + "# comment";

    private static final String CSV_INPUT_MULTILINE_HEADER_TRAILER_COMMENT =
            "# multi-line"
                    + CRLF
                    + "# header comment"
                    + CRLF
                    + "A,B"
                    + CRLF
                    + "1,2"
                    + CRLF
                    + "# multi-line"
                    + CRLF
                    + "# comment";

    CSVRecord parse(final CSVParser parser, final int failParseRecordNo) throws IOException {
        if (parser.getRecordNumber() + 1 == failParseRecordNo) {
            assertThrows(IOException.class, () -> parser.nextRecord());
            return null;
        }
        return parser.nextRecord();
    }

    private void parseFully(final CSVParser parser) {
        parser.forEach(Assertions::assertNotNull);
    }

    

    

    @Test
    @Disabled
    public void testBackslashEscapingOld() throws IOException {
        final String code =
                "one,two,three\n"
                        + "on\\\"e,two\n"
                        + "on\"e,two\n"
                        + "one,\"tw\\\"o\"\n"
                        + "one,\"t\\,wo\"\n"
                        + "one,two,\"th,ree\"\n"
                        + "\"a\\\\\"\n"
                        + "a\\,b\n"
                        + "\"a\\\\,b\"";
        final String[][] res = {
            {"one", "two", "three"},
            {"on\\\"e", "two"},
            {"on\"e", "two"},
            {"one", "tw\"o"},
            {"one", "t\\,wo"}, // backslash in quotes only
            {"one", "two", "th,ree"},
            {"a\\\\"}, // backslash in quotes only escapes a delimiter (",")
            {"a\\", "b"}, // a backslash must be returned
            {"a\\\\,b"} // backslash in quotes only escapes a delimiter (",")
        };
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(res.length, records.size());
            assertFalse(records.isEmpty());
            for (int i = 0; i < res.length; i++) {
                assertArrayEquals(res[i], records.get(i).values());
            }
        }
    }

    

    

    

    

    

    

    

    @Test
    @Disabled("PR 295 does not work")
    public void testCSV141Excel() throws Exception {
        testCSV141Ok(CSVFormat.EXCEL);
    }

    private void testCSV141Failure(final CSVFormat format, final int failParseRecordNo)
            throws IOException {
        final Path path =
                Paths.get("src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv");
        try (final CSVParser parser = CSVParser.parse2(path, StandardCharsets.UTF_8, format)) {
            CSVRecord record = parse(parser, failParseRecordNo);
            if (record == null) {
                return; // expected failure
            }
            assertEquals("1414770317901", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1 _84*|*", record.get1(2));
            assertEquals("0", record.get1(3));
            assertEquals("pass sem1 _8", record.get1(4));
            assertEquals(5, record.size());
            record = parse(parser, failParseRecordNo);
            if (record == null) {
                return; // expected failure
            }
            assertEquals("1414770318470", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1 _84:|", record.get1(2));
            assertEquals("0", record.get1(3));
            assertEquals("pass sem1 _84:\\", record.get1(4));
            assertEquals(5, record.size());
            assertThrows(IOException.class, () -> parser.nextRecord());
        }
    }

    private void testCSV141Ok(final CSVFormat format) throws IOException {
        final Path path =
                Paths.get("src/test/resources/org/apache/commons/csv/CSV-141/csv-141.csv");
        try (final CSVParser parser = CSVParser.parse2(path, StandardCharsets.UTF_8, format)) {
            CSVRecord record = parser.nextRecord();
            assertEquals("1414770317901", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1 _84*|*", record.get1(2));
            assertEquals("0", record.get1(3));
            assertEquals("pass sem1 _8", record.get1(4));
            assertEquals(5, record.size());
            record = parser.nextRecord();
            assertEquals("1414770318470", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1 _84:|", record.get1(2));
            assertEquals("0", record.get1(3));
            assertEquals("pass sem1 _84:\\", record.get1(4));
            assertEquals(5, record.size());
            record = parser.nextRecord();
            assertEquals("1414770318327", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1", record.get1(2));
            assertEquals(3, record.size());
            record = parser.nextRecord();
            assertEquals("1414770318628", record.get1(0));
            assertEquals("android.widget.EditText", record.get1(1));
            assertEquals("pass sem1 _84*|*", record.get1(2));
            assertEquals("0", record.get1(3));
            assertEquals("pass sem1", record.get1(4));
            assertEquals(5, record.size());
        }
    }

    

    

    

    

    

    

    

    

    

    

    

    

    /**
     * Tests an exported Excel worksheet with a header row and rows that have more columns than the
     * headers
     */
    

    

    

    

    

    

    

    

    

    /**
     * Tests reusing a parser to process new string records one at a time as they are being
     * discovered. See [CSV-110].
     *
     * @throws IOException when an I/O error occurs.
     */
    

    

    

    

    

    

    

    

    

    

    

    

    

    @Test
    @Disabled
    public void testMongoDbCsv() throws Exception {
        try (final CSVParser parser =
                CSVParser.parse4("\"a a\",b,c" + LF + "d,e,f", CSVFormat.MONGODB_CSV)) {
            final Iterator<CSVRecord> itr1 = parser.iterator();
            final Iterator<CSVRecord> itr2 = parser.iterator();

            final CSVRecord first = itr1.next();
            assertEquals("a a", first.get1(0));
            assertEquals("b", first.get1(1));
            assertEquals("c", first.get1(2));

            final CSVRecord second = itr2.next();
            assertEquals("d", second.get1(0));
            assertEquals("e", second.get1(1));
            assertEquals("f", second.get1(2));
        }
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    @Test
    @Disabled
    public void testStartWithEmptyLinesThenHeaders() throws Exception {
        final String[] codes = {
            "\r\n\r\n\r\nhello,\r\n\r\n\r\n",
            "hello,\n\n\n",
            "hello,\"\"\r\n\r\n\r\n",
            "hello,\"\"\n\n\n"
        };
        final String[][] res = {
            {"hello", ""},
            {""}, // Excel format does not ignore empty lines
            {""}
        };
        for (final String code : codes) {
            try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.EXCEL)) {
                final List<CSVRecord> records = parser.getRecords();
                assertEquals(res.length, records.size());
                assertFalse(records.isEmpty());
                for (int i = 0; i < res.length; i++) {
                    assertArrayEquals(res[i], records.get(i).values());
                }
            }
        }
    }

    

    private void validateLineNumbers(final String lineSeparator) throws IOException {
        try (final CSVParser parser =
                CSVParser.parse4(
                        "a" + lineSeparator + "b" + lineSeparator + "c",
                        CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator))) {
            assertEquals(0, parser.getCurrentLineNumber());
            assertNotNull(parser.nextRecord());
            assertEquals(1, parser.getCurrentLineNumber());
            assertNotNull(parser.nextRecord());
            assertEquals(2, parser.getCurrentLineNumber());
            assertNotNull(parser.nextRecord());
            assertEquals(3, parser.getCurrentLineNumber());
            assertNull(parser.nextRecord());
            assertEquals(3, parser.getCurrentLineNumber());
        }
    }

    private void validateRecordNumbers(final String lineSeparator) throws IOException {
        try (final CSVParser parser =
                CSVParser.parse4(
                        "a" + lineSeparator + "b" + lineSeparator + "c",
                        CSVFormat.DEFAULT.withRecordSeparator1(lineSeparator))) {
            CSVRecord record;
            assertEquals(0, parser.getRecordNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(1, record.getRecordNumber());
            assertEquals(1, parser.getRecordNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(2, record.getRecordNumber());
            assertEquals(2, parser.getRecordNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(3, record.getRecordNumber());
            assertEquals(3, parser.getRecordNumber());
            assertNull(record = parser.nextRecord());
            assertEquals(3, parser.getRecordNumber());
        }
    }

    private void validateRecordPosition(final String lineSeparator) throws IOException {
        final String nl = lineSeparator; // used as linebreak in values for better distinction

        final String code =
                "a,b,c"
                        + lineSeparator
                        + "1,2,3"
                        + lineSeparator
                        + "'A"
                        + nl
                        + "A','B"
                        + nl
                        + "B',CC"
                        + lineSeparator
                        + "\u00c4,\u00d6,\u00dc"
                        + lineSeparator
                        + "EOF,EOF,EOF";

        final CSVFormat format =
                CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(lineSeparator);
        CSVParser parser = CSVParser.parse4(code, format);

        CSVRecord record;
        assertEquals(0, parser.getRecordNumber());

        assertNotNull(record = parser.nextRecord());
        assertEquals(1, record.getRecordNumber());
        assertEquals(code.indexOf('a'), record.getCharacterPosition());

        assertNotNull(record = parser.nextRecord());
        assertEquals(2, record.getRecordNumber());
        assertEquals(code.indexOf('1'), record.getCharacterPosition());

        assertNotNull(record = parser.nextRecord());
        final long positionRecord3 = record.getCharacterPosition();
        assertEquals(3, record.getRecordNumber());
        assertEquals(code.indexOf("'A"), record.getCharacterPosition());
        assertEquals("A" + lineSeparator + "A", record.get1(0));
        assertEquals("B" + lineSeparator + "B", record.get1(1));
        assertEquals("CC", record.get1(2));

        assertNotNull(record = parser.nextRecord());
        assertEquals(4, record.getRecordNumber());
        assertEquals(code.indexOf('\u00c4'), record.getCharacterPosition());

        assertNotNull(record = parser.nextRecord());
        assertEquals(5, record.getRecordNumber());
        assertEquals(code.indexOf("EOF"), record.getCharacterPosition());

        parser.close();

        parser =
                new CSVParser(
                        new StringReader(code.substring((int) positionRecord3)),
                        format,
                        positionRecord3,
                        3);

        assertNotNull(record = parser.nextRecord());
        assertEquals(3, record.getRecordNumber());
        assertEquals(code.indexOf("'A"), record.getCharacterPosition());
        assertEquals("A" + lineSeparator + "A", record.get1(0));
        assertEquals("B" + lineSeparator + "B", record.get1(1));
        assertEquals("CC", record.get1(2));

        assertNotNull(record = parser.nextRecord());
        assertEquals(4, record.getRecordNumber());
        assertEquals(code.indexOf('\u00c4'), record.getCharacterPosition());
        assertEquals("\u00c4", record.get1(0));

        parser.close();
    }

    @Test
    public void testBackslashEscaping_test0_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
    }

    @Test
    public void testBackslashEscaping_test1_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withQuote0('\'');
    }

    @Test
    public void testBackslashEscaping_test2_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withQuote0('\'');
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF);
    }

    @Test
    public void testBackslashEscaping_test3_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withQuote0('\'');
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF).withEscape0('/');
    }

    @Test
    public void testBackslashEscaping_test4_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withQuote0('\'');
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF).withEscape0('/');
        final CSVFormat format =
                CSVFormat.newFormat(',')
                        .withQuote0('\'')
                        .withRecordSeparator1(CRLF)
                        .withEscape0('/')
                        .withIgnoreEmptyLines0();
    }

    @Test
    public void testBackslashEscaping_test5_decomposed() throws IOException {
        final String code =
                "one,two,three\n" // 0
                        + "'',''\n" // 1) empty encapsulators
                        + "/',/'\n" // 2) single encapsulators
                        + "'/'','/''\n" // 3) single encapsulators encapsulated via escape
                        + "'''',''''\n" // 4) single encapsulators encapsulated via doubling
                        + "/,,/,\n" // 5) separator escaped
                        + "//,//\n" // 6) escape escaped
                        + "'//','//'\n" // 7) escape escaped in encapsulation
                        + "   8   ,   \"quoted \"\" /\" // string\"   \n" // don't eat spaces
                        + "9,   /\n   \n" // escaped newline
                        + "";
        final String[][] res = {
            {"one", "two", "three"}, // 0
            {"", ""}, // 1
            {"'", "'"}, // 2
            {"'", "'"}, // 3
            {"'", "'"}, // 4
            {",", ","}, // 5
            {"/", "/"}, // 6
            {"/", "/"}, // 7
            {"   8   ", "   \"quoted \"\" /\" / string\"   "},
            {"9", "   \n   "},
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withQuote0('\'');
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withQuote0('\'').withRecordSeparator1(CRLF).withEscape0('/');
        final CSVFormat format =
                CSVFormat.newFormat(',')
                        .withQuote0('\'')
                        .withRecordSeparator1(CRLF)
                        .withEscape0('/')
                        .withIgnoreEmptyLines0();
        try (final CSVParser parser = CSVParser.parse4(code, format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());

            Utils.compare("Records do not match expected result", res, records);
        }
    }

    @Test
    public void testBackslashEscaping2_test0_decomposed() throws IOException {
        final String code =
                ""
                        + " , , \n" // 1)
                        + " \t ,  , \n" // 2)
                        + " // , /, , /,\n" // 3)
                        + "";
        final String[][] res = {
            {" ", " ", " "}, // 1
            {" \t ", "  ", " "}, // 2
            {" / ", " , ", " ,"}, // 3
        };
        CSVFormat.newFormat(',');
    }

    @Test
    public void testBackslashEscaping2_test1_decomposed() throws IOException {
        final String code =
                ""
                        + " , , \n" // 1)
                        + " \t ,  , \n" // 2)
                        + " // , /, , /,\n" // 3)
                        + "";
        final String[][] res = {
            {" ", " ", " "}, // 1
            {" \t ", "  ", " "}, // 2
            {" / ", " , ", " ,"}, // 3
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF);
    }

    @Test
    public void testBackslashEscaping2_test2_decomposed() throws IOException {
        final String code =
                ""
                        + " , , \n" // 1)
                        + " \t ,  , \n" // 2)
                        + " // , /, , /,\n" // 3)
                        + "";
        final String[][] res = {
            {" ", " ", " "}, // 1
            {" \t ", "  ", " "}, // 2
            {" / ", " , ", " ,"}, // 3
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF).withEscape0('/');
    }

    @Test
    public void testBackslashEscaping2_test3_decomposed() throws IOException {
        final String code =
                ""
                        + " , , \n" // 1)
                        + " \t ,  , \n" // 2)
                        + " // , /, , /,\n" // 3)
                        + "";
        final String[][] res = {
            {" ", " ", " "}, // 1
            {" \t ", "  ", " "}, // 2
            {" / ", " , ", " ,"}, // 3
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF).withEscape0('/');
        final CSVFormat format =
                CSVFormat.newFormat(',')
                        .withRecordSeparator1(CRLF)
                        .withEscape0('/')
                        .withIgnoreEmptyLines0();
    }

    @Test
    public void testBackslashEscaping2_test4_decomposed() throws IOException {
        final String code =
                ""
                        + " , , \n" // 1)
                        + " \t ,  , \n" // 2)
                        + " // , /, , /,\n" // 3)
                        + "";
        final String[][] res = {
            {" ", " ", " "}, // 1
            {" \t ", "  ", " "}, // 2
            {" / ", " , ", " ,"}, // 3
        };
        CSVFormat.newFormat(',');
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF);
        CSVFormat.newFormat(',').withRecordSeparator1(CRLF).withEscape0('/');
        final CSVFormat format =
                CSVFormat.newFormat(',')
                        .withRecordSeparator1(CRLF)
                        .withEscape0('/')
                        .withIgnoreEmptyLines0();
        try (final CSVParser parser = CSVParser.parse4(code, format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());

            Utils.compare("", res, records);
        }
    }

    @Test
    public void testCarriageReturnEndings_test0_decomposed() throws IOException {
        final String code = "foo\rbaar,\rhello,world\r,kanu";
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
        }
    }

    @Test
    public void testCarriageReturnLineFeedEndings_test0_decomposed() throws IOException {
        final String code = "foo\r\nbaar,\r\nhello,world\r\n,kanu";
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
        }
    }

    @Test
    public void testCSV141CSVFormat_DEFAULT_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.DEFAULT, 3);
    }

    @Test
    public void testCSV141CSVFormat_INFORMIX_UNLOAD_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.INFORMIX_UNLOAD, 1);
    }

    @Test
    public void testCSV141CSVFormat_INFORMIX_UNLOAD_CSV_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.INFORMIX_UNLOAD_CSV, 3);
    }

    @Test
    public void testCSV141CSVFormat_ORACLE_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.ORACLE, 2);
    }

    @Test
    public void testCSV141CSVFormat_POSTGRESQL_CSV_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.POSTGRESQL_CSV, 3);
    }

    @Test
    public void testCSV141RFC4180_test0_decomposed() throws Exception {
        testCSV141Failure(CSVFormat.RFC4180, 3);
    }

    @Test
    public void testCSV235_test0_decomposed() throws IOException {
        final String dqString = "\"aaa\",\"b\"\"bb\",\"ccc\"";
        try (final CSVParser parser = CSVFormat.RFC4180.parse(new StringReader(dqString))) {
            final Iterator<CSVRecord> records = parser.iterator();
            final CSVRecord record = records.next();
            assertFalse(records.hasNext());
            assertEquals(3, record.size());
            assertEquals("aaa", record.get1(0));
            assertEquals("b\"bb", record.get1(1));
            assertEquals("ccc", record.get1(2));
        }
    }

    @Test
    public void testCSV57_test0_decomposed() throws Exception {
        try (final CSVParser parser = CSVParser.parse4("", CSVFormat.DEFAULT)) {
            final List<CSVRecord> list = parser.getRecords();
            assertNotNull(list);
            assertEquals(0, list.size());
        }
    }

    @Test
    public void testDefaultFormat_test0_decomposed() throws IOException {
        final String code =
                ""
                        + "a,b#\n" // 1)
                        + "\"\n\",\" \",#\n" // 2)
                        + "#,\"\"\n" // 3)
                        + "# Final comment\n" // 4)
                ;
        final String[][] res = {{"a", "b#"}, {"\n", " ", "#"}, {"#", ""}, {"# Final comment"}};
        CSVFormat format = CSVFormat.DEFAULT;
        assertFalse(format.isCommentMarkerSet());
    }

    @Test
    public void testDefaultFormat_test1_decomposed() throws IOException {
        final String code =
                ""
                        + "a,b#\n" // 1)
                        + "\"\n\",\" \",#\n" // 2)
                        + "#,\"\"\n" // 3)
                        + "# Final comment\n" // 4)
                ;
        final String[][] res = {{"a", "b#"}, {"\n", " ", "#"}, {"#", ""}, {"# Final comment"}};
        CSVFormat format = CSVFormat.DEFAULT;
        assertFalse(format.isCommentMarkerSet());
        final String[][] res_comments = {
            {"a", "b#"}, {"\n", " ", "#"},
        };
        try (final CSVParser parser = CSVParser.parse4(code, format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());

            Utils.compare("Failed to parse without comments", res, records);

            format = CSVFormat.DEFAULT.withCommentMarker0('#');
        }
    }

    @Test
    public void testDefaultFormat_test2_decomposed() throws IOException {
        final String code =
                ""
                        + "a,b#\n" // 1)
                        + "\"\n\",\" \",#\n" // 2)
                        + "#,\"\"\n" // 3)
                        + "# Final comment\n" // 4)
                ;
        final String[][] res = {{"a", "b#"}, {"\n", " ", "#"}, {"#", ""}, {"# Final comment"}};
        CSVFormat format = CSVFormat.DEFAULT;
        assertFalse(format.isCommentMarkerSet());
        final String[][] res_comments = {
            {"a", "b#"}, {"\n", " ", "#"},
        };
        try (final CSVParser parser = CSVParser.parse4(code, format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());

            Utils.compare("Failed to parse without comments", res, records);

            format = CSVFormat.DEFAULT.withCommentMarker0('#');
        }
        try (final CSVParser parser = CSVParser.parse4(code, format)) {
            final List<CSVRecord> records = parser.getRecords();

            Utils.compare("Failed to parse with comments", res_comments, records);
        }
    }

    @Test
    public void testEmptyFile_test0_decomposed() throws Exception {
        try (final CSVParser parser =
                CSVParser.parse2(
                        Paths.get("src/test/resources/org/apache/commons/csv/empty.txt"),
                        StandardCharsets.UTF_8,
                        CSVFormat.DEFAULT)) {
            assertNull(parser.nextRecord());
        }
    }

    @Test
    public void testEmptyLineBehaviorCSV_test0_decomposed() throws Exception {
        final String[] codes = {
            "hello,\r\n\r\n\r\n", "hello,\n\n\n", "hello,\"\"\r\n\r\n\r\n", "hello,\"\"\n\n\n"
        };
        final String[][] res = {
            {"hello", ""} // CSV format ignores empty lines
        };
        for (final String code : codes) {
            try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
                final List<CSVRecord> records = parser.getRecords();
                assertEquals(res.length, records.size());
                assertFalse(records.isEmpty());
                for (int i = 0; i < res.length; i++) {
                    assertArrayEquals(res[i], records.get(i).values());
                }
            }
        }
    }

    @Test
    public void testEmptyLineBehaviorExcel_test0_decomposed() throws Exception {
        final String[] codes = {
            "hello,\r\n\r\n\r\n", "hello,\n\n\n", "hello,\"\"\r\n\r\n\r\n", "hello,\"\"\n\n\n"
        };
        final String[][] res = {
            {"hello", ""},
            {""}, // Excel format does not ignore empty lines
            {""}
        };
        for (final String code : codes) {
            try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.EXCEL)) {
                final List<CSVRecord> records = parser.getRecords();
                assertEquals(res.length, records.size());
                assertFalse(records.isEmpty());
                for (int i = 0; i < res.length; i++) {
                    assertArrayEquals(res[i], records.get(i).values());
                }
            }
        }
    }

    @Test
    public void testEmptyString_test0_decomposed() throws Exception {
        try (final CSVParser parser = CSVParser.parse4("", CSVFormat.DEFAULT)) {
            assertNull(parser.nextRecord());
        }
    }

    @Test
    public void testEndOfFileBehaviorCSV_test0_decomposed() throws Exception {
        final String[] codes = {
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            "hello,\r\n\r\nworld,\"\"\r\n",
            "hello,\r\n\r\nworld,\"\"",
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            "hello,\r\n\r\nworld,\"\"\n",
            "hello,\r\n\r\nworld,\"\""
        };
        final String[][] res = {
            {"hello", ""}, // CSV format ignores empty lines
            {"world", ""}
        };
        for (final String code : codes) {
            try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
                final List<CSVRecord> records = parser.getRecords();
                assertEquals(res.length, records.size());
                assertFalse(records.isEmpty());
                for (int i = 0; i < res.length; i++) {
                    assertArrayEquals(res[i], records.get(i).values());
                }
            }
        }
    }

    @Test
    public void testEndOfFileBehaviorExcel_test0_decomposed() throws Exception {
        final String[] codes = {
            "hello,\r\n\r\nworld,\r\n",
            "hello,\r\n\r\nworld,",
            "hello,\r\n\r\nworld,\"\"\r\n",
            "hello,\r\n\r\nworld,\"\"",
            "hello,\r\n\r\nworld,\n",
            "hello,\r\n\r\nworld,",
            "hello,\r\n\r\nworld,\"\"\n",
            "hello,\r\n\r\nworld,\"\""
        };
        final String[][] res = {
            {"hello", ""},
            {""}, // Excel format does not ignore empty lines
            {"world", ""}
        };
        for (final String code : codes) {
            try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.EXCEL)) {
                final List<CSVRecord> records = parser.getRecords();
                assertEquals(res.length, records.size());
                assertFalse(records.isEmpty());
                for (int i = 0; i < res.length; i++) {
                    assertArrayEquals(res[i], records.get(i).values());
                }
            }
        }
    }

    @Test
    public void testExcelFormat1_test0_decomposed() throws IOException {
        final String code =
                "value1,value2,value3,value4\r\na,b,c,d\r\n  x,,,"
                        + "\r\n\r\n\"\"\"hello\"\"\",\"  \"\"world\"\"\",\"abc\ndef\",\r\n";
        final String[][] res = {
            {"value1", "value2", "value3", "value4"},
            {"a", "b", "c", "d"},
            {"  x", "", "", ""},
            {""},
            {"\"hello\"", "  \"world\"", "abc\ndef", ""}
        };
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.EXCEL)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(res.length, records.size());
            assertFalse(records.isEmpty());
            for (int i = 0; i < res.length; i++) {
                assertArrayEquals(res[i], records.get(i).values());
            }
        }
    }

    @Test
    public void testExcelFormat2_test0_decomposed() throws Exception {
        final String code = "foo,baar\r\n\r\nhello,\r\n\r\nworld,\r\n";
        final String[][] res = {{"foo", "baar"}, {""}, {"hello", ""}, {""}, {"world", ""}};
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.EXCEL)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(res.length, records.size());
            assertFalse(records.isEmpty());
            for (int i = 0; i < res.length; i++) {
                assertArrayEquals(res[i], records.get(i).values());
            }
        }
    }

    @Test
    public void testFirstEndOfLineCr_test0_decomposed() throws IOException {
        final String data = "foo\rbaar,\rhello,world\r,kanu";
        try (final CSVParser parser = CSVParser.parse4(data, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
            assertEquals("\r", parser.getFirstEndOfLine());
        }
    }

    @Test
    public void testFirstEndOfLineCrLf_test0_decomposed() throws IOException {
        final String data = "foo\r\nbaar,\r\nhello,world\r\n,kanu";
        try (final CSVParser parser = CSVParser.parse4(data, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
            assertEquals("\r\n", parser.getFirstEndOfLine());
        }
    }

    @Test
    public void testFirstEndOfLineLf_test0_decomposed() throws IOException {
        final String data = "foo\nbaar,\nhello,world\n,kanu";
        try (final CSVParser parser = CSVParser.parse4(data, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
            assertEquals("\n", parser.getFirstEndOfLine());
        }
    }

    @Test
    public void testForEach_test0_decomposed() throws Exception {
        try (final Reader in = new StringReader("a,b,c\n1,2,3\nx,y,z");
                final CSVParser parser = CSVFormat.DEFAULT.parse(in)) {
            final List<CSVRecord> records = new ArrayList<>();
            for (final CSVRecord record : parser) {
                records.add(record);
            }
            assertEquals(3, records.size());
            assertArrayEquals(new String[] {"a", "b", "c"}, records.get(0).values());
            assertArrayEquals(new String[] {"1", "2", "3"}, records.get(1).values());
            assertArrayEquals(new String[] {"x", "y", "z"}, records.get(2).values());
        }
    }

    @Test
    public void testGetLine_test0_decomposed() throws IOException {
        try (final CSVParser parser =
                CSVParser.parse4(CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0())) {
            for (final String[] re : RESULT) {
                assertArrayEquals(re, parser.nextRecord().values());
            }

            assertNull(parser.nextRecord());
        }
    }

    @Test
    public void testGetLineNumberWithCR_test0_decomposed() throws Exception {
        String.valueOf(CR);
    }

    @Test
    public void testGetLineNumberWithCR_test1_decomposed() throws Exception {
        String.valueOf(CR);
        this.validateLineNumbers(String.valueOf(CR));
    }

    @Test
    public void testGetLineNumberWithCRLF_test0_decomposed() throws Exception {
        this.validateLineNumbers(CRLF);
    }

    @Test
    public void testGetLineNumberWithLF_test0_decomposed() throws Exception {
        String.valueOf(LF);
    }

    @Test
    public void testGetLineNumberWithLF_test1_decomposed() throws Exception {
        String.valueOf(LF);
        this.validateLineNumbers(String.valueOf(LF));
    }

    @Test
    public void testGetOneLine_test0_decomposed() throws IOException {
        try (final CSVParser parser = CSVParser.parse4(CSV_INPUT_1, CSVFormat.DEFAULT)) {
            final CSVRecord record = parser.getRecords().get(0);
            assertArrayEquals(RESULT[0], record.values());
        }
    }

    @Test
    public void testGetOneLineOneParser_test0_decomposed() throws IOException {
        final CSVFormat format = CSVFormat.DEFAULT;
        try (final PipedWriter writer = new PipedWriter();
                final CSVParser parser = CSVParser.CSVParser1(new PipedReader(writer), format)) {
            writer.append(CSV_INPUT_1);
            writer.append(format.getRecordSeparator());
            final CSVRecord record1 = parser.nextRecord();
            assertArrayEquals(RESULT[0], record1.values());
            writer.append(CSV_INPUT_2);
            writer.append(format.getRecordSeparator());
            final CSVRecord record2 = parser.nextRecord();
            assertArrayEquals(RESULT[1], record2.values());
        }
    }

    @Test
    public void testGetRecordNumberWithCR_test0_decomposed() throws Exception {
        String.valueOf(CR);
    }

    @Test
    public void testGetRecordNumberWithCR_test1_decomposed() throws Exception {
        String.valueOf(CR);
        this.validateRecordNumbers(String.valueOf(CR));
    }

    @Test
    public void testGetRecordNumberWithCRLF_test0_decomposed() throws Exception {
        this.validateRecordNumbers(CRLF);
    }

    @Test
    public void testGetRecordNumberWithLF_test0_decomposed() throws Exception {
        String.valueOf(LF);
    }

    @Test
    public void testGetRecordNumberWithLF_test1_decomposed() throws Exception {
        String.valueOf(LF);
        this.validateRecordNumbers(String.valueOf(LF));
    }

    @Test
    public void testGetRecordPositionWithCRLF_test0_decomposed() throws Exception {
        this.validateRecordPosition(CRLF);
    }

    @Test
    public void testGetRecordPositionWithLF_test0_decomposed() throws Exception {
        String.valueOf(LF);
    }

    @Test
    public void testGetRecordPositionWithLF_test1_decomposed() throws Exception {
        String.valueOf(LF);
        this.validateRecordPosition(String.valueOf(LF));
    }

    @Test
    public void testGetRecords_test0_decomposed() throws IOException {
        try (final CSVParser parser =
                CSVParser.parse4(CSV_INPUT, CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0())) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(RESULT.length, records.size());
            assertFalse(records.isEmpty());
            for (int i = 0; i < RESULT.length; i++) {
                assertArrayEquals(RESULT[i], records.get(i).values());
            }
        }
    }

    @Test
    public void testGetRecordWithMultiLineValues_test0_decomposed() throws Exception {
        try (final CSVParser parser =
                CSVParser.parse4(
                        "\"a\r\n1\",\"a\r\n2\""
                                + CRLF
                                + "\"b\r\n1\",\"b\r\n2\""
                                + CRLF
                                + "\"c\r\n1\",\"c\r\n2\"",
                        CSVFormat.DEFAULT.withRecordSeparator1(CRLF))) {
            CSVRecord record;
            assertEquals(0, parser.getRecordNumber());
            assertEquals(0, parser.getCurrentLineNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(3, parser.getCurrentLineNumber());
            assertEquals(1, record.getRecordNumber());
            assertEquals(1, parser.getRecordNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(6, parser.getCurrentLineNumber());
            assertEquals(2, record.getRecordNumber());
            assertEquals(2, parser.getRecordNumber());
            assertNotNull(record = parser.nextRecord());
            assertEquals(9, parser.getCurrentLineNumber());
            assertEquals(3, record.getRecordNumber());
            assertEquals(3, parser.getRecordNumber());
            assertNull(record = parser.nextRecord());
            assertEquals(9, parser.getCurrentLineNumber());
            assertEquals(3, parser.getRecordNumber());
        }
    }

    @Test
    public void testIgnoreEmptyLines_test0_decomposed() throws IOException {
        final String code = "\nfoo,baar\n\r\n,\n\n,world\r\n\n";
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(3, records.size());
        }
    }

    @Test
    public void testInvalidFormat_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withDelimiter(CR));
    }

    @Test
    public void testIterator_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a,b,c\n1,2,3\nx,y,z");
        try (final CSVParser parser = CSVFormat.DEFAULT.parse(in)) {
            final Iterator<CSVRecord> iterator = parser.iterator();

            assertTrue(iterator.hasNext());
            assertThrows(UnsupportedOperationException.class, iterator::remove);
            assertArrayEquals(new String[] {"a", "b", "c"}, iterator.next().values());
            assertArrayEquals(new String[] {"1", "2", "3"}, iterator.next().values());
            assertTrue(iterator.hasNext());
            assertTrue(iterator.hasNext());
            assertTrue(iterator.hasNext());
            assertArrayEquals(new String[] {"x", "y", "z"}, iterator.next().values());
            assertFalse(iterator.hasNext());

            assertThrows(NoSuchElementException.class, iterator::next);
        }
    }

    @Test
    public void testIteratorSequenceBreaking_test0_decomposed() throws IOException {
        final String fiveRows = "1\n2\n3\n4\n5\n";
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {

            final Iterator<CSVRecord> iter = parser.iterator();
            int recordNumber = 0;
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            iter.hasNext();
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
    }

    @Test
    public void testIteratorSequenceBreaking_test1_decomposed() throws IOException {
        final String fiveRows = "1\n2\n3\n4\n5\n";
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {

            final Iterator<CSVRecord> iter = parser.iterator();
            int recordNumber = 0;
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            iter.hasNext();
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {
            int recordNumber = 0;
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
    }

    @Test
    public void testIteratorSequenceBreaking_test2_decomposed() throws IOException {
        final String fiveRows = "1\n2\n3\n4\n5\n";
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {

            final Iterator<CSVRecord> iter = parser.iterator();
            int recordNumber = 0;
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            iter.hasNext();
            while (iter.hasNext()) {
                final CSVRecord record = iter.next();
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {
            int recordNumber = 0;
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
        try (CSVParser parser = CSVFormat.DEFAULT.parse(new StringReader(fiveRows))) {
            int recordNumber = 0;
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
                if (recordNumber >= 2) {
                    break;
                }
            }
            parser.iterator().hasNext();
            for (final CSVRecord record : parser) {
                recordNumber++;
                assertEquals(String.valueOf(recordNumber), record.get1(0));
            }
        }
    }

    @Test
    public void testLineFeedEndings_test0_decomposed() throws IOException {
        final String code = "foo\nbaar,\nhello,world\n,kanu";
        try (final CSVParser parser = CSVParser.parse4(code, CSVFormat.DEFAULT)) {
            final List<CSVRecord> records = parser.getRecords();
            assertEquals(4, records.size());
        }
    }

    @Test
    public void testMultipleIterators_test0_decomposed() throws Exception {
        try (final CSVParser parser =
                CSVParser.parse4("a,b,c" + CRLF + "d,e,f", CSVFormat.DEFAULT)) {
            final Iterator<CSVRecord> itr1 = parser.iterator();

            final CSVRecord first = itr1.next();
            assertEquals("a", first.get1(0));
            assertEquals("b", first.get1(1));
            assertEquals("c", first.get1(2));

            final CSVRecord second = itr1.next();
            assertEquals("d", second.get1(0));
            assertEquals("e", second.get1(1));
            assertEquals("f", second.get1(2));
        }
    }

    @Test
    public void testNewCSVParserNullReaderFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class, () -> CSVParser.CSVParser1(null, CSVFormat.DEFAULT));
    }

    @Test
    public void testNewCSVParserReaderNullFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class, () -> CSVParser.CSVParser1(new StringReader(""), null));
    }

    @Test
    public void testNoHeaderMap_test0_decomposed() throws Exception {
        try (final CSVParser parser = CSVParser.parse4("a,b,c\n1,2,3\nx,y,z", CSVFormat.DEFAULT)) {
            assertNull(parser.getHeaderMap());
        }
    }

    @Test
    public void testNotValueCSV_test0_decomposed() throws IOException {
        final String source = "#";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withCommentMarker0('#');
    }

    @Test
    public void testNotValueCSV_test1_decomposed() throws IOException {
        final String source = "#";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withCommentMarker0('#');
        try (final CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            final CSVRecord csvRecord = csvParser.nextRecord();
            assertNull(csvRecord);
        }
    }

    @Test
    public void testParseFileNullFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () ->
                        CSVParser.parse0(
                                new File("CSVFileParser/test.csv"),
                                Charset.defaultCharset(),
                                null));
    }

    @Test
    public void testParseNullFileFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () -> CSVParser.parse0((File) null, Charset.defaultCharset(), CSVFormat.DEFAULT));
    }

    @Test
    public void testParseNullPathFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () -> CSVParser.parse2((Path) null, Charset.defaultCharset(), CSVFormat.DEFAULT));
    }

    @Test
    public void testParseNullStringFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () -> CSVParser.parse4((String) null, CSVFormat.DEFAULT));
    }

    @Test
    public void testParseNullUrlCharsetFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () -> CSVParser.parse5((URL) null, Charset.defaultCharset(), CSVFormat.DEFAULT));
    }

    @Test
    public void testParserUrlNullCharsetFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () ->
                        CSVParser.parse5(
                                new URL("https://commons.apache.org"), null, CSVFormat.DEFAULT));
    }

    @Test
    public void testParseStringNullFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class, () -> CSVParser.parse4("csv data", (CSVFormat) null));
    }

    @Test
    public void testParseUrlCharsetNullFormat_test0_decomposed()  {
        assertThrows(
                NullPointerException.class,
                () ->
                        CSVParser.parse5(
                                new URL("https://commons.apache.org"),
                                Charset.defaultCharset(),
                                null));
    }

    @Test
    public void testParseWithDelimiterStringWithEscape_test0_decomposed() throws IOException {
        final String source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testParseWithDelimiterStringWithEscape_test1_decomposed() throws IOException {
        final String source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
    }

    @Test
    public void testParseWithDelimiterStringWithEscape_test2_decomposed() throws IOException {
        final String source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
    }

    @Test
    public void testParseWithDelimiterStringWithEscape_test3_decomposed() throws IOException {
        final String source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').build();
    }

    @Test
    public void testParseWithDelimiterStringWithEscape_test4_decomposed() throws IOException {
        final String source = "a![!|!]b![|]c[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').build();
        try (CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            CSVRecord csvRecord = csvParser.nextRecord();
            assertEquals("a[|]b![|]c", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
            csvRecord = csvParser.nextRecord();
            assertEquals("abc[abc]", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
        }
    }

    @Test
    public void testParseWithDelimiterStringWithQuote_test0_decomposed() throws IOException {
        final String source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testParseWithDelimiterStringWithQuote_test1_decomposed() throws IOException {
        final String source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
    }

    @Test
    public void testParseWithDelimiterStringWithQuote_test2_decomposed() throws IOException {
        final String source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'');
    }

    @Test
    public void testParseWithDelimiterStringWithQuote_test3_decomposed() throws IOException {
        final String source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'');
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'').build();
    }

    @Test
    public void testParseWithDelimiterStringWithQuote_test4_decomposed() throws IOException {
        final String source = "'a[|]b[|]c'[|]xyz\r\nabc[abc][|]xyz";
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'');
        final CSVFormat csvFormat =
                CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'').build();
        try (CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            CSVRecord csvRecord = csvParser.nextRecord();
            assertEquals("a[|]b[|]c", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
            csvRecord = csvParser.nextRecord();
            assertEquals("abc[abc]", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
        }
    }

    @Test
    public void testParseWithDelimiterWithEscape_test0_decomposed() throws IOException {
        final String source = "a!,b!,c,xyz";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withEscape0('!');
    }

    @Test
    public void testParseWithDelimiterWithEscape_test1_decomposed() throws IOException {
        final String source = "a!,b!,c,xyz";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withEscape0('!');
        try (CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            final CSVRecord csvRecord = csvParser.nextRecord();
            assertEquals("a,b,c", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
        }
    }

    @Test
    public void testParseWithDelimiterWithQuote_test0_decomposed() throws IOException {
        final String source = "'a,b,c',xyz";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'');
    }

    @Test
    public void testParseWithDelimiterWithQuote_test1_decomposed() throws IOException {
        final String source = "'a,b,c',xyz";
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'');
        try (CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            final CSVRecord csvRecord = csvParser.nextRecord();
            assertEquals("a,b,c", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
        }
    }

    @Test
    public void testParseWithQuoteThrowsException_test0_decomposed()  {
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'');
    }

    @Test
    public void testParseWithQuoteThrowsException_test1_decomposed()  {
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'');
        assertThrows(
                IOException.class,
                () -> csvFormat.parse(new StringReader("'a,b,c','")).nextRecord());
        assertThrows(
                IOException.class,
                () -> csvFormat.parse(new StringReader("'a,b,c'abc,xyz")).nextRecord());
        assertThrows(
                IOException.class,
                () -> csvFormat.parse(new StringReader("'abc'a,b,c',xyz")).nextRecord());
    }

    @Test
    public void testParseWithQuoteWithEscape_test0_decomposed() throws IOException {
        final String source = "'a?,b?,c?d',xyz";
        CSVFormat.DEFAULT.withQuote0('\'');
    }

    @Test
    public void testParseWithQuoteWithEscape_test1_decomposed() throws IOException {
        final String source = "'a?,b?,c?d',xyz";
        CSVFormat.DEFAULT.withQuote0('\'');
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'').withEscape0('?');
    }

    @Test
    public void testParseWithQuoteWithEscape_test2_decomposed() throws IOException {
        final String source = "'a?,b?,c?d',xyz";
        CSVFormat.DEFAULT.withQuote0('\'');
        final CSVFormat csvFormat = CSVFormat.DEFAULT.withQuote0('\'').withEscape0('?');
        try (CSVParser csvParser = csvFormat.parse(new StringReader(source))) {
            final CSVRecord csvRecord = csvParser.nextRecord();
            assertEquals("a,b,c?d", csvRecord.get1(0));
            assertEquals("xyz", csvRecord.get1(1));
        }
    }

    @Test
    public void testRoundtrip_test0_decomposed() throws Exception {
        final StringWriter out = new StringWriter();
        final String data = "a,b,c\r\n1,2,3\r\nx,y,z\r\n";
        try (final CSVPrinter printer = new CSVPrinter(out, CSVFormat.DEFAULT);
                final CSVParser parse = CSVParser.parse4(data, CSVFormat.DEFAULT)) {
            for (final CSVRecord record : parse) {
                printer.printRecord0(record);
            }
            assertEquals(data, out.toString());
        }
    }

    @Test
    public void testStream_test0_decomposed() throws Exception {
        final Reader in = new StringReader("a,b,c\n1,2,3\nx,y,z");
        try (final CSVParser parser = CSVFormat.DEFAULT.parse(in)) {
            final List<CSVRecord> list = parser.stream().collect(Collectors.toList());
            assertFalse(list.isEmpty());
            assertArrayEquals(new String[] {"a", "b", "c"}, list.get(0).values());
            assertArrayEquals(new String[] {"1", "2", "3"}, list.get(1).values());
            assertArrayEquals(new String[] {"x", "y", "z"}, list.get(2).values());
        }
    }
}