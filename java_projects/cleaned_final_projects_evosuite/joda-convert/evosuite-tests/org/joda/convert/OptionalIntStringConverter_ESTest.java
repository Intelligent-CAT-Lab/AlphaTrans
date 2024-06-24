
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
import org.joda.convert.OptionalIntStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptionalIntStringConverter_ESTest extends OptionalIntStringConverter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      OptionalIntStringConverter optionalIntStringConverter0 = new OptionalIntStringConverter();
      Object object0 = new Object();
      // Undeclared exception!
      try { 
        optionalIntStringConverter0.convertToString(object0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.IllegalArgumentException: java.lang.ClassCastException@1851f3a9
         //
         verifyException("org.joda.convert.OptionalIntStringConverter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      OptionalIntStringConverter optionalIntStringConverter0 = new OptionalIntStringConverter();
      Class<Integer> class0 = Integer.class;
      // Undeclared exception!
      try { 
        optionalIntStringConverter0.convertFromString(class0, "isPresent");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
         //
         // For input string: \"isPresent\"
         //
         verifyException("java.lang.NumberFormatException", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      OptionalIntStringConverter optionalIntStringConverter0 = new OptionalIntStringConverter();
      Class<Integer> class0 = Integer.class;
      Object object0 = optionalIntStringConverter0.convertFromString(class0, "9");
      String string0 = optionalIntStringConverter0.convertToString(object0);
      assertEquals("9", string0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      OptionalIntStringConverter optionalIntStringConverter0 = new OptionalIntStringConverter();
      Class<Integer> class0 = Integer.class;
      Object object0 = optionalIntStringConverter0.convertFromString(class0, "");
      String string0 = optionalIntStringConverter0.convertToString(object0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      OptionalIntStringConverter optionalIntStringConverter0 = new OptionalIntStringConverter();
      Class<?> class0 = optionalIntStringConverter0.getEffectiveType();
      assertFalse(class0.isPrimitive());
  }
}
