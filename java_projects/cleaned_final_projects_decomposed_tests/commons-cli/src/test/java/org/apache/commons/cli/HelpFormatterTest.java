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
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.Comparator;

/** Test case for the HelpFormatter class. */
public class HelpFormatterTest {
    private static final String EOL = System.getProperty("line.separator");

    @Test
    public void testAccessors_test0_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testAccessors_test1_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
    }

    @Test
    public void testAccessors_test2_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
    }

    @Test
    public void testAccessors_test3_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
    }

    @Test
    public void testAccessors_test4_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
    }

    @Test
    public void testAccessors_test5_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
    }

    @Test
    public void testAccessors_test6_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
    }

    @Test
    public void testAccessors_test7_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
    }

    @Test
    public void testAccessors_test8_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
    }

    @Test
    public void testAccessors_test9_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
    }

    @Test
    public void testAccessors_test10_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
    }

    @Test
    public void testAccessors_test11_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
    }

    @Test
    public void testAccessors_test12_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
        assertEquals("opt prefix", "~", formatter.getOptPrefix());
    }

    @Test
    public void testAccessors_test13_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
        assertEquals("opt prefix", "~", formatter.getOptPrefix());
        formatter.setSyntaxPrefix("-> ");
    }

    @Test
    public void testAccessors_test14_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
        assertEquals("opt prefix", "~", formatter.getOptPrefix());
        formatter.setSyntaxPrefix("-> ");
        assertEquals("syntax prefix", "-> ", formatter.getSyntaxPrefix());
    }

    @Test
    public void testAccessors_test15_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
        assertEquals("opt prefix", "~", formatter.getOptPrefix());
        formatter.setSyntaxPrefix("-> ");
        assertEquals("syntax prefix", "-> ", formatter.getSyntaxPrefix());
        formatter.setWidth(80);
    }

    @Test
    public void testAccessors_test16_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argname");
        assertEquals("arg name", "argname", formatter.getArgName());
        formatter.setDescPadding(3);
        assertEquals("desc padding", 3, formatter.getDescPadding());
        formatter.setLeftPadding(7);
        assertEquals("left padding", 7, formatter.getLeftPadding());
        formatter.setLongOptPrefix("~~");
        assertEquals("long opt prefix", "~~", formatter.getLongOptPrefix());
        formatter.setNewLine("\n");
        assertEquals("new line", "\n", formatter.getNewLine());
        formatter.setOptPrefix("~");
        assertEquals("opt prefix", "~", formatter.getOptPrefix());
        formatter.setSyntaxPrefix("-> ");
        assertEquals("syntax prefix", "-> ", formatter.getSyntaxPrefix());
        formatter.setWidth(80);
        assertEquals("width", 80, formatter.getWidth());
    }

    @Test
    public void testAutomaticUsage_test0_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
    }

    @Test
    public void testAutomaticUsage_test1_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
    }

    @Test
    public void testAutomaticUsage_test2_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
    }

    @Test
    public void testAutomaticUsage_test3_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
    }

    @Test
    public void testAutomaticUsage_test4_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
    }

    @Test
    public void testAutomaticUsage_test5_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
        expected = "usage: app [-a] [-b]";
        options =
                new Options()
                        .addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa")
                        .addOption1("b", false, "bbb");
    }

    @Test
    public void testAutomaticUsage_test6_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
        expected = "usage: app [-a] [-b]";
        options =
                new Options()
                        .addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa")
                        .addOption1("b", false, "bbb");
        hf.printUsage1(pw, 60, "app", options);
    }

    @Test
    public void testAutomaticUsage_test7_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
        expected = "usage: app [-a] [-b]";
        options =
                new Options()
                        .addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa")
                        .addOption1("b", false, "bbb");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
    }

    @Test
    public void testAutomaticUsage_test8_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        Options options;
        String expected = "usage: app [-a]";
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
        expected = "usage: app [-a] [-b]";
        options =
                new Options()
                        .addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa")
                        .addOption1("b", false, "bbb");
        hf.printUsage1(pw, 60, "app", options);
        pw.flush();
        assertEquals("simple auto usage", expected, out.toString().trim());
        out.reset();
    }

    @Test
    public void testDefaultArgName_test0_decomposed()  {
        Option.builder1("f");
    }

    @Test
    public void testDefaultArgName_test1_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
    }

    @Test
    public void testDefaultArgName_test2_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
    }

    @Test
    public void testDefaultArgName_test3_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
    }

    @Test
    public void testDefaultArgName_test4_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
    }

    @Test
    public void testDefaultArgName_test5_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
        options.addOption0(option);
    }

    @Test
    public void testDefaultArgName_test6_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testDefaultArgName_test7_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argument");
    }

    @Test
    public void testDefaultArgName_test8_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argument");
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
    }

    @Test
    public void testDefaultArgName_test9_decomposed()  {
        Option.builder1("f");
        Option.builder1("f").hasArg0();
        Option.builder1("f").hasArg0().required1(true);
        final Option option = Option.builder1("f").hasArg0().required1(true).build();
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setArgName("argument");
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
        assertEquals("usage: app -f <argument>" + EOL, out.toString());
    }

    @Test
    public void testFindWrapPos_test0_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
    }

    @Test
    public void testFindWrapPos_test1_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
    }

    @Test
    public void testFindWrapPos_test2_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
    }

    @Test
    public void testFindWrapPos_test3_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
        text = "aaaa aa";
        assertEquals("wrap position 3", 3, hf.findWrapPos(text, 3, 0));
    }

    @Test
    public void testFindWrapPos_test4_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
        text = "aaaa aa";
        assertEquals("wrap position 3", 3, hf.findWrapPos(text, 3, 0));
        text = "aaaaaa aaaaaa";
        assertEquals("wrap position 4", 6, hf.findWrapPos(text, 6, 0));
    }

    @Test
    public void testFindWrapPos_test5_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
        text = "aaaa aa";
        assertEquals("wrap position 3", 3, hf.findWrapPos(text, 3, 0));
        text = "aaaaaa aaaaaa";
        assertEquals("wrap position 4", 6, hf.findWrapPos(text, 6, 0));
        assertEquals("wrap position 4", -1, hf.findWrapPos(text, 6, 7));
    }

    @Test
    public void testFindWrapPos_test6_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
        text = "aaaa aa";
        assertEquals("wrap position 3", 3, hf.findWrapPos(text, 3, 0));
        text = "aaaaaa aaaaaa";
        assertEquals("wrap position 4", 6, hf.findWrapPos(text, 6, 0));
        assertEquals("wrap position 4", -1, hf.findWrapPos(text, 6, 7));
        text = "aaaaaa\n aaaaaa";
        assertEquals("wrap position 5", 7, hf.findWrapPos(text, 6, 0));
    }

    @Test
    public void testFindWrapPos_test7_decomposed()  {
        final HelpFormatter hf = new HelpFormatter();
        String text = "This is a test.";
        assertEquals("wrap position", 7, hf.findWrapPos(text, 8, 0));
        assertEquals("wrap position 2", -1, hf.findWrapPos(text, 8, 8));
        text = "aaaa aa";
        assertEquals("wrap position 3", 3, hf.findWrapPos(text, 3, 0));
        text = "aaaaaa aaaaaa";
        assertEquals("wrap position 4", 6, hf.findWrapPos(text, 6, 0));
        assertEquals("wrap position 4", -1, hf.findWrapPos(text, 6, 7));
        text = "aaaaaa\n aaaaaa";
        assertEquals("wrap position 5", 7, hf.findWrapPos(text, 6, 0));
        text = "aaaaaa\t aaaaaa";
        assertEquals("wrap position 6", 7, hf.findWrapPos(text, 6, 0));
    }

    @Test
    public void testHeaderStartingWithLineSeparator_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testHeaderStartingWithLineSeparator_test1_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testHeaderStartingWithLineSeparator_test2_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
        final String header = EOL + "Header";
        final String footer = "Footer";
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, true);
    }

    @Test
    public void testHeaderStartingWithLineSeparator_test3_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
        final String header = EOL + "Header";
        final String footer = "Footer";
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, true);
        assertEquals(
                "usage: foobar" + EOL + "" + EOL + "Header" + EOL + "" + EOL + "Footer" + EOL,
                out.toString());
    }

    @Test
    public void testHelpWithLongOptSeparator_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testHelpWithLongOptSeparator_test1_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
    }

    @Test
    public void testHelpWithLongOptSeparator_test2_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
    }

    @Test
    public void testHelpWithLongOptSeparator_test3_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
    }

    @Test
    public void testHelpWithLongOptSeparator_test4_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
    }

    @Test
    public void testHelpWithLongOptSeparator_test5_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
    }

    @Test
    public void testHelpWithLongOptSeparator_test6_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
    }

    @Test
    public void testHelpWithLongOptSeparator_test7_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
    }

    @Test
    public void testHelpWithLongOptSeparator_test8_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
    }

    @Test
    public void testHelpWithLongOptSeparator_test9_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
    }

    @Test
    public void testHelpWithLongOptSeparator_test10_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
    }

    @Test
    public void testHelpWithLongOptSeparator_test11_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
    }

    @Test
    public void testHelpWithLongOptSeparator_test12_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
    }

    @Test
    public void testHelpWithLongOptSeparator_test13_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
    }

    @Test
    public void testHelpWithLongOptSeparator_test14_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
    }

    @Test
    public void testHelpWithLongOptSeparator_test15_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testHelpWithLongOptSeparator_test16_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        assertEquals(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator());
    }

    @Test
    public void testHelpWithLongOptSeparator_test17_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        assertEquals(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator());
        formatter.setLongOptSeparator("=");
    }

    @Test
    public void testHelpWithLongOptSeparator_test18_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        assertEquals(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator());
        formatter.setLongOptSeparator("=");
        assertEquals("=", formatter.getLongOptSeparator());
    }

    @Test
    public void testHelpWithLongOptSeparator_test19_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        assertEquals(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator());
        formatter.setLongOptSeparator("=");
        assertEquals("=", formatter.getLongOptSeparator());
        final StringWriter out = new StringWriter();
        formatter.printHelp2(new PrintWriter(out), 80, "create", "header", options, 2, 2, "footer");
    }

    @Test
    public void testHelpWithLongOptSeparator_test20_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        assertEquals(HelpFormatter.DEFAULT_LONG_OPT_SEPARATOR, formatter.getLongOptSeparator());
        formatter.setLongOptSeparator("=");
        assertEquals("=", formatter.getLongOptSeparator());
        final StringWriter out = new StringWriter();
        formatter.printHelp2(new PrintWriter(out), 80, "create", "header", options, 2, 2, "footer");
        assertEquals(
                "usage: create"
                        + EOL
                        + "header"
                        + EOL
                        + "     --age=<arg>    the age"
                        + EOL
                        + "  -f <arg>          the file"
                        + EOL
                        + "  -s,--size=<SIZE>  the size"
                        + EOL
                        + "footer"
                        + EOL,
                out.toString());
    }

    @Test
    public void testIndentedHeaderAndFooter_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testIndentedHeaderAndFooter_test1_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testIndentedHeaderAndFooter_test2_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
        final String header = "  Header1\n  Header2";
        final String footer = "  Footer1\n  Footer2";
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, true);
    }

    @Test
    public void testIndentedHeaderAndFooter_test3_decomposed()  {
        final Options options = new Options();
        final HelpFormatter formatter = new HelpFormatter();
        final String header = "  Header1\n  Header2";
        final String footer = "  Footer1\n  Footer2";
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "foobar", header, options, 2, 2, footer, true);
        assertEquals(
                "usage: foobar"
                        + EOL
                        + "  Header1"
                        + EOL
                        + "  Header2"
                        + EOL
                        + ""
                        + EOL
                        + "  Footer1"
                        + EOL
                        + "  Footer2"
                        + EOL,
                out.toString());
    }

    @Test
    public void testOptionWithoutShortFormat_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testOptionWithoutShortFormat_test1_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
    }

    @Test
    public void testOptionWithoutShortFormat_test2_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(new Option(0, null, "bbb", "bbbbbbb", false, null));
    }

    @Test
    public void testOptionWithoutShortFormat_test3_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(new Option(0, null, "bbb", "bbbbbbb", false, null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
    }

    @Test
    public void testOptionWithoutShortFormat_test4_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(new Option(0, null, "bbb", "bbbbbbb", false, null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testOptionWithoutShortFormat_test5_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(new Option(0, null, "bbb", "bbbbbbb", false, null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
        final HelpFormatter formatter = new HelpFormatter();
        final StringWriter out = new StringWriter();
        formatter.printHelp3(new PrintWriter(out), 80, "foobar", "", options, 2, 2, "", true);
    }

    @Test
    public void testOptionWithoutShortFormat_test6_decomposed()  {
        final Options options = new Options();
        options.addOption0(new Option(0, "a", "aaa", "aaaaaaa", false, null));
        options.addOption0(new Option(0, null, "bbb", "bbbbbbb", false, null));
        options.addOption0(new Option(0, "c", null, "ccccccc", false, null));
        final HelpFormatter formatter = new HelpFormatter();
        final StringWriter out = new StringWriter();
        formatter.printHelp3(new PrintWriter(out), 80, "foobar", "", options, 2, 2, "", true);
        assertEquals(
                "usage: foobar [-a] [--bbb] [-c]"
                        + EOL
                        + "  -a,--aaa  aaaaaaa"
                        + EOL
                        + "     --bbb  bbbbbbb"
                        + EOL
                        + "  -c        ccccccc"
                        + EOL,
                out.toString());
    }

    @Test
    public void testOptionWithoutShortFormat2_test0_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
    }

    @Test
    public void testOptionWithoutShortFormat2_test1_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
    }

    @Test
    public void testOptionWithoutShortFormat2_test2_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
    }

    @Test
    public void testOptionWithoutShortFormat2_test3_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
    }

    @Test
    public void testOptionWithoutShortFormat2_test4_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
    }

    @Test
    public void testOptionWithoutShortFormat2_test5_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
    }

    @Test
    public void testOptionWithoutShortFormat2_test6_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test7_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test8_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
    }

    @Test
    public void testOptionWithoutShortFormat2_test9_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
    }

    @Test
    public void testOptionWithoutShortFormat2_test10_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
    }

    @Test
    public void testOptionWithoutShortFormat2_test11_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
    }

    @Test
    public void testOptionWithoutShortFormat2_test12_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test13_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test14_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
    }

    @Test
    public void testOptionWithoutShortFormat2_test15_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
    }

    @Test
    public void testOptionWithoutShortFormat2_test16_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
    }

    @Test
    public void testOptionWithoutShortFormat2_test17_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
    }

    @Test
    public void testOptionWithoutShortFormat2_test18_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test19_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test20_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
    }

    @Test
    public void testOptionWithoutShortFormat2_test21_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
    }

    @Test
    public void testOptionWithoutShortFormat2_test22_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
    }

    @Test
    public void testOptionWithoutShortFormat2_test23_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
    }

    @Test
    public void testOptionWithoutShortFormat2_test24_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test25_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test26_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
    }

    @Test
    public void testOptionWithoutShortFormat2_test27_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
    }

    @Test
    public void testOptionWithoutShortFormat2_test28_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test29_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
    }

    @Test
    public void testOptionWithoutShortFormat2_test30_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test31_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
    }

    @Test
    public void testOptionWithoutShortFormat2_test32_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
    }

    @Test
    public void testOptionWithoutShortFormat2_test33_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
    }

    @Test
    public void testOptionWithoutShortFormat2_test34_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
        final Options mOptions = new Options();
    }

    @Test
    public void testOptionWithoutShortFormat2_test35_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
        final Options mOptions = new Options();
        mOptions.addOption0(help);
        mOptions.addOption0(version);
        mOptions.addOption0(newRun);
        mOptions.addOption0(trackerRun);
        mOptions.addOption0(timeLimit);
        mOptions.addOption0(age);
        mOptions.addOption0(server);
        mOptions.addOption0(numResults);
        mOptions.addOption0(configFile);
    }

    @Test
    public void testOptionWithoutShortFormat2_test36_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
        final Options mOptions = new Options();
        mOptions.addOption0(help);
        mOptions.addOption0(version);
        mOptions.addOption0(newRun);
        mOptions.addOption0(trackerRun);
        mOptions.addOption0(timeLimit);
        mOptions.addOption0(age);
        mOptions.addOption0(server);
        mOptions.addOption0(numResults);
        mOptions.addOption0(configFile);
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testOptionWithoutShortFormat2_test37_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
        final Options mOptions = new Options();
        mOptions.addOption0(help);
        mOptions.addOption0(version);
        mOptions.addOption0(newRun);
        mOptions.addOption0(trackerRun);
        mOptions.addOption0(timeLimit);
        mOptions.addOption0(age);
        mOptions.addOption0(server);
        mOptions.addOption0(numResults);
        mOptions.addOption0(configFile);
        final HelpFormatter formatter = new HelpFormatter();
        final String eol = System.getProperty("line.separator");
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "commandline", "header", mOptions, 2, 2, "footer", true);
    }

    @Test
    public void testOptionWithoutShortFormat2_test38_decomposed()  {
        final Option help = new Option(0, "h", "help", "print this message", false, null);
        final Option version =
                new Option(0, "v", "version", "print version information", false, null);
        final Option newRun =
                new Option(
                        0, "n", "new", "Create NLT cache entries only for new items", false, null);
        final Option trackerRun =
                new Option(
                        0,
                        "t",
                        "tracker",
                        "Create NLT cache entries only for tracker items",
                        false,
                        null);
        Option.builder1("l");
        Option.builder1("l").longOpt("limit");
        Option.builder1("l").longOpt("limit").hasArg0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0();
        Option.builder1("l").longOpt("limit").hasArg0().valueSeparator0().desc("Set time limit for execution, in mintues");
        final Option timeLimit =
                Option.builder1("l")
                        .longOpt("limit")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Set time limit for execution, in mintues")
                        .build();
        Option.builder1("a");
        Option.builder1("a").longOpt("age");
        Option.builder1("a").longOpt("age").hasArg0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0();
        Option.builder1("a").longOpt("age").hasArg0().valueSeparator0().desc("Age (in days) of cache item before being recomputed");
        final Option age =
                Option.builder1("a")
                        .longOpt("age")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Age (in days) of cache item before being recomputed")
                        .build();
        Option.builder1("s");
        Option.builder1("s").longOpt("server");
        Option.builder1("s").longOpt("server").hasArg0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0();
        Option.builder1("s").longOpt("server").hasArg0().valueSeparator0().desc("The NLT server address");
        final Option server =
                Option.builder1("s")
                        .longOpt("server")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("The NLT server address")
                        .build();
        Option.builder1("r");
        Option.builder1("r").longOpt("results");
        Option.builder1("r").longOpt("results").hasArg0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0();
        Option.builder1("r").longOpt("results").hasArg0().valueSeparator0().desc("Number of results per item");
        final Option numResults =
                Option.builder1("r")
                        .longOpt("results")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Number of results per item")
                        .build();
        Option.builder0();
        Option.builder0().longOpt("config");
        Option.builder0().longOpt("config").hasArg0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0();
        Option.builder0().longOpt("config").hasArg0().valueSeparator0().desc("Use the specified configuration file");
        final Option configFile =
                Option.builder0()
                        .longOpt("config")
                        .hasArg0()
                        .valueSeparator0()
                        .desc("Use the specified configuration file")
                        .build();
        final Options mOptions = new Options();
        mOptions.addOption0(help);
        mOptions.addOption0(version);
        mOptions.addOption0(newRun);
        mOptions.addOption0(trackerRun);
        mOptions.addOption0(timeLimit);
        mOptions.addOption0(age);
        mOptions.addOption0(server);
        mOptions.addOption0(numResults);
        mOptions.addOption0(configFile);
        final HelpFormatter formatter = new HelpFormatter();
        final String eol = System.getProperty("line.separator");
        final StringWriter out = new StringWriter();
        formatter.printHelp3(
                new PrintWriter(out), 80, "commandline", "header", mOptions, 2, 2, "footer", true);
        assertEquals(
                "usage: commandline [-a <arg>] [--config <arg>] [-h] [-l <arg>] [-n] [-r <arg>]"
                        + eol
                        + "       [-s <arg>] [-t] [-v]"
                        + eol
                        + "header"
                        + eol
                        + "  -a,--age <arg>      Age (in days) of cache item before being"
                        + " recomputed"
                        + eol
                        + "     --config <arg>   Use the specified configuration file"
                        + eol
                        + "  -h,--help           print this message"
                        + eol
                        + "  -l,--limit <arg>    Set time limit for execution, in mintues"
                        + eol
                        + "  -n,--new            Create NLT cache entries only for new items"
                        + eol
                        + "  -r,--results <arg>  Number of results per item"
                        + eol
                        + "  -s,--server <arg>   The NLT server address"
                        + eol
                        + "  -t,--tracker        Create NLT cache entries only for tracker items"
                        + eol
                        + "  -v,--version        print version information"
                        + eol
                        + "footer"
                        + eol,
                out.toString());
    }

    @Test
    public void testPrintHelpNewlineFooter_test0_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintHelpNewlineFooter_test1_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
    }

    @Test
    public void testPrintHelpNewlineFooter_test2_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
    }

    @Test
    public void testPrintHelpNewlineFooter_test3_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
        formatter.printHelp2(pw, 80, "test" + EOL, "header" + EOL, options, 0, 0, EOL);
    }

    @Test
    public void testPrintHelpNewlineFooter_test4_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
        formatter.printHelp2(pw, 80, "test" + EOL, "header" + EOL, options, 0, 0, EOL);
        final String expected = "usage: test" + EOL + "header" + EOL + "-ab" + EOL + EOL;
        pw.flush();
        assertEquals("footer newline", expected, out.toString());
    }

    @Test
    public void testPrintHelpNewlineHeader_test0_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintHelpNewlineHeader_test1_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
    }

    @Test
    public void testPrintHelpNewlineHeader_test2_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
    }

    @Test
    public void testPrintHelpNewlineHeader_test3_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
        formatter.printHelp2(pw, 80, "test" + EOL, EOL, options, 0, 0, "footer" + EOL);
    }

    @Test
    public void testPrintHelpNewlineHeader_test4_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        final ByteArrayOutputStream out = new ByteArrayOutputStream();
        final PrintWriter pw = new PrintWriter(out);
        final Options options = new Options();
        options.addOption2("a", "b");
        formatter.printHelp2(pw, 80, "test" + EOL, EOL, options, 0, 0, "footer" + EOL);
        final String expected = "usage: test" + EOL + EOL + "-ab" + EOL + "footer" + EOL;
        pw.flush();
        assertEquals("header newline", expected, out.toString());
    }

    @Test
    public void testPrintHelpWithEmptySyntax_test0_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintHelpWithEmptySyntax_test1_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        try {
            formatter.printHelp4(null, new Options());
            fail("null command line syntax should be rejected");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testPrintHelpWithEmptySyntax_test2_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        try {
            formatter.printHelp4(null, new Options());
            fail("null command line syntax should be rejected");
        } catch (final IllegalArgumentException e) {
        }
        try {
            formatter.printHelp4("", new Options());
            fail("empty command line syntax should be rejected");
        } catch (final IllegalArgumentException e) {
        }
    }

    @Test
    public void testPrintOptionGroupUsage_test0_decomposed()  {
        final OptionGroup group = new OptionGroup();
    }

    @Test
    public void testPrintOptionGroupUsage_test1_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
    }

    @Test
    public void testPrintOptionGroupUsage_test2_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
    }

    @Test
    public void testPrintOptionGroupUsage_test3_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
    }

    @Test
    public void testPrintOptionGroupUsage_test4_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
    }

    @Test
    public void testPrintOptionGroupUsage_test5_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
    }

    @Test
    public void testPrintOptionGroupUsage_test6_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
    }

    @Test
    public void testPrintOptionGroupUsage_test7_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
    }

    @Test
    public void testPrintOptionGroupUsage_test8_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
    }

    @Test
    public void testPrintOptionGroupUsage_test9_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
    }

    @Test
    public void testPrintOptionGroupUsage_test10_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        final Options options = new Options();
    }

    @Test
    public void testPrintOptionGroupUsage_test11_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        final Options options = new Options();
        options.addOptionGroup(group);
    }

    @Test
    public void testPrintOptionGroupUsage_test12_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintOptionGroupUsage_test13_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
    }

    @Test
    public void testPrintOptionGroupUsage_test14_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
        assertEquals("usage: app [-a | -b | -c]" + EOL, out.toString());
    }

    @Test
    public void testPrintOptions_test0_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
    }

    @Test
    public void testPrintOptions_test1_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
    }

    @Test
    public void testPrintOptions_test2_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
    }

    @Test
    public void testPrintOptions_test3_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
    }

    @Test
    public void testPrintOptions_test4_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
    }

    @Test
    public void testPrintOptions_test5_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
    }

    @Test
    public void testPrintOptions_test6_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
    }

    @Test
    public void testPrintOptions_test7_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
    }

    @Test
    public void testPrintOptions_test8_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
    }

    @Test
    public void testPrintOptions_test9_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
    }

    @Test
    public void testPrintOptions_test10_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
    }

    @Test
    public void testPrintOptions_test11_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
    }

    @Test
    public void testPrintOptions_test12_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
    }

    @Test
    public void testPrintOptions_test13_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
    }

    @Test
    public void testPrintOptions_test14_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
    }

    @Test
    public void testPrintOptions_test15_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
        new Options().addOption3("a","aaa",false,"dddd dddd dddd dddd");
    }

    @Test
    public void testPrintOptions_test16_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
        new Options().addOption3("a","aaa",false,"dddd dddd dddd dddd");
        options =
                new Options()
                        .addOption3("a", "aaa", false, "dddd dddd dddd dddd")
                        .addOption1("b", false, "feeee eeee eeee eeee");
    }

    @Test
    public void testPrintOptions_test17_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
        new Options().addOption3("a","aaa",false,"dddd dddd dddd dddd");
        options =
                new Options()
                        .addOption3("a", "aaa", false, "dddd dddd dddd dddd")
                        .addOption1("b", false, "feeee eeee eeee eeee");
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd"
                        + EOL
                        + lpad
                        + "-b      "
                        + dpad
                        + "feeee eeee"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "eeee eeee";
    }

    @Test
    public void testPrintOptions_test18_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
        new Options().addOption3("a","aaa",false,"dddd dddd dddd dddd");
        options =
                new Options()
                        .addOption3("a", "aaa", false, "dddd dddd dddd dddd")
                        .addOption1("b", false, "feeee eeee eeee eeee");
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd"
                        + EOL
                        + lpad
                        + "-b      "
                        + dpad
                        + "feeee eeee"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "eeee eeee";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
    }

    @Test
    public void testPrintOptions_test19_decomposed()  {
        final StringBuffer sb = new StringBuffer();
        final HelpFormatter hf = new HelpFormatter();
        final int leftPad = 1;
        final int descPad = 3;
        final String lpad = hf.createPadding(leftPad);
        final String dpad = hf.createPadding(descPad);
        Options options;
        String expected;
        options = new Options().addOption1("a", false, "aaaa aaaa aaaa aaaa aaaa");
        expected = lpad + "-a" + dpad + "aaaa aaaa aaaa aaaa aaaa";
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("simple non-wrapped option", expected, sb.toString());
        int nextLineTabStop = leftPad + descPad + "-a".length();
        expected =
                lpad
                        + "-a"
                        + dpad
                        + "aaaa aaaa aaaa"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "aaaa aaaa";
        sb.setLength(0);
        hf.renderOptions(sb, nextLineTabStop + 17, options, leftPad, descPad);
        assertEquals("simple wrapped option", expected, sb.toString());
        options = new Options().addOption3("a", "aaa", false, "dddd dddd dddd dddd");
        expected = lpad + "-a,--aaa" + dpad + "dddd dddd dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 60, options, leftPad, descPad);
        assertEquals("long non-wrapped option", expected, sb.toString());
        nextLineTabStop = leftPad + descPad + "-a,--aaa".length();
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("long wrapped option", expected, sb.toString());
        new Options().addOption3("a","aaa",false,"dddd dddd dddd dddd");
        options =
                new Options()
                        .addOption3("a", "aaa", false, "dddd dddd dddd dddd")
                        .addOption1("b", false, "feeee eeee eeee eeee");
        expected =
                lpad
                        + "-a,--aaa"
                        + dpad
                        + "dddd dddd"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "dddd dddd"
                        + EOL
                        + lpad
                        + "-b      "
                        + dpad
                        + "feeee eeee"
                        + EOL
                        + hf.createPadding(nextLineTabStop)
                        + "eeee eeee";
        sb.setLength(0);
        hf.renderOptions(sb, 25, options, leftPad, descPad);
        assertEquals("multiple wrapped options", expected, sb.toString());
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test0_decomposed()  {
        final Option option = Option.Option2("f", true, null);
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test1_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test2_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test3_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
        final Options options = new Options();
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test4_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
        final Options options = new Options();
        options.addOption0(option);
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test5_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test6_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
    }

    @Test
    public void testPrintOptionWithEmptyArgNameUsage_test7_decomposed()  {
        final Option option = Option.Option2("f", true, null);
        option.setArgName("");
        option.setRequired(true);
        final Options options = new Options();
        options.addOption0(option);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
        assertEquals("usage: app -f" + EOL, out.toString());
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test0_decomposed()  {
        final OptionGroup group = new OptionGroup();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test1_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test2_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test3_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test4_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test5_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test6_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test7_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test8_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test9_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test10_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test11_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
        final Options options = new Options();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test12_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
        final Options options = new Options();
        options.addOptionGroup(group);
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test13_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test14_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
    }

    @Test
    public void testPrintRequiredOptionGroupUsage_test15_decomposed()  {
        final OptionGroup group = new OptionGroup();
        Option.builder1("a");
        Option.builder1("a").build();
        group.addOption(Option.builder1("a").build());
        Option.builder1("b");
        Option.builder1("b").build();
        group.addOption(Option.builder1("b").build());
        Option.builder1("c");
        Option.builder1("c").build();
        group.addOption(Option.builder1("c").build());
        group.setRequired(true);
        final Options options = new Options();
        options.addOptionGroup(group);
        final StringWriter out = new StringWriter();
        final HelpFormatter formatter = new HelpFormatter();
        formatter.printUsage1(new PrintWriter(out), 80, "app", options);
        assertEquals("usage: app -a | -b | -c" + EOL, out.toString());
    }

    @Test
    public void testPrintSortedUsage_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testPrintSortedUsage_test1_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
    }

    @Test
    public void testPrintSortedUsage_test2_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
    }

    @Test
    public void testPrintSortedUsage_test3_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
    }

    @Test
    public void testPrintSortedUsage_test4_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
    }

    @Test
    public void testPrintSortedUsage_test5_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
    }

    @Test
    public void testPrintSortedUsage_test6_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
        opts.addOption0(Option.Option1("c", "third"));
    }

    @Test
    public void testPrintSortedUsage_test7_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
        opts.addOption0(Option.Option1("c", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
    }

    @Test
    public void testPrintSortedUsage_test8_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
        opts.addOption0(Option.Option1("c", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(
                new Comparator<Option>() {
                    @Override
                    public int compare(final Option opt1, final Option opt2) {
                        return opt2.getKey().compareToIgnoreCase(opt1.getKey());
                    }
                });
    }

    @Test
    public void testPrintSortedUsage_test9_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
        opts.addOption0(Option.Option1("c", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(
                new Comparator<Option>() {
                    @Override
                    public int compare(final Option opt1, final Option opt2) {
                        return opt2.getKey().compareToIgnoreCase(opt1.getKey());
                    }
                });
        final StringWriter out = new StringWriter();
        helpFormatter.printUsage1(new PrintWriter(out), 80, "app", opts);
    }

    @Test
    public void testPrintSortedUsage_test10_decomposed()  {
        final Options opts = new Options();
        Option.Option1("a","first");
        opts.addOption0(Option.Option1("a", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("c","third");
        opts.addOption0(Option.Option1("c", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(
                new Comparator<Option>() {
                    @Override
                    public int compare(final Option opt1, final Option opt2) {
                        return opt2.getKey().compareToIgnoreCase(opt1.getKey());
                    }
                });
        final StringWriter out = new StringWriter();
        helpFormatter.printUsage1(new PrintWriter(out), 80, "app", opts);
        assertEquals("usage: app [-c] [-b] [-a]" + EOL, out.toString());
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test0_decomposed()  {
        final Options opts = new Options();
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test1_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test2_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test3_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test4_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test5_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test6_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
        opts.addOption0(Option.Option1("a", "third"));
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test7_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
        opts.addOption0(Option.Option1("a", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test8_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
        opts.addOption0(Option.Option1("a", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(null);
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test9_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
        opts.addOption0(Option.Option1("a", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(null);
        final StringWriter out = new StringWriter();
        helpFormatter.printUsage1(new PrintWriter(out), 80, "app", opts);
    }

    @Test
    public void testPrintSortedUsageWithNullComparator_test10_decomposed()  {
        final Options opts = new Options();
        Option.Option1("c","first");
        opts.addOption0(Option.Option1("c", "first"));
        Option.Option1("b","second");
        opts.addOption0(Option.Option1("b", "second"));
        Option.Option1("a","third");
        opts.addOption0(Option.Option1("a", "third"));
        final HelpFormatter helpFormatter = new HelpFormatter();
        helpFormatter.setOptionComparator(null);
        final StringWriter out = new StringWriter();
        helpFormatter.printUsage1(new PrintWriter(out), 80, "app", opts);
        assertEquals("usage: app [-c] [-b] [-a]" + EOL, out.toString());
    }

    @Test
    public void testPrintUsage_test0_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
    }

    @Test
    public void testPrintUsage_test1_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
        final Options opts = new Options();
    }

    @Test
    public void testPrintUsage_test2_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
        final Options opts = new Options();
        opts.addOption0(optionA);
        opts.addOption0(optionB);
        opts.addOption0(optionC);
    }

    @Test
    public void testPrintUsage_test3_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
        final Options opts = new Options();
        opts.addOption0(optionA);
        opts.addOption0(optionB);
        opts.addOption0(optionC);
        final HelpFormatter helpFormatter = new HelpFormatter();
    }

    @Test
    public void testPrintUsage_test4_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
        final Options opts = new Options();
        opts.addOption0(optionA);
        opts.addOption0(optionB);
        opts.addOption0(optionC);
        final HelpFormatter helpFormatter = new HelpFormatter();
        final ByteArrayOutputStream bytesOut = new ByteArrayOutputStream();
        try (PrintWriter printWriter = new PrintWriter(bytesOut)) {
            helpFormatter.printUsage1(printWriter, 80, "app", opts);
        }
    }

    @Test
    public void testPrintUsage_test5_decomposed()  {
        final Option optionA = Option.Option1("a", "first");
        final Option optionB = Option.Option1("b", "second");
        final Option optionC = Option.Option1("c", "third");
        final Options opts = new Options();
        opts.addOption0(optionA);
        opts.addOption0(optionB);
        opts.addOption0(optionC);
        final HelpFormatter helpFormatter = new HelpFormatter();
        final ByteArrayOutputStream bytesOut = new ByteArrayOutputStream();
        try (PrintWriter printWriter = new PrintWriter(bytesOut)) {
            helpFormatter.printUsage1(printWriter, 80, "app", opts);
        }
        assertEquals("usage: app [-a] [-b] [-c]" + EOL, bytesOut.toString());
    }

    @Test
    public void testRenderWrappedTextMultiLine_test0_decomposed()  {
        final int width = 16;
        final int padding = 0;
        final String expected = "aaaa aaaa aaaa" + EOL + "aaaaaa" + EOL + "aaaaa";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, expected);
    }

    @Test
    public void testRenderWrappedTextMultiLine_test1_decomposed()  {
        final int width = 16;
        final int padding = 0;
        final String expected = "aaaa aaaa aaaa" + EOL + "aaaaaa" + EOL + "aaaaa";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, expected);
        assertEquals("multi line text", expected, sb.toString());
    }

    @Test
    public void testRenderWrappedTextMultiLinePadded_test0_decomposed()  {
        final int width = 16;
        final int padding = 4;
        final String text = "aaaa aaaa aaaa" + EOL + "aaaaaa" + EOL + "aaaaa";
        final String expected = "aaaa aaaa aaaa" + EOL + "    aaaaaa" + EOL + "    aaaaa";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
    }

    @Test
    public void testRenderWrappedTextMultiLinePadded_test1_decomposed()  {
        final int width = 16;
        final int padding = 4;
        final String text = "aaaa aaaa aaaa" + EOL + "aaaaaa" + EOL + "aaaaa";
        final String expected = "aaaa aaaa aaaa" + EOL + "    aaaaaa" + EOL + "    aaaaa";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
        assertEquals("multi-line padded text", expected, sb.toString());
    }

    @Test
    public void testRenderWrappedTextSingleLine_test0_decomposed()  {
        final int width = 12;
        final int padding = 0;
        final String text = "This is a test.";
        final String expected = "This is a" + EOL + "test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
    }

    @Test
    public void testRenderWrappedTextSingleLine_test1_decomposed()  {
        final int width = 12;
        final int padding = 0;
        final String text = "This is a test.";
        final String expected = "This is a" + EOL + "test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
        assertEquals("single line text", expected, sb.toString());
    }

    @Test
    public void testRenderWrappedTextSingleLinePadded_test0_decomposed()  {
        final int width = 12;
        final int padding = 4;
        final String text = "This is a test.";
        final String expected = "This is a" + EOL + "    test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
    }

    @Test
    public void testRenderWrappedTextSingleLinePadded_test1_decomposed()  {
        final int width = 12;
        final int padding = 4;
        final String text = "This is a test.";
        final String expected = "This is a" + EOL + "    test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
        assertEquals("single line padded text", expected, sb.toString());
    }

    @Test
    public void testRenderWrappedTextSingleLinePadded2_test0_decomposed()  {
        final int width = 53;
        final int padding = 24;
        final String text =
                "  -p,--period <PERIOD>  PERIOD is time duration of form "
                        + "DATE[-DATE] where DATE has form YYYY[MM[DD]]";
        final String expected =
                "  -p,--period <PERIOD>  PERIOD is time duration of"
                        + EOL
                        + "                        form DATE[-DATE] where DATE"
                        + EOL
                        + "                        has form YYYY[MM[DD]]";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
    }

    @Test
    public void testRenderWrappedTextSingleLinePadded2_test1_decomposed()  {
        final int width = 53;
        final int padding = 24;
        final String text =
                "  -p,--period <PERIOD>  PERIOD is time duration of form "
                        + "DATE[-DATE] where DATE has form YYYY[MM[DD]]";
        final String expected =
                "  -p,--period <PERIOD>  PERIOD is time duration of"
                        + EOL
                        + "                        form DATE[-DATE] where DATE"
                        + EOL
                        + "                        has form YYYY[MM[DD]]";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
        assertEquals("single line padded text 2", expected, sb.toString());
    }

    @Test
    public void testRenderWrappedTextWordCut_test0_decomposed()  {
        final int width = 7;
        final int padding = 0;
        final String text = "Thisisatest.";
        final String expected = "Thisisa" + EOL + "test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
    }

    @Test
    public void testRenderWrappedTextWordCut_test1_decomposed()  {
        final int width = 7;
        final int padding = 0;
        final String text = "Thisisatest.";
        final String expected = "Thisisa" + EOL + "test.";
        final StringBuffer sb = new StringBuffer();
        new HelpFormatter().renderWrappedText(sb, width, padding, text);
        assertEquals("cut and wrap", expected, sb.toString());
    }

    @Test
    public void testRtrim_test0_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testRtrim_test1_decomposed()  {
        final HelpFormatter formatter = new HelpFormatter();
        assertNull(formatter.rtrim(null));
        assertEquals("", formatter.rtrim(""));
        assertEquals("  foo", formatter.rtrim("  foo  "));
    }

    @Test
    public void testUsageWithLongOptSeparator_test0_decomposed()  {
        final Options options = new Options();
    }

    @Test
    public void testUsageWithLongOptSeparator_test1_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
    }

    @Test
    public void testUsageWithLongOptSeparator_test2_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
    }

    @Test
    public void testUsageWithLongOptSeparator_test3_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
    }

    @Test
    public void testUsageWithLongOptSeparator_test4_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
    }

    @Test
    public void testUsageWithLongOptSeparator_test5_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
    }

    @Test
    public void testUsageWithLongOptSeparator_test6_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
    }

    @Test
    public void testUsageWithLongOptSeparator_test7_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
    }

    @Test
    public void testUsageWithLongOptSeparator_test8_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
    }

    @Test
    public void testUsageWithLongOptSeparator_test9_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
    }

    @Test
    public void testUsageWithLongOptSeparator_test10_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
    }

    @Test
    public void testUsageWithLongOptSeparator_test11_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
    }

    @Test
    public void testUsageWithLongOptSeparator_test12_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
    }

    @Test
    public void testUsageWithLongOptSeparator_test13_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
    }

    @Test
    public void testUsageWithLongOptSeparator_test14_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
    }

    @Test
    public void testUsageWithLongOptSeparator_test15_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
    }

    @Test
    public void testUsageWithLongOptSeparator_test16_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setLongOptSeparator("=");
    }

    @Test
    public void testUsageWithLongOptSeparator_test17_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setLongOptSeparator("=");
        final StringWriter out = new StringWriter();
        formatter.printUsage1(new PrintWriter(out), 80, "create", options);
    }

    @Test
    public void testUsageWithLongOptSeparator_test18_decomposed()  {
        final Options options = new Options();
        options.addOption1("f", true, "the file");
        Option.builder1("s");
        Option.builder1("s").longOpt("size");
        Option.builder1("s").longOpt("size").desc("the size");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0();
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE");
        Option.builder1("s").longOpt("size").desc("the size").hasArg0().argName("SIZE").build();
        options.addOption0(
                Option.builder1("s")
                        .longOpt("size")
                        .desc("the size")
                        .hasArg0()
                        .argName("SIZE")
                        .build());
        Option.builder0();
        Option.builder0().longOpt("age");
        Option.builder0().longOpt("age").desc("the age");
        Option.builder0().longOpt("age").desc("the age").hasArg0();
        Option.builder0().longOpt("age").desc("the age").hasArg0().build();
        options.addOption0(Option.builder0().longOpt("age").desc("the age").hasArg0().build());
        final HelpFormatter formatter = new HelpFormatter();
        formatter.setLongOptSeparator("=");
        final StringWriter out = new StringWriter();
        formatter.printUsage1(new PrintWriter(out), 80, "create", options);
        assertEquals("usage: create [--age=<arg>] [-f <arg>] [-s <SIZE>]", out.toString().trim());
    }
}