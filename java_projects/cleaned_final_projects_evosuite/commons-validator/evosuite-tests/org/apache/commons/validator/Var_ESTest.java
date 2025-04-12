

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
import org.apache.commons.validator.Var;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Var_ESTest extends Var_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Var var0 = new Var(1, (String) null, "", "");
      assertEquals("", var0.getJsType());
      assertEquals("", var0.getValue());
      assertFalse(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Var var0 = new Var((-1), (String) null, (String) null, (String) null);
      assertFalse(var0.isResource());
      
      var0.setResource(true);
      boolean boolean0 = var0.isResource();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Var var0 = new Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "");
      var0.setValue("Var: name=");
      var0.getValue();
      assertFalse(var0.isResource());
      assertEquals("Var: name=", var0.getValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Var var0 = new Var(0, "", "", (String) null);
      var0.setValue("");
      String string0 = var0.getValue();
      assertFalse(var0.isResource());
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Var var0 = new Var(0, "", "", (String) null);
      var0.setName("sD@!");
      var0.getName();
      assertFalse(var0.isResource());
      assertEquals("sD@!", var0.getName());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Var var0 = new Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "");
      var0.setName("");
      var0.getName();
      assertFalse(var0.isResource());
      assertEquals("", var0.getName());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Var var0 = new Var(0, "", "", (String) null);
      String string0 = var0.getJsType();
      assertFalse(var0.isResource());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Var var0 = new Var((-1), (String) null, (String) null, (String) null);
      var0.setBundle("org.apache.commons.validator.Var");
      String string0 = var0.getBundle();
      assertEquals("org.apache.commons.validator.Var", string0);
      assertFalse(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Var var0 = new Var(0, "AeWI3qh|de}", "AeWI3qh|de}", "");
      var0.setBundle("");
      String string0 = var0.getBundle();
      assertEquals("", string0);
      assertFalse(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Var var0 = new Var(3188, "", "", "a;zTu9C8@s{8xNzX");
      String string0 = var0.toString();
      assertEquals("Var: name=null  value=null  resource=false  jsType=null\n", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Var var0 = new Var(1, "eD\"`+mvS,e\t-", "eD\"`+mvS,e\t-", "");
      var0.setBundle("");
      assertEquals("", var0.getJsType());
      assertEquals("eD\"`+mvS,e\t-", var0.getName());
      assertEquals("eD\"`+mvS,e\t-", var0.getValue());
      assertFalse(var0.isResource());
      assertEquals("", var0.getBundle());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Var var0 = new Var(3188, "", "", "a;zTu9C8@s{8xNzX");
      Var var1 = (Var)var0.clone();
      assertFalse(var1.isResource());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Var var0 = new Var(3188, "", "", "a;zTu9C8@s{8xNzX");
      String string0 = var0.getBundle();
      assertNull(string0);
      assertFalse(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Var var0 = new Var((-1), (String) null, (String) null, (String) null);
      boolean boolean0 = var0.isResource();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Var var0 = new Var(3188, "", "", "a;zTu9C8@s{8xNzX");
      String string0 = var0.getValue();
      assertFalse(var0.isResource());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Var var0 = new Var(3188, "", "", "a;zTu9C8@s{8xNzX");
      String string0 = var0.getName();
      assertNull(string0);
      assertFalse(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Var var0 = new Var(1, "eD\"`+mvS,e\t-", "eD\"`+mvS,e\t-", "");
      assertFalse(var0.isResource());
      
      var0.setResource(true);
      var0.toString();
      assertTrue(var0.isResource());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Var var0 = new Var(1, "eD\"`+mvS,e\t-", "eD\"`+mvS,e\t-", "");
      assertEquals("", var0.getJsType());
      
      var0.setJsType("eD\"`+mvS,e\t-");
      String string0 = var0.getJsType();
      assertEquals("eD\"`+mvS,e\t-", string0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Var var0 = new Var(1, "eD\"`+mvS,e\t-", "eD\"`+mvS,e\t-", "");
      String string0 = var0.getJsType();
      assertFalse(var0.isResource());
      assertNotNull(string0);
      assertEquals("", string0);
      assertEquals("eD\"`+mvS,e\t-", var0.getValue());
      assertEquals("eD\"`+mvS,e\t-", var0.getName());
  }
}
