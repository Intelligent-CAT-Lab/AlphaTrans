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

package org.apache.commons.cli;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

public class DefaultParserTest extends ParserTestCase {

    @Override
    @Before
    public void setUp() {
        super.setUp();
        parser = new DefaultParser(2, false, null);
    }

    @Test
    public void testBuilder_test0_decomposed()  {
        DefaultParser.builder();
    }

    @Test
    public void testBuilder_test1_decomposed()  {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
    }

    @Test
    public void testBuilder_test2_decomposed()  {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).setAllowPartialMatching(false);
    }

    @Test
    public void testBuilder_test3_decomposed()  {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).setAllowPartialMatching(false);
        parser =
                DefaultParser.builder()
                        .setStripLeadingAndTrailingQuotes(false)
                        .setAllowPartialMatching(false)
                        .build();
    }

    @Test
    public void testBuilder_test4_decomposed()  {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).setAllowPartialMatching(false);
        parser =
                DefaultParser.builder()
                        .setStripLeadingAndTrailingQuotes(false)
                        .setAllowPartialMatching(false)
                        .build();
        assertEquals(DefaultParser.class, parser.getClass());
    }

    @Test
    public void testLongOptionQuoteHandlingWithoutStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testLongOptionQuoteHandlingWithoutStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
    }

    @Test
    public void testLongOptionQuoteHandlingWithoutStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
    }

    @Test
    public void testLongOptionQuoteHandlingWithoutStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"--bfile", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testLongOptionQuoteHandlingWithoutStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"--bfile", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm --bfile \"arg\" keeps quotes",
                "\"quoted string\"",
                cl.getOptionValue4("b"));
    }

    @Test
    public void testLongOptionQuoteHandlingWithStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testLongOptionQuoteHandlingWithStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
    }

    @Test
    public void testLongOptionQuoteHandlingWithStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
    }

    @Test
    public void testLongOptionQuoteHandlingWithStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"--bfile", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testLongOptionQuoteHandlingWithStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"--bfile", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm --bfile \"arg\" strips quotes", "quoted string", cl.getOptionValue4("b"));
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandling_test0_decomposed() throws Exception {
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandling_test1_decomposed() throws Exception {
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm --bfile=\"arg\" strips quotes",
                "\"quoted string\"",
                cl.getOptionValue4("b"));
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithoutStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithoutStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithoutStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithoutStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithoutStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm --bfile=\"arg\" keeps quotes",
                "\"quoted string\"",
                cl.getOptionValue4("b"));
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testLongOptionWithEqualsQuoteHandlingWithStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"--bfile=\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm --bfile=\"arg\" strips quotes", "quoted string", cl.getOptionValue4("b"));
    }

    @Test
    public void testShortOptionConcatenatedQuoteHandling_test0_decomposed() throws Exception {
        final String[] args = {"-b\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testShortOptionConcatenatedQuoteHandling_test1_decomposed() throws Exception {
        final String[] args = {"-b\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm -b\"arg\" keeps quotes", "\"quoted string\"", cl.getOptionValue4("b"));
    }

    @Test
    public void testShortOptionQuoteHandlingWithoutStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testShortOptionQuoteHandlingWithoutStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
    }

    @Test
    public void testShortOptionQuoteHandlingWithoutStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
    }

    @Test
    public void testShortOptionQuoteHandlingWithoutStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"-b", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testShortOptionQuoteHandlingWithoutStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(false);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(false).build();
        final String[] args = {"-b", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals(
                "Confirm -b \"arg\" keeps quotes", "\"quoted string\"", cl.getOptionValue4("b"));
    }

    @Test
    public void testShortOptionQuoteHandlingWithStrip_test0_decomposed() throws Exception {
        DefaultParser.builder();
    }

    @Test
    public void testShortOptionQuoteHandlingWithStrip_test1_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
    }

    @Test
    public void testShortOptionQuoteHandlingWithStrip_test2_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
    }

    @Test
    public void testShortOptionQuoteHandlingWithStrip_test3_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"-b", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
    }

    @Test
    public void testShortOptionQuoteHandlingWithStrip_test4_decomposed() throws Exception {
        DefaultParser.builder();
        DefaultParser.builder().setStripLeadingAndTrailingQuotes(true);
        parser = DefaultParser.builder().setStripLeadingAndTrailingQuotes(true).build();
        final String[] args = {"-b", "\"quoted string\""};
        final CommandLine cl = parser.parse0(options, args);
        assertEquals("Confirm -b \"arg\" strips quotes", "quoted string", cl.getOptionValue4("b"));
    }
}