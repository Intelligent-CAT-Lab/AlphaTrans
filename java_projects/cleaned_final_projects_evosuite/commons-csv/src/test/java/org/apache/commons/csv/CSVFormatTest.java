
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */


package org.apache.commons.csv;

import static org.apache.commons.csv.CSVFormat.RFC4180;
import static org.apache.commons.csv.Constants.CR;
import static org.apache.commons.csv.Constants.CRLF;
import static org.apache.commons.csv.Constants.LF;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import org.apache.commons.csv.CSVFormat.Builder;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Reader;
import java.io.StringReader;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Objects;

/** Tests {@link CSVFormat}. */
public class CSVFormatTest {

    public enum EmptyEnum {}

    public enum Header {
        Name,
        Email,
        Phone
    }

    private static void assertNotEquals0(final Object right, final Object left) {
        Assertions.assertNotEquals(right, left);
        Assertions.assertNotEquals(left, right);
    }

    private static CSVFormat copy(final CSVFormat format) {
        return format.builder().setDelimiter0(format.getDelimiter()).build();
    }

    private void assertNotEquals1(
            final String name, final String type, final Object left, final Object right) {
        if (left.equals(right) || right.equals(left)) {
            fail("Objects must not compare equal for " + name + "(" + type + ")");
        }
        if (left.hashCode() == right.hashCode()) {
            fail("Hash code should not be equal for " + name + "(" + type + ")");
        }
    }

    @Test
    public void testDelimiterEmptyStringThrowsException1() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.builder().setDelimiter1("").build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testDelimiterSameAsCommentStartThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withDelimiter('!').withCommentMarker0('!'));
    }

    @Test
    public void testDelimiterSameAsCommentStartThrowsException1() {
        assertThrows(
                IllegalArgumentException.class,
                () ->
                        CSVFormat.DEFAULT
                                .builder()
                                .setDelimiter0('!')
                                .setCommentMarker0('!')
                                .build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testDelimiterSameAsEscapeThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withDelimiter('!').withEscape0('!'));
    }

    @Test
    public void testDelimiterSameAsEscapeThrowsException1() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.builder().setDelimiter0('!').setEscape0('!').build());
    }

    @Test
    public void testDelimiterSameAsRecordSeparatorThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.newFormat(CR));
    }

    @Test
    public void testEquals() {
        final CSVFormat right = CSVFormat.DEFAULT;
        final CSVFormat left = copy(right);

        Assertions.assertNotEquals(null, right);
        Assertions.assertNotEquals("A String Instance", right);

        assertEquals(right, right);
        assertEquals(right, left);
        assertEquals(left, right);

        assertEquals(right.hashCode(), right.hashCode());
        assertEquals(right.hashCode(), left.hashCode());
    }

    @Test
    public void testEqualsCommentStart() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setQuote0('"')
                        .setCommentMarker0('#')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setCommentMarker0('!').build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsCommentStart_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withQuote0('"')
                        .withCommentMarker0('#')
                        .withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withCommentMarker0('!');

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsDelimiter() {
        final CSVFormat right = CSVFormat.newFormat('!');
        final CSVFormat left = CSVFormat.newFormat('?');

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsEscape() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setQuote0('"')
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setEscape0('!').build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsEscape_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withQuote0('"')
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withEscape0('!');

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsHash() throws Exception {
        final Method[] methods = CSVFormat.class.getDeclaredMethods();
        for (final Method method : methods) {
            if (Modifier.isPublic(method.getModifiers())) {
                final String name = method.getName();
                if (name.startsWith("with")) {
                    for (final Class<?> cls : method.getParameterTypes()) {
                        final String type = cls.getCanonicalName();
                        if ("boolean".equals(type)) {
                            final Object defTrue = method.invoke(CSVFormat.DEFAULT, Boolean.TRUE);
                            final Object defFalse = method.invoke(CSVFormat.DEFAULT, Boolean.FALSE);
                            assertNotEquals1(name, type, defTrue, defFalse);
                        } else if ("char".equals(type)) {
                            final Object a = method.invoke(CSVFormat.DEFAULT, 'a');
                            final Object b = method.invoke(CSVFormat.DEFAULT, 'b');
                            assertNotEquals1(name, type, a, b);
                        } else if ("java.lang.Character".equals(type)) {
                            final Object a = method.invoke(CSVFormat.DEFAULT, new Object[] {null});
                            final Object b =
                                    method.invoke(CSVFormat.DEFAULT, Character.valueOf('d'));
                            assertNotEquals1(name, type, a, b);
                        } else if ("java.lang.String".equals(type)) {
                            final Object a = method.invoke(CSVFormat.DEFAULT, new Object[] {null});
                            final Object b = method.invoke(CSVFormat.DEFAULT, "e");
                            assertNotEquals1(name, type, a, b);
                        } else if ("java.lang.String[]".equals(type)) {
                            final Object a =
                                    method.invoke(
                                            CSVFormat.DEFAULT,
                                            new Object[] {new String[] {null, null}});
                            final Object b =
                                    method.invoke(
                                            CSVFormat.DEFAULT,
                                            new Object[] {new String[] {"f", "g"}});
                            assertNotEquals1(name, type, a, b);
                        } else if ("org.apache.commons.csv.QuoteMode".equals(type)) {
                            final Object a = method.invoke(CSVFormat.DEFAULT, QuoteMode.MINIMAL);
                            final Object b = method.invoke(CSVFormat.DEFAULT, QuoteMode.ALL);
                            assertNotEquals1(name, type, a, b);
                        } else if ("org.apache.commons.csv.DuplicateHeaderMode".equals(type)) {
                            final Object a =
                                    method.invoke(CSVFormat.DEFAULT, DuplicateHeaderMode.ALLOW_ALL);
                            final Object b =
                                    method.invoke(CSVFormat.DEFAULT, DuplicateHeaderMode.DISALLOW);
                            assertNotEquals1(name, type, a, b);
                        } else if ("java.lang.Object[]".equals(type)) {
                            final Object a =
                                    method.invoke(
                                            CSVFormat.DEFAULT,
                                            new Object[] {new Object[] {null, null}});
                            final Object b =
                                    method.invoke(
                                            CSVFormat.DEFAULT,
                                            new Object[] {
                                                new Object[] {new Object(), new Object()}
                                            });
                            assertNotEquals1(name, type, a, b);
                        } else if ("withHeader".equals(name)) { // covered above by String[]
                        } else {
                            fail("Unhandled method: " + name + "(" + type + ")");
                        }
                    }
                }
            }
        }
    }

    @Test
    public void testEqualsIgnoreEmptyLines() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setIgnoreEmptyLines(true)
                        .setIgnoreSurroundingSpaces(true)
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setIgnoreEmptyLines(false).build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsIgnoreEmptyLines_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withIgnoreEmptyLines0()
                        .withIgnoreSurroundingSpaces0()
                        .withQuote0('"')
                        .withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withIgnoreEmptyLines1(false);

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsIgnoreSurroundingSpaces() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setIgnoreSurroundingSpaces(true)
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setIgnoreSurroundingSpaces(false).build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsIgnoreSurroundingSpaces_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withIgnoreSurroundingSpaces0()
                        .withQuote0('"')
                        .withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withIgnoreSurroundingSpaces1(false);

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsLeftNoQuoteRightQuote() {
        final CSVFormat left = CSVFormat.newFormat(',').builder().setQuote1(null).build();
        final CSVFormat right = left.builder().setQuote0('#').build();

        assertNotEquals0(left, right);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsLeftNoQuoteRightQuote_Deprecated() {
        final CSVFormat left = CSVFormat.newFormat(',').withQuote1(null);
        final CSVFormat right = left.withQuote0('#');

        assertNotEquals0(left, right);
    }

    @Test
    public void testEqualsNoQuotes() {
        final CSVFormat left = CSVFormat.newFormat(',').builder().setQuote1(null).build();
        final CSVFormat right = left.builder().setQuote1(null).build();

        assertEquals(left, right);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsNoQuotes_Deprecated() {
        final CSVFormat left = CSVFormat.newFormat(',').withQuote1(null);
        final CSVFormat right = left.withQuote1(null);

        assertEquals(left, right);
    }

    @Test
    public void testEqualsNullString() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setRecordSeparator0(CR)
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setIgnoreEmptyLines(true)
                        .setIgnoreSurroundingSpaces(true)
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .setNullString("null")
                        .build();
        final CSVFormat left = right.builder().setNullString("---").build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsNullString_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withRecordSeparator0(CR)
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withIgnoreEmptyLines0()
                        .withIgnoreSurroundingSpaces0()
                        .withQuote0('"')
                        .withQuoteMode(QuoteMode.ALL)
                        .withNullString("null");
        final CSVFormat left = right.withNullString("---");

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsOne() {

        final CSVFormat csvFormatOne = CSVFormat.INFORMIX_UNLOAD;
        final CSVFormat csvFormatTwo = CSVFormat.MYSQL;

        assertEquals('\\', (char) csvFormatOne.getEscapeCharacter());
        assertNull(csvFormatOne.getQuoteMode());

        assertTrue(csvFormatOne.getIgnoreEmptyLines());
        assertFalse(csvFormatOne.getSkipHeaderRecord());

        assertFalse(csvFormatOne.getIgnoreHeaderCase());
        assertNull(csvFormatOne.getCommentMarker());

        assertFalse(csvFormatOne.isCommentMarkerSet());
        assertTrue(csvFormatOne.isQuoteCharacterSet());

        assertEquals('|', csvFormatOne.getDelimiter());
        assertFalse(csvFormatOne.getAllowMissingColumnNames());

        assertTrue(csvFormatOne.isEscapeCharacterSet());
        assertEquals("\n", csvFormatOne.getRecordSeparator());

        assertEquals('\"', (char) csvFormatOne.getQuoteCharacter());
        assertFalse(csvFormatOne.getTrailingDelimiter());

        assertFalse(csvFormatOne.getTrim());
        assertFalse(csvFormatOne.isNullStringSet());

        assertNull(csvFormatOne.getNullString());
        assertFalse(csvFormatOne.getIgnoreSurroundingSpaces());

        assertTrue(csvFormatTwo.isEscapeCharacterSet());
        assertNull(csvFormatTwo.getQuoteCharacter());

        assertFalse(csvFormatTwo.getAllowMissingColumnNames());
        assertEquals(QuoteMode.ALL_NON_NULL, csvFormatTwo.getQuoteMode());

        assertEquals('\t', csvFormatTwo.getDelimiter());
        assertEquals("\n", csvFormatTwo.getRecordSeparator());

        assertFalse(csvFormatTwo.isQuoteCharacterSet());
        assertTrue(csvFormatTwo.isNullStringSet());

        assertEquals('\\', (char) csvFormatTwo.getEscapeCharacter());
        assertFalse(csvFormatTwo.getIgnoreHeaderCase());

        assertFalse(csvFormatTwo.getTrim());
        assertFalse(csvFormatTwo.getIgnoreEmptyLines());

        assertEquals("\\N", csvFormatTwo.getNullString());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertFalse(csvFormatTwo.getTrailingDelimiter());
        assertFalse(csvFormatTwo.getSkipHeaderRecord());

        assertNull(csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.isCommentMarkerSet());

        assertNotSame(csvFormatTwo, csvFormatOne);
        Assertions.assertNotEquals(csvFormatTwo, csvFormatOne);

        assertEquals('\\', (char) csvFormatOne.getEscapeCharacter());
        assertNull(csvFormatOne.getQuoteMode());

        assertTrue(csvFormatOne.getIgnoreEmptyLines());
        assertFalse(csvFormatOne.getSkipHeaderRecord());

        assertFalse(csvFormatOne.getIgnoreHeaderCase());
        assertNull(csvFormatOne.getCommentMarker());

        assertFalse(csvFormatOne.isCommentMarkerSet());
        assertTrue(csvFormatOne.isQuoteCharacterSet());

        assertEquals('|', csvFormatOne.getDelimiter());
        assertFalse(csvFormatOne.getAllowMissingColumnNames());

        assertTrue(csvFormatOne.isEscapeCharacterSet());
        assertEquals("\n", csvFormatOne.getRecordSeparator());

        assertEquals('\"', (char) csvFormatOne.getQuoteCharacter());
        assertFalse(csvFormatOne.getTrailingDelimiter());

        assertFalse(csvFormatOne.getTrim());
        assertFalse(csvFormatOne.isNullStringSet());

        assertNull(csvFormatOne.getNullString());
        assertFalse(csvFormatOne.getIgnoreSurroundingSpaces());

        assertTrue(csvFormatTwo.isEscapeCharacterSet());
        assertNull(csvFormatTwo.getQuoteCharacter());

        assertFalse(csvFormatTwo.getAllowMissingColumnNames());
        assertEquals(QuoteMode.ALL_NON_NULL, csvFormatTwo.getQuoteMode());

        assertEquals('\t', csvFormatTwo.getDelimiter());
        assertEquals("\n", csvFormatTwo.getRecordSeparator());

        assertFalse(csvFormatTwo.isQuoteCharacterSet());
        assertTrue(csvFormatTwo.isNullStringSet());

        assertEquals('\\', (char) csvFormatTwo.getEscapeCharacter());
        assertFalse(csvFormatTwo.getIgnoreHeaderCase());

        assertFalse(csvFormatTwo.getTrim());
        assertFalse(csvFormatTwo.getIgnoreEmptyLines());

        assertEquals("\\N", csvFormatTwo.getNullString());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertFalse(csvFormatTwo.getTrailingDelimiter());
        assertFalse(csvFormatTwo.getSkipHeaderRecord());

        assertNull(csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.isCommentMarkerSet());

        assertNotSame(csvFormatOne, csvFormatTwo);
        assertNotSame(csvFormatTwo, csvFormatOne);

        Assertions.assertNotEquals(csvFormatOne, csvFormatTwo);
        Assertions.assertNotEquals(csvFormatTwo, csvFormatOne);

        Assertions.assertNotEquals(csvFormatTwo, csvFormatOne);
    }

    @Test
    public void testEqualsQuoteChar() {
        final CSVFormat right = CSVFormat.newFormat('\'').builder().setQuote0('"').build();
        final CSVFormat left = right.builder().setQuote0('!').build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsQuoteChar_Deprecated() {
        final CSVFormat right = CSVFormat.newFormat('\'').withQuote0('"');
        final CSVFormat left = right.withQuote0('!');

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsQuotePolicy() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setQuoteMode(QuoteMode.MINIMAL).build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsQuotePolicy_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'').withQuote0('"').withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withQuoteMode(QuoteMode.MINIMAL);

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsRecordSeparator() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setRecordSeparator0(CR)
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setIgnoreEmptyLines(true)
                        .setIgnoreSurroundingSpaces(true)
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .build();
        final CSVFormat left = right.builder().setRecordSeparator0(LF).build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsRecordSeparator_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withRecordSeparator0(CR)
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withIgnoreEmptyLines0()
                        .withIgnoreSurroundingSpaces0()
                        .withQuote0('"')
                        .withQuoteMode(QuoteMode.ALL);
        final CSVFormat left = right.withRecordSeparator0(LF);

        assertNotEquals0(right, left);
    }

    public void testEqualsSkipHeaderRecord() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .builder()
                        .setRecordSeparator0(CR)
                        .setCommentMarker0('#')
                        .setEscape0('+')
                        .setIgnoreEmptyLines(true)
                        .setIgnoreSurroundingSpaces(true)
                        .setQuote0('"')
                        .setQuoteMode(QuoteMode.ALL)
                        .setNullString("null")
                        .setSkipHeaderRecord(true)
                        .build();
        final CSVFormat left = right.builder().setSkipHeaderRecord(false).build();

        assertNotEquals0(right, left);
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEqualsSkipHeaderRecord_Deprecated() {
        final CSVFormat right =
                CSVFormat.newFormat('\'')
                        .withRecordSeparator0(CR)
                        .withCommentMarker0('#')
                        .withEscape0('+')
                        .withIgnoreEmptyLines0()
                        .withIgnoreSurroundingSpaces0()
                        .withQuote0('"')
                        .withQuoteMode(QuoteMode.ALL)
                        .withNullString("null")
                        .withSkipHeaderRecord0();
        final CSVFormat left = right.withSkipHeaderRecord1(false);

        assertNotEquals0(right, left);
    }

    @Test
    public void testEqualsWithNull() {

        final CSVFormat csvFormat = CSVFormat.POSTGRESQL_TEXT;

        assertEquals('\\', (char) csvFormat.getEscapeCharacter());
        assertFalse(csvFormat.getIgnoreSurroundingSpaces());

        assertFalse(csvFormat.getTrailingDelimiter());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isQuoteCharacterSet());
        assertEquals("\\N", csvFormat.getNullString());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertTrue(csvFormat.isEscapeCharacterSet());

        assertFalse(csvFormat.isCommentMarkerSet());
        assertNull(csvFormat.getCommentMarker());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertEquals(QuoteMode.ALL_NON_NULL, csvFormat.getQuoteMode());

        assertEquals('\t', csvFormat.getDelimiter());
        assertFalse(csvFormat.getSkipHeaderRecord());

        assertEquals("\n", csvFormat.getRecordSeparator());
        assertFalse(csvFormat.getIgnoreEmptyLines());

        assertNull(csvFormat.getQuoteCharacter());
        assertTrue(csvFormat.isNullStringSet());

        assertEquals('\\', (char) csvFormat.getEscapeCharacter());
        assertFalse(csvFormat.getIgnoreSurroundingSpaces());

        assertFalse(csvFormat.getTrailingDelimiter());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isQuoteCharacterSet());
        assertEquals("\\N", csvFormat.getNullString());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertTrue(csvFormat.isEscapeCharacterSet());

        assertFalse(csvFormat.isCommentMarkerSet());
        assertNull(csvFormat.getCommentMarker());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertEquals(QuoteMode.ALL_NON_NULL, csvFormat.getQuoteMode());

        assertEquals('\t', csvFormat.getDelimiter());
        assertFalse(csvFormat.getSkipHeaderRecord());

        assertEquals("\n", csvFormat.getRecordSeparator());
        assertFalse(csvFormat.getIgnoreEmptyLines());

        assertNull(csvFormat.getQuoteCharacter());
        assertTrue(csvFormat.isNullStringSet());

        Assertions.assertNotEquals(null, csvFormat);
    }

    @Test
    public void testEscapeSameAsCommentStartThrowsException() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.builder().setEscape0('!').setCommentMarker0('!').build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEscapeSameAsCommentStartThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withEscape0('!').withCommentMarker0('!'));
    }

    @Test
    public void testEscapeSameAsCommentStartThrowsExceptionForWrapperType() {
        assertThrows(
                IllegalArgumentException.class,
                () ->
                        CSVFormat.DEFAULT
                                .builder()
                                .setEscape1(Character.valueOf('!'))
                                .setCommentMarker1(Character.valueOf('!'))
                                .build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testEscapeSameAsCommentStartThrowsExceptionForWrapperType_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () ->
                        CSVFormat.DEFAULT
                                .withEscape1(Character.valueOf('!'))
                                .withCommentMarker1(Character.valueOf('!')));
    }

    @Test
    public void testFormat() {
        final CSVFormat format = CSVFormat.DEFAULT;

        assertEquals("", format.format());
        assertEquals("a,b,c", format.format("a", "b", "c"));
        assertEquals("\"x,y\",z", format.format("x,y", "z"));
    }

    @Test // I assume this to be a defect.
    public void testFormatThrowsNullPointerException() {

        final CSVFormat csvFormat = CSVFormat.MYSQL;

        final NullPointerException e =
                assertThrows(NullPointerException.class, () -> csvFormat.format((Object[]) null));
        assertEquals(Objects.class.getName(), e.getStackTrace()[0].getClassName());
    }

    @Test
    public void testGetAllowDuplicateHeaderNames() {
        final Builder builder = CSVFormat.DEFAULT.builder();
        assertTrue(builder.build().getAllowDuplicateHeaderNames());
        assertTrue(
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
                        .build()
                        .getAllowDuplicateHeaderNames());
        assertFalse(
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
                        .build()
                        .getAllowDuplicateHeaderNames());
        assertFalse(
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)
                        .build()
                        .getAllowDuplicateHeaderNames());
    }

    @Test
    public void testGetDuplicateHeaderMode() {
        final Builder builder = CSVFormat.DEFAULT.builder();

        assertEquals(DuplicateHeaderMode.ALLOW_ALL, builder.build().getDuplicateHeaderMode());
        assertEquals(
                DuplicateHeaderMode.ALLOW_ALL,
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_ALL)
                        .build()
                        .getDuplicateHeaderMode());
        assertEquals(
                DuplicateHeaderMode.ALLOW_EMPTY,
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
                        .build()
                        .getDuplicateHeaderMode());
        assertEquals(
                DuplicateHeaderMode.DISALLOW,
                builder.setDuplicateHeaderMode(DuplicateHeaderMode.DISALLOW)
                        .build()
                        .getDuplicateHeaderMode());
    }

    @Test
    public void testHashCodeAndWithIgnoreHeaderCase() {

        final CSVFormat csvFormat = CSVFormat.INFORMIX_UNLOAD_CSV;
        final CSVFormat csvFormatTwo = csvFormat.withIgnoreHeaderCase0();
        csvFormatTwo.hashCode();

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertTrue(csvFormatTwo.getIgnoreHeaderCase()); // now different
        assertFalse(csvFormatTwo.getTrailingDelimiter());

        Assertions.assertNotEquals(csvFormatTwo, csvFormat); // CSV-244 - should not be equal
        assertFalse(csvFormatTwo.getAllowMissingColumnNames());

        assertFalse(csvFormatTwo.getTrim());
    }

    @Test
    public void testNewFormat() {

        final CSVFormat csvFormat = CSVFormat.newFormat('X');

        assertFalse(csvFormat.getSkipHeaderRecord());
        assertFalse(csvFormat.isEscapeCharacterSet());

        assertNull(csvFormat.getRecordSeparator());
        assertNull(csvFormat.getQuoteMode());

        assertNull(csvFormat.getCommentMarker());
        assertFalse(csvFormat.getIgnoreHeaderCase());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isNullStringSet());
        assertNull(csvFormat.getEscapeCharacter());

        assertFalse(csvFormat.getIgnoreSurroundingSpaces());
        assertFalse(csvFormat.getTrailingDelimiter());

        assertEquals('X', csvFormat.getDelimiter());
        assertNull(csvFormat.getNullString());

        assertFalse(csvFormat.isQuoteCharacterSet());
        assertFalse(csvFormat.isCommentMarkerSet());

        assertNull(csvFormat.getQuoteCharacter());
        assertFalse(csvFormat.getIgnoreEmptyLines());

        assertFalse(csvFormat.getSkipHeaderRecord());
        assertFalse(csvFormat.isEscapeCharacterSet());

        assertNull(csvFormat.getRecordSeparator());
        assertNull(csvFormat.getQuoteMode());

        assertNull(csvFormat.getCommentMarker());
        assertFalse(csvFormat.getIgnoreHeaderCase());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isNullStringSet());
        assertNull(csvFormat.getEscapeCharacter());

        assertFalse(csvFormat.getIgnoreSurroundingSpaces());
        assertFalse(csvFormat.getTrailingDelimiter());

        assertEquals('X', csvFormat.getDelimiter());
        assertNull(csvFormat.getNullString());

        assertFalse(csvFormat.isQuoteCharacterSet());
        assertFalse(csvFormat.isCommentMarkerSet());

        assertNull(csvFormat.getQuoteCharacter());
        assertFalse(csvFormat.getIgnoreEmptyLines());
    }

    @Test
    public void testPrintRecord() throws IOException {
        final Appendable out = new StringBuilder();
        final CSVFormat format = CSVFormat.RFC4180;
        format.printRecord(out, "a", "b", "c");
        assertEquals("a,b,c" + format.getRecordSeparator(), out.toString());
    }

    @Test
    public void testPrintRecordEmpty() throws IOException {
        final Appendable out = new StringBuilder();
        final CSVFormat format = CSVFormat.RFC4180;
        format.printRecord(out);
        assertEquals(format.getRecordSeparator(), out.toString());
    }

    @Test
    public void testPrintWithEscapesEndWithCRLF() throws IOException {
        final Reader in = new StringReader("x,y,x\r\na,?b,c\r\n");
        final Appendable out = new StringBuilder();
        final CSVFormat format =
                CSVFormat.RFC4180
                        .withEscape0('?')
                        .withDelimiter(',')
                        .withQuote1(null)
                        .withRecordSeparator1(CRLF);
        format.print2(in, out, true);
        assertEquals("x?,y?,x?r?na?,??b?,c?r?n", out.toString());
    }

    @Test
    public void testPrintWithEscapesEndWithoutCRLF() throws IOException {
        final Reader in = new StringReader("x,y,x");
        final Appendable out = new StringBuilder();
        final CSVFormat format =
                CSVFormat.RFC4180
                        .withEscape0('?')
                        .withDelimiter(',')
                        .withQuote1(null)
                        .withRecordSeparator1(CRLF);
        format.print2(in, out, true);
        assertEquals("x?,y?,x", out.toString());
    }

    @Test
    public void testPrintWithoutQuotes() throws IOException {
        final Reader in = new StringReader("");
        final Appendable out = new StringBuilder();
        final CSVFormat format =
                CSVFormat.RFC4180
                        .withDelimiter(',')
                        .withQuote0('"')
                        .withEscape0('?')
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        format.print2(in, out, true);
        assertEquals("\"\"", out.toString());
    }

    @Test
    public void testPrintWithQuoteModeIsNONE() throws IOException {
        final Reader in = new StringReader("a,b,c");
        final Appendable out = new StringBuilder();
        final CSVFormat format =
                CSVFormat.RFC4180
                        .withDelimiter(',')
                        .withQuote0('"')
                        .withEscape0('?')
                        .withQuoteMode(QuoteMode.NONE);
        format.print2(in, out, true);
        assertEquals("a?,b?,c", out.toString());
    }

    @Test
    public void testPrintWithQuotes() throws IOException {
        final Reader in = new StringReader("\"a,b,c\r\nx,y,z");
        final Appendable out = new StringBuilder();
        final CSVFormat format =
                CSVFormat.RFC4180
                        .withDelimiter(',')
                        .withQuote0('"')
                        .withEscape0('?')
                        .withQuoteMode(QuoteMode.NON_NUMERIC);
        format.print2(in, out, true);
        assertEquals("\"\"\"a,b,c\r\nx,y,z\"", out.toString());
    }

    @Test
    public void testQuoteCharSameAsCommentStartThrowsException() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.builder().setQuote0('!').setCommentMarker0('!').build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testQuoteCharSameAsCommentStartThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withQuote0('!').withCommentMarker0('!'));
    }

    @Test
    public void testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType() {
        assertThrows(
                IllegalArgumentException.class,
                () ->
                        CSVFormat.DEFAULT
                                .builder()
                                .setQuote1(Character.valueOf('!'))
                                .setCommentMarker0('!')
                                .build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testQuoteCharSameAsCommentStartThrowsExceptionForWrapperType_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withQuote1(Character.valueOf('!')).withCommentMarker0('!'));
    }

    @Test
    public void testQuoteCharSameAsDelimiterThrowsException() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.builder().setQuote0('!').setDelimiter0('!').build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testQuoteCharSameAsDelimiterThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.DEFAULT.withQuote0('!').withDelimiter('!'));
    }

    @Test
    public void testQuotePolicyNoneWithoutEscapeThrowsException() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.newFormat('!').builder().setQuoteMode(QuoteMode.NONE).build());
    }

    @SuppressWarnings("deprecation")
    @Test
    public void testQuotePolicyNoneWithoutEscapeThrowsException_Deprecated() {
        assertThrows(
                IllegalArgumentException.class,
                () -> CSVFormat.newFormat('!').withQuoteMode(QuoteMode.NONE));
    }

    @Test
    public void testRFC4180() {
        assertNull(RFC4180.getCommentMarker());
        assertEquals(',', RFC4180.getDelimiter());
        assertNull(RFC4180.getEscapeCharacter());
        assertFalse(RFC4180.getIgnoreEmptyLines());
        assertEquals(Character.valueOf('"'), RFC4180.getQuoteCharacter());
        assertNull(RFC4180.getQuoteMode());
        assertEquals("\r\n", RFC4180.getRecordSeparator());
    }

    @SuppressWarnings("boxing") // no need to worry about boxing here
    @Test
    public void testSerialization() throws Exception {
        final ByteArrayOutputStream out = new ByteArrayOutputStream();

        try (final ObjectOutputStream oos = new ObjectOutputStream(out)) {
            oos.writeObject(CSVFormat.DEFAULT);
            oos.flush();
        }

        final ObjectInputStream in =
                new ObjectInputStream(new ByteArrayInputStream(out.toByteArray()));
        final CSVFormat format = (CSVFormat) in.readObject();

        assertNotNull(format);
        assertEquals(CSVFormat.DEFAULT.getDelimiter(), format.getDelimiter(), "delimiter");
        assertEquals(
                CSVFormat.DEFAULT.getQuoteCharacter(), format.getQuoteCharacter(), "encapsulator");
        assertEquals(
                CSVFormat.DEFAULT.getCommentMarker(), format.getCommentMarker(), "comment start");
        assertEquals(
                CSVFormat.DEFAULT.getRecordSeparator(),
                format.getRecordSeparator(),
                "record separator");
        assertEquals(CSVFormat.DEFAULT.getEscapeCharacter(), format.getEscapeCharacter(), "escape");
        assertEquals(
                CSVFormat.DEFAULT.getIgnoreSurroundingSpaces(),
                format.getIgnoreSurroundingSpaces(),
                "trim");
        assertEquals(
                CSVFormat.DEFAULT.getIgnoreEmptyLines(),
                format.getIgnoreEmptyLines(),
                "empty lines");
    }

    @Test
    public void testToString() {

        final String string = CSVFormat.INFORMIX_UNLOAD.toString();

        assertEquals(
                "Delimiter=<|> Escape=<\\> QuoteChar=<\"> RecordSeparator=<\n"
                        + "> EmptyLines:ignored SkipHeaderRecord:false",
                string);
    }

    @Test
    public void testToStringAndWithCommentMarkerTakingCharacter() {

        final CSVFormat.Predefined csvFormat_Predefined = CSVFormat.Predefined.Default;
        final CSVFormat csvFormat = csvFormat_Predefined.getFormat();

        assertNull(csvFormat.getEscapeCharacter());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getTrim());
        assertFalse(csvFormat.getIgnoreSurroundingSpaces());

        assertFalse(csvFormat.getTrailingDelimiter());
        assertEquals(',', csvFormat.getDelimiter());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertEquals("\r\n", csvFormat.getRecordSeparator());

        assertFalse(csvFormat.isCommentMarkerSet());
        assertNull(csvFormat.getCommentMarker());

        assertFalse(csvFormat.isNullStringSet());
        assertFalse(csvFormat.getAllowMissingColumnNames());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertFalse(csvFormat.getSkipHeaderRecord());

        assertNull(csvFormat.getNullString());
        assertNull(csvFormat.getQuoteMode());

        assertTrue(csvFormat.getIgnoreEmptyLines());
        assertEquals('\"', (char) csvFormat.getQuoteCharacter());

        final Character character = Character.valueOf('n');

        final CSVFormat csvFormatTwo = csvFormat.withCommentMarker1(character);

        assertNull(csvFormat.getEscapeCharacter());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getTrim());
        assertFalse(csvFormat.getIgnoreSurroundingSpaces());

        assertFalse(csvFormat.getTrailingDelimiter());
        assertEquals(',', csvFormat.getDelimiter());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertEquals("\r\n", csvFormat.getRecordSeparator());

        assertFalse(csvFormat.isCommentMarkerSet());
        assertNull(csvFormat.getCommentMarker());

        assertFalse(csvFormat.isNullStringSet());
        assertFalse(csvFormat.getAllowMissingColumnNames());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertFalse(csvFormat.getSkipHeaderRecord());

        assertNull(csvFormat.getNullString());
        assertNull(csvFormat.getQuoteMode());

        assertTrue(csvFormat.getIgnoreEmptyLines());
        assertEquals('\"', (char) csvFormat.getQuoteCharacter());

        assertFalse(csvFormatTwo.isNullStringSet());
        assertFalse(csvFormatTwo.getAllowMissingColumnNames());

        assertEquals('\"', (char) csvFormatTwo.getQuoteCharacter());
        assertNull(csvFormatTwo.getNullString());

        assertEquals(',', csvFormatTwo.getDelimiter());
        assertFalse(csvFormatTwo.getTrailingDelimiter());

        assertTrue(csvFormatTwo.isCommentMarkerSet());
        assertFalse(csvFormatTwo.getIgnoreHeaderCase());

        assertFalse(csvFormatTwo.getTrim());
        assertNull(csvFormatTwo.getEscapeCharacter());

        assertTrue(csvFormatTwo.isQuoteCharacterSet());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertEquals("\r\n", csvFormatTwo.getRecordSeparator());
        assertNull(csvFormatTwo.getQuoteMode());

        assertEquals('n', (char) csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.getSkipHeaderRecord());

        assertFalse(csvFormatTwo.isEscapeCharacterSet());
        assertTrue(csvFormatTwo.getIgnoreEmptyLines());

        assertNotSame(csvFormat, csvFormatTwo);
        assertNotSame(csvFormatTwo, csvFormat);

        Assertions.assertNotEquals(csvFormatTwo, csvFormat);

        assertNull(csvFormat.getEscapeCharacter());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getTrim());
        assertFalse(csvFormat.getIgnoreSurroundingSpaces());

        assertFalse(csvFormat.getTrailingDelimiter());
        assertEquals(',', csvFormat.getDelimiter());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertEquals("\r\n", csvFormat.getRecordSeparator());

        assertFalse(csvFormat.isCommentMarkerSet());
        assertNull(csvFormat.getCommentMarker());

        assertFalse(csvFormat.isNullStringSet());
        assertFalse(csvFormat.getAllowMissingColumnNames());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertFalse(csvFormat.getSkipHeaderRecord());

        assertNull(csvFormat.getNullString());
        assertNull(csvFormat.getQuoteMode());

        assertTrue(csvFormat.getIgnoreEmptyLines());
        assertEquals('\"', (char) csvFormat.getQuoteCharacter());

        assertFalse(csvFormatTwo.isNullStringSet());
        assertFalse(csvFormatTwo.getAllowMissingColumnNames());

        assertEquals('\"', (char) csvFormatTwo.getQuoteCharacter());
        assertNull(csvFormatTwo.getNullString());

        assertEquals(',', csvFormatTwo.getDelimiter());
        assertFalse(csvFormatTwo.getTrailingDelimiter());

        assertTrue(csvFormatTwo.isCommentMarkerSet());
        assertFalse(csvFormatTwo.getIgnoreHeaderCase());

        assertFalse(csvFormatTwo.getTrim());
        assertNull(csvFormatTwo.getEscapeCharacter());

        assertTrue(csvFormatTwo.isQuoteCharacterSet());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertEquals("\r\n", csvFormatTwo.getRecordSeparator());
        assertNull(csvFormatTwo.getQuoteMode());

        assertEquals('n', (char) csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.getSkipHeaderRecord());

        assertFalse(csvFormatTwo.isEscapeCharacterSet());
        assertTrue(csvFormatTwo.getIgnoreEmptyLines());

        assertNotSame(csvFormat, csvFormatTwo);
        assertNotSame(csvFormatTwo, csvFormat);

        Assertions.assertNotEquals(csvFormat, csvFormatTwo);

        Assertions.assertNotEquals(csvFormatTwo, csvFormat);
        assertEquals(
                "Delimiter=<,> QuoteChar=<\"> CommentStart=<n> "
                        + "RecordSeparator=<\r\n> EmptyLines:ignored SkipHeaderRecord:false",
                csvFormatTwo.toString());
    }

    @Test
    public void testTrim() throws IOException {
        final CSVFormat formatWithTrim =
                CSVFormat.DEFAULT
                        .withDelimiter(',')
                        .withTrim0()
                        .withQuote1(null)
                        .withRecordSeparator1(CRLF);

        CharSequence in = "a,b,c";
        final StringBuilder out = new StringBuilder();
        formatWithTrim.print2(in, out, true);
        assertEquals("a,b,c", out.toString());

        in = new StringBuilder(" x,y,z");
        out.setLength(0);
        formatWithTrim.print2(in, out, true);
        assertEquals("x,y,z", out.toString());

        in = new StringBuilder("");
        out.setLength(0);
        formatWithTrim.print2(in, out, true);
        assertEquals("", out.toString());

        in = new StringBuilder("header\r\n");
        out.setLength(0);
        formatWithTrim.print2(in, out, true);
        assertEquals("header", out.toString());
    }

    @Test
    public void testWithCommentStart() {
        final CSVFormat formatWithCommentStart = CSVFormat.DEFAULT.withCommentMarker0('#');
        assertEquals(Character.valueOf('#'), formatWithCommentStart.getCommentMarker());
    }

    @Test
    public void testWithCommentStartCRThrowsException() {
        assertThrows(
                IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withCommentMarker0(CR));
    }

    @Test
    public void testWithDelimiter() {
        final CSVFormat formatWithDelimiter = CSVFormat.DEFAULT.withDelimiter('!');
        assertEquals('!', formatWithDelimiter.getDelimiter());
    }

    @Test
    public void testWithDelimiterLFThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withDelimiter(LF));
    }

    @Test
    public void testWithEmptyDuplicates() {
        final CSVFormat formatWithEmptyDuplicates =
                CSVFormat.DEFAULT
                        .builder()
                        .setDuplicateHeaderMode(DuplicateHeaderMode.ALLOW_EMPTY)
                        .build();

        assertEquals(
                DuplicateHeaderMode.ALLOW_EMPTY,
                formatWithEmptyDuplicates.getDuplicateHeaderMode());
        assertFalse(formatWithEmptyDuplicates.getAllowDuplicateHeaderNames());
    }

    @Test
    public void testWithEscape() {
        final CSVFormat formatWithEscape = CSVFormat.DEFAULT.withEscape0('&');
        assertEquals(Character.valueOf('&'), formatWithEscape.getEscapeCharacter());
    }

    @Test
    public void testWithEscapeCRThrowsExceptions() {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withEscape0(CR));
    }

    @Test
    public void testWithHeaderComments() {

        final CSVFormat csvFormat = CSVFormat.DEFAULT;

        assertEquals('\"', (char) csvFormat.getQuoteCharacter());
        assertFalse(csvFormat.isCommentMarkerSet());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getSkipHeaderRecord());
        assertNull(csvFormat.getQuoteMode());

        assertEquals(',', csvFormat.getDelimiter());
        assertTrue(csvFormat.getIgnoreEmptyLines());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertNull(csvFormat.getCommentMarker());

        assertEquals("\r\n", csvFormat.getRecordSeparator());
        assertFalse(csvFormat.getTrailingDelimiter());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isNullStringSet());
        assertNull(csvFormat.getNullString());

        assertFalse(csvFormat.getIgnoreSurroundingSpaces());
        assertNull(csvFormat.getEscapeCharacter());

        final Object[] objectArray = new Object[8];
        final CSVFormat csvFormatTwo = csvFormat.withHeaderComments(objectArray);

        assertEquals('\"', (char) csvFormat.getQuoteCharacter());
        assertFalse(csvFormat.isCommentMarkerSet());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getSkipHeaderRecord());
        assertNull(csvFormat.getQuoteMode());

        assertEquals(',', csvFormat.getDelimiter());
        assertTrue(csvFormat.getIgnoreEmptyLines());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertNull(csvFormat.getCommentMarker());

        assertEquals("\r\n", csvFormat.getRecordSeparator());
        assertFalse(csvFormat.getTrailingDelimiter());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isNullStringSet());
        assertNull(csvFormat.getNullString());

        assertFalse(csvFormat.getIgnoreSurroundingSpaces());
        assertNull(csvFormat.getEscapeCharacter());

        assertFalse(csvFormatTwo.getIgnoreHeaderCase());
        assertNull(csvFormatTwo.getQuoteMode());

        assertTrue(csvFormatTwo.getIgnoreEmptyLines());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertNull(csvFormatTwo.getEscapeCharacter());
        assertFalse(csvFormatTwo.getTrim());

        assertFalse(csvFormatTwo.isEscapeCharacterSet());
        assertTrue(csvFormatTwo.isQuoteCharacterSet());

        assertFalse(csvFormatTwo.getSkipHeaderRecord());
        assertEquals('\"', (char) csvFormatTwo.getQuoteCharacter());

        assertFalse(csvFormatTwo.getAllowMissingColumnNames());
        assertNull(csvFormatTwo.getNullString());

        assertFalse(csvFormatTwo.isNullStringSet());
        assertFalse(csvFormatTwo.getTrailingDelimiter());

        assertEquals("\r\n", csvFormatTwo.getRecordSeparator());
        assertEquals(',', csvFormatTwo.getDelimiter());

        assertNull(csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.isCommentMarkerSet());

        assertNotSame(csvFormat, csvFormatTwo);
        assertNotSame(csvFormatTwo, csvFormat);

        Assertions.assertNotEquals(csvFormatTwo, csvFormat); // CSV-244 - should not be equal

        final String string = csvFormatTwo.format(objectArray);

        assertEquals('\"', (char) csvFormat.getQuoteCharacter());
        assertFalse(csvFormat.isCommentMarkerSet());

        assertFalse(csvFormat.isEscapeCharacterSet());
        assertTrue(csvFormat.isQuoteCharacterSet());

        assertFalse(csvFormat.getSkipHeaderRecord());
        assertNull(csvFormat.getQuoteMode());

        assertEquals(',', csvFormat.getDelimiter());
        assertTrue(csvFormat.getIgnoreEmptyLines());

        assertFalse(csvFormat.getIgnoreHeaderCase());
        assertNull(csvFormat.getCommentMarker());

        assertEquals("\r\n", csvFormat.getRecordSeparator());
        assertFalse(csvFormat.getTrailingDelimiter());

        assertFalse(csvFormat.getAllowMissingColumnNames());
        assertFalse(csvFormat.getTrim());

        assertFalse(csvFormat.isNullStringSet());
        assertNull(csvFormat.getNullString());

        assertFalse(csvFormat.getIgnoreSurroundingSpaces());
        assertNull(csvFormat.getEscapeCharacter());

        assertFalse(csvFormatTwo.getIgnoreHeaderCase());
        assertNull(csvFormatTwo.getQuoteMode());

        assertTrue(csvFormatTwo.getIgnoreEmptyLines());
        assertFalse(csvFormatTwo.getIgnoreSurroundingSpaces());

        assertNull(csvFormatTwo.getEscapeCharacter());
        assertFalse(csvFormatTwo.getTrim());

        assertFalse(csvFormatTwo.isEscapeCharacterSet());
        assertTrue(csvFormatTwo.isQuoteCharacterSet());

        assertFalse(csvFormatTwo.getSkipHeaderRecord());
        assertEquals('\"', (char) csvFormatTwo.getQuoteCharacter());

        assertFalse(csvFormatTwo.getAllowMissingColumnNames());
        assertNull(csvFormatTwo.getNullString());

        assertFalse(csvFormatTwo.isNullStringSet());
        assertFalse(csvFormatTwo.getTrailingDelimiter());

        assertEquals("\r\n", csvFormatTwo.getRecordSeparator());
        assertEquals(',', csvFormatTwo.getDelimiter());

        assertNull(csvFormatTwo.getCommentMarker());
        assertFalse(csvFormatTwo.isCommentMarkerSet());

        assertNotSame(csvFormat, csvFormatTwo);
        assertNotSame(csvFormatTwo, csvFormat);

        assertNotNull(string);
        Assertions.assertNotEquals(csvFormat, csvFormatTwo); // CSV-244 - should not be equal

        Assertions.assertNotEquals(csvFormatTwo, csvFormat); // CSV-244 - should not be equal
        assertEquals(",,,,,,,", string);
    }

    @Test
    public void testWithIgnoreEmptyLines() {
        assertFalse(CSVFormat.DEFAULT.withIgnoreEmptyLines1(false).getIgnoreEmptyLines());
        assertTrue(CSVFormat.DEFAULT.withIgnoreEmptyLines0().getIgnoreEmptyLines());
    }

    @Test
    public void testWithIgnoreSurround() {
        assertFalse(
                CSVFormat.DEFAULT.withIgnoreSurroundingSpaces1(false).getIgnoreSurroundingSpaces());
        assertTrue(CSVFormat.DEFAULT.withIgnoreSurroundingSpaces0().getIgnoreSurroundingSpaces());
    }

    @Test
    public void testWithNullString() {
        final CSVFormat formatWithNullString = CSVFormat.DEFAULT.withNullString("null");
        assertEquals("null", formatWithNullString.getNullString());
    }

    @Test
    public void testWithQuoteChar() {
        final CSVFormat formatWithQuoteChar = CSVFormat.DEFAULT.withQuote0('"');
        assertEquals(Character.valueOf('"'), formatWithQuoteChar.getQuoteCharacter());
    }

    @Test
    public void testWithQuoteLFThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> CSVFormat.DEFAULT.withQuote0(LF));
    }

    @Test
    public void testWithQuotePolicy() {
        final CSVFormat formatWithQuotePolicy = CSVFormat.DEFAULT.withQuoteMode(QuoteMode.ALL);
        assertEquals(QuoteMode.ALL, formatWithQuotePolicy.getQuoteMode());
    }

    @Test
    public void testWithRecordSeparatorCR() {
        final CSVFormat formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(CR);
        assertEquals(String.valueOf(CR), formatWithRecordSeparator.getRecordSeparator());
    }

    @Test
    public void testWithRecordSeparatorCRLF() {
        final CSVFormat formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator1(CRLF);
        assertEquals(CRLF, formatWithRecordSeparator.getRecordSeparator());
    }

    @Test
    public void testWithRecordSeparatorLF() {
        final CSVFormat formatWithRecordSeparator = CSVFormat.DEFAULT.withRecordSeparator0(LF);
        assertEquals(String.valueOf(LF), formatWithRecordSeparator.getRecordSeparator());
    }

    @Test
    public void testWithSystemRecordSeparator() {
        final CSVFormat formatWithRecordSeparator = CSVFormat.DEFAULT.withSystemRecordSeparator();
        assertEquals(System.lineSeparator(), formatWithRecordSeparator.getRecordSeparator());
    }
}
