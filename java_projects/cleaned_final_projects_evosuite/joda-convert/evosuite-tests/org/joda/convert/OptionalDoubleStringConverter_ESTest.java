
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
import org.joda.convert.OptionalDoubleStringConverter;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptionalDoubleStringConverter_ESTest extends OptionalDoubleStringConverter_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      // Undeclared exception!
      try { 
        optionalDoubleStringConverter0.convertToString(optionalDoubleStringConverter0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // java.lang.IllegalArgumentException: java.lang.ClassCastException@204af07e
         //
         verifyException("org.joda.convert.OptionalDoubleStringConverter", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      Class<Integer> class0 = Integer.class;
      // Undeclared exception!
      try { 
        optionalDoubleStringConverter0.convertFromString(class0, "AikOdfqjjTLCd<2");
        fail("Expecting exception: NumberFormatException");
      
      } catch(NumberFormatException e) {
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      Class<Integer> class0 = Integer.class;
      // Undeclared exception!
      try { 
        optionalDoubleStringConverter0.convertFromString(class0, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      Class<Integer> class0 = Integer.class;
      Object object0 = optionalDoubleStringConverter0.convertFromString(class0, "78");
      String string0 = optionalDoubleStringConverter0.convertToString(object0);
      assertEquals("78.0", string0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      Class<Integer> class0 = Integer.class;
      Object object0 = optionalDoubleStringConverter0.convertFromString(class0, "");
      String string0 = optionalDoubleStringConverter0.convertToString(object0);
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      OptionalDoubleStringConverter optionalDoubleStringConverter0 = new OptionalDoubleStringConverter();
      Class<?> class0 = optionalDoubleStringConverter0.getEffectiveType();
      assertEquals(17, class0.getModifiers());
  }
}
