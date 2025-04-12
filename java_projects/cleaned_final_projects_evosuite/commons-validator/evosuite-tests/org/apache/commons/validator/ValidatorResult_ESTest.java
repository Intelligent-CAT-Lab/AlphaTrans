

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
import java.util.Iterator;
import java.util.Map;
import org.apache.commons.validator.Field;
import org.apache.commons.validator.ValidatorResult;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class ValidatorResult_ESTest extends ValidatorResult_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      ValidatorResult validatorResult0 = new ValidatorResult((Field) null);
      Field field0 = validatorResult0.getField();
      assertNull(field0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedListProperty("g(a\rQk");
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      Field field1 = validatorResult0.getField();
      assertSame(field1, field0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      field0.setClientValidation(false);
      Field field1 = validatorResult0.getField();
      assertEquals(0, field1.getPage());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      field0.setPage(1701);
      Field field1 = validatorResult0.getField();
      assertNull(field1.getDepends());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      field0.page = (-4423);
      Field field1 = validatorResult0.getField();
      assertEquals(0, field1.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      field0.setFieldOrder(1086);
      Field field1 = validatorResult0.getField();
      assertNull(field1.getProperty());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      field0.setFieldOrder((-1604));
      Field field1 = validatorResult0.getField();
      assertNull(field1.getDepends());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.isValid("[]");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResult", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.getResult("X&5g^!+`");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResult", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.getActions();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Collections$UnmodifiableMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.getActionMap();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Collections$UnmodifiableMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.containsAction("[]");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      Map<String, ValidatorResult.ResultStatus> map0 = validatorResult0.getActionMap();
      validatorResult0.hAction = map0;
      // Undeclared exception!
      try { 
        validatorResult0.add1("[]", false, "[]");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Collections$UnmodifiableMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.add1("[]", false, field0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResult", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.hAction = null;
      // Undeclared exception!
      try { 
        validatorResult0.add0("[]", true);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.ValidatorResult", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      ValidatorResult.ResultStatus validatorResult_ResultStatus0 = new ValidatorResult.ResultStatus(1, (Object) null, validatorResult0, false);
      assertFalse(validatorResult_ResultStatus0.isValid());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      Object object0 = validatorResult0.getResult("org.apache.commons.validator.ValidatorResult");
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.add1("[]", true, field0);
      Field field1 = (Field)validatorResult0.getResult("[]");
      assertEquals(0, field1.getPage());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      boolean boolean0 = validatorResult0.isValid("[]");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.add1("[]", false, field0);
      boolean boolean0 = validatorResult0.containsAction("[]");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      boolean boolean0 = validatorResult0.containsAction("[]");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      ValidatorResult validatorResult0 = new ValidatorResult((Field) null);
      Iterator<String> iterator0 = validatorResult0.getActions();
      assertNotNull(iterator0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      Map<String, ValidatorResult.ResultStatus> map0 = validatorResult0.getActionMap();
      validatorResult0.hAction = map0;
      // Undeclared exception!
      try { 
        validatorResult0.add0("[]", false);
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Collections$UnmodifiableMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      validatorResult0.add0("[]", true);
      boolean boolean0 = validatorResult0.isValid("[]");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Object object0 = new Object();
      ValidatorResult validatorResult0 = new ValidatorResult((Field) null);
      ValidatorResult.ResultStatus validatorResult_ResultStatus0 = new ValidatorResult.ResultStatus((-1), object0, validatorResult0, false);
      validatorResult_ResultStatus0.setResult((Object) null);
      assertFalse(validatorResult_ResultStatus0.isValid());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      ValidatorResult validatorResult0 = new ValidatorResult((Field) null);
      ValidatorResult.ResultStatus validatorResult_ResultStatus0 = ValidatorResult.ResultStatus.ResultStatus0(validatorResult0, false, validatorResult0);
      validatorResult_ResultStatus0.setValid(false);
      assertFalse(validatorResult_ResultStatus0.isValid());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Field field0 = new Field();
      ValidatorResult validatorResult0 = new ValidatorResult(field0);
      ValidatorResult.ResultStatus validatorResult_ResultStatus0 = ValidatorResult.ResultStatus.ResultStatus0(validatorResult0, true, field0);
      validatorResult_ResultStatus0.getResult();
      assertTrue(validatorResult_ResultStatus0.isValid());
  }
}
