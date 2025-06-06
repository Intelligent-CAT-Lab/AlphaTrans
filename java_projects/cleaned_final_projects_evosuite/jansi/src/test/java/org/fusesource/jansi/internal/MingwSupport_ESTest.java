/*
 * Copyright (C) 2009-2023 the original author(s).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.fusesource.jansi.internal;

import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class MingwSupport_ESTest extends MingwSupport_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test0() throws Throwable {
        Future<?> future = executor.submit(new Runnable() {
            @Override
            public void run() {
                MingwSupport mingwSupport0 = new MingwSupport();
                // Undeclared exception!
                try {
                    mingwSupport0.getTerminalWidth("");
                    fail("Expecting exception: RuntimeException");

                } catch (RuntimeException e) {
                    //
                    // java.lang.SecurityException: Security manager blocks (\"java.io.FilePermission\" \"<<ALL
                    // FILES>>\" \"execute\")
                    // java.base/java.lang.Thread.getStackTrace(Thread.java:1602)
                    // org.evosuite.runtime.sandbox.MSecurityManager.checkPermission(MSecurityManager.java:424)
                    // java.base/java.lang.SecurityManager.checkExec(SecurityManager.java:572)
                    // java.base/java.lang.ProcessBuilder.start(ProcessBuilder.java:1096)
                    // java.base/java.lang.ProcessBuilder.start(ProcessBuilder.java:1071)
                    // org.fusesource.jansi.internal.MingwSupport.getTerminalWidth(MingwSupport.java:90)
                    // jdk.internal.reflect.GeneratedMethodAccessor25.invoke(Unknown Source)
                    // java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
                    // java.base/java.lang.reflect.Method.invoke(Method.java:566)
                    // org.evosuite.testcase.statements.MethodStatement$1.execute(MethodStatement.java:256)
                    // org.evosuite.testcase.statements.AbstractStatement.exceptionHandler(AbstractStatement.java:165)
                    // org.evosuite.testcase.statements.MethodStatement.execute(MethodStatement.java:219)
                    // org.evosuite.testcase.execution.TestRunnable.executeStatements(TestRunnable.java:286)
                    // org.evosuite.testcase.execution.TestRunnable.call(TestRunnable.java:192)
                    // org.evosuite.testcase.execution.TestRunnable.call(TestRunnable.java:49)
                    // java.base/java.util.concurrent.FutureTask.run(FutureTask.java:264)
                    // java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1128)
                    // java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:628)
                    // java.base/java.lang.Thread.run(Thread.java:829)
                    //
                    verifyException("org.fusesource.jansi.internal.MingwSupport", e);
                }
            }
        });
        future.get(4000, TimeUnit.MILLISECONDS);
    }

    @Test(timeout = 4000)
    public void test1() throws Throwable {
        Future<?> future = executor.submit(new Runnable() {
            @Override
            public void run() {
                MingwSupport mingwSupport0 = new MingwSupport();
                String string0 = mingwSupport0.getConsoleName(true);
                assertNull(string0);
            }
        });
        future.get(4000, TimeUnit.MILLISECONDS);
    }

    @Test(timeout = 4000)
    public void test2() throws Throwable {
        EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile("/home/ali/.dotnet/tools/stty.exe");
        byte[] byteArray0 = new byte[0];
        FileSystemHandling.appendDataToFile(evoSuiteFile0, byteArray0);
        MingwSupport mingwSupport0 = new MingwSupport();
    }

    @Test(timeout = 4000)
    public void test3() throws Throwable {
        EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile("/opt/maven/bin/tty.exe");
        byte[] byteArray0 = new byte[8];
        FileSystemHandling.appendDataToFile(evoSuiteFile0, byteArray0);
        MingwSupport mingwSupport0 = new MingwSupport();
    }

    @Test(timeout = 4000)
    public void test4() throws Throwable {
        Future<?> future = executor.submit(new Runnable() {
            @Override
            public void run() {
                MingwSupport mingwSupport0 = new MingwSupport();
                String string0 = mingwSupport0.getConsoleName(false);
                assertNull(string0);
            }
        });
        future.get(4000, TimeUnit.MILLISECONDS);
    }
}
