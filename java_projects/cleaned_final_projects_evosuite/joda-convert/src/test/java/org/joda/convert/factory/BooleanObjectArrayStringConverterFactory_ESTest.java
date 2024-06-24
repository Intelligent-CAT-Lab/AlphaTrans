
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
import org.joda.convert.factory.BooleanArrayStringConverterFactory;
import org.joda.convert.factory.BooleanObjectArrayStringConverterFactory;
import org.joda.convert.factory.NumericArrayStringConverterFactory;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BooleanObjectArrayStringConverterFactory_ESTest extends BooleanObjectArrayStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      NumericArrayStringConverterFactory numericArrayStringConverterFactory0 = (NumericArrayStringConverterFactory)NumericArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        numericArrayStringConverterFactory0.toString();
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Class<Object> class0 = Object.class;
      BooleanArrayStringConverterFactory booleanArrayStringConverterFactory0 = (BooleanArrayStringConverterFactory)BooleanArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        booleanArrayStringConverterFactory0.findConverter(class0);
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      BooleanObjectArrayStringConverterFactory booleanObjectArrayStringConverterFactory0 = (BooleanObjectArrayStringConverterFactory)BooleanObjectArrayStringConverterFactory.INSTANCE;
      Class<Boolean> class0 = Boolean.class;
      StringConverter stringConverter0 = booleanObjectArrayStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      BooleanObjectArrayStringConverterFactory booleanObjectArrayStringConverterFactory0 = (BooleanObjectArrayStringConverterFactory)BooleanObjectArrayStringConverterFactory.INSTANCE;
      String string0 = booleanObjectArrayStringConverterFactory0.toString();
      assertEquals("BooleanObjectArrayStringConverterFactory", string0);
  }
}
