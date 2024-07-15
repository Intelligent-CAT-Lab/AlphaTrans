
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


package org.joda.convert;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.EnumStringConverterFactory;
import org.joda.convert.StringConverter;
import org.joda.convert.TypeStringConverterFactory;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class EnumStringConverterFactory_ESTest extends EnumStringConverterFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        typeStringConverterFactory0.toString();
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      EnumStringConverterFactory enumStringConverterFactory0 = (EnumStringConverterFactory)EnumStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        enumStringConverterFactory0.findConverter((Class) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.convert.EnumStringConverterFactory", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Class<EnumStringConverterFactory> class0 = EnumStringConverterFactory.class;
      TypeStringConverterFactory typeStringConverterFactory0 = TypeStringConverterFactory.INSTANCE;
      // Undeclared exception!
      try { 
        typeStringConverterFactory0.findConverter(class0);
       //  fail("Expecting exception: IllegalArgumentException");
       // Unstable assertion
      } catch(IllegalArgumentException e) {
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      EnumStringConverterFactory enumStringConverterFactory0 = (EnumStringConverterFactory)EnumStringConverterFactory.INSTANCE;
      Class<Object> class0 = Object.class;
      StringConverter stringConverter0 = enumStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      EnumStringConverterFactory enumStringConverterFactory0 = (EnumStringConverterFactory)EnumStringConverterFactory.INSTANCE;
      Class<EnumStringConverterFactory> class0 = EnumStringConverterFactory.class;
      StringConverter stringConverter0 = enumStringConverterFactory0.findConverter(class0);
      assertNull(stringConverter0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Class<Object> class0 = Object.class;
      EnumStringConverterFactory.EnumStringConverter enumStringConverterFactory_EnumStringConverter0 = new EnumStringConverterFactory.EnumStringConverter(class0);
      Class<?> class1 = enumStringConverterFactory_EnumStringConverter0.getEffectiveType();
      assertFalse(class1.isPrimitive());
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      EnumStringConverterFactory enumStringConverterFactory0 = (EnumStringConverterFactory)EnumStringConverterFactory.INSTANCE;
      String string0 = enumStringConverterFactory0.toString();
      assertEquals("EnumStringConverterFactory", string0);
  }
}
