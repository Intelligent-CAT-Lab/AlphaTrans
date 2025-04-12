

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
import org.apache.commons.fileupload.DefaultFileItemFactory;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultFileItemFactory_ESTest extends DefaultFileItemFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      MockFile mockFile0 = new MockFile("C5AWUwSj8ab#HRV;P", "V_rMYkO'#++=toF5an6");
      DefaultFileItemFactory defaultFileItemFactory0 = new DefaultFileItemFactory(2515, mockFile0);
      assertEquals("ISO-8859-1", defaultFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultFileItemFactory defaultFileItemFactory0 = DefaultFileItemFactory.DefaultFileItemFactory1();
      assertEquals(0, defaultFileItemFactory0.getSizeThreshold());
  }
}
