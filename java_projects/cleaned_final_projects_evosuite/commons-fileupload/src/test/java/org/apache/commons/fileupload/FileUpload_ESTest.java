

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



package org.apache.commons.fileupload;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileUpload;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FileUpload_ESTest extends FileUpload_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      FileItemFactory fileItemFactory1 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(fileItemFactory1).toString();
      fileUpload0.setFileItemFactory(fileItemFactory1);
      FileItemFactory fileItemFactory2 = fileUpload0.getFileItemFactory();
      assertSame(fileItemFactory2, fileItemFactory1);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(1, fileItemFactory0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(0, (FileItemFactory) null);
      FileItemFactory fileItemFactory0 = fileUpload0.getFileItemFactory();
      assertNull(fileItemFactory0);
  }
}
