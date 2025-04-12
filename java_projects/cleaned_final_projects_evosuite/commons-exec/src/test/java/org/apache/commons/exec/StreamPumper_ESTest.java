
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
import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PipedInputStream;
import java.io.PipedOutputStream;
import java.io.PushbackInputStream;
import java.io.SequenceInputStream;
import java.util.Enumeration;
import org.apache.commons.exec.StreamPumper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class StreamPumper_ESTest extends StreamPumper_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      BufferedInputStream bufferedInputStream0 = new BufferedInputStream(sequenceInputStream0);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      StreamPumper streamPumper0 = StreamPumper.StreamPumper0(bufferedInputStream0, pipedOutputStream0);
      streamPumper0.run();
      boolean boolean0 = streamPumper0.isFinished();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      PushbackInputStream pushbackInputStream0 = new PushbackInputStream(pipedInputStream0);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      StreamPumper streamPumper0 = StreamPumper.StreamPumper0(pushbackInputStream0, pipedOutputStream0);
      streamPumper0.run();
      assertTrue(streamPumper0.isFinished());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      StreamPumper streamPumper0 = new StreamPumper(sequenceInputStream0, pipedOutputStream0, true, (byte)0);
      streamPumper0.run();
      assertTrue(streamPumper0.isFinished());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      StreamPumper streamPumper0 = StreamPumper.StreamPumper0(sequenceInputStream0, pipedOutputStream0);
      streamPumper0.run();
      streamPumper0.waitFor();
      assertTrue(streamPumper0.isFinished());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      ByteArrayOutputStream byteArrayOutputStream0 = new ByteArrayOutputStream(0);
      StreamPumper streamPumper0 = new StreamPumper(sequenceInputStream0, byteArrayOutputStream0, true, 1);
      assertFalse(streamPumper0.isFinished());
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Enumeration<SequenceInputStream> enumeration0 = (Enumeration<SequenceInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      PipedOutputStream pipedOutputStream0 = new PipedOutputStream();
      StreamPumper streamPumper0 = StreamPumper.StreamPumper0(sequenceInputStream0, pipedOutputStream0);
      boolean boolean0 = streamPumper0.isFinished();
      assertFalse(boolean0);
  }
}
