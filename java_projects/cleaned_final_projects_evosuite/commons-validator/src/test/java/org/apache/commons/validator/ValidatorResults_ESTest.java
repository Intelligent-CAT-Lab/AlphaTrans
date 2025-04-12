

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



package org.apache.commons.validator;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Map;
import java.util.Set;
import org.apache.commons.validator.Field;
import org.apache.commons.validator.ValidatorResult;
import org.apache.commons.validator.ValidatorResults;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ValidatorResults_ESTest extends ValidatorResults_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      Field field0 = new Field();
      validatorResults0.add0(field0, "org.apache.commons.validator.ValidatorResult$ResultStatus", false);
      ValidatorResult validatorResult0 = validatorResults0.getValidatorResult((String) null);
      assertNotNull(validatorResult0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      // Undeclared exception!
      try { 
        validatorResults0.merge((ValidatorResults) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.hResults = null;
      // Undeclared exception!
      try { 
        validatorResults0.isEmpty();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.hResults = null;
      // Undeclared exception!
      try { 
        validatorResults0.getValidatorResult("[]");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.hResults = null;
      // Undeclared exception!
      try { 
        validatorResults0.getResultValueMap();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.hResults = null;
      // Undeclared exception!
      try { 
        validatorResults0.getPropertyNames();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.hResults = null;
      // Undeclared exception!
      try { 
        validatorResults0.clear();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      // Undeclared exception!
      try { 
        validatorResults0.add1((Field) null, "", true, "");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      // Undeclared exception!
      try { 
        validatorResults0.add0((Field) null, "L*", true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResults", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      Field field0 = new Field();
      Object object0 = new Object();
      validatorResults0.add1(field0, "", false, object0);
      validatorResults0.add1(field0, "~+^*", false, object0);
      assertNull(field0.getProperty());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      ValidatorResult validatorResult0 = validatorResults0.getValidatorResult((String) null);
      assertNull(validatorResult0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      Field field0 = new Field();
      Object object0 = new Object();
      validatorResults0.add1(field0, "[]", false, object0);
      Map<String, Object> map0 = validatorResults0.getResultValueMap();
      assertFalse(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      Field field0 = new Field();
      validatorResults0.add0(field0, "[]", true);
      Map<String, Object> map0 = validatorResults0.getResultValueMap();
      assertTrue(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      boolean boolean0 = validatorResults0.isEmpty();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.clear();
      assertTrue(validatorResults0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      validatorResults0.merge(validatorResults0);
      assertTrue(validatorResults0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      assertTrue(validatorResults0.isEmpty());
      
      Field field0 = new Field();
      validatorResults0.add0(field0, "[]", true);
      boolean boolean0 = validatorResults0.isEmpty();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      ValidatorResults validatorResults0 = new ValidatorResults();
      Set<String> set0 = validatorResults0.getPropertyNames();
      assertEquals(0, set0.size());
  }
}
