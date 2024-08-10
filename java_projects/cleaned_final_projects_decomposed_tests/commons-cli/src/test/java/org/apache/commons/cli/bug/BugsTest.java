/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.cli.bug;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.GnuParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.MissingArgumentException;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.OptionBuilder;
import org.apache.commons.cli.OptionGroup;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.apache.commons.cli.Parser;
import org.apache.commons.cli.PosixParser;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Iterator;
import java.util.Properties;

@SuppressWarnings("deprecation") // tests some deprecated classes
public class BugsTest {

    @Test
    public void test11456_test0_decomposed() throws Exception {
        Options options = new Options();
    }

    @Test
    public void test11456_test1_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
    }

    @Test
    public void test11456_test2_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
    }

    @Test
    public void test11456_test3_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
    }

    @Test
    public void test11456_test4_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
    }

    @Test
    public void test11456_test5_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
    }

    @Test
    public void test11456_test6_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
    }

    @Test
    public void test11456_test7_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test11456_test8_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
    }

    @Test
    public void test11456_test9_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
    }

    @Test
    public void test11456_test10_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
    }

    @Test
    public void test11456_test11_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
    }

    @Test
    public void test11456_test12_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
    }

    @Test
    public void test11456_test13_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
    }

    @Test
    public void test11456_test14_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
    }

    @Test
    public void test11456_test15_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
    }

    @Test
    public void test11456_test16_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
    }

    @Test
    public void test11456_test17_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        args = new String[] {"-a", "-b", "value"};
        parser = new GnuParser();
    }

    @Test
    public void test11456_test18_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        args = new String[] {"-a", "-b", "value"};
        parser = new GnuParser();
        cmd = parser.parse0(options, args);
    }

    @Test
    public void test11456_test19_decomposed() throws Exception {
        Options options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        String[] args = {"-a", "-bvalue"};
        CommandLineParser parser = new PosixParser();
        CommandLine cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
        options = new Options();
        OptionBuilder.hasOptionalArg();
        OptionBuilder.hasOptionalArg().create1('a');
        options.addOption0(OptionBuilder.hasOptionalArg().create1('a'));
        OptionBuilder.hasArg0();
        OptionBuilder.hasArg0().create1('b');
        options.addOption0(OptionBuilder.hasArg0().create1('b'));
        args = new String[] {"-a", "-b", "value"};
        parser = new GnuParser();
        cmd = parser.parse0(options, args);
        assertEquals(cmd.getOptionValue0('b'), "value");
    }

    @Test
    public void test11457_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void test11457_test1_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
    }

    @Test
    public void test11457_test2_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
    }

    @Test
    public void test11457_test3_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
    }

    @Test
    public void test11457_test4_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
        final String[] args = {"--verbose"};
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test11457_test5_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
        final String[] args = {"--verbose"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
    }

    @Test
    public void test11457_test6_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("verbose");
        OptionBuilder.withLongOpt("verbose").create0();
        options.addOption0(OptionBuilder.withLongOpt("verbose").create0());
        final String[] args = {"--verbose"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        assertTrue(cmd.hasOption2("verbose"));
    }

    @Test
    public void test11458_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void test11458_test1_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
    }

    @Test
    public void test11458_test2_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
    }

    @Test
    public void test11458_test3_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
    }

    @Test
    public void test11458_test4_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
    }

    @Test
    public void test11458_test5_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
    }

    @Test
    public void test11458_test6_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
    }

    @Test
    public void test11458_test7_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
    }

    @Test
    public void test11458_test8_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
    }

    @Test
    public void test11458_test9_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test11458_test10_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
    }

    @Test
    public void test11458_test11_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
    }

    @Test
    public void test11458_test12_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
        assertEquals(values[0], "JAVA_HOME");
        assertEquals(values[1], "/opt/java");
    }

    @Test
    public void test11458_test13_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
        assertEquals(values[0], "JAVA_HOME");
        assertEquals(values[1], "/opt/java");
        values = cmd.getOptionValues0('p');
    }

    @Test
    public void test11458_test14_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
        assertEquals(values[0], "JAVA_HOME");
        assertEquals(values[1], "/opt/java");
        values = cmd.getOptionValues0('p');
        assertEquals(values[0], "file1");
        assertEquals(values[1], "file2");
    }

    @Test
    public void test11458_test15_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
        assertEquals(values[0], "JAVA_HOME");
        assertEquals(values[1], "/opt/java");
        values = cmd.getOptionValues0('p');
        assertEquals(values[0], "file1");
        assertEquals(values[1], "file2");
        assertEquals(values[2], "file3");
        final Iterator<Option> iter = cmd.iterator();
    }

    @Test
    public void test11458_test16_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withValueSeparator1('=');
        OptionBuilder.withValueSeparator1('=').hasArgs0();
        OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D');
        options.addOption0(OptionBuilder.withValueSeparator1('=').hasArgs0().create1('D'));
        OptionBuilder.withValueSeparator1(':');
        OptionBuilder.withValueSeparator1(':').hasArgs0();
        OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p');
        options.addOption0(OptionBuilder.withValueSeparator1(':').hasArgs0().create1('p'));
        final String[] args = {"-DJAVA_HOME=/opt/java", "-pfile1:file2:file3"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        String[] values = cmd.getOptionValues0('D');
        assertEquals(values[0], "JAVA_HOME");
        assertEquals(values[1], "/opt/java");
        values = cmd.getOptionValues0('p');
        assertEquals(values[0], "file1");
        assertEquals(values[1], "file2");
        assertEquals(values[2], "file3");
        final Iterator<Option> iter = cmd.iterator();
        while (iter.hasNext()) {
            final Option opt = iter.next();
            switch (opt.getId()) {
                case 'D':
                    assertEquals(opt.getValue1(0), "JAVA_HOME");
                    assertEquals(opt.getValue1(1), "/opt/java");
                    break;
                case 'p':
                    assertEquals(opt.getValue1(0), "file1");
                    assertEquals(opt.getValue1(1), "file2");
                    assertEquals(opt.getValue1(2), "file3");
                    break;
                default:
                    fail("-D option not found");
            }
        }
    }

    @Test
    public void test11680_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void test11680_test1_decomposed() throws Exception {
        final Options options = new Options();
        options.addOption1("f", true, "foobar");
        options.addOption1("m", true, "missing");
    }

    @Test
    public void test11680_test2_decomposed() throws Exception {
        final Options options = new Options();
        options.addOption1("f", true, "foobar");
        options.addOption1("m", true, "missing");
        final String[] args = {"-f", "foo"};
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test11680_test3_decomposed() throws Exception {
        final Options options = new Options();
        options.addOption1("f", true, "foobar");
        options.addOption1("m", true, "missing");
        final String[] args = {"-f", "foo"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
    }

    @Test
    public void test11680_test4_decomposed() throws Exception {
        final Options options = new Options();
        options.addOption1("f", true, "foobar");
        options.addOption1("m", true, "missing");
        final String[] args = {"-f", "foo"};
        final CommandLineParser parser = new PosixParser();
        final CommandLine cmd = parser.parse0(options, args);
        cmd.getOptionValue5("f", "default f");
        cmd.getOptionValue5("m", "default m");
    }

    @Test
    public void test12210_test0_decomposed() throws Exception {
        final Options mainOptions = new Options();
    }

    @Test
    public void test12210_test1_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
    }

    @Test
    public void test12210_test2_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
    }

    @Test
    public void test12210_test3_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
    }

    @Test
    public void test12210_test4_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
    }

    @Test
    public void test12210_test5_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
    }

    @Test
    public void test12210_test6_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
    }

    @Test
    public void test12210_test7_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
    }

    @Test
    public void test12210_test8_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
    }

    @Test
    public void test12210_test9_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
    }

    @Test
    public void test12210_test10_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
        repOptions.addOption1("repopto", false, "desc");
        repOptions.addOption1("repoptt", false, "desc");
    }

    @Test
    public void test12210_test11_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
        repOptions.addOption1("repopto", false, "desc");
        repOptions.addOption1("repoptt", false, "desc");
        final GnuParser parser = new GnuParser();
    }

    @Test
    public void test12210_test12_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
        repOptions.addOption1("repopto", false, "desc");
        repOptions.addOption1("repoptt", false, "desc");
        final GnuParser parser = new GnuParser();
        CommandLine cmd = parser.parse1(mainOptions, argv, true);
    }

    @Test
    public void test12210_test13_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
        repOptions.addOption1("repopto", false, "desc");
        repOptions.addOption1("repoptt", false, "desc");
        final GnuParser parser = new GnuParser();
        CommandLine cmd = parser.parse1(mainOptions, argv, true);
        argv = cmd.getArgs();
    }

    @Test
    public void test12210_test14_decomposed() throws Exception {
        final Options mainOptions = new Options();
        String[] argv = {"-exec", "-exec_opt1", "-exec_opt2"};
        final OptionGroup grp = new OptionGroup();
        Option.Option2("exec",false,"description for this option");
        grp.addOption(Option.Option2("exec", false, "description for this option"));
        Option.Option2("rep",false,"description for this option");
        grp.addOption(Option.Option2("rep", false, "description for this option"));
        mainOptions.addOptionGroup(grp);
        final Options execOptions = new Options();
        execOptions.addOption1("exec_opt1", false, " desc");
        execOptions.addOption1("exec_opt2", false, " desc");
        final Options repOptions = new Options();
        repOptions.addOption1("repopto", false, "desc");
        repOptions.addOption1("repoptt", false, "desc");
        final GnuParser parser = new GnuParser();
        CommandLine cmd = parser.parse1(mainOptions, argv, true);
        argv = cmd.getArgs();
        if (cmd.hasOption2("exec")) {
            cmd = parser.parse1(execOptions, argv, false);
            assertTrue(cmd.hasOption2("exec_opt1"));
            assertTrue(cmd.hasOption2("exec_opt2"));
        } else if (cmd.hasOption2("rep")) {
            cmd = parser.parse1(repOptions, argv, false);
        } else {
            fail("exec option not found");
        }
    }

    @Test
    public void test13425_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void test13425_test1_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
    }

    @Test
    public void test13425_test2_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
    }

    @Test
    public void test13425_test3_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
    }

    @Test
    public void test13425_test4_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
    }

    @Test
    public void test13425_test5_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
    }

    @Test
    public void test13425_test6_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
    }

    @Test
    public void test13425_test7_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
    }

    @Test
    public void test13425_test8_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
        final Option newpass =
                OptionBuilder.withLongOpt("new-password")
                        .withDescription("Use this option to specify the new password")
                        .hasArg0()
                        .create1('n');
    }

    @Test
    public void test13425_test9_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
        final Option newpass =
                OptionBuilder.withLongOpt("new-password")
                        .withDescription("Use this option to specify the new password")
                        .hasArg0()
                        .create1('n');
        final String[] args = {"-o", "-n", "newpassword"};
        options.addOption0(oldpass);
    }

    @Test
    public void test13425_test10_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
        final Option newpass =
                OptionBuilder.withLongOpt("new-password")
                        .withDescription("Use this option to specify the new password")
                        .hasArg0()
                        .create1('n');
        final String[] args = {"-o", "-n", "newpassword"};
        options.addOption0(oldpass);
        options.addOption0(newpass);
    }

    @Test
    public void test13425_test11_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
        final Option newpass =
                OptionBuilder.withLongOpt("new-password")
                        .withDescription("Use this option to specify the new password")
                        .hasArg0()
                        .create1('n');
        final String[] args = {"-o", "-n", "newpassword"};
        options.addOption0(oldpass);
        options.addOption0(newpass);
        final Parser parser = new PosixParser();
    }

    @Test
    public void test13425_test12_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withLongOpt("old-password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password");
        OptionBuilder.withLongOpt("old-password").withDescription("Use this option to specify the old password").hasArg0();
        final Option oldpass =
                OptionBuilder.withLongOpt("old-password")
                        .withDescription("Use this option to specify the old password")
                        .hasArg0()
                        .create1('o');
        OptionBuilder.withLongOpt("new-password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password");
        OptionBuilder.withLongOpt("new-password").withDescription("Use this option to specify the new password").hasArg0();
        final Option newpass =
                OptionBuilder.withLongOpt("new-password")
                        .withDescription("Use this option to specify the new password")
                        .hasArg0()
                        .create1('n');
        final String[] args = {"-o", "-n", "newpassword"};
        options.addOption0(oldpass);
        options.addOption0(newpass);
        final Parser parser = new PosixParser();
        try {
            parser.parse0(options, args);
            fail("MissingArgumentException not caught.");
        } catch (final MissingArgumentException expected) {
        }
    }

    @Test
    public void test13666_test0_decomposed() throws Exception {
        final Options options = new Options();
    }

    @Test
    public void test13666_test1_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withDescription("dir");
    }

    @Test
    public void test13666_test2_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withDescription("dir");
        OptionBuilder.withDescription("dir").hasArg0();
    }

    @Test
    public void test13666_test3_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withDescription("dir");
        OptionBuilder.withDescription("dir").hasArg0();
        final Option dir = OptionBuilder.withDescription("dir").hasArg0().create1('d');
    }

    @Test
    public void test13666_test4_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withDescription("dir");
        OptionBuilder.withDescription("dir").hasArg0();
        final Option dir = OptionBuilder.withDescription("dir").hasArg0().create1('d');
        options.addOption0(dir);
    }

    @Test
    public void test13666_test5_decomposed() throws Exception {
        final Options options = new Options();
        OptionBuilder.withDescription("dir");
        OptionBuilder.withDescription("dir").hasArg0();
        final Option dir = OptionBuilder.withDescription("dir").hasArg0().create1('d');
        options.addOption0(dir);
        final PrintStream oldSystemOut = System.out;
        try {
            final ByteArrayOutputStream bytes = new ByteArrayOutputStream();
            final PrintStream print = new PrintStream(bytes);

            print.println();
            final String eol = bytes.toString();
            bytes.reset();

            System.setOut(new PrintStream(bytes));

            final HelpFormatter formatter = new HelpFormatter();
            formatter.printHelp4("dir", options);

            assertEquals("usage: dir" + eol + " -d <arg>   dir" + eol, bytes.toString());
        } finally {
            System.setOut(oldSystemOut);
        }
    }

    @Test
    public void test13935_test0_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
    }

    @Test
    public void test13935_test1_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
    }

    @Test
    public void test13935_test2_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
    }

    @Test
    public void test13935_test3_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
    }

    @Test
    public void test13935_test4_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
    }

    @Test
    public void test13935_test5_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
    }

    @Test
    public void test13935_test6_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
    }

    @Test
    public void test13935_test7_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
    }

    @Test
    public void test13935_test8_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
    }

    @Test
    public void test13935_test9_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
    }

    @Test
    public void test13935_test10_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
    }

    @Test
    public void test13935_test11_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test13935_test12_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
    }

    @Test
    public void test13935_test13_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s"};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
    }

    @Test
    public void test13935_test14_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s"};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s", "-l"};
        CommandLine line = parser.parse0(opts, args);
    }

    @Test
    public void test13935_test15_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s"};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s", "-l"};
        CommandLine line = parser.parse0(opts, args);
        assertNotNull(line);
        opts.addOption0(forward);
    }

    @Test
    public void test13935_test16_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s"};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s", "-l"};
        CommandLine line = parser.parse0(opts, args);
        assertNotNull(line);
        opts.addOption0(forward);
        args = new String[] {"-s", "-l", "-f"};
        line = parser.parse0(opts, args);
    }

    @Test
    public void test13935_test17_decomposed() throws Exception {
        final OptionGroup directions = new OptionGroup();
        final Option left = new Option(0, "l", "left", "go left", false, null);
        final Option right = new Option(0, "r", "right", "go right", false, null);
        final Option straight = new Option(0, "s", "straight", "go straight", false, null);
        final Option forward = new Option(0, "f", "forward", "go forward", false, null);
        forward.setRequired(true);
        directions.addOption(left);
        directions.addOption(right);
        directions.setRequired(true);
        final Options opts = new Options();
        opts.addOptionGroup(directions);
        opts.addOption0(straight);
        final CommandLineParser parser = new PosixParser();
        String[] args = {};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s"};
        try {
            parser.parse0(opts, args);
            fail("Expected ParseException");
        } catch (final ParseException expected) {
        }
        args = new String[] {"-s", "-l"};
        CommandLine line = parser.parse0(opts, args);
        assertNotNull(line);
        opts.addOption0(forward);
        args = new String[] {"-s", "-l", "-f"};
        line = parser.parse0(opts, args);
        assertNotNull(line);
    }

    @Test
    public void test14786_test0_decomposed() throws Exception {
        OptionBuilder.isRequired0();
    }

    @Test
    public void test14786_test1_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
    }

    @Test
    public void test14786_test2_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
    }

    @Test
    public void test14786_test3_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
        final Options opts = new Options();
    }

    @Test
    public void test14786_test4_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
        final Options opts = new Options();
        opts.addOption0(o);
        opts.addOption0(o);
    }

    @Test
    public void test14786_test5_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
        final Options opts = new Options();
        opts.addOption0(o);
        opts.addOption0(o);
        final CommandLineParser parser = new GnuParser();
    }

    @Test
    public void test14786_test6_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
        final Options opts = new Options();
        opts.addOption0(o);
        opts.addOption0(o);
        final CommandLineParser parser = new GnuParser();
        final String[] args = {"-test"};
        final CommandLine line = parser.parse0(opts, args);
    }

    @Test
    public void test14786_test7_decomposed() throws Exception {
        OptionBuilder.isRequired0();
        OptionBuilder.isRequired0().withDescription("test");
        final Option o = OptionBuilder.isRequired0().withDescription("test").create2("test");
        final Options opts = new Options();
        opts.addOption0(o);
        opts.addOption0(o);
        final CommandLineParser parser = new GnuParser();
        final String[] args = {"-test"};
        final CommandLine line = parser.parse0(opts, args);
        assertTrue(line.hasOption2("test"));
    }

    @Test
    public void test15046_test0_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test15046_test1_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
    }

    @Test
    public void test15046_test2_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
    }

    @Test
    public void test15046_test3_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
        parser.parse0(options, cliArgs);
    }

    @Test
    public void test15046_test4_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
        parser.parse0(options, cliArgs);
        options.addOption3("c", "conflict", true, "conflict option");
    }

    @Test
    public void test15046_test5_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
        parser.parse0(options, cliArgs);
        options.addOption3("c", "conflict", true, "conflict option");
        final CommandLine line = parser.parse0(options, cliArgs);
    }

    @Test
    public void test15046_test6_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
        parser.parse0(options, cliArgs);
        options.addOption3("c", "conflict", true, "conflict option");
        final CommandLine line = parser.parse0(options, cliArgs);
        assertEquals(line.getOptionValue0('z'), "c");
    }

    @Test
    public void test15046_test7_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] cliArgs = {"-z", "c"};
        final Options options = new Options();
        options.addOption0(new Option(0, "z", "timezone", "affected option", true, null));
        parser.parse0(options, cliArgs);
        options.addOption3("c", "conflict", true, "conflict option");
        final CommandLine line = parser.parse0(options, cliArgs);
        assertEquals(line.getOptionValue0('z'), "c");
        assertFalse(line.hasOption2("c"));
    }

    @Test
    public void test15648_test0_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void test15648_test1_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
    }

    @Test
    public void test15648_test2_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
        final Option m = OptionBuilder.hasArgs0().create2("m");
    }

    @Test
    public void test15648_test3_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
        final Option m = OptionBuilder.hasArgs0().create2("m");
        final Options options = new Options();
    }

    @Test
    public void test15648_test4_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
        final Option m = OptionBuilder.hasArgs0().create2("m");
        final Options options = new Options();
        options.addOption0(m);
    }

    @Test
    public void test15648_test5_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
        final Option m = OptionBuilder.hasArgs0().create2("m");
        final Options options = new Options();
        options.addOption0(m);
        final CommandLine line = parser.parse0(options, args);
    }

    @Test
    public void test15648_test6_decomposed() throws Exception {
        final CommandLineParser parser = new PosixParser();
        final String[] args = {"-m", "\"Two Words\""};
        OptionBuilder.hasArgs0();
        final Option m = OptionBuilder.hasArgs0().create2("m");
        final Options options = new Options();
        options.addOption0(m);
        final CommandLine line = parser.parse0(options, args);
        assertEquals("Two Words", line.getOptionValue4("m"));
    }

    @Test
    public void test31148_test0_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
    }

    @Test
    public void test31148_test1_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
    }

    @Test
    public void test31148_test2_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
    }

    @Test
    public void test31148_test3_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
        options.addOption0(multiArgOption);
    }

    @Test
    public void test31148_test4_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
        options.addOption0(multiArgOption);
        final Parser parser = new PosixParser();
    }

    @Test
    public void test31148_test5_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
        options.addOption0(multiArgOption);
        final Parser parser = new PosixParser();
        final String[] args = {};
        final Properties props = new Properties();
        props.setProperty("o", "ovalue");
        final CommandLine cl = parser.parse2(options, args, props);
    }

    @Test
    public void test31148_test6_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
        options.addOption0(multiArgOption);
        final Parser parser = new PosixParser();
        final String[] args = {};
        final Properties props = new Properties();
        props.setProperty("o", "ovalue");
        final CommandLine cl = parser.parse2(options, args, props);
        assertTrue(cl.hasOption0('o'));
    }

    @Test
    public void test31148_test7_decomposed() throws ParseException {
        final Option multiArgOption = Option.Option1("o", "option with multiple args");
        multiArgOption.setArgs(1);
        final Options options = new Options();
        options.addOption0(multiArgOption);
        final Parser parser = new PosixParser();
        final String[] args = {};
        final Properties props = new Properties();
        props.setProperty("o", "ovalue");
        final CommandLine cl = parser.parse2(options, args, props);
        assertTrue(cl.hasOption0('o'));
        assertEquals("ovalue", cl.getOptionValue0('o'));
    }
}