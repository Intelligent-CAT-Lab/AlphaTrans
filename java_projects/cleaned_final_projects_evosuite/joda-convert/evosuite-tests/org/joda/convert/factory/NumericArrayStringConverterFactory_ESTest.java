
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


package org.joda.convert.factory;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.StringConverter;
import org.joda.convert.factory.BooleanObjectArrayStringConverterFactory;
import org.joda.convert.factory.CharObjectArrayStringConverterFactory;
import org.joda.convert.factory.NumericArrayStringConverterFactory;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class NumericArrayStringConverterFactory_ESTest extends NumericArrayStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CharObjectArrayStringConverterFactory charObjectArrayStringConverterFactory0 = (CharObjectArrayStringConverterFactory)CharObjectArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        charObjectArrayStringConverterFactory0.toString();
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      NumericArrayStringConverterFactory numericArrayStringConverterFactory0 = (NumericArrayStringConverterFactory)NumericArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        numericArrayStringConverterFactory0.findConverter((Class<?>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.factory.NumericArrayStringConverterFactory", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Class<Object> class0 = Object.class;
      BooleanObjectArrayStringConverterFactory booleanObjectArrayStringConverterFactory0 = (BooleanObjectArrayStringConverterFactory)BooleanObjectArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        booleanObjectArrayStringConverterFactory0.findConverter(class0);
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      NumericArrayStringConverterFactory numericArrayStringConverterFactory0 = (NumericArrayStringConverterFactory)NumericArrayStringConverterFactory.INSTANCE;
      Class<Integer> class0 = Integer.class;
      StringConverter stringConverter0 = numericArrayStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      NumericArrayStringConverterFactory numericArrayStringConverterFactory0 = (NumericArrayStringConverterFactory)NumericArrayStringConverterFactory.INSTANCE;
      String string0 = numericArrayStringConverterFactory0.toString();
      assertEquals("NumericArrayStringConverterFactory", string0);
  }
}
