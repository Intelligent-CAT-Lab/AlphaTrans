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
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.io.File;
import java.io.FileInputStream;
import java.net.URL;
import java.util.Calendar;
import java.util.Date;
import java.util.Vector;

/** Test case for the PatternOptionBuilder class. */
@SuppressWarnings("deprecation") // tests some deprecated classes
public class PatternOptionBuilderTest {

    @Test
    public void testClassPattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("c+d+");
    }

    @Test
    public void testClassPattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("c+d+");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testClassPattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("c+d+");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {"-c", "java.util.Calendar", "-d", "System.DateTime"});
    }

    @Test
    public void testClassPattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("c+d+");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {"-c", "java.util.Calendar", "-d", "System.DateTime"});
        assertEquals("c value", Calendar.class, line.getOptionObject1("c"));
        assertNull("d value", line.getOptionObject1("d"));
    }

    @Test
    public void testEmptyPattern_test0_decomposed()  {
        final Options options = PatternOptionBuilder.parsePattern("");
    }

    @Test
    public void testEmptyPattern_test1_decomposed()  {
        final Options options = PatternOptionBuilder.parsePattern("");
        assertTrue(options.getOptions().isEmpty());
    }

    @Test
    public void testExistingFilePattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("g<");
    }

    @Test
    public void testExistingFilePattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("g<");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testExistingFilePattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("g<");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"
                        });
    }

    @Test
    public void testExistingFilePattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("g<");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"
                        });
        final Object parsedReadableFileStream = line.getOptionObject1("g");
    }

    @Test
    public void testExistingFilePattern_test4_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("g<");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-g", "src/test/resources/org/apache/commons/cli/existing-readable.file"
                        });
        final Object parsedReadableFileStream = line.getOptionObject1("g");
        assertNotNull("option g not parsed", parsedReadableFileStream);
        assertTrue(
                "option g not FileInputStream",
                parsedReadableFileStream instanceof FileInputStream);
    }

    @Test
    public void testExistingFilePatternFileNotExist_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("f<");
    }

    @Test
    public void testExistingFilePatternFileNotExist_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("f<");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testExistingFilePatternFileNotExist_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("f<");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-f", "non-existing.file"});
    }

    @Test
    public void testExistingFilePatternFileNotExist_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("f<");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-f", "non-existing.file"});
        assertNull("option f parsed", line.getOptionObject1("f"));
    }

    @Test
    public void testNumberPattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("n%d%x%");
    }

    @Test
    public void testNumberPattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("n%d%x%");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testNumberPattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("n%d%x%");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(options, new String[] {"-n", "1", "-d", "2.1", "-x", "3,5"});
    }

    @Test
    public void testNumberPattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("n%d%x%");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(options, new String[] {"-n", "1", "-d", "2.1", "-x", "3,5"});
        assertEquals("n object class", Long.class, line.getOptionObject1("n").getClass());
        assertEquals("n value", Long.valueOf(1), line.getOptionObject1("n"));
        assertEquals("d object class", Double.class, line.getOptionObject1("d").getClass());
        assertEquals("d value", Double.valueOf(2.1), line.getOptionObject1("d"));
        assertNull("x object", line.getOptionObject1("x"));
    }

    @Test
    public void testObjectPattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("o@i@n@");
    }

    @Test
    public void testObjectPattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("o@i@n@");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testObjectPattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("o@i@n@");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-o",
                            "java.lang.String",
                            "-i",
                            "java.util.Calendar",
                            "-n",
                            "System.DateTime"
                        });
    }

    @Test
    public void testObjectPattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("o@i@n@");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-o",
                            "java.lang.String",
                            "-i",
                            "java.util.Calendar",
                            "-n",
                            "System.DateTime"
                        });
        assertEquals("o value", "", line.getOptionObject1("o"));
        assertNull("i value", line.getOptionObject1("i"));
        assertNull("n value", line.getOptionObject1("n"));
    }

    @Test
    public void testRequiredOption_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("!n%m%");
    }

    @Test
    public void testRequiredOption_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("!n%m%");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testRequiredOption_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("!n%m%");
        final CommandLineParser parser = new PosixParser();
        try {
            parser.parse0(options, new String[] {""});
            fail("MissingOptionException wasn't thrown");
        } catch (final MissingOptionException e) {
            assertEquals(1, e.getMissingOptions().size());
            assertTrue(e.getMissingOptions().contains("n"));
        }
    }

    @Test
    public void testSimplePattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
    }

    @Test
    public void testSimplePattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testSimplePattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
    }

    @Test
    public void testSimplePattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
    }

    @Test
    public void testSimplePattern_test4_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
    }

    @Test
    public void testSimplePattern_test5_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
    }

    @Test
    public void testSimplePattern_test6_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject1("e"));
        assertEquals("class flag f", Calendar.class, line.getOptionObject1("f"));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject1("n"));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject1("t"));
    }

    @Test
    public void testSimplePattern_test7_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject1("e"));
        assertEquals("class flag f", Calendar.class, line.getOptionObject1("f"));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject1("n"));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject1("t"));
        assertEquals("flag a", "foo", line.getOptionValue0('a'));
    }

    @Test
    public void testSimplePattern_test8_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject1("e"));
        assertEquals("class flag f", Calendar.class, line.getOptionObject1("f"));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject1("n"));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject1("t"));
        assertEquals("flag a", "foo", line.getOptionValue0('a'));
        assertEquals("string flag a", "foo", line.getOptionObject0('a'));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject0('b'));
    }

    @Test
    public void testSimplePattern_test9_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject1("e"));
        assertEquals("class flag f", Calendar.class, line.getOptionObject1("f"));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject1("n"));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject1("t"));
        assertEquals("flag a", "foo", line.getOptionValue0('a'));
        assertEquals("string flag a", "foo", line.getOptionObject0('a'));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject0('b'));
        assertTrue("boolean true flag c", line.hasOption0('c'));
        assertFalse("boolean false flag d", line.hasOption0('d'));
    }

    @Test
    public void testSimplePattern_test10_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("a:b@cde>f+n%t/m*z#");
        final String[] args = {
            "-c",
            "-a",
            "foo",
            "-b",
            "java.util.Vector",
            "-e",
            "build.xml",
            "-f",
            "java.util.Calendar",
            "-n",
            "4.5",
            "-t",
            "https://commons.apache.org",
            "-z",
            "Thu Jun 06 17:48:57 EDT 2002",
            "-m",
            "test*"
        };
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, args);
        assertEquals("flag a", "foo", line.getOptionValue4("a"));
        assertEquals("string flag a", "foo", line.getOptionObject1("a"));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject1("b"));
        assertTrue("boolean true flag c", line.hasOption2("c"));
        assertFalse("boolean false flag d", line.hasOption2("d"));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject1("e"));
        assertEquals("class flag f", Calendar.class, line.getOptionObject1("f"));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject1("n"));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject1("t"));
        assertEquals("flag a", "foo", line.getOptionValue0('a'));
        assertEquals("string flag a", "foo", line.getOptionObject0('a'));
        assertEquals("object flag b", new Vector<>(), line.getOptionObject0('b'));
        assertTrue("boolean true flag c", line.hasOption0('c'));
        assertFalse("boolean false flag d", line.hasOption0('d'));
        assertEquals("file flag e", new File("build.xml"), line.getOptionObject0('e'));
        assertEquals("class flag f", Calendar.class, line.getOptionObject0('f'));
        assertEquals("number flag n", Double.valueOf(4.5), line.getOptionObject0('n'));
        assertEquals(
                "url flag t", new URL("https://commons.apache.org"), line.getOptionObject0('t'));
        try {
            assertEquals("files flag m", new File[0], line.getOptionObject0('m'));
            fail("Multiple files are not supported yet, should have failed");
        } catch (final UnsupportedOperationException uoe) {
        }
        try {
            assertEquals("date flag z", new Date(1023400137276L), line.getOptionObject0('z'));
            fail("Date is not supported yet, should have failed");
        } catch (final UnsupportedOperationException uoe) {
        }
    }

    @Test
    public void testUntypedPattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
    }

    @Test
    public void testUntypedPattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testUntypedPattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
    }

    @Test
    public void testUntypedPattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
    }

    @Test
    public void testUntypedPattern_test4_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
        assertNull("value a", line.getOptionObject0('a'));
    }

    @Test
    public void testUntypedPattern_test5_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
        assertNull("value a", line.getOptionObject0('a'));
        assertTrue(line.hasOption0('b'));
    }

    @Test
    public void testUntypedPattern_test6_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
        assertNull("value a", line.getOptionObject0('a'));
        assertTrue(line.hasOption0('b'));
        assertNull("value b", line.getOptionObject0('b'));
    }

    @Test
    public void testUntypedPattern_test7_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
        assertNull("value a", line.getOptionObject0('a'));
        assertTrue(line.hasOption0('b'));
        assertNull("value b", line.getOptionObject0('b'));
        assertTrue(line.hasOption0('c'));
    }

    @Test
    public void testUntypedPattern_test8_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("abc");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line = parser.parse0(options, new String[] {"-abc"});
        assertTrue(line.hasOption0('a'));
        assertNull("value a", line.getOptionObject0('a'));
        assertTrue(line.hasOption0('b'));
        assertNull("value b", line.getOptionObject0('b'));
        assertTrue(line.hasOption0('c'));
        assertNull("value c", line.getOptionObject0('c'));
    }

    @Test
    public void testURLPattern_test0_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("u/v/");
    }

    @Test
    public void testURLPattern_test1_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("u/v/");
        final CommandLineParser parser = new PosixParser();
    }

    @Test
    public void testURLPattern_test2_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("u/v/");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"
                        });
    }

    @Test
    public void testURLPattern_test3_decomposed() throws Exception {
        final Options options = PatternOptionBuilder.parsePattern("u/v/");
        final CommandLineParser parser = new PosixParser();
        final CommandLine line =
                parser.parse0(
                        options,
                        new String[] {
                            "-u", "https://commons.apache.org", "-v", "foo://commons.apache.org"
                        });
        assertEquals("u value", new URL("https://commons.apache.org"), line.getOptionObject1("u"));
        assertNull("v value", line.getOptionObject1("v"));
    }
}