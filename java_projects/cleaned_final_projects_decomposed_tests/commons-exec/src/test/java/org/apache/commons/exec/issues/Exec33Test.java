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

import java.io.File;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.Executor;
import org.apache.commons.exec.PumpStreamHandler;
import org.apache.commons.exec.TestUtil;
import org.junit.jupiter.api.Test;

/**
 * Test the patch for EXEC-33 (https://issues.apache.org/jira/browse/EXEC-33)
 *
 * PumpStreamHandler hangs if System.in is redirect to process input stream .
 */
public class Exec33Test {

    private final Executor exec = DefaultExecutor.builder().get();
    private final File testDir = new File("src/test/scripts");
    private final File testScript = TestUtil.resolveScriptForOS(testDir + "/test");

    @Test
    public void testExec33_test0_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
    }

    @Test
    public void testExec33_test1_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
    }

    @Test
    public void testExec33_test2_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
        DefaultExecutor.builder();
    }

    @Test
    public void testExec33_test3_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
    }

    @Test
    public void testExec33_test4_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        executor.setStreamHandler(pumpStreamHandler);
    }

    @Test
    public void testExec33_test5_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        executor.setStreamHandler(pumpStreamHandler);
        final int exitValue = executor.execute0(cl);
    }

    @Test
    public void testExec33_test6_decomposed() throws Exception {
        final CommandLine cl = new CommandLine(1, null, testScript, null);
        final PumpStreamHandler pumpStreamHandler = PumpStreamHandler.PumpStreamHandler3(System.out, System.err, System.in);
        DefaultExecutor.builder();
        final DefaultExecutor executor = DefaultExecutor.builder().get();
        executor.setStreamHandler(pumpStreamHandler);
        final int exitValue = executor.execute0(cl);
        assertFalse(exec.isFailure(exitValue));
    }
}