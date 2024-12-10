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

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.File;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecuteResultHandler;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.ExecuteWatchdog;
import org.apache.commons.exec.Executor;
import org.apache.commons.exec.TestUtil;
import org.junit.jupiter.api.Test;

/**
 * EXEC-34 https://issues.apache.org/jira/browse/EXEC-34
 */
public class Exec34Test {

    private final Executor exec = DefaultExecutor.builder().get();
    private final File testDir = new File("src/test/scripts");
    private final File pingScript = TestUtil.resolveScriptForOS(testDir + "/ping");

    /**
     *
     * Race condition prevent watchdog working using ExecuteStreamHandler. The test fails because when watchdog.destroyProcess() is invoked the external process
     * is not bound to the watchdog yet.
     *
     * @throws Exception the test failed
     */
    

    /**
     * Some user waited for an asynchronous process using watchdog.isWatching() which is now properly implemented using {@code DefaultExecuteResultHandler}.
     *
     * @throws Exception the test failed
     */

    @Test
    public void testExec34_1_test0_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
    }

    @Test
    public void testExec34_1_test1_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
    }

    @Test
    public void testExec34_1_test2_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
    }

    @Test
    public void testExec34_1_test3_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
    }

    @Test
    public void testExec34_1_test4_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
    }

    @Test
    public void testExec34_1_test5_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
    }

    @Test
    public void testExec34_1_test6_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        assertTrue(watchdog.isWatching());
    }

    @Test
    public void testExec34_1_test7_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        assertTrue(watchdog.isWatching());
        watchdog.destroyProcess();
    }

    @Test
    public void testExec34_1_test8_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        assertTrue(watchdog.isWatching());
        watchdog.destroyProcess();
        assertTrue(watchdog.killedProcess(), "Watchdog should have killed the process");
    }

    @Test
    public void testExec34_1_test9_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(Integer.MAX_VALUE);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        assertTrue(watchdog.isWatching());
        watchdog.destroyProcess();
        assertTrue(watchdog.killedProcess(), "Watchdog should have killed the process");
        assertFalse(watchdog.isWatching(), "Watchdog is no longer watching the process");
    }

    @Test
    public void testExec34_2_test0_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
    }

    @Test
    public void testExec34_2_test1_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
    }

    @Test
    public void testExec34_2_test2_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
    }

    @Test
    public void testExec34_2_test3_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
    }

    @Test
    public void testExec34_2_test4_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
    }

    @Test
    public void testExec34_2_test5_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
    }

    @Test
    public void testExec34_2_test6_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        handler.waitFor0();
    }

    @Test
    public void testExec34_2_test7_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        handler.waitFor0();
        assertTrue(handler.hasResult(), "Process has exited");
    }

    @Test
    public void testExec34_2_test8_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        handler.waitFor0();
        assertTrue(handler.hasResult(), "Process has exited");
        assertNotNull(handler.getException(), "Process was aborted");
    }

    @Test
    public void testExec34_2_test9_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        handler.waitFor0();
        assertTrue(handler.hasResult(), "Process has exited");
        assertNotNull(handler.getException(), "Process was aborted");
        assertTrue(watchdog.killedProcess(), "Watchdog should have killed the process");
    }

    @Test
    public void testExec34_2_test10_decomposed() throws Exception {
        final CommandLine cmdLine = new CommandLine(1, null, pingScript, null);
        cmdLine.addArgument0("10");
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(5000);
        final DefaultExecuteResultHandler handler = new DefaultExecuteResultHandler();
        exec.setWatchdog(watchdog);
        exec.execute1(cmdLine, handler);
        handler.waitFor0();
        assertTrue(handler.hasResult(), "Process has exited");
        assertNotNull(handler.getException(), "Process was aborted");
        assertTrue(watchdog.killedProcess(), "Watchdog should have killed the process");
        assertFalse(watchdog.isWatching(), "Watchdog is no longer watching the process");
    }
}