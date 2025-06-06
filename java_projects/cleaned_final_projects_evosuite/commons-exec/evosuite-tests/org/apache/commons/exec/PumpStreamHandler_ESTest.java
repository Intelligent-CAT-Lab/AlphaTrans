
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

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.BufferedOutputStream;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PipedInputStream;
import java.io.SequenceInputStream;
import java.time.Duration;
import java.util.Enumeration;
import org.apache.commons.exec.PumpStreamHandler;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.evosuite.runtime.mock.java.io.MockPrintStream;
import org.evosuite.runtime.mock.java.lang.MockThread;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PumpStreamHandler_ESTest extends PumpStreamHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("t+hw_");
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2(mockFileOutputStream0, mockFileOutputStream0);
      pumpStreamHandler0.setProcessInputStream(mockFileOutputStream0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler1((OutputStream) null);
      OutputStream outputStream0 = pumpStreamHandler0.getOut();
      assertNull(outputStream0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler1((OutputStream) null);
      OutputStream outputStream0 = pumpStreamHandler0.getErr();
      assertNull(outputStream0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      BufferedOutputStream bufferedOutputStream0 = new BufferedOutputStream((OutputStream) null, 1);
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2(bufferedOutputStream0, (OutputStream) null);
      Enumeration<ByteArrayInputStream> enumeration0 = (Enumeration<ByteArrayInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      Thread thread0 = pumpStreamHandler0.createPump1(sequenceInputStream0, bufferedOutputStream0, true);
      assertTrue(thread0.isDaemon());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Thread thread0 = MockThread.currentThread();
      MockPrintStream mockPrintStream0 = new MockPrintStream("(bQ;SuuIS8nfg^=");
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2(mockPrintStream0, mockPrintStream0);
      // Undeclared exception!
      try { 
        pumpStreamHandler0.stopThread(thread0, (-2044L));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // timeout value is negative
         //
         verifyException("java.lang.Thread", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      pumpStreamHandler0.stop0();
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2((OutputStream) null, (OutputStream) null);
      pumpStreamHandler0.stop0();
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      DataOutputStream dataOutputStream0 = new DataOutputStream(outputStream0);
      InputStream inputStream0 = InputStream.nullInputStream();
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler3(dataOutputStream0, dataOutputStream0, inputStream0);
      pumpStreamHandler0.createProcessErrorPump(inputStream0, dataOutputStream0);
      pumpStreamHandler0.stop();
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream("(bQ;SuuIS8nfg^=");
      MockPrintStream mockPrintStream0 = new MockPrintStream("(bQ;SuuIS8nfg^=");
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2(mockFileOutputStream0, mockPrintStream0);
      pumpStreamHandler0.stop0();
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2((OutputStream) null, (OutputStream) null);
      pumpStreamHandler0.setProcessOutputStream((InputStream) null);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      DataOutputStream dataOutputStream0 = new DataOutputStream(outputStream0);
      InputStream inputStream0 = InputStream.nullInputStream();
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler3(dataOutputStream0, dataOutputStream0, inputStream0);
      MockPrintStream mockPrintStream0 = new MockPrintStream(dataOutputStream0, false);
      pumpStreamHandler0.setProcessInputStream(mockPrintStream0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      // Undeclared exception!
      try { 
        pumpStreamHandler0.setProcessInputStream((OutputStream) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.PumpStreamHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      byte[] byteArray0 = new byte[3];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      pumpStreamHandler0.setProcessErrorStream(byteArrayInputStream0);
      assertEquals(3, byteArrayInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler2((OutputStream) null, (OutputStream) null);
      pumpStreamHandler0.setProcessErrorStream((InputStream) null);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      pumpStreamHandler0.setProcessOutputStream((InputStream) null);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      OutputStream outputStream0 = pumpStreamHandler0.getOut();
      byte[] byteArray0 = new byte[7];
      ByteArrayInputStream byteArrayInputStream0 = new ByteArrayInputStream(byteArray0);
      pumpStreamHandler0.createProcessOutputPump(byteArrayInputStream0, outputStream0);
      assertEquals(7, byteArrayInputStream0.available());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      pumpStreamHandler0.start();
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream();
      DataOutputStream dataOutputStream0 = new DataOutputStream(byteArrayOutputStream0);
      InputStream inputStream0 = InputStream.nullInputStream();
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler3(dataOutputStream0, dataOutputStream0, inputStream0);
      pumpStreamHandler0.setStopTimeout1((-1L));
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      Thread thread0 = MockThread.currentThread();
      pumpStreamHandler0.stopThread(thread0, (-1L));
      //  // Unstable assertion: assertEquals(18, thread0.countStackFrames());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      DataOutputStream dataOutputStream0 = new DataOutputStream(outputStream0);
      InputStream inputStream0 = InputStream.nullInputStream();
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler3(dataOutputStream0, dataOutputStream0, inputStream0);
      Duration duration0 = pumpStreamHandler0.getStopTimeout();
      pumpStreamHandler0.setStopTimeout0(duration0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler1((OutputStream) null);
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      Thread thread0 = pumpStreamHandler0.createPump0(pipedInputStream0, (OutputStream) null);
      assertTrue(thread0.isDaemon());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler0();
      OutputStream outputStream0 = pumpStreamHandler0.getErr();
      assertNotNull(outputStream0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      OutputStream outputStream0 = OutputStream.nullOutputStream();
      DataOutputStream dataOutputStream0 = new DataOutputStream(outputStream0);
      InputStream inputStream0 = InputStream.nullInputStream();
      PumpStreamHandler pumpStreamHandler0 = PumpStreamHandler.PumpStreamHandler3(dataOutputStream0, dataOutputStream0, inputStream0);
      pumpStreamHandler0.createProcessErrorPump(inputStream0, dataOutputStream0);
      pumpStreamHandler0.start0();
  }
}
