
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
import org.joda.convert.factory.CharObjectArrayStringConverterFactory;
import org.joda.convert.factory.NumericObjectArrayStringConverterFactory;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CharObjectArrayStringConverterFactory_ESTest extends CharObjectArrayStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      NumericObjectArrayStringConverterFactory numericObjectArrayStringConverterFactory0 = (NumericObjectArrayStringConverterFactory)NumericObjectArrayStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        numericObjectArrayStringConverterFactory0.toString();
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      BooleanArrayStringConverterFactory booleanArrayStringConverterFactory0 = (BooleanArrayStringConverterFactory)BooleanArrayStringConverterFactory.INSTANCE;
      Class<Character> class0 = Character.class;
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
      CharObjectArrayStringConverterFactory charObjectArrayStringConverterFactory0 = (CharObjectArrayStringConverterFactory)CharObjectArrayStringConverterFactory.INSTANCE;
      Class<Object> class0 = Object.class;
      StringConverter stringConverter0 = charObjectArrayStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      CharObjectArrayStringConverterFactory charObjectArrayStringConverterFactory0 = (CharObjectArrayStringConverterFactory)CharObjectArrayStringConverterFactory.INSTANCE;
      String string0 = charObjectArrayStringConverterFactory0.toString();
      assertEquals("CharObjectArrayStringConverterFactory", string0);
  }
}
