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
package org.fusesource.jansi;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class WindowsSupport_ESTest extends WindowsSupport_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test0() throws Throwable {
        // Undeclared exception!
        try {
            WindowsSupport.getErrorMessage(877);
            fail("Expecting exception: UnsatisfiedLinkError");

        } catch (UnsatisfiedLinkError e) {
            //
            // 'int org.fusesource.jansi.internal.Kernel32.FormatMessageW(int, long, int, int, byte[], int, long[])'
            //
            verifyException("org.fusesource.jansi.internal.Kernel32", e);
        }
    }

    @Test(timeout = 4000)
    public void test1() throws Throwable {
        // Undeclared exception!
        try {
            WindowsSupport.getLastErrorMessage();
            fail("Expecting exception: UnsatisfiedLinkError");

        } catch (UnsatisfiedLinkError e) {
            //
            // 'int org.fusesource.jansi.internal.Kernel32.GetLastError()'
            //
            verifyException("org.fusesource.jansi.internal.Kernel32", e);
        }
    }

    @Test(timeout = 4000)
    public void test2() throws Throwable {
        WindowsSupport windowsSupport0 = new WindowsSupport();
    }
}
