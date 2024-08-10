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

package org.apache.commons.exec.issues;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.File;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.ExecuteException;
import org.apache.commons.exec.ExecuteWatchdog;
import org.apache.commons.exec.OS;
import org.apache.commons.exec.PumpStreamHandler;
import org.apache.commons.exec.TestUtil;
import org.junit.jupiter.api.Test;

/**
 * Test the patch for EXEC-41 (https://issues.apache.org/jira/browse/EXEC-41).
 */
public class Exec41Test {

    private final File testDir = new File("src/test/scripts");
    private final File pingScript = TestUtil.resolveScriptForOS(testDir + "/ping");

    /**
     * Test EXEC-41 with a disabled PumpStreamHandler to check if we could return immediately after killing the process (no streams implies no blocking stream
     * pumper threads). But you have to be 100% sure that the subprocess is not writing to 'stdout' and 'stderr'.
     *
     * For this test we are using the batch file - under Windows the 'ping' process can't be killed (not supported by Win32) and will happily run the given time
     * (e.g. 10 seconds) even hwen the batch file is already killed.
     *
     * @throws Exception the test failed
     */
    

    /**
     *
     * When a process runs longer than allowed by a configured watchdog's timeout, the watchdog tries to destroy it and then DefaultExecutor tries to clean up
     * by joining with all installed pump stream threads. Problem is, that sometimes the native process doesn't die and thus streams aren't closed and the
     * stream threads do not complete.
     *
     * @throws Exception the test failed
     */

    @Test
    public void testExec41WithoutStreams_test0_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
    }

    @Test
    public void testExec41WithoutStreams_test1_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
    }

    @Test
    public void testExec41WithoutStreams_test2_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
    }

    @Test
    public void testExec41WithoutStreams_test3_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
    }

    @Test
    public void testExec41WithoutStreams_test4_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
    }

    @Test
    public void testExec41WithoutStreams_test5_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
    }

    @Test
    public void testExec41WithoutStreams_test6_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
    }

    @Test
    public void testExec41WithoutStreams_test7_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
    }

    @Test
    public void testExec41WithoutStreams_test8_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            System.out.println(e);
        }
    }

    @Test
    public void testExec41WithoutStreams_test9_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            System.out.println(e);
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed.");
        }
    }

    @Test
    public void testExec41WithoutStreams_test10_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            System.out.println(e);
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed.");
        }
        assertTrue(watchdog.killedProcess(), "The process was killed by the watchdog");
    }

    @Test
    public void testExec41WithoutStreams_test11_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(null, null, null);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            System.out.println(e);
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed.");
        }
        assertTrue(watchdog.killedProcess(), "The process was killed by the watchdog");
        assertTrue(duration < 9000, () -> "Skipping the Thread.join() did not work, duration=" + duration);
    }

    @Test
    public void testExec41WithStreams_test0_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
    }

    @Test
    public void testExec41WithStreams_test1_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
    }

    @Test
    public void testExec41WithStreams_test2_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
    }

    @Test
    public void testExec41WithStreams_test3_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
    }

    @Test
    public void testExec41WithStreams_test4_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
    }

    @Test
    public void testExec41WithStreams_test5_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
    }

    @Test
    public void testExec41WithStreams_test6_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
    }

    @Test
    public void testExec41WithStreams_test7_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            // nothing to do
        }
    }

    @Test
    public void testExec41WithStreams_test8_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            // nothing to do
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed by watchdog.");
        }
    }

    @Test
    public void testExec41WithStreams_test9_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            // nothing to do
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed by watchdog.");
        }
        assertTrue(watchdog.killedProcess(), "The process was killed by the watchdog");
    }

    @Test
    public void testExec41WithStreams_test10_decomposed() throws Exception {
        CommandLine cmdLine;
        if (OS.isFamilyWindows()) {
            cmdLine = CommandLine.parse0("ping.exe -n 10 -w 1000 127.0.0.1");
        } else if ("HP-UX".equals(System.getProperty("os.name"))) {
            // see EXEC-52 - option must appear after the hostname!
            cmdLine = CommandLine.parse0("ping 127.0.0.1 -n 10");
        } else if (OS.isFamilyUnix()) {
            cmdLine = CommandLine.parse0("ping -c 10 127.0.0.1");
        } else {
            System.err.println("The test 'testExec41WithStreams' does not support the following OS : " + System.getProperty("os.name"));
            return;
        }
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(2 * 1000);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler2(System.out, System.err);
        executor.setWatchdog(watchdog);
        executor.setStreamHandler(pumpStreamHandler);
        final long startTime = System.currentTimeMillis();
        try {
            executor.execute0(cmdLine);
        } catch (final ExecuteException e) {
            // nothing to do
        }
        final long duration = System.currentTimeMillis() - startTime;
        System.out.println("Process completed in " + duration + " millis; below is its output");
        if (watchdog.killedProcess()) {
            System.out.println("Process timed out and was killed by watchdog.");
        }
        assertTrue(watchdog.killedProcess(), "The process was killed by the watchdog");
        assertTrue(duration < 9000, "Skipping the Thread.join() did not work");
    }
}