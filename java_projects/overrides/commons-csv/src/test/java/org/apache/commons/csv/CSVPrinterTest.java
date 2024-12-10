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

import static org.apache.commons.csv.Constants.BACKSLASH;
import static org.apache.commons.csv.Constants.CR;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.io.StringReader;
import java.io.StringWriter;
import java.io.Writer;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;
import java.util.Random;

/** Tests {@link CSVPrinter}. */
public class CSVPrinterTest {

    private static final char DQUOTE_CHAR = '"';
    private static final char EURO_CH = '\u20AC';
    private static final int ITERATIONS_FOR_RANDOM_TEST = 1; // was: 50000
    private static final char QUOTE_CH = '\'';

    private static String printable(final String s) {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            final char ch = s.charAt(i);
            if (ch <= ' ' || ch >= 128) {
                sb.append("(").append((int) ch).append(")");
            } else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }

    private String longText2;

    private final String recordSeparator = CSVFormat.DEFAULT.getRecordSeparator();

    private File createTempFile() throws IOException {
        return createTempPath().toFile();
    }

    private Path createTempPath() throws IOException {
        return Files.createTempFile(getClass().getName(), ".csv");
    }

    private void doOneRandom(final CSVFormat format) throws Exception {
        final Random r = new Random();

        final int nLines = r.nextInt(4) + 1;
        final int nCol = r.nextInt(3) + 1;
        final String[][] lines = generateLines(nLines, nCol);

        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {

            for (int i = 0; i < nLines; i++) {
                printer.printRecord1((Object[]) lines[i]);
            }

            printer.flush();
        }
        final String result = sw.toString();

        try (final CSVParser parser = CSVParser.parse4(result, format)) {
            final List<CSVRecord> parseResult = parser.getRecords();

            final String[][] expected = lines.clone();
            for (int i = 0; i < expected.length; i++) {
                expected[i] = expectNulls(expected[i], format);
            }
            Utils.compare("Printer output :" + printable(result), expected, parseResult);
        }
    }

    private void doRandom(final CSVFormat format, final int iter) throws Exception {
        for (int i = 0; i < iter; i++) {
            doOneRandom(format);
        }
    }

    /**
     * Converts an input CSV array into expected output values WRT NULLs. NULL strings are converted
     * to null values because the parser will convert these strings to null.
     */
    private <T> T[] expectNulls(final T[] original, final CSVFormat csvFormat) {
        final T[] fixed = original.clone();
        for (int i = 0; i < fixed.length; i++) {
            if (Objects.equals(csvFormat.getNullString(), fixed[i])) {
                fixed[i] = null;
            }
        }
        return fixed;
    }

    private String[][] generateLines(final int nLines, final int nCol) {
        final String[][] lines = new String[nLines][];
        for (int i = 0; i < nLines; i++) {
            final String[] line = new String[nCol];
            lines[i] = line;
            for (int j = 0; j < nCol; j++) {
                line[j] = randStr();
            }
        }
        return lines;
    }

    private String randStr() {
        final Random r = new Random();

        final int sz = r.nextInt(20);
        final char[] buf = new char[sz];
        for (int i = 0; i < sz; i++) {
            final char ch;
            final int what = r.nextInt(20);
            switch (what) {
                case 0:
                    ch = '\r';
                    break;
                case 1:
                    ch = '\n';
                    break;
                case 2:
                    ch = '\t';
                    break;
                case 3:
                    ch = '\f';
                    break;
                case 4:
                    ch = ' ';
                    break;
                case 5:
                    ch = ',';
                    break;
                case 6:
                    ch = DQUOTE_CHAR;
                    break;
                case 7:
                    ch = '\'';
                    break;
                case 8:
                    ch = BACKSLASH;
                    break;
                default:
                    ch = (char) r.nextInt(300);
                    break;
            }
            buf[i] = ch;
        }
        return new String(buf);
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    @Test
    @Disabled
    public void testJira135_part2() throws IOException {
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\n");
            printer.printRecord0(list);
        }
        final String expected = "\"\\n\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(list.toArray(), format), record0);
    }

    

    @Test
    @Disabled
    public void testJira135All() throws IOException {
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            list.add("\n");
            list.add("\\");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\"\",\"\\n\",\"\\\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(list.toArray(), format), record0);
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    @Test
    @Disabled
    public void testPostgreSqlCsvNullOutput() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat format =
                CSVFormat.POSTGRESQL_CSV
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.ALL_NON_NULL);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\",NULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(new Object[2], record0);

        s = new String[] {"\\N", null};
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\N", "A"};
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\n", "A"};
        format = CSVFormat.POSTGRESQL_CSV.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"", null};
        format = CSVFormat.POSTGRESQL_CSV.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"", null};
        format = CSVFormat.POSTGRESQL_CSV;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.POSTGRESQL_CSV;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.POSTGRESQL_CSV;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\\r"};
        format = CSVFormat.POSTGRESQL_CSV;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    @Disabled
    public void testPostgreSqlCsvTextOutput() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat format =
                CSVFormat.POSTGRESQL_TEXT
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.ALL_NON_NULL);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(new Object[2], record0);

        s = new String[] {"\\N", null};
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\N", "A"};
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\n", "A"};
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"", null};
        format = CSVFormat.POSTGRESQL_TEXT.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"", null};
        format = CSVFormat.POSTGRESQL_TEXT;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.POSTGRESQL_TEXT;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.POSTGRESQL_TEXT;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);

        s = new String[] {"\\\r"};
        format = CSVFormat.POSTGRESQL_TEXT;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    /**
     * Test to target the use of {@link IOUtils#copy(java.io.Reader, Appendable)} which directly
     * buffers the value from the Reader to the Appendable.
     *
     * <p>Requires the format to have no quote or escape character, value to be a {@link
     * java.io.Reader Reader} and the output <i>MUST NOT</i> be a {@link java.io.Writer Writer} but
     * some other Appendable.
     *
     * @throws IOException Not expected to happen
     */
    

    /**
     * Test to target the use of {@link IOUtils#copyLarge(java.io.Reader, Writer)} which directly
     * buffers the value from the Reader to the Writer.
     *
     * <p>Requires the format to have no quote or escape character, value to be a {@link
     * java.io.Reader Reader} and the output <i>MUST</i> be a {@link java.io.Writer Writer}.
     *
     * @throws IOException Not expected to happen
     */
    

    

    

    

    

    

    

    

    @Test
    @Disabled
    public void testRandomMongoDbCsv() throws Exception {
        doRandom(CSVFormat.MONGODB_CSV, ITERATIONS_FOR_RANDOM_TEST);
    }

    

    @Test
    @Disabled
    public void testRandomOracle() throws Exception {
        doRandom(CSVFormat.ORACLE, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    @Disabled
    public void testRandomPostgreSqlCsv() throws Exception {
        doRandom(CSVFormat.POSTGRESQL_CSV, ITERATIONS_FOR_RANDOM_TEST);
    }

    

    

    

    

    

    

    

    

    

    private String[] toFirstRecordValues(final String expected, final CSVFormat format)
            throws IOException {
        try (final CSVParser parser = CSVParser.parse4(expected, format)) {
            return parser.getRecords().get(0).values();
        }
    }

    private void tryFormat(
            final List<String> list,
            final Character quote,
            final Character escape,
            final String expected)
            throws IOException {
        final CSVFormat format =
                CSVFormat.DEFAULT.withQuote1(quote).withEscape1(escape).withRecordSeparator1(null);
        final Appendable out = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(out, format)) {
            printer.printRecord0(list);
        }
        assertEquals(expected, out.toString());
    }

    @Test
    public void testCRComment_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final Object value = "abc";
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))) {
            printer.print(value);
            printer.printComment("This is a comment\r\non multiple lines\rthis is next comment\r");
            assertEquals(
                    "abc"
                            + recordSeparator
                            + "# This is a comment"
                            + recordSeparator
                            + "# on multiple lines"
                            + recordSeparator
                            + "# this is next comment"
                            + recordSeparator
                            + "# "
                            + recordSeparator,
                    sw.toString());
        }
    }

    @Test
    public void testCSV135_test0_decomposed() throws IOException {
        final List<String> list = new LinkedList<>();
        list.add("\"\"");
        list.add("\\\\");
        list.add("\\\"\\");
        tryFormat(list, null, null, "\"\",\\\\,\\\"\\");
    }

    @Test
    public void testCSV135_test1_decomposed() throws IOException {
        final List<String> list = new LinkedList<>();
        list.add("\"\"");
        list.add("\\\\");
        list.add("\\\"\\");
        tryFormat(list, null, null, "\"\",\\\\,\\\"\\");
        tryFormat(list, '"', null, "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"");
        tryFormat(list, null, '\\', "\"\",\\\\\\\\,\\\\\"\\\\");
        tryFormat(list, '"', '\\', "\"\\\"\\\"\",\"\\\\\\\\\",\"\\\\\\\"\\\\\"");
        tryFormat(list, '"', '"', "\"\"\"\"\"\",\\\\,\"\\\"\"\\\"");
    }

    @Test
    public void testCSV259_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final Reader reader =
                        new FileReader(
                                "src/test/resources/org/apache/commons/csv/CSV-259/sample.txt");
                final CSVPrinter printer =
                        new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape0('!').withQuote1(null))) {
            printer.print(reader);
            assertEquals("x!,y!,z", sw.toString());
        }
    }

    @Test
    public void testDelimeterQuoted_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))) {
            printer.print("a,b,c");
            printer.print("xyz");
            assertEquals("'a,b,c',xyz", sw.toString());
        }
    }

    @Test
    public void testDelimeterQuoteNone_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.withEscape0('!');
    }

    @Test
    public void testDelimeterQuoteNone_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.withEscape0('!');
        final CSVFormat format = CSVFormat.DEFAULT.withEscape0('!').withQuoteMode(QuoteMode.NONE);
    }

    @Test
    public void testDelimeterQuoteNone_test2_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.withEscape0('!');
        final CSVFormat format = CSVFormat.DEFAULT.withEscape0('!').withQuoteMode(QuoteMode.NONE);
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            printer.print("a,b,c");
            printer.print("xyz");
            assertEquals("a!,b!,c,xyz", sw.toString());
        }
    }

    @Test
    public void testDelimeterStringQuoted_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(
                        sw,
                        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setQuote0('\'').build())) {
            printer.print("a[|]b[|]c");
            printer.print("xyz");
            assertEquals("'a[|]b[|]c'[|]xyz", sw.toString());
        }
    }

    @Test
    public void testDelimeterStringQuoteNone_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
    }

    @Test
    public void testDelimeterStringQuoteNone_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
    }

    @Test
    public void testDelimeterStringQuoteNone_test2_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
    }

    @Test
    public void testDelimeterStringQuoteNone_test3_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').setQuoteMode(QuoteMode.NONE);
    }

    @Test
    public void testDelimeterStringQuoteNone_test4_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').setQuoteMode(QuoteMode.NONE);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .builder()
                        .setDelimiter1("[|]")
                        .setEscape0('!')
                        .setQuoteMode(QuoteMode.NONE)
                        .build();
    }

    @Test
    public void testDelimeterStringQuoteNone_test5_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        CSVFormat.DEFAULT.builder();
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]");
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!');
        CSVFormat.DEFAULT.builder().setDelimiter1("[|]").setEscape0('!').setQuoteMode(QuoteMode.NONE);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .builder()
                        .setDelimiter1("[|]")
                        .setEscape0('!')
                        .setQuoteMode(QuoteMode.NONE)
                        .build();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            printer.print("a[|]b[|]c");
            printer.print("xyz");
            printer.print("a[xy]bc[]");
            assertEquals("a![!|!]b![!|!]c[|]xyz[|]a[xy]bc[]", sw.toString());
        }
    }

    @Test
    public void testDelimiterEscaped_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape0('!').withQuote1(null))) {
            printer.print("a,b,c");
            printer.print("xyz");
            assertEquals("a!,b!,c,xyz", sw.toString());
        }
    }

    @Test
    public void testDelimiterPlain_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            printer.print("a,b,c");
            printer.print("xyz");
            assertEquals("a,b,c,xyz", sw.toString());
        }
    }

    @Test
    public void testDelimiterStringEscaped_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(
                        sw,
                        CSVFormat.DEFAULT
                                .builder()
                                .setDelimiter1("|||")
                                .setEscape0('!')
                                .setQuote1(null)
                                .build())) {
            printer.print("a|||b|||c");
            printer.print("xyz");
            assertEquals("a!|!|!|b!|!|!|c|||xyz", sw.toString());
        }
    }

    @Test
    public void testDisabledComment_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printComment("This is a comment");
            assertEquals("", sw.toString());
        }
    }

    @Test
    public void testDontQuoteEuroFirstChar_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.RFC4180)) {
            printer.printRecord1(EURO_CH, "Deux");
            assertEquals(EURO_CH + ",Deux" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testEolEscaped_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null).withEscape0('!'))) {
            printer.print("a\rb\nc");
            printer.print("x\fy\bz");
            assertEquals("a!rb!nc,x\fy\bz", sw.toString());
        }
    }

    @Test
    public void testEolPlain_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            printer.print("a\rb\nc");
            printer.print("x\fy\bz");
            assertEquals("a\rb\nc,x\fy\bz", sw.toString());
        }
    }

    @Test
    public void testEolQuoted_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))) {
            printer.print("a\rb\nc");
            printer.print("x\by\fz");
            assertEquals("'a\rb\nc',x\by\fz", sw.toString());
        }
    }

    @Test
    public void testEscapeBackslash1_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\");
        }
    }

    @Test
    public void testEscapeBackslash1_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\");
        }
        assertEquals("\\", sw.toString());
    }

    @Test
    public void testEscapeBackslash2_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\r");
        }
    }

    @Test
    public void testEscapeBackslash2_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\r");
        }
        assertEquals("'\\\r'", sw.toString());
    }

    @Test
    public void testEscapeBackslash3_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("X\\\r");
        }
    }

    @Test
    public void testEscapeBackslash3_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("X\\\r");
        }
        assertEquals("'X\\\r'", sw.toString());
    }

    @Test
    public void testEscapeBackslash4_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\\");
        }
    }

    @Test
    public void testEscapeBackslash4_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\\");
        }
        assertEquals("\\\\", sw.toString());
    }

    @Test
    public void testEscapeBackslash5_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\\");
        }
    }

    @Test
    public void testEscapeBackslash5_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0(QUOTE_CH))) {
            printer.print("\\\\");
        }
        assertEquals("\\\\", sw.toString());
    }

    @Test
    public void testEscapeNull1_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\");
        }
    }

    @Test
    public void testEscapeNull1_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\");
        }
        assertEquals("\\", sw.toString());
    }

    @Test
    public void testEscapeNull2_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\r");
        }
    }

    @Test
    public void testEscapeNull2_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\r");
        }
        assertEquals("\"\\\r\"", sw.toString());
    }

    @Test
    public void testEscapeNull3_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("X\\\r");
        }
    }

    @Test
    public void testEscapeNull3_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("X\\\r");
        }
        assertEquals("\"X\\\r\"", sw.toString());
    }

    @Test
    public void testEscapeNull4_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\\");
        }
    }

    @Test
    public void testEscapeNull4_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\\");
        }
        assertEquals("\\\\", sw.toString());
    }

    @Test
    public void testEscapeNull5_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\\");
        }
    }

    @Test
    public void testEscapeNull5_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withEscape1(null))) {
            printer.print("\\\\");
        }
        assertEquals("\\\\", sw.toString());
    }

    @Test
    public void testExcelPrintAllArrayOfArrays_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecords1((Object[]) new String[][] {{"r1c1", "r1c2"}, {"r2c1", "r2c2"}});
            assertEquals(
                    "r1c1,r1c2" + recordSeparator + "r2c1,r2c2" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testExcelPrintAllArrayOfLists_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecords1(
                    (Object[])
                            new List[] {
                                Arrays.asList("r1c1", "r1c2"), Arrays.asList("r2c1", "r2c2")
                            });
            assertEquals(
                    "r1c1,r1c2" + recordSeparator + "r2c1,r2c2" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testExcelPrintAllIterableOfArrays_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecords0(
                    Arrays.asList(new String[][] {{"r1c1", "r1c2"}, {"r2c1", "r2c2"}}));
            assertEquals(
                    "r1c1,r1c2" + recordSeparator + "r2c1,r2c2" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testExcelPrintAllIterableOfLists_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecords0(
                    Arrays.asList(Arrays.asList("r1c1", "r1c2"), Arrays.asList("r2c1", "r2c2")));
            assertEquals(
                    "r1c1,r1c2" + recordSeparator + "r2c1,r2c2" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testExcelPrinter1_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecord1("a", "b");
            assertEquals("a,b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testExcelPrinter2_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.EXCEL)) {
            printer.printRecord1("a,b", "b");
            assertEquals("\"a,b\",b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testHeaderNotSet_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            printer.printRecord1("a", "b", "c");
            printer.printRecord1("x", "y", "z");
            assertEquals("a,b,c\r\nx,y,z\r\n", sw.toString());
        }
    }

    @Test
    public void testInvalidFormat_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withDelimiter(CR));
    }

    @Test
    public void testJira135_part1_test0_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
    }

    @Test
    public void testJira135_part1_test1_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
    }

    @Test
    public void testJira135_part1_test2_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
    }

    @Test
    public void testJira135_part1_test3_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            printer.printRecord0(list);
        }
    }

    @Test
    public void testJira135_part1_test4_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\"\"" + format.getRecordSeparator();
    }

    @Test
    public void testJira135_part1_test5_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\"\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
    }

    @Test
    public void testJira135_part1_test6_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\"\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testJira135_part1_test7_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\"");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\"\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(list.toArray(), format), record0);
    }

    @Test
    public void testJira135_part3_test0_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
    }

    @Test
    public void testJira135_part3_test1_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
    }

    @Test
    public void testJira135_part3_test2_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
    }

    @Test
    public void testJira135_part3_test3_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\\");
            printer.printRecord0(list);
        }
    }

    @Test
    public void testJira135_part3_test4_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\\");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\\\"" + format.getRecordSeparator();
    }

    @Test
    public void testJira135_part3_test5_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\\");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\\\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
    }

    @Test
    public void testJira135_part3_test6_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\\");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\\\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testJira135_part3_test7_decomposed() throws IOException {
        CSVFormat.DEFAULT.withRecordSeparator0('\n');
        CSVFormat.DEFAULT.withRecordSeparator0('\n').withQuote0(DQUOTE_CHAR);
        final CSVFormat format =
                CSVFormat.DEFAULT
                        .withRecordSeparator0('\n')
                        .withQuote0(DQUOTE_CHAR)
                        .withEscape0(BACKSLASH);
        final StringWriter sw = new StringWriter();
        final List<String> list = new LinkedList<>();
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            list.add("\\");
            printer.printRecord0(list);
        }
        final String expected = "\"\\\\\"" + format.getRecordSeparator();
        assertEquals(expected, sw.toString());
        final String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(list.toArray(), format), record0);
    }

    @Test
    public void testMongoDbCsvBasic_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_CSV)) {
            printer.printRecord1("a", "b");
            assertEquals("a,b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbCsvCommaInValue_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_CSV)) {
            printer.printRecord1("a,b", "c");
            assertEquals("\"a,b\",c" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbCsvDoubleQuoteInValue_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_CSV)) {
            printer.printRecord1("a \"c\" b", "d");
            assertEquals("\"a \"\"c\"\" b\",d" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbCsvTabInValue_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_CSV)) {
            printer.printRecord1("a\tb", "c");
            assertEquals("a\tb,c" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbTsvBasic_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_TSV)) {
            printer.printRecord1("a", "b");
            assertEquals("a\tb" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbTsvCommaInValue_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_TSV)) {
            printer.printRecord1("a,b", "c");
            assertEquals("a,b\tc" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMongoDbTsvTabInValue_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.MONGODB_TSV)) {
            printer.printRecord1("a\tb", "c");
            assertEquals("\"a\tb\"\tc" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testMultiLineComment_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))) {
            printer.printComment("This is a comment\non multiple lines");

            assertEquals(
                    "# This is a comment"
                            + recordSeparator
                            + "# on multiple lines"
                            + recordSeparator,
                    sw.toString());
        }
    }

    @Test
    public void testMySqlNullOutput_test0_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
    }

    @Test
    public void testMySqlNullOutput_test1_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
    }

    @Test
    public void testMySqlNullOutput_test2_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
    }

    @Test
    public void testMySqlNullOutput_test3_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test4_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test5_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test6_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
    }

    @Test
    public void testMySqlNullOutput_test7_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test8_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test9_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test10_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test11_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
    }

    @Test
    public void testMySqlNullOutput_test12_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test13_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test14_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test15_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test16_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
    }

    @Test
    public void testMySqlNullOutput_test17_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test18_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test19_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test20_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test21_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
    }

    @Test
    public void testMySqlNullOutput_test22_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test23_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test24_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test25_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test26_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test27_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test28_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test29_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test30_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test31_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test32_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test33_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test34_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test35_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test36_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test37_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullOutput_test38_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
    }

    @Test
    public void testMySqlNullOutput_test39_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\\\r\n";
        assertEquals(expected, writer.toString());
    }

    @Test
    public void testMySqlNullOutput_test40_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
    }

    @Test
    public void testMySqlNullOutput_test41_decomposed() throws IOException {
        Object[] s = new String[] {"NULL", null};
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR);
        CSVFormat.MYSQL.withQuote0(DQUOTE_CHAR).withNullString("NULL");
        CSVFormat format =
                CSVFormat.MYSQL
                        .withQuote0(DQUOTE_CHAR)
                        .withNullString("NULL")
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        StringWriter writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        String expected = "\"NULL\"\tNULL\n";
        assertEquals(expected, writer.toString());
        String[] record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(s, record0);
        s = new String[] {"\\N", null};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\n", "A"};
        format = CSVFormat.MYSQL.withNullString("\\N");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\n\tA\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL.withNullString("NULL");
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\tNULL\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"", null};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\t\\N\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\N", "", "\u000e,\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\N\t\t\u000e,\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"NULL", "\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "NULL\t\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
        s = new String[] {"\\\r"};
        format = CSVFormat.MYSQL;
        writer = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(writer, format)) {
            printer.printRecord1(s);
        }
        expected = "\\\\\\r\n";
        assertEquals(expected, writer.toString());
        record0 = toFirstRecordValues(expected, format);
        assertArrayEquals(expectNulls(s, format), record0);
    }

    @Test
    public void testMySqlNullStringDefault_test0_decomposed()  {
        assertEquals("\\N", CSVFormat.MYSQL.getNullString());
    }

    @Test
    public void testNewCsvPrinterAppendableNullFormat_test0_decomposed()  {
        assertThrows(NullPointerException.class, () -> new CSVPrinter(new StringWriter(), null));
    }

    @Test
    public void testNewCsvPrinterNullAppendableFormat_test0_decomposed()  {
        assertThrows(NullPointerException.class, () -> new CSVPrinter(null, CSVFormat.DEFAULT));
    }

    @Test
    public void testNotFlushable_test0_decomposed() throws IOException {
        final Appendable out = new StringBuilder();
        try (final CSVPrinter printer = new CSVPrinter(out, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b", "c");
            assertEquals("a,b,c" + recordSeparator, out.toString());
            printer.flush();
        }
    }

    @Test
    public void testParseCustomNullValues_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final CSVFormat format = CSVFormat.DEFAULT.withNullString("NULL");
    }

    @Test
    public void testParseCustomNullValues_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final CSVFormat format = CSVFormat.DEFAULT.withNullString("NULL");
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            printer.printRecord1("a", null, "b");
        }
    }

    @Test
    public void testParseCustomNullValues_test2_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final CSVFormat format = CSVFormat.DEFAULT.withNullString("NULL");
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            printer.printRecord1("a", null, "b");
        }
        final String csvString = sw.toString();
    }

    @Test
    public void testParseCustomNullValues_test3_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final CSVFormat format = CSVFormat.DEFAULT.withNullString("NULL");
        try (final CSVPrinter printer = new CSVPrinter(sw, format)) {
            printer.printRecord1("a", null, "b");
        }
        final String csvString = sw.toString();
        assertEquals("a,NULL,b" + recordSeparator, csvString);
        try (final CSVParser iterable = format.parse(new StringReader(csvString))) {
            final Iterator<CSVRecord> iterator = iterable.iterator();
            final CSVRecord record = iterator.next();
            assertEquals("a", record.get1(0));
            assertNull(record.get1(1));
            assertEquals("b", record.get1(2));
            assertFalse(iterator.hasNext());
        }
    }

    @Test
    public void testPlainEscaped_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null).withEscape0('!'))) {
            printer.print("abc");
            printer.print("xyz");
            assertEquals("abc,xyz", sw.toString());
        }
    }

    @Test
    public void testPlainPlain_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            printer.print("abc");
            printer.print("xyz");
            assertEquals("abc,xyz", sw.toString());
        }
    }

    @Test
    public void testPlainQuoted_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))) {
            printer.print("abc");
            assertEquals("abc", sw.toString());
        }
    }

    @Test
    public void testPostgreSqlNullStringDefaultCsv_test0_decomposed()  {
        assertEquals("", CSVFormat.POSTGRESQL_CSV.getNullString());
    }

    @Test
    public void testPostgreSqlNullStringDefaultText_test0_decomposed()  {
        assertEquals("\\N", CSVFormat.POSTGRESQL_TEXT.getNullString());
    }

    @Test
    public void testPrint_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = CSVFormat.DEFAULT.print0(sw)) {
            printer.printRecord1("a", "b\\c");
            assertEquals("a,b\\c" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrintCSVParser_test0_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            printer.printRecords0(parser);
        }
    }

    @Test
    public void testPrintCSVParser_test1_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            printer.printRecords0(parser);
        }
        try (final CSVParser parser = CSVParser.parse4(sw.toString(), format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());
            Utils.compare("Fail", res, records);
        }
    }

    @Test
    public void testPrintCSVRecord_test0_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            for (final CSVRecord record : parser) {
                printer.printRecord0(record);
            }
        }
    }

    @Test
    public void testPrintCSVRecord_test1_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            for (final CSVRecord record : parser) {
                printer.printRecord0(record);
            }
        }
        try (final CSVParser parser = CSVParser.parse4(sw.toString(), format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());
            Utils.compare("Fail", res, records);
        }
    }

    @Test
    public void testPrintCSVRecords_test0_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            printer.printRecords0(parser.getRecords());
        }
    }

    @Test
    public void testPrintCSVRecords_test1_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            printer.printRecords0(parser.getRecords());
        }
        try (final CSVParser parser = CSVParser.parse4(sw.toString(), format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());
            Utils.compare("Fail", res, records);
        }
    }

    @Test
    public void testPrintCustomNullValues_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withNullString("NULL"))) {
            printer.printRecord1("a", null, "b");
            assertEquals("a,NULL,b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter1_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b");
            assertEquals("a,b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter2_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a,b", "b");
            assertEquals("\"a,b\",b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter3_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a, b", "b ");
            assertEquals("\"a, b\",\"b \"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter4_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b\"c");
            assertEquals("a,\"b\"\"c\"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter5_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b\nc");
            assertEquals("a,\"b\nc\"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter6_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b\r\nc");
            assertEquals("a,\"b\r\nc\"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrinter7_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", "b\\c");
            assertEquals("a,b\\c" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrintNullValues_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT)) {
            printer.printRecord1("a", null, "b");
            assertEquals("a,,b" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testPrintOnePositiveInteger_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.MINIMAL))) {
            printer.print(Integer.MAX_VALUE);
            assertEquals(String.valueOf(Integer.MAX_VALUE), sw.toString());
        }
    }

    @Test
    public void testPrintReaderWithoutQuoteToAppendable_test0_decomposed() throws IOException {
        final StringBuilder sb = new StringBuilder();
        final String content = "testValue";
        try (final CSVPrinter printer = new CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(null))) {
            final StringReader value = new StringReader(content);
            printer.print(value);
        }
    }

    @Test
    public void testPrintReaderWithoutQuoteToAppendable_test1_decomposed() throws IOException {
        final StringBuilder sb = new StringBuilder();
        final String content = "testValue";
        try (final CSVPrinter printer = new CSVPrinter(sb, CSVFormat.DEFAULT.withQuote1(null))) {
            final StringReader value = new StringReader(content);
            printer.print(value);
        }
        assertEquals(content, sb.toString());
    }

    @Test
    public void testPrintReaderWithoutQuoteToWriter_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final String content = "testValue";
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            final StringReader value = new StringReader(content);
            printer.print(value);
        }
    }

    @Test
    public void testPrintReaderWithoutQuoteToWriter_test1_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        final String content = "testValue";
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote1(null))) {
            final StringReader value = new StringReader(content);
            printer.print(value);
        }
        assertEquals(content, sw.toString());
    }

    @Test
    public void testPrintRecordStream_test0_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            for (final CSVRecord record : parser) {
                printer.printRecord2(record.stream());
            }
        }
    }

    @Test
    public void testPrintRecordStream_test1_decomposed() throws IOException {
        final String code =
                "a1,b1\n" // 1)
                        + "a2,b2\n" // 2)
                        + "a3,b3\n" // 3)
                        + "a4,b4\n" // 4)
                ;
        final String[][] res = {{"a1", "b1"}, {"a2", "b2"}, {"a3", "b3"}, {"a4", "b4"}};
        final CSVFormat format = CSVFormat.DEFAULT;
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = format.print0(sw);
                final CSVParser parser = CSVParser.parse4(code, format)) {
            for (final CSVRecord record : parser) {
                printer.printRecord2(record.stream());
            }
        }
        try (final CSVParser parser = CSVParser.parse4(sw.toString(), format)) {
            final List<CSVRecord> records = parser.getRecords();
            assertFalse(records.isEmpty());
            Utils.compare("Fail", res, records);
        }
    }

    @Test
    public void testPrintToPathWithDefaultCharset_test0_decomposed() throws IOException {
        final Path file = createTempPath();
    }

    @Test
    public void testPrintToPathWithDefaultCharset_test1_decomposed() throws IOException {
        final Path file = createTempPath();
        try (final CSVPrinter printer = CSVFormat.DEFAULT.print4(file, Charset.defaultCharset())) {
            printer.printRecord1("a", "b\\c");
        }
    }

    @Test
    public void testPrintToPathWithDefaultCharset_test2_decomposed() throws IOException {
        final Path file = createTempPath();
        try (final CSVPrinter printer = CSVFormat.DEFAULT.print4(file, Charset.defaultCharset())) {
            printer.printRecord1("a", "b\\c");
        }
        assertEquals(
                "a,b\\c" + recordSeparator,
                new String(Files.readAllBytes(file), Charset.defaultCharset()));
    }

    @Test
    public void testQuoteAll_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL))) {
            printer.printRecord1("a", "b\nc", "d");
            assertEquals("\"a\",\"b\nc\",\"d\"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testQuoteCommaFirstChar_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.RFC4180)) {
            printer.printRecord1(",");
            assertEquals("\",\"" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testQuoteNonNumeric_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withQuoteMode(QuoteMode.NON_NUMERIC))) {
            printer.printRecord1("a", "b\nc", Integer.valueOf(1));
            assertEquals("\"a\",\"b\nc\",1" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testRandomDefault_test0_decomposed() throws Exception {
        doRandom(CSVFormat.DEFAULT, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testRandomExcel_test0_decomposed() throws Exception {
        doRandom(CSVFormat.EXCEL, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testRandomMySql_test0_decomposed() throws Exception {
        doRandom(CSVFormat.MYSQL, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testRandomPostgreSqlText_test0_decomposed() throws Exception {
        doRandom(CSVFormat.POSTGRESQL_TEXT, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testRandomRfc4180_test0_decomposed() throws Exception {
        doRandom(CSVFormat.RFC4180, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testRandomTdf_test0_decomposed() throws Exception {
        doRandom(CSVFormat.TDF, ITERATIONS_FOR_RANDOM_TEST);
    }

    @Test
    public void testSingleLineComment_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withCommentMarker0('#'))) {
            printer.printComment("This is a comment");
            assertEquals("# This is a comment" + recordSeparator, sw.toString());
        }
    }

    @Test
    public void testSingleQuoteQuoted_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withQuote0('\''))) {
            printer.print("a'b'c");
            printer.print("xyz");
            assertEquals("'a''b''c',xyz", sw.toString());
        }
    }

    @Test
    public void testTrailingDelimiterOnTwoColumns_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer =
                new CSVPrinter(sw, CSVFormat.DEFAULT.withTrailingDelimiter0())) {
            printer.printRecord1("A", "B");
            assertEquals("A,B,\r\n", sw.toString());
        }
    }

    @Test
    public void testTrimOffOneColumn_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withTrim1(false))) {
            printer.print(" A ");
            assertEquals("\" A \"", sw.toString());
        }
    }

    @Test
    public void testTrimOnOneColumn_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0())) {
            printer.print(" A ");
            assertEquals("A", sw.toString());
        }
    }

    @Test
    public void testTrimOnTwoColumns_test0_decomposed() throws IOException {
        final StringWriter sw = new StringWriter();
        try (final CSVPrinter printer = new CSVPrinter(sw, CSVFormat.DEFAULT.withTrim0())) {
            printer.print(" A ");
            printer.print(" B ");
            assertEquals("A,B", sw.toString());
        }
    }
}
