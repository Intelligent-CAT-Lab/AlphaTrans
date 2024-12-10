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

import static org.apache.commons.csv.Constants.BACKSPACE;
import static org.apache.commons.csv.Constants.FF;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.StringReader;

/** */
public class LexerTest {

    private CSVFormat formatWithEscaping;

    @SuppressWarnings("resource")
    private Lexer createLexer(final String input, final CSVFormat format) {
        return new Lexer(format, new ExtendedBufferedReader(new StringReader(input)));
    }

    @BeforeEach
    public void setUp() {
        formatWithEscaping = CSVFormat.DEFAULT.withEscape0('\\');
    }

    @Test
    public void testEscapingAtEOF_test0_decomposed() throws Exception {
        final String code = "escaping at EOF is evil\\";
        try (final Lexer lexer = createLexer(code, formatWithEscaping)) {
            assertThrows(IOException.class, () -> lexer.nextToken(new Token()));
        }
    }

    @Test
    public void testIsMetaCharCommentStart_test0_decomposed() throws IOException {
        try (final Lexer lexer = createLexer("#", CSVFormat.DEFAULT.withCommentMarker0('#'))) {
            final int ch = lexer.readEscape();
            assertEquals('#', ch);
        }
    }

    @Test
    public void testReadEscapeBackspace_test0_decomposed() throws IOException {
        try (final Lexer lexer = createLexer("b", CSVFormat.DEFAULT.withEscape0('\b'))) {
            final int ch = lexer.readEscape();
            assertEquals(BACKSPACE, ch);
        }
    }

    @Test
    public void testReadEscapeFF_test0_decomposed() throws IOException {
        try (final Lexer lexer = createLexer("f", CSVFormat.DEFAULT.withEscape0('\f'))) {
            final int ch = lexer.readEscape();
            assertEquals(FF, ch);
        }
    }
}