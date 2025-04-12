
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


package org.apache.commons.cli;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.cli.BasicParser;
import org.apache.commons.cli.Options;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BasicParser_ESTest extends BasicParser_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      BasicParser basicParser0 = new BasicParser();
      String[] stringArray0 = basicParser0.flatten((Options) null, (String[]) null, false);
      assertNull(stringArray0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      BasicParser basicParser0 = new BasicParser();
      String[] stringArray0 = new String[0];
      String[] stringArray1 = basicParser0.flatten((Options) null, stringArray0, true);
      assertEquals(0, stringArray1.length);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      BasicParser basicParser0 = new BasicParser();
      String[] stringArray0 = new String[8];
      String[] stringArray1 = basicParser0.flatten((Options) null, stringArray0, false);
      assertSame(stringArray0, stringArray1);
  }
}
