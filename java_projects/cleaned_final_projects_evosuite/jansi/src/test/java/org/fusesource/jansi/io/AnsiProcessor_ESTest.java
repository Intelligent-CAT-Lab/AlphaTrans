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

import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FilterOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.util.ArrayList;
import java.util.ConcurrentModificationException;
import java.util.Iterator;

import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.evosuite.runtime.EvoAssertions.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.junit.Assert.*;

@RunWith(EvoRunner.class)
@EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true)
public class AnsiProcessor_ESTest extends AnsiProcessor_ESTest_scaffolding {

    @Test(timeout = 4000)
    public void test000() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) null);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 74);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test001() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) null);
        arrayList0.add((Object) ansiProcessor0);
        // Undeclared exception!
        try {
            ansiProcessor0.processEscapeCommand(arrayList0, 72);
            fail("Expecting exception: ClassCastException");

        } catch (ClassCastException e) {
            //
            // class org.fusesource.jansi.io.AnsiProcessor cannot be cast to class java.lang.Integer
            // (org.fusesource.jansi.io.AnsiProcessor is in unnamed module of loader
            // org.evosuite.instrumentation.InstrumentingClassLoader @39d9ccdf; java.lang.Integer is in module java.base
            // of loader 'bootstrap')
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test002() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ansiProcessor0.processCursorRight((-1001));
    }

    @Test(timeout = 4000)
    public void test003() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ansiProcessor0.processCursorDownLine((-2292));
    }

    @Test(timeout = 4000)
    public void test004() throws Throwable {
        File file0 = MockFile.createTempFile("axpA", "axpA");
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0, false);
        DataOutputStream dataOutputStream0 = new DataOutputStream(mockFileOutputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(dataOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        ansiProcessor0.processUnknownExtension(arrayList0, (byte) 0);
        assertTrue(arrayList0.isEmpty());
    }

    @Test(timeout = 4000)
    public void test005() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processScrollDown(1);
    }

    @Test(timeout = 4000)
    public void test006() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processInsertLine(4589);
    }

    @Test(timeout = 4000)
    public void test007() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processEraseScreen((-1));
    }

    @Test(timeout = 4000)
    public void test008() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processDeleteLine(0);
    }

    @Test(timeout = 4000)
    public void test009() throws Throwable {
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("b+PXI+xGbhy2>s", false);
        FilterOutputStream filterOutputStream0 = new FilterOutputStream(mockFileOutputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(filterOutputStream0);
        ansiProcessor0.processCursorUp(0);
    }

    @Test(timeout = 4000)
    public void test010() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ansiProcessor0.processCursorLeft((-1417));
    }

    @Test(timeout = 4000)
    public void test011() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ansiProcessor0.processCursorDown(7);
    }

    @Test(timeout = 4000)
    public void test012() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processChangeWindowTitle("*-uQ");
    }

    @Test(timeout = 4000)
    public void test013() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processChangeIconName("u7Jnj^cT<]?K 6X8\"T");
    }

    @Test(timeout = 4000)
    public void test014() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        // Undeclared exception!
        try {
            ansiProcessor0.processOperatingSystemCommand((ArrayList<Object>) null);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test015() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        // Undeclared exception!
        try {
            ansiProcessor0.processEscapeCommand(arrayList0, 67);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test016() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        try {
            ansiProcessor0.processEscapeCommand(arrayList0, 67);
            fail("Expecting exception: IOException");

        } catch (IOException e) {
            //
            // Pipe not connected
            //
            verifyException("java.io.PipedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test017() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        // Undeclared exception!
        try {
            ansiProcessor0.processCursorRight(88);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test018() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        try {
            ansiProcessor0.processCursorRight(98);
            fail("Expecting exception: IOException");

        } catch (IOException e) {
            //
            // Pipe not connected
            //
            verifyException("java.io.PipedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test019() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        // Undeclared exception!
        try {
            ansiProcessor0.processCursorDownLine(100);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test020() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        try {
            ansiProcessor0.processCursorDownLine(117);
            fail("Expecting exception: IOException");

        } catch (IOException e) {
            //
            // Pipe not connected
            //
            verifyException("java.io.PipedOutputStream", e);
        }
    }

    @Test(timeout = 4000)
    public void test021() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        // Undeclared exception!
        try {
            ansiProcessor0.processCharsetSelect0((ArrayList<Object>) null);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test022() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        Iterator<Object> iterator0 = (Iterator<Object>) mock(Iterator.class, new ViolatedAssumptionAnswer());
        doReturn(true, false).when(iterator0).hasNext();
        doReturn((Object) null).when(iterator0).next();
        // Undeclared exception!
        try {
            ansiProcessor0.getNextOptionInt(iterator0);
            fail("Expecting exception: IllegalArgumentException");

        } catch (IllegalArgumentException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test023() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        Object object0 = new Object();
        Iterator<Object> iterator0 = arrayList0.iterator();
        arrayList0.add(object0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        // Undeclared exception!
        try {
            ansiProcessor0.getNextOptionInt(iterator0);
            fail("Expecting exception: ConcurrentModificationException");

        } catch (ConcurrentModificationException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("java.util.ArrayList$Itr", e);
        }
    }

    @Test(timeout = 4000)
    public void test024() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        // Undeclared exception!
        try {
            ansiProcessor0.getNextOptionInt((Iterator<Object>) null);
            fail("Expecting exception: NullPointerException");

        } catch (NullPointerException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test025() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 72);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test026() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) ansiProcessor0);
        // Undeclared exception!
        try {
            ansiProcessor0.processEscapeCommand(arrayList0, 84);
            fail("Expecting exception: ClassCastException");

        } catch (ClassCastException e) {
            //
            // class org.fusesource.jansi.io.AnsiProcessor cannot be cast to class java.lang.Integer
            // (org.fusesource.jansi.io.AnsiProcessor is in unnamed module of loader
            // org.evosuite.instrumentation.InstrumentingClassLoader @39d9ccdf; java.lang.Integer is in module java.base
            // of loader 'bootstrap')
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test027() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) null);
        // Undeclared exception!
        try {
            ansiProcessor0.processCharsetSelect0(arrayList0);
            fail("Expecting exception: IllegalArgumentException");

        } catch (IllegalArgumentException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test028() throws Throwable {
        Character character0 = Character.valueOf('c');
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) character0);
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        // Undeclared exception!
        try {
            ansiProcessor0.processOperatingSystemCommand(arrayList0);
            fail("Expecting exception: IllegalArgumentException");

        } catch (IllegalArgumentException e) {
            //
            // no message in exception (getMessage() returned null)
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test029() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 4691);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test030() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) ansiProcessor0);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 109);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test031() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        arrayList0.add((Object) null);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 109);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test032() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, (-2417));
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test033() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 117);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test034() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand((ArrayList<Object>) null, 116);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test035() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 115);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test036() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 114);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test037() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 113);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test038() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 112);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test039() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 111);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test040() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 110);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test041() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 108);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test042() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 107);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test043() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 105);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test044() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 104);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test045() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 103);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test046() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 102);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test047() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 101);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test048() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand((ArrayList<Object>) null, 100);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test049() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 99);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test050() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 98);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test051() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 97);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test052() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 96);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test053() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 95);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test054() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 94);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test055() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 93);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test056() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 92);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test057() throws Throwable {
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 91);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test058() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 90);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test059() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 89);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test060() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand((ArrayList<Object>) null, 88);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test061() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 87);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test062() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 86);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test063() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 85);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test064() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 83);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test065() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 82);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test066() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 81);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test067() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 80);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test068() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 79);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test069() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 78);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test070() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 75);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test071() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 73);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test072() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 71);
        assertFalse(boolean0);
    }

    @Test(timeout = 4000)
    public void test073() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 70);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test074() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("/n>a C43#%t)g0");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 69);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test075() throws Throwable {
        BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream((OutputStream) null);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(bufferedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 67);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test076() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        Iterator<Object> iterator0 = (Iterator<Object>) mock(Iterator.class, new ViolatedAssumptionAnswer());
        doReturn(true).when(iterator0).hasNext();
        doReturn(arrayList0).when(iterator0).next();
        // Undeclared exception!
        try {
            ansiProcessor0.getNextOptionInt(iterator0);
            fail("Expecting exception: ClassCastException");

        } catch (ClassCastException e) {
            //
            // class java.util.ArrayList cannot be cast to class java.lang.Integer (java.util.ArrayList and
            // java.lang.Integer are in module java.base of loader 'bootstrap')
            //
            verifyException("org.fusesource.jansi.io.AnsiProcessor", e);
        }
    }

    @Test(timeout = 4000)
    public void test077() throws Throwable {
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 65);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test078() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processSetForegroundColorExt1((-1268), (-1725), (-1725));
    }

    @Test(timeout = 4000)
    public void test079() throws Throwable {
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        ansiProcessor0.processEraseLine(766);
    }

    @Test(timeout = 4000)
    public void test080() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 66);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test081() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processSetForegroundColor0((-377));
    }

    @Test(timeout = 4000)
    public void test082() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processCursorTo(0, 28);
    }

    @Test(timeout = 4000)
    public void test083() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processSetBackgroundColor0((-4226));
    }

    @Test(timeout = 4000)
    public void test084() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ansiProcessor0.processDefaultBackgroundColor();
    }

    @Test(timeout = 4000)
    public void test085() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 106);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test086() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processSetBackgroundColor1(2491, false);
    }

    @Test(timeout = 4000)
    public void test087() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 68);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test088() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processCursorToColumn((-1));
    }

    @Test(timeout = 4000)
    public void test089() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processSetForegroundColorExt0(2491);
    }

    @Test(timeout = 4000)
    public void test090() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 76);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test091() throws Throwable {
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        ansiProcessor0.processSetBackgroundColorExt0(2418);
    }

    @Test(timeout = 4000)
    public void test092() throws Throwable {
        File file0 = MockFile.createTempFile("axpA", "axpA");
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0, false);
        DataOutputStream dataOutputStream0 = new DataOutputStream(mockFileOutputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(dataOutputStream0);
        ansiProcessor0.processRestoreCursorPosition();
    }

    @Test(timeout = 4000)
    public void test093() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processCursorUpLine(2491);
    }

    @Test(timeout = 4000)
    public void test094() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processScrollUp(2491);
    }

    @Test(timeout = 4000)
    public void test095() throws Throwable {
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        ansiProcessor0.processSetBackgroundColorExt1(1285, 1285, 766);
    }

    @Test(timeout = 4000)
    public void test096() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processDefaultTextColor();
    }

    @Test(timeout = 4000)
    public void test097() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processSetForegroundColor1(2491, true);
    }

    @Test(timeout = 4000)
    public void test098() throws Throwable {
        AnsiProcessor ansiProcessor0 = new AnsiProcessor((OutputStream) null);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 77);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test099() throws Throwable {
        File file0 = MockFile.createTempFile("u7Jnj^cT<]?K 6X8\"T", (String) null);
        MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockFileOutputStream0);
        ansiProcessor0.processSaveCursorPosition();
    }

    @Test(timeout = 4000)
    public void test100() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processAttributeReset();
    }

    @Test(timeout = 4000)
    public void test101() throws Throwable {
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        ansiProcessor0.processChangeIconNameAndWindowTitle("org.fusesource.jansi.io.AnsiProcessor");
    }

    @Test(timeout = 4000)
    public void test102() throws Throwable {
        ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(byteArrayOutputStream0);
        ansiProcessor0.processSetAttribute(0);
    }

    @Test(timeout = 4000)
    public void test103() throws Throwable {
        PipedInputStream pipedInputStream0 = new PipedInputStream();
        PipedOutputStream pipedOutputStream0 = new PipedOutputStream(pipedInputStream0);
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(pipedOutputStream0);
        ArrayList<Object> arrayList0 = new ArrayList<Object>();
        boolean boolean0 = ansiProcessor0.processEscapeCommand(arrayList0, 84);
        assertTrue(boolean0);
    }

    @Test(timeout = 4000)
    public void test104() throws Throwable {
        OutputStream outputStream0 = OutputStream.nullOutputStream();
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(outputStream0);
        ansiProcessor0.processCharsetSelect1(1630, '~');
    }

    @Test(timeout = 4000)
    public void test105() throws Throwable {
        MockPrintStream mockPrintStream0 = new MockPrintStream("*-uQ");
        AnsiProcessor ansiProcessor0 = new AnsiProcessor(mockPrintStream0);
        ansiProcessor0.processUnknownOperatingSystemCommand((-377), "HM}r~");
    }
}
