
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
import org.joda.convert.OptionalLongStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptionalLongStringConverter_ESTest extends OptionalLongStringConverter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      OptionalLongStringConverter optionalLongStringConverter0 = new OptionalLongStringConverter();
      // Undeclared exception!
      try { 
        optionalLongStringConverter0.convertToString(optionalLongStringConverter0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.IllegalArgumentException: java.lang.ClassCastException@7f87a618
         //
         verifyException("org.joda.convert.OptionalLongStringConverter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      OptionalLongStringConverter optionalLongStringConverter0 = new OptionalLongStringConverter();
      Class<Integer> class0 = Integer.class;
      // Undeclared exception!
      try { 
        optionalLongStringConverter0.convertFromString(class0, "Q4Y L");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"Q4Y L\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Class<Integer> class0 = Integer.class;
      OptionalLongStringConverter optionalLongStringConverter0 = new OptionalLongStringConverter();
      Object object0 = optionalLongStringConverter0.convertFromString(class0, "7");
      String string0 = optionalLongStringConverter0.convertToString(object0);
      assertEquals("7", string0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Class<Integer> class0 = Integer.class;
      OptionalLongStringConverter optionalLongStringConverter0 = new OptionalLongStringConverter();
      Object object0 = optionalLongStringConverter0.convertFromString(class0, "");
      String string0 = optionalLongStringConverter0.convertToString(object0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      OptionalLongStringConverter optionalLongStringConverter0 = new OptionalLongStringConverter();
      Class<?> class0 = optionalLongStringConverter0.getEffectiveType();
      assertFalse(class0.isSynthetic());
  }
}
