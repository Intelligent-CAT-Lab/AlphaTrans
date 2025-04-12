
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
import java.io.DataInputStream;
import java.io.File;
import java.io.OutputStream;
import java.io.PipedInputStream;
import java.io.SequenceInputStream;
import java.util.Enumeration;
import org.apache.commons.exec.InputStreamPumper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.mock.java.io.MockFileInputStream;
import org.evosuite.runtime.mock.java.io.MockFileOutputStream;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class InputStreamPumper_ESTest extends InputStreamPumper_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      File file0 = MockFile.createTempFile("Got exception while reading/writing the stream", ":WB=UH_5qOzP_2i5");
      MockFileInputStream mockFileInputStream0 = new MockFileInputStream(file0);
      MockFileOutputStream mockFileOutputStream0 = new MockFileOutputStream(file0);
      mockFileOutputStream0.write(927);
      InputStreamPumper inputStreamPumper0 = new InputStreamPumper(mockFileInputStream0, mockFileOutputStream0);
      inputStreamPumper0.run();
      assertEquals(10000L, file0.length());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      PipedInputStream pipedInputStream0 = new PipedInputStream();
      InputStreamPumper inputStreamPumper0 = new InputStreamPumper(pipedInputStream0, (OutputStream) null);
      inputStreamPumper0.run();
      assertEquals(100, InputStreamPumper.SLEEPING_TIME);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Enumeration<DataInputStream> enumeration0 = (Enumeration<DataInputStream>) mock(Enumeration.class, new ViolatedAssumptionAnswer());
      doReturn(false).when(enumeration0).hasMoreElements();
      SequenceInputStream sequenceInputStream0 = new SequenceInputStream(enumeration0);
      InputStreamPumper inputStreamPumper0 = new InputStreamPumper(sequenceInputStream0, (OutputStream) null);
      inputStreamPumper0.stopProcessing();
      inputStreamPumper0.run();
      assertEquals(100, InputStreamPumper.SLEEPING_TIME);
  }
}
