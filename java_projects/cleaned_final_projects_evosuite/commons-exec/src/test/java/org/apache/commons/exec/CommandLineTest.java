
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

    @Test
    public void testAddArgument() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");

        cmdl.addArgument0("foo");
        cmdl.addArgument0("bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArguments() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsArray() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2(new String[] { "foo", "bar" });
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsArrayNull() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments2((String[]) null);
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsWithQuotes() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'foo' \"bar\"");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentsWithQuotesAndSpaces() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArguments0("'fo o' \"ba r\"");
        assertEquals("[test, \"fo o\", \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "\"fo o\"", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithBothQuotes() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertThrows(IllegalArgumentException.class, () -> cmdl.addArgument0("b\"a'r"));
    }

    @Test
    public void testAddArgumentWithQuote() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba\"r");
        assertEquals("[test, foo, 'ba\"r']", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "'ba\"r'" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithQuotesAround() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("\'foo\'");
        cmdl.addArgument0("\"bar\"");
        cmdl.addArgument0("\"fe z\"");
        assertEquals("[test, foo, bar, \"fe z\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar", "\"fe z\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithSingleQuote() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");

        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba'r");
        assertEquals("[test, foo, \"ba'r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba\'r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddArgumentWithSpace() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        cmdl.addArgument0("foo");
        cmdl.addArgument0("ba r");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testAddNullArgument() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");

        cmdl.addArgument0(null);
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
    }

    /**
     * A little example how to add two command line arguments in one line, e.g. to make commenting out some options less error prone.
     */
    @Test
    public void testAddTwoArguments() {

        final CommandLine userAddCL1 = new CommandLine(2, null, null, "useradd");
        userAddCL1.addArgument0("-g");
        userAddCL1.addArgument0("tomcat");
        userAddCL1.addArgument0("foo");

        final CommandLine userAddCL2 = new CommandLine(2, null, null, "useradd");
        userAddCL2.addArgument0("-g").addArgument0("tomcat");
        userAddCL2.addArgument0("foo");

        assertEquals(userAddCL1.toString(), userAddCL2.toString());
    }

    /**
     * Test expanding the command line based on a user-supplied map.
     */
    @Test
    public void testCommandLineParsingWithExpansion1() {

        CommandLine cmdl;

        final HashMap<String, Object> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "/usr/local/java");
        substitutionMap.put("appMainClass", "foo.bar.Main");
        substitutionMap.put("file1", new File("./pom.xml"));
        substitutionMap.put("file2", new File(".\\temp\\READ ME.txt"));

        final HashMap<String, String> incompleteMap = new HashMap<>();
        incompleteMap.put("JAVA_HOME", "/usr/local/java");

        // do not pass substitution map
        cmdl = CommandLine.parse0("${JAVA_HOME}/bin/java ${appMainClass}");
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());

        // pass arguments with an empty map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", new HashMap<>());
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") == 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());

        // pass an complete substitution map
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "foo.bar.Main" }, cmdl.getArguments());

        // pass an incomplete substitution map resulting in unresolved variables
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass}", incompleteMap);
        assertTrue(cmdl.getExecutable().indexOf("${JAVA_HOME}") < 0);
        assertTrue(cmdl.getExecutable().indexOf("local") > 0);
        assertArrayEquals(new String[] { "${appMainClass}" }, cmdl.getArguments());

        // pass a file
        cmdl = CommandLine.parse1("${JAVA_HOME}/bin/java ${appMainClass} ${file1} ${file2}", substitutionMap);
        assertTrue(cmdl.getExecutable().indexOf("${file}") < 0);
    }

    /**
     * Test expanding the command line based on a user-supplied map. The main goal of the test is to setup a command line using macros and reuse it multiple
     * times.
     */
    @Test
    public void testCommandLineParsingWithExpansion2() {

        CommandLine cmdl;
        String[] result;

        // build the user supplied parameters
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("JAVA_HOME", "C:\\Programme\\jdk1.5.0_12");
        substitutionMap.put("appMainClass", "foo.bar.Main");

        // build the command line
        cmdl = new CommandLine(2, null, null, "${JAVA_HOME}\\bin\\java");
        cmdl.addArgument0("-class");
        cmdl.addArgument0("${appMainClass}");
        cmdl.addArgument0("${file}");

        // build the first command line
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432431.pdf");
        cmdl.setSubstitutionMap(substitutionMap);
        result = cmdl.toStrings();

        // verify the first command line
        // please note - the executable argument is changed to using platform specific file separator char
        // whereas all other variable substitution are not touched
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", result[3]);

        // verify the first command line again but by
        // accessing the executable and arguments directly
        final String executable = cmdl.getExecutable();
        final String[] arguments = cmdl.getArguments();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), executable);
        assertEquals("-class", arguments[0]);
        assertEquals("foo.bar.Main", arguments[1]);
        assertEquals("\"C:\\Document And Settings\\documents\\432431.pdf\"", arguments[2]);

        // build the second command line with updated parameters resulting in a different command line
        substitutionMap.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        result = cmdl.toStrings();
        assertEquals(StringUtils.fixFileSeparatorChar("C:\\Programme\\jdk1.5.0_12\\bin\\java"), result[0]);
        assertEquals("-class", result[1]);
        assertEquals("foo.bar.Main", result[2]);
        assertEquals("\"C:\\Document And Settings\\documents\\432432.pdf\"", result[3]);
    }

    @Test
    public void testCommandLineParsingWithExpansion3() {
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

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\""
     */
    @Test
    public void testComplexAddArgument() {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArgument1("10", false);
        cmdl.addArgument1("30", false);
        cmdl.addArgument1("-XX:+UseParallelGC", false);
        cmdl.addArgument1("\"-XX:ParallelGCThreads=2\"", false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\""
     */
    @Test
    public void testComplexAddArguments1() {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments3(new String[] { "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    /**
     * Create a command line with pre-quoted strings to test SANDBOX-192, e.g. "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC",
     * "\"-XX:ParallelGCThreads=2\"" Please not that we re forced to add additional single quotes to get the test working - don't know if this is a bug or a
     * feature.
     */
    @Test
    public void testComplexAddArguments2() {
        final CommandLine cmdl = new CommandLine(2, null, null, "runMemorySud.cmd");
        cmdl.addArguments1("10 30 -XX:+UseParallelGC '\"-XX:ParallelGCThreads=2\"'", false);
        assertArrayEquals(new String[] { "runMemorySud.cmd", "10", "30", "-XX:+UseParallelGC", "\"-XX:ParallelGCThreads=2\"" }, cmdl.toStrings());
    }

    @Test
    public void testCopyConstructor() {
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
    public void testExecutable() {
        final CommandLine cmdl = new CommandLine(2, null, null, "test");
        assertEquals("[test]", cmdl.toString());
        assertArrayEquals(new String[] { "test" }, cmdl.toStrings());
        assertEquals("test", cmdl.getExecutable());
        assertTrue(cmdl.getArguments().length == 0);
    }

    @Test
    public void testExecutableWhitespaceString() {
        assertThrows(IllegalArgumentException.class, () -> new CommandLine(2, null, null, "   "));
    }

    @Test
    public void testExecutableZeroLengthString() {
        assertThrows(IllegalArgumentException.class, () -> new CommandLine(2, null, null, ""));
    }

    @Test
    public void testNullExecutable() {
        assertThrows(NullPointerException.class, () -> new CommandLine(2, null, null, (String) null));
    }

    @Test
    public void testParseCommandLine() {
        final CommandLine cmdl = CommandLine.parse0("test foo bar");
        assertEquals("[test, foo, bar]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "bar" }, cmdl.toStrings());
    }

    @Test
    public void testParseCommandLineWithNull() {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0(null));
    }

    @Test
    public void testParseCommandLineWithOnlyWhitespace() {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0("  "));
    }

    @Test
    public void testParseCommandLineWithQuotes() {
        final CommandLine cmdl = CommandLine.parse0("test \"foo\" \'ba r\'");
        assertEquals("[test, foo, \"ba r\"]", cmdl.toString());
        assertArrayEquals(new String[] { "test", "foo", "\"ba r\"" }, cmdl.toStrings());
    }

    @Test
    public void testParseCommandLineWithUnevenQuotes() {
        assertThrows(IllegalArgumentException.class, () -> CommandLine.parse0("test \"foo bar"), "IllegalArgumentException must be thrown due to uneven quotes");
    }

    /**
     * A command line parsing puzzle from Tino Schoellhorn - ImageMagix expects a "500x>" parameter (including quotes) and it is simply not possible to do that
     * without adding a space, e.g. "500x> ".
     */
    @Test
    public void testParseComplexCommandLine1() {
        final HashMap<String, String> substitutionMap = new HashMap<>();
        substitutionMap.put("in", "source.jpg");
        substitutionMap.put("out", "target.jpg");
        final CommandLine cmdl = CommandLine.parse1("cmd /C convert ${in} -resize \"\'500x> \'\" ${out}", substitutionMap);
        assertEquals("[cmd, /C, convert, source.jpg, -resize, \"500x> \", target.jpg]", cmdl.toString());
    }

    /**
     * Another command line parsing puzzle from Kai Hu - as far as I understand it there is no way to express that in a one-line command string.
     */
    @Test
    public void testParseComplexCommandLine2() {
        final String commandline = "./script/jrake cruise:publish_installers " + "INSTALLER_VERSION=unstable_2_1 "
                + "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\" " + "INSTALLER_DOWNLOAD_SERVER=\'something\' " + "WITHOUT_HELP_DOC=true";
        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
        assertEquals(args[0], "cruise:publish_installers");
        assertEquals(args[1], "INSTALLER_VERSION=unstable_2_1");
        // assertEquals(args[2], "INSTALLER_PATH=\"/var/lib/ cruise-agent/installers\"");
        // assertEquals(args[3], "INSTALLER_DOWNLOAD_SERVER='something'");
        assertEquals(args[4], "WITHOUT_HELP_DOC=true");
    }

    /**
     * Test the following command line
     *
     * cmd.exe /C c:\was51\Web Sphere\AppServer\bin\versionInfo.bat
     */
    @Test
    public void testParseRealLifeCommandLine_1() {

        final String commandline = "cmd.exe /C \"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"";

        final CommandLine cmdl = CommandLine.parse0(commandline);
        final String[] args = cmdl.getArguments();
        assertEquals("/C", args[0]);
        assertEquals("\"c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat\"", args[1]);
    }

    /**
     * Test the toString() method.
     *
     * @throws Exception the test failed
     */
    @Test
    public void testToString() throws Exception {
        CommandLine cmdl;
        final HashMap<String, String> params = new HashMap<>();

        // use no arguments
        cmdl = CommandLine.parse1("AcroRd32.exe", params);
        assertEquals("[AcroRd32.exe]", cmdl.toString());

        // use an argument containing spaces
        params.put("file", "C:\\Document And Settings\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, \"C:\\Document And Settings\\documents\\432432.pdf\"]", cmdl.toString());

        // use an argument without spaces
        params.put("file", "C:\\documents\\432432.pdf");
        cmdl = CommandLine.parse1("AcroRd32.exe /p /h '${file}'", params);
        assertEquals("[AcroRd32.exe, /p, /h, C:\\documents\\432432.pdf]", cmdl.toString());
    }

    /**
     * Test that toString() produces output that is useful for troubleshooting.
     *
     * @throws Exception the test failed
     */
    @Test
    public void testToStringTroubleshooting() throws Exception {
        System.out.println("testToStringTroubleshooting");
        // On HP-UX quotes handling leads to errors,
        // also usage of quotes isn't mandatory on other platforms too
        // so it probably should work correctly either way.
        final CommandLine cmd1 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument1("echo 1", false);
        final CommandLine cmd2 = new CommandLine(2, null, null, "sh").addArgument0("-c").addArgument0("echo").addArgument0("1");
        System.out.println("cmd1: " + cmd1.toString());
        System.out.println("cmd2: " + cmd2.toString());
        assertTrue(!cmd1.toString().equals(cmd2.toString()), "toString() is useful for troubleshooting");
    }

}
