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

package org.apache.commons.cli.bug;

import static org.junit.Assert.assertEquals;

import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Options;
import org.junit.Before;
import org.junit.Test;

import java.io.PrintWriter;
import java.io.StringWriter;

public class BugCLI162Test {
    /** Constant for the line separator. */
    private static final String CR = System.getProperty("line.separator");

    private static final String OPT = "-";

    private static final String OPT_COLUMN_NAMES = "l";

    private static final String OPT_CONNECTION = "c";

    private static final String OPT_DESCRIPTION = "e";

    private static final String OPT_DRIVER = "d";

    private static final String OPT_DRIVER_INFO = "n";

    private static final String OPT_FILE_BINDING = "b";

    private static final String OPT_FILE_JDBC = "j";

    private static final String OPT_FILE_SFMD = "f";

    private static final String OPT_HELP = "h";

    private static final String OPT_HELP_LONG = "help";

    private static final String OPT_INTERACTIVE = "i";

    private static final String OPT_JDBC_TO_SFMD = "2";

    private static final String OPT_JDBC_TO_SFMD_L = "jdbc2sfmd";

    private static final String OPT_METADATA = "m";

    private static final String OPT_PARAM_MODES_INT = "o";

    private static final String OPT_PARAM_MODES_NAME = "O";

    private static final String OPT_PARAM_NAMES = "a";

    private static final String OPT_PARAM_TYPES_INT = "y";

    private static final String OPT_PARAM_TYPES_NAME = "Y";

    private static final String OPT_PASSWORD = "p";

    private static final String OPT_PASSWORD_L = "password";

    private static final String OPT_SQL = "s";

    private static final String OPT_SQL_L = "sql";

    private static final String OPT_STACK_TRACE = "t";

    private static final String OPT_TIMING = "g";

    private static final String OPT_TRIM_L = "trim";

    private static final String OPT_USER = "u";

    private static final String OPT_WRITE_TO_FILE = "w";

    private static final String PMODE_IN = "IN";

    private static final String PMODE_INOUT = "INOUT";

    private static final String PMODE_OUT = "OUT";

    private static final String PMODE_UNK = "Unknown";

    private static final String PMODES =
            PMODE_IN + ", " + PMODE_INOUT + ", " + PMODE_OUT + ", " + PMODE_UNK;

    private HelpFormatter formatter;

    private StringWriter sw;

    @Before
    public void setUp() {
        formatter = new HelpFormatter();
        sw = new StringWriter();
    }

    @Test
    public void testInfiniteLoop_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testInfiniteLoop_test1_decomposed()  {
        final Options options = new Options();
        options.addOption3("h", "help", false, "This is a looooong description");
    }

    @Test
    public void testInfiniteLoop_test2_decomposed()  {
        final Options options = new Options();
        options.addOption3("h", "help", false, "This is a looooong description");
        formatter.printHelp2(
                new PrintWriter(sw),
                20,
                "app",
                null,
                options,
                HelpFormatter.DEFAULT_LEFT_PAD,
                HelpFormatter.DEFAULT_DESC_PAD,
                null);
    }

    @Test
    public void testInfiniteLoop_test3_decomposed()  {
        final Options options = new Options();
        options.addOption3("h", "help", false, "This is a looooong description");
        formatter.printHelp2(
                new PrintWriter(sw),
                20,
                "app",
                null,
                options,
                HelpFormatter.DEFAULT_LEFT_PAD,
                HelpFormatter.DEFAULT_DESC_PAD,
                null);
        final String expected =
                "usage: app"
                        + CR
                        + " -h,--help   This is"
                        + CR
                        + "             a"
                        + CR
                        + "             looooon"
                        + CR
                        + "             g"
                        + CR
                        + "             descrip"
                        + CR
                        + "             tion"
                        + CR;
        assertEquals(expected, sw.toString());
    }

    @Test
    public void testLongLineChunking_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testLongLineChunking_test1_decomposed()  {
        final Options options = new Options();
        options.addOption3(
                "x",
                "extralongarg",
                false,
                "This description has ReallyLongValuesThatAreLongerThanTheWidthOfTheColumns and"
                    + " also other"
                    + " ReallyLongValuesThatAreHugerAndBiggerThanTheWidthOfTheColumnsBob, yes. ");
    }

    @Test
    public void testLongLineChunking_test2_decomposed()  {
        final Options options = new Options();
        options.addOption3(
                "x",
                "extralongarg",
                false,
                "This description has ReallyLongValuesThatAreLongerThanTheWidthOfTheColumns and"
                    + " also other"
                    + " ReallyLongValuesThatAreHugerAndBiggerThanTheWidthOfTheColumnsBob, yes. ");
        formatter.printHelp2(
                new PrintWriter(sw),
                35,
                this.getClass().getName(),
                "Header",
                options,
                0,
                5,
                "Footer");
    }

    @Test
    public void testLongLineChunking_test3_decomposed()  {
        final Options options = new Options();
        options.addOption3(
                "x",
                "extralongarg",
                false,
                "This description has ReallyLongValuesThatAreLongerThanTheWidthOfTheColumns and"
                    + " also other"
                    + " ReallyLongValuesThatAreHugerAndBiggerThanTheWidthOfTheColumnsBob, yes. ");
        formatter.printHelp2(
                new PrintWriter(sw),
                35,
                this.getClass().getName(),
                "Header",
                options,
                0,
                5,
                "Footer");
        final String expected =
                "usage:"
                        + CR
                        + "       org.apache.commons.cli.bug.B"
                        + CR
                        + "       ugCLI162Test"
                        + CR
                        + "Header"
                        + CR
                        + "-x,--extralongarg     This"
                        + CR
                        + "                      description"
                        + CR
                        + "                      has"
                        + CR
                        + "                      ReallyLongVal"
                        + CR
                        + "                      uesThatAreLon"
                        + CR
                        + "                      gerThanTheWid"
                        + CR
                        + "                      thOfTheColumn"
                        + CR
                        + "                      s and also"
                        + CR
                        + "                      other"
                        + CR
                        + "                      ReallyLongVal"
                        + CR
                        + "                      uesThatAreHug"
                        + CR
                        + "                      erAndBiggerTh"
                        + CR
                        + "                      anTheWidthOfT"
                        + CR
                        + "                      heColumnsBob,"
                        + CR
                        + "                      yes."
                        + CR
                        + "Footer"
                        + CR;
        assertEquals("Long arguments did not split as expected", expected, sw.toString());
    }

    @Test
    public void testLongLineChunkingIndentIgnored_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testLongLineChunkingIndentIgnored_test1_decomposed()  {
        final Options options = new Options();
        options.addOption3("x", "extralongarg", false, "This description is Long.");
    }

    @Test
    public void testLongLineChunkingIndentIgnored_test2_decomposed()  {
        final Options options = new Options();
        options.addOption3("x", "extralongarg", false, "This description is Long.");
        formatter.printHelp2(
                new PrintWriter(sw),
                22,
                this.getClass().getName(),
                "Header",
                options,
                0,
                5,
                "Footer");
    }

    @Test
    public void testLongLineChunkingIndentIgnored_test3_decomposed()  {
        final Options options = new Options();
        options.addOption3("x", "extralongarg", false, "This description is Long.");
        formatter.printHelp2(
                new PrintWriter(sw),
                22,
                this.getClass().getName(),
                "Header",
                options,
                0,
                5,
                "Footer");
        final String expected =
                "usage:"
                        + CR
                        + "       org.apache.comm"
                        + CR
                        + "       ons.cli.bug.Bug"
                        + CR
                        + "       CLI162Test"
                        + CR
                        + "Header"
                        + CR
                        + "-x,--extralongarg"
                        + CR
                        + " This description is"
                        + CR
                        + " Long."
                        + CR
                        + "Footer"
                        + CR;
        assertEquals("Long arguments did not split as expected", expected, sw.toString());
    }
}