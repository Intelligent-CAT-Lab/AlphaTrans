
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


package org.apache.commons.exec.issues;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assumptions.assumeFalse;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

import java.io.File;
import java.util.concurrent.TimeUnit;

import org.apache.commons.exec.AbstractExecTest;
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.ExecuteException;
import org.apache.commons.exec.ExecuteWatchdog;
import org.apache.commons.exec.OS;
import org.apache.commons.exec.PumpStreamHandler;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Timeout;

/**
 * Test to show that watchdog can destroy 'sudo' and 'sleep'.
 *
 * @see <a href="https://issues.apache.org/jira/browse/EXEC-65">EXEC-65</a>
 */
public class Exec65Test extends AbstractExecTest {

    /**
     * This test currently only works for macOS X
     * <ul>
     * <li>Linux hangs on the process stream while the process is finished</li>
     * <li>Windows seems to have similar problems</li>
     * </ul>
     *
     * @TODO Fix tests for Windows & Linux
     */
    @Test
    @Timeout(value = TEST_TIMEOUT, unit = TimeUnit.MILLISECONDS)
    public void testExec65WithSleepUsingShellScript() throws Exception {
        assumeTrue(OS.isFamilyMac());
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        executor.setStreamHandler(PumpStreamHandler.PumpStreamHandler2(System.out, System.err));
        executor.setWatchdog(ExecuteWatchdog.ExecuteWatchdog0(WATCHDOG_TIMEOUT));
        final CommandLine command = new CommandLine(1, null, resolveTestScript0("sleep"), null);

        assertThrows(ExecuteException.class, () -> executor.execute0(command));
    }

    /**
     * This is the original code snippet from the JIRA to show that killing the process actually works with JDK only but it does not re-direct any streams.
     */
    @Test
    @Timeout(value = TEST_TIMEOUT, unit = TimeUnit.MILLISECONDS)
    public void testExec65WithSleepUsingShellScriptAndJDKOnly() throws Exception {

        final Process process = Runtime.getRuntime().exec(resolveTestScript0("sleep").getAbsolutePath());
        Thread.sleep(WATCHDOG_TIMEOUT);

        process.destroy();

        process.waitFor();

        assertTrue(process.exitValue() != 0);
    }

    /**
     * Please note that this tests make assumptions about the environment. It assumes that user "root" exists and that the current user is not a "sudoer"
     * already (thereby requiring a password).
     */
    @Test
    @Timeout(value = TEST_TIMEOUT, unit = TimeUnit.MILLISECONDS)
    public void testExec65WithSudoUsingShellScript() throws Exception {
        assumeFalse(new File(".").getAbsolutePath().contains("travis"),
                "Test is skipped on travis, because we have to be a sudoer to make the other tests pass.");
        // TODO Fails on GitHub
        assumeTrue(System.getenv("GITHUB_WORKFLOW") == null);
        if (!OS.isFamilyUnix()) {
            throw new ExecuteException(testNotSupportedForCurrentOperatingSystem(), 0, null);
        }
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        executor.setStreamHandler(PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in));
        executor.setWatchdog(ExecuteWatchdog.ExecuteWatchdog0(WATCHDOG_TIMEOUT));
        final CommandLine command = new CommandLine(1, null, resolveTestScript1("issues", "exec-65"), null);

        assertThrows(ExecuteException.class, () -> executor.execute0(command));
    }

    @Test
    @Timeout(value = TEST_TIMEOUT, unit = TimeUnit.MILLISECONDS)
    public void testExec65WitSleepUsingSleepCommandDirectly() throws Exception {

        if (!OS.isFamilyUnix()) {
            throw new ExecuteException(testNotSupportedForCurrentOperatingSystem(), 0, null);
        }
        final ExecuteWatchdog watchdog = ExecuteWatchdog.ExecuteWatchdog0(WATCHDOG_TIMEOUT);
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        final CommandLine command = new CommandLine(2, null, null, "sleep");
        command.addArgument0("60");
        executor.setStreamHandler(PumpStreamHandler.PumpStreamHandler2(System.out, System.err));
        executor.setWatchdog(watchdog);

        assertThrows(ExecuteException.class, () -> executor.execute0(command));
    }
}
