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
package org.fusesource.jansi.io;

import java.io.OutputStream;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class WindowsAnsiProcessor_ESTest extends WindowsAnsiProcessor_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test0() throws Throwable {
        WindowsAnsiProcessor windowsAnsiProcessor0 = null;
        try {
            windowsAnsiProcessor0 = new WindowsAnsiProcessor((OutputStream) null, 15L);
            fail("Expecting exception: NoClassDefFoundError");

        } catch (NoClassDefFoundError e) {
            //
            // Could not initialize class org.fusesource.jansi.internal.Kernel32$CONSOLE_SCREEN_BUFFER_INFO
            //
            verifyException("org.fusesource.jansi.io.WindowsAnsiProcessor", e);
        }
    }
}
