/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.apache.commons.exec;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import java.io.File;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.exec.util.StringUtils;
import org.junit.jupiter.api.Test;

/**
 */
public class CommandLineTest {

    

    

    

    

    

    

    

    

    

    

    

    

    /**
     * A little example how to add two command line arguments in one line, e.g. to make commenting out some options less error prone.
     */
    

    /**
     * Test expanding the command line based on a user-supplied map.
     */
    

    /**
     * Test expanding the command line based on a user-supplied map. The main goal of the test is to setup a command line using macros and reuse it multiple
     * times.
     */
    

    

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\""
     */
    

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\""
     */
    

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\"" Please not that we re forced to add additional single quotes to get the test working - don't know if this is a bug or a
     * feature.
     */
    

    

    

    

    

    

    

    

    

    

    

    /**
     * A command line parsing puzzle from Tino Schoellhorn - ImageMagix expects a "500x>" parameter (including quotes) and it is simply not possible to do that
     * without adding a space, e.g. "500x> ".
     */
    

    /**
     * Another command line parsing puzzle from Kai Hu - as far as I understand it there is no way to express that in a one-line command string.
     */
    

    /**
     * Test the following command line
     *
     * cmd.exe /C c:\was51\Web Sphere\AppServer\bin\versionInfo.bat
     */
    

    /**
     * Test the toString() method.
     *
     * @throws Exception the test failed
     */
    

    /**
     * Test that toString() produces output that is useful for troubleshooting.
     *
     * @throws Exception the test failed
     */

    @Test
    public void testAddArgument_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgument_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("bar");
    }

    @Test
    public void testAddArgument_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
    }

    @Test
    public void testAddArgument_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArguments_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArguments_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("foo bar");
    }

    @Test
    public void testAddArguments_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
    }

    @Test
    public void testAddArguments_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsArray_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentsArray_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2(new String[] { "foo", "bar" });
    }

    @Test
    public void testAddArgumentsArray_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2(new String[] { "foo", "bar" });
        assertEquals("[test, foo, bar]", cmdl.toString());
    }

    @Test
    public void testAddArgumentsArray_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2(new String[] { "foo", "bar" });
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsArrayNull_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentsArrayNull_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2((String[]) null);
    }

    @Test
    public void testAddArgumentsArrayNull_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2((String[]) null);
        assertEquals("[test]", cmdl.toString());
    }

    @Test
    public void testAddArgumentsArrayNull_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2((String[]) null);
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsWithQuotes_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentsWithQuotes_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'foo' \"bar\"");
    }

    @Test
    public void testAddArgumentsWithQuotes_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'foo' \"bar\"");
        assertEquals("[test, foo, bar]", cmdl.toString());
    }

    @Test
    public void testAddArgumentsWithQuotes_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'foo' \"bar\"");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsWithQuotesAndSpaces_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentsWithQuotesAndSpaces_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'fo o' \"ba r\"");
    }

    @Test
    public void testAddArgumentsWithQuotesAndSpaces_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'fo o' \"ba r\"");
        assertEquals("[test, \"fo o\", \"ba r\"]", cmdl.toString());
    }

    @Test
    public void testAddArgumentsWithQuotesAndSpaces_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'fo o' \"ba r\"");
        assertEquals("[test, \"fo o\", \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "\"fo o\"", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithBothQuotes_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentWithBothQuotes_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertThrows(IllegalArgumentException.class, () -> cmdl.addArgument0("b\"a'r"));
    }

    @Test
    public void testAddArgumentWithQuote_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentWithQuote_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba\"r");
    }

    @Test
    public void testAddArgumentWithQuote_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba\"r");
        assertEquals("[test, foo, 'ba\"r']", cmdl.toString());
    }

    @Test
    public void testAddArgumentWithQuote_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba\"r");
        assertEquals("[test, foo, 'ba\"r']", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "'ba\"r'" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithQuotesAround_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentWithQuotesAround_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("\'foo\'");
        cmdl.addArgument0("\"bar\"");
        cmdl.addArgument0("\"fe z\"");
    }

    @Test
    public void testAddArgumentWithQuotesAround_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("\'foo\'");
        cmdl.addArgument0("\"bar\"");
        cmdl.addArgument0("\"fe z\"");
        assertEquals("[test, foo, bar, \"fe z\"]", cmdl.toString());
    }

    @Test
    public void testAddArgumentWithQuotesAround_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("\'foo\'");
        cmdl.addArgument0("\"bar\"");
        cmdl.addArgument0("\"fe z\"");
        assertEquals("[test, foo, bar, \"fe z\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar", "\"fe z\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithSingleQuote_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentWithSingleQuote_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba'r");
    }

    @Test
    public void testAddArgumentWithSingleQuote_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba'r");
        assertEquals("[test, foo, \"ba'r\"]", cmdl.toString());
    }

    @Test
    public void testAddArgumentWithSingleQuote_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba'r");
        assertEquals("[test, foo, \"ba'r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba\'r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithSpace_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddArgumentWithSpace_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba r");
    }

    @Test
    public void testAddArgumentWithSpace_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba r");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
    }

    @Test
    public void testAddArgumentWithSpace_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba r");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddNullArgument_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testAddNullArgument_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0(null);
    }

    @Test
    public void testAddNullArgument_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0(null);
        assertEquals("[test]", cmdl.toString());
    }

    @Test
    public void testAddNullArgument_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0(null);
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
    }

    @Test
    public void testAddTwoArguments_test0_decomposed()  {
        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
    }

    @Test
    public void testAddTwoArguments_test1_decomposed()  {
        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
        userAddCL1.addArgument0("-g");
        userAddCL1.addArgument0("tomcat");
        userAddCL1.addArgument0("foo");
    }

    @Test
    public void testAddTwoArguments_test2_decomposed()  {
        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
        userAddCL1.addArgument0("-g");
        userAddCL1.addArgument0("tomcat");
        userAddCL1.addArgument0("foo");
        final CommandLine userAddCL2 = new CommandLine(2, null, null, "useradd");
    }

    @Test
    public void testAddTwoArguments_test3_decomposed()  {
        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
        userAddCL1.addArgument0("-g");
        userAddCL1.addArgument0("tomcat");
        userAddCL1.addArgument0("foo");
        final CommandLine userAddCL2 = new CommandLine(2, null, null, "useradd");
        userAddCL2.addArgument0("-g").addArgument0("tomcat");
        userAddCL2.addArgument0("foo");
    }

    @Test
    public void testAddTwoArguments_test4_decomposed()  {
        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
        userAddCL1.addArgument0("-g");
        userAddCL1.addArgument0("tomcat");
        userAddCL1.addArgument0("foo");
        final CommandLine userAddCL2 = new CommandLine(2, null, null, "useradd");
        userAddCL2.addArgument0("-g").addArgument0("tomcat");
        userAddCL2.addArgument0("foo");
        assertEquals(userAddCL1.toString(), userAddCL2.toString());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test0_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test1_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test2_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test3_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test4_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test5_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test6_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test7_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test8_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test9_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test10_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test11_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test12_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass} ${file1} ${file2}", substitutionMap);
    }

    @Test
    public void testCommandLineParsingWithExpansion1_test13_decomposed()  {
        CommandLine cmdl;
        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));
        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass} ${file1} ${file2}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${file}") < 0);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test0_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test1_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test2_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test3_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test4_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test5_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test6_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test7_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test8_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test9_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test10_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", arguments[2]);
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        result = cmdl.toStrings();
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test11_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", arguments[2]);
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test12_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", arguments[2]);
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
    }

    @Test
    public void testCommandLineParsingWithExpansion2_test13_decomposed()  {
        CommandLine cmdl;
        String[] result;
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", arguments[2]);
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432432.pdf\"", result[3]);
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test0_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test1_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test2_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
        cmdl.addArgument1("${file}", false);
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test3_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
        cmdl.addArgument1("${file}", false);
        final HashMap<String, String> params = new HashMap<>();
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl.setSubstitutionMap(params);
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test4_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
        cmdl.addArgument1("${file}", false);
        final HashMap<String, String> params = new HashMap<>();
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl.setSubstitutionMap(params);
        final String[] result = cmdl.toStrings();
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test5_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
        cmdl.addArgument1("${file}", false);
        final HashMap<String, String> params = new HashMap<>();
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl.setSubstitutionMap(params);
        final String[] result = cmdl.toStrings();
        assertEquals("AcroRd32.exe", result[0]);
        assertEquals("/p", result[1]);
    }

    @Test
    public void testCommandLineParsingWithExpansion3_test6_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("AcroRd32.exe");
        cmdl.addArgument0("/p");
        cmdl.addArgument0("/h");
        cmdl.addArgument1("${file}", false);
        final HashMap<String, String> params = new HashMap<>();
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl.setSubstitutionMap(params);
        final String[] result = cmdl.toStrings();
        assertEquals("AcroRd32.exe", result[0]);
        assertEquals("/p", result[1]);
        assertEquals("/h", result[2]);
        assertEquals("C:\\Document And Settings\\documents\\432432.pdf", result[3]);
    }

    @Test
    public void testComplexAddArgument_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
    }

    @Test
    public void testComplexAddArgument_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArgument1("10", false);
        cmdl.addArgument1("30", false);
        cmdl.addArgument1("-XX:+UseParallelGC", false);
        cmdl.addArgument1("\"-XX:ParallelGCThreads=2\"", false);
    }

    @Test
    public void testComplexAddArgument_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArgument1("10", false);
        cmdl.addArgument1("30", false);
        cmdl.addArgument1("-XX:+UseParallelGC", false);
        cmdl.addArgument1("\"-XX:ParallelGCThreads=2\"", false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    @Test
    public void testComplexAddArguments1_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
    }

    @Test
    public void testComplexAddArguments1_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments3(new String[] { "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, false);
    }

    @Test
    public void testComplexAddArguments1_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments3(new String[] { "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    @Test
    public void testComplexAddArguments2_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
    }

    @Test
    public void testComplexAddArguments2_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments1("10 30 -XX:+UseParallelGC '\"-XX:ParallelGCThreads=2\"'", false);
    }

    @Test
    public void testComplexAddArguments2_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments1("10 30 -XX:+UseParallelGC '\"-XX:ParallelGCThreads=2\"'", false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    @Test
    public void testCopyConstructor_test0_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testCopyConstructor_test1_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
    }

    @Test
    public void testCopyConstructor_test2_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
    }

    @Test
    public void testCopyConstructor_test3_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
        final CommandLine cmdl = new CommandLine(0, other, null, null);
    }

    @Test
    public void testCopyConstructor_test4_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
        final CommandLine cmdl = new CommandLine(0, other, null, null);
        assertEquals(other.getExecutable(), cmdl.getExecutable());
    }

    @Test
    public void testCopyConstructor_test5_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
        final CommandLine cmdl = new CommandLine(0, other, null, null);
        assertEquals(other.getExecutable(), cmdl.getExecutable());
        assertArrayEquals(other.getArguments(), cmdl.getArguments());
    }

    @Test
    public void testCopyConstructor_test6_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
        final CommandLine cmdl = new CommandLine(0, other, null, null);
        assertEquals(other.getExecutable(), cmdl.getExecutable());
        assertArrayEquals(other.getArguments(), cmdl.getArguments());
        assertEquals(other.isFile(), cmdl.isFile());
    }

    @Test
    public void testCopyConstructor_test7_decomposed()  {
        final Map<String, String> map = new HashMap<>();
        map.put("bar", "bar");
        final CommandLine other = new CommandLine(2, null, null, "test");
        other.addArgument0("foo");
        other.setSubstitutionMap(map);
        final CommandLine cmdl = new CommandLine(0, other, null, null);
        assertEquals(other.getExecutable(), cmdl.getExecutable());
        assertArrayEquals(other.getArguments(), cmdl.getArguments());
        assertEquals(other.isFile(), cmdl.isFile());
        assertEquals(other.getSubstitutionMap(), cmdl.getSubstitutionMap());
    }

    @Test
    public void testExecutable_test0_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
    }

    @Test
    public void testExecutable_test1_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertEquals("[test]", cmdl.toString());
    }

    @Test
    public void testExecutable_test2_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
    }

    @Test
    public void testExecutable_test3_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
        assertEquals("test", cmdl.getExecutable());
    }

    @Test
    public void testExecutable_test4_decomposed()  {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
        assertEquals("test", cmdl.getExecutable());
        assertTrue(cmdl.getArguments().length == 0);
    }

    @Test
    public void testExecutableWhitespaceString_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> new CommandLine(2, null, null, "   "));
    }

    @Test
    public void testExecutableZeroLengthString_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> new CommandLine(2, null, null, ""));
    }

    @Test
    public void testNullExecutable_test0_decomposed()  {
        assertThrows(NullPointerException.class, () -> new CommandLine(2, null, null, (String) null));
    }

    @Test
    public void testParseCommandLine_test0_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test foo bar");
    }

    @Test
    public void testParseCommandLine_test1_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
    }

    @Test
    public void testParseCommandLine_test2_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testParseCommandLineWithNull_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0(null));
    }

    @Test
    public void testParseCommandLineWithOnlyWhitespace_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0("  "));
    }

    @Test
    public void testParseCommandLineWithQuotes_test0_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test \"foo\" \'ba r\'");
    }

    @Test
    public void testParseCommandLineWithQuotes_test1_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test \"foo\" \'ba r\'");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
    }

    @Test
    public void testParseCommandLineWithQuotes_test2_decomposed()  {
        final CommandLine cmdl = CommandLine.parse0("test \"foo\" \'ba r\'");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testParseCommandLineWithUnevenQuotes_test0_decomposed()  {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0("test \"foo bar"), "IllegalArgumentException must be thrown due to uneven quotes");
    }

    @Test
    public void testParseComplexCommandLine1_test0_decomposed()  {
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("in", "source.jpg");
        substitutionMap.put("out", "target.jpg");
        final CommandLine cmdl = CommandLine.parse1("cmd /C convert ${in} -resize \"\'500x> \'\" ${out}", substitutionMap);
    }

    @Test
    public void testParseComplexCommandLine1_test1_decomposed()  {
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("in", "source.jpg");
        substitutionMap.put("out", "target.jpg");
        final CommandLine cmdl = CommandLine.parse1("cmd /C convert ${in} -resize \"\'500x> \'\" ${out}", substitutionMap);
        assertEquals("[cmd, /C, convert, source.jpg, -resize, \"500x> \", target.jpg]", cmdl.toString());
    }

    @Test
    public void testParseComplexCommandLine2_test0_decomposed()  {
        final String commandline = "./script/jrake cruise:publish_installers " + "INSTALLER_VERSION=unstable_2_1 "
                + "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\" " + "INSTALLER_DOWNLOAD_SERVER=\'something\' " + "WITHOUT_HELP_DOC=true";
        final CommandLine cmdl = CommandLine.parse0(commandline);
    }

    @Test
    public void testParseComplexCommandLine2_test1_decomposed()  {
        final String commandline = "./script/jrake cruise:publish_installers " + "INSTALLER_VERSION=unstable_2_1 "
                + "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\" " + "INSTALLER_DOWNLOAD_SERVER=\'something\' " + "WITHOUT_HELP_DOC=true";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
    }

    @Test
    public void testParseComplexCommandLine2_test2_decomposed()  {
        final String commandline = "./script/jrake cruise:publish_installers " + "INSTALLER_VERSION=unstable_2_1 "
                + "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\" " + "INSTALLER_DOWNLOAD_SERVER=\'something\' " + "WITHOUT_HELP_DOC=true";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
        assertEquals(args[0], "cruise:publish_installers");
        assertEquals(args[1], "INSTALLER_VERSION=unstable_2_1");
    }

    @Test
    public void testParseComplexCommandLine2_test3_decomposed()  {
        final String commandline = "./script/jrake cruise:publish_installers " + "INSTALLER_VERSION=unstable_2_1 "
                + "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\" " + "INSTALLER_DOWNLOAD_SERVER=\'something\' " + "WITHOUT_HELP_DOC=true";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
        assertEquals(args[0], "cruise:publish_installers");
        assertEquals(args[1], "INSTALLER_VERSION=unstable_2_1");
        assertEquals(args[4], "WITHOUT_HELP_DOC=true");
    }

    @Test
    public void testParseRealLifeCommandLine_1_test0_decomposed()  {
        final String commandline = "cmd.exe /C \"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"";
        final CommandLine cmdl = CommandLine.parse0(commandline);
    }

    @Test
    public void testParseRealLifeCommandLine_1_test1_decomposed()  {
        final String commandline = "cmd.exe /C \"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
    }

    @Test
    public void testParseRealLifeCommandLine_1_test2_decomposed()  {
        final String commandline = "cmd.exe /C \"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
        assertEquals("/C", args[0]);
        assertEquals("\"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"", args[1]);
    }

    @Test
    public void testToString_test0_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
    }

    @Test
    public void testToString_test1_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());
    }

    @Test
    public void testToString_test2_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
    }

    @Test
    public void testToString_test3_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, \"C:\\Document And Settings\\documents\\432432.pdf\"]", cmdl.toString());
    }

    @Test
    public void testToString_test4_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, \"C:\\Document And Settings\\documents\\432432.pdf\"]", cmdl.toString());
        params.put("file", "C:\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
    }

    @Test
    public void testToString_test5_decomposed() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, \"C:\\Document And Settings\\documents\\432432.pdf\"]", cmdl.toString());
        params.put("file", "C:\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, C:\\documents\\432432.pdf]", cmdl.toString());
    }

    @Test
    public void testToStringTroubleshooting_test0_decomposed() throws Exception {
        System.out.println("testToStringTroubleshooting");
        new CommandLine(2, null, null, "sh").addArgument0("-c");
    }

    @Test
    public void testToStringTroubleshooting_test1_decomposed() throws Exception {
        System.out.println("testToStringTroubleshooting");
        new CommandLine(2, null, null, "sh").addArgument0("-c");
        final CommandLine cmd1 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument1("echo 1", false);
    }

    @Test
    public void testToStringTroubleshooting_test2_decomposed() throws Exception {
        System.out.println("testToStringTroubleshooting");
        new CommandLine(2, null, null, "sh").addArgument0("-c");
        final CommandLine cmd1 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument1("echo 1", false);
        final CommandLine cmd2 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument0("echo").addArgument0("1");
    }

    @Test
    public void testToStringTroubleshooting_test3_decomposed() throws Exception {
        System.out.println("testToStringTroubleshooting");
        new CommandLine(2, null, null, "sh").addArgument0("-c");
        final CommandLine cmd1 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument1("echo 1", false);
        final CommandLine cmd2 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument0("echo").addArgument0("1");
        System.out.println("cmd1: " + cmd1.toString());
        System.out.println("cmd2: " + cmd2.toString());
        assertTrue(!cmd1.toString().equals(cmd2.toString()), "toString() is useful for troubleshooting");
    }
}