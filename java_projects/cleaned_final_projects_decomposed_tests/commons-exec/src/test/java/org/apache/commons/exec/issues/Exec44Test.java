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
 * Test EXEC-44 (https://issues.apache.org/jira/browse/EXEC-44).
 */
public class Exec44Test {

    private final Executor exec = DefaultExecutor.builder().get();
    private final File testDir = new File("src/test/scripts");
    private final File foreverTestScript = TestUtil.resolveScriptForOS(testDir + "/forever");

    /**
     *
     * Because the ExecuteWatchdog is the only way to destroy asynchronous processes, it should be possible to set it to an infinite timeout, for processes
     * which should not timeout, but manually destroyed under some circumstances.
     *
     * @throws Exception the test failed
     */

    @Test
    public void testExec44_test0_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
    }

    @Test
    public void testExec44_test1_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
    }

    @Test
    public void testExec44_test2_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
    }

    @Test
    public void testExec44_test3_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
    }

    @Test
    public void testExec44_test4_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
        exec.execute1(cl, resultHandler);
    }

    @Test
    public void testExec44_test5_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
        exec.execute1(cl, resultHandler);
        Thread.sleep(5000);
        assertTrue(watchdog.isWatching(), "The watchdog is watching the process");
    }

    @Test
    public void testExec44_test6_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
        exec.execute1(cl, resultHandler);
        Thread.sleep(5000);
        assertTrue(watchdog.isWatching(), "The watchdog is watching the process");
        watchdog.destroyProcess();
    }

    @Test
    public void testExec44_test7_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
        exec.execute1(cl, resultHandler);
        Thread.sleep(5000);
        assertTrue(watchdog.isWatching(), "The watchdog is watching the process");
        watchdog.destroyProcess();
        assertTrue(watchdog.killedProcess(), "The watchdog has killed the process");
    }

    @Test
    public void testExec44_test8_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, foreverTestScript, null);
        final DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(ExecuteWatchdog.INFINITE_TIMEOUT);
        exec.setWatchdog(watchdog);
        exec.execute1(cl, resultHandler);
        Thread.sleep(5000);
        assertTrue(watchdog.isWatching(), "The watchdog is watching the process");
        watchdog.destroyProcess();
        assertTrue(watchdog.killedProcess(), "The watchdog has killed the process");
        assertFalse(watchdog.isWatching(), "The watchdog is no longer watching any process");
    }
}