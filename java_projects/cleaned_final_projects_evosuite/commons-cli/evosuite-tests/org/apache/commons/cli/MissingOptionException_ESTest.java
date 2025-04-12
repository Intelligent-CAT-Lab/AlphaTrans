
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
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.cli.MissingOptionException;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MissingOptionException_ESTest extends MissingOptionException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      Integer integer0 = new Integer(1);
      linkedList0.add((Object) integer0);
      MissingOptionException missingOptionException0 = new MissingOptionException(1, linkedList0, (String) null);
      List list0 = missingOptionException0.getMissingOptions();
      assertFalse(list0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      // Undeclared exception!
      try { 
        MissingOptionException.MissingOptionException1(1, (List) null, "3cF!AtCi7c4Vm\n-");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.MissingOptionException", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      MissingOptionException missingOptionException0 = new MissingOptionException((-16), linkedList0, (String) null);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      List<Object> list0 = List.of((Object) "6^+dgsR4h5*| 2u6", (Object) "6^+dgsR4h5*| 2u6");
      MissingOptionException missingOptionException0 = MissingOptionException.MissingOptionException1(1, list0, "");
      assertNotNull(missingOptionException0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      linkedList0.add((Object) "");
      MissingOptionException missingOptionException0 = MissingOptionException.MissingOptionException1(1, linkedList0, "");
      assertNotNull(missingOptionException0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      MissingOptionException missingOptionException0 = MissingOptionException.MissingOptionException1(1, linkedList0, ", ");
      List list0 = missingOptionException0.getMissingOptions();
      assertEquals(0, list0.size());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      LinkedList<Object> linkedList0 = new LinkedList<Object>();
      MissingOptionException missingOptionException0 = MissingOptionException.MissingOptionException1(1379, linkedList0, "X$k#k=IoA pgf9");
      List list0 = missingOptionException0.getMissingOptions();
      assertNull(list0);
  }
}
