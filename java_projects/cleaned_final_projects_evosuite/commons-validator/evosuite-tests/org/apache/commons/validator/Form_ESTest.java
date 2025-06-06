

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
import java.util.LinkedList;
import java.util.List;
import org.apache.commons.validator.Field;
import org.apache.commons.validator.Form;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Form_ESTest extends Form_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Form form0 = new Form();
      form0.name = "Arg: name=";
      String string0 = form0.toString();
      assertFalse(form0.isProcessed());
      assertEquals("Form: Arg: name=\n", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Form form0 = new Form();
      form0.name = "Arg: name=";
      String string0 = form0.getName();
      assertNotNull(string0);
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Form form0 = new Form();
      form0.name = "";
      String string0 = form0.getName();
      assertNotNull(string0);
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Form form0 = new Form();
      form0.inherit = "h{IL5tqkx+D_z[)";
      String string0 = form0.getExtends();
      assertFalse(form0.isProcessed());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Form form0 = new Form();
      form0.setExtends("");
      form0.getExtends();
      assertTrue(form0.isExtending());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Form form0 = new Form();
      form0.lFields = null;
      // Undeclared exception!
      try { 
        form0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.Form", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Form form0 = new Form();
      form0.lFields = null;
      // Undeclared exception!
      try { 
        form0.getFields();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Collections$UnmodifiableCollection", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Form form0 = new Form();
      boolean boolean0 = form0.isExtending();
      assertFalse(boolean0);
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Form form0 = new Form();
      LinkedList<Field> linkedList0 = new LinkedList<Field>();
      form0.lFields = (List<Field>) linkedList0;
      Field field0 = new Field();
      linkedList0.add(field0);
      form0.toString();
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Form form0 = new Form();
      boolean boolean0 = form0.isProcessed();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Form form0 = new Form();
      form0.getName();
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Form form0 = new Form();
      form0.setExtends("");
      boolean boolean0 = form0.isExtending();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Form form0 = new Form();
      form0.setName("Arg: name=");
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Form form0 = new Form();
      form0.getExtends();
      assertFalse(form0.isProcessed());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Form form0 = new Form();
      form0.getFields();
      assertFalse(form0.isProcessed());
  }
}
