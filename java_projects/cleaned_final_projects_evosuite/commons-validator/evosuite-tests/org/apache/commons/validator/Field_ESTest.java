

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
import java.lang.reflect.Array;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.validator.Arg;
import org.apache.commons.validator.Field;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Field_ESTest extends Field_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Field field0 = new Field();
      field0.setProperty("dpG'G8 F*m");
      field0.generateKey();
      assertEquals("dpG'G8 F*m", field0.getProperty());
      assertEquals(0, field0.getPage());
      assertFalse(field0.isIndexed());
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Field field0 = new Field();
      field0.setProperty("  key=");
      field0.indexedListProperty = "/s[Vy/[";
      field0.generateKey();
      assertTrue(field0.isIndexed());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Field field0 = new Field();
      field0.getArg0(1);
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Field field0 = new Field();
      field0.setDepends("Tp9~S:($*K'@*d.\"Y,");
      assertEquals(0, field0.getFieldOrder());
      assertEquals("Tp9~S:($*K'@*d.\"Y,", field0.getDepends());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Field field0 = new Field();
      assertTrue(field0.isClientValidation());
      
      field0.setClientValidation(false);
      boolean boolean0 = field0.isClientValidation();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Field field0 = new Field();
      field0.setProperty("  key=");
      String string0 = field0.getProperty();
      assertNotNull(string0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertEquals("  key=", string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Field field0 = new Field();
      field0.setProperty("");
      String string0 = field0.getProperty();
      assertEquals(0, field0.getPage());
      assertNotNull(string0);
      assertEquals(0, field0.getFieldOrder());
      assertEquals("", string0);
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Field field0 = new Field();
      field0.setPage(502);
      int int0 = field0.getPage();
      assertEquals(502, int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Field field0 = new Field();
      field0.setPage((-4551));
      int int0 = field0.getPage();
      assertEquals((-4551), int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedProperty("0FRgz[b3e+WQ=zW3ADw");
      String string0 = field0.getIndexedProperty();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertEquals("0FRgz[b3e+WQ=zW3ADw", string0);
      assertTrue(field0.isClientValidation());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedProperty("");
      String string0 = field0.getIndexedProperty();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertNotNull(string0);
      assertTrue(field0.isClientValidation());
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Field field0 = new Field();
      field0.indexedListProperty = "BaFJjva0n;X^N-V-";
      String string0 = field0.getIndexedListProperty();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertNotNull(string0);
      assertTrue(field0.isClientValidation());
      assertEquals("BaFJjva0n;X^N-V-", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedListProperty("");
      String string0 = field0.getIndexedListProperty();
      assertTrue(field0.isClientValidation());
      assertEquals("", string0);
      assertNotNull(string0);
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Field field0 = new Field();
      field0.setFieldOrder(182);
      int int0 = field0.getFieldOrder();
      assertEquals(182, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Field field0 = new Field();
      field0.setFieldOrder((-143));
      int int0 = field0.getFieldOrder();
      assertEquals((-143), int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Field field0 = new Field();
      field0.setDepends("Ki");
      String string0 = field0.getDepends();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertEquals("Ki", string0);
      assertNotNull(string0);
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Field field0 = new Field();
      field0.depends = "";
      String string0 = field0.getDepends();
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
      assertEquals("", string0);
      assertEquals(0, field0.getFieldOrder());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Field field0 = new Field();
      Arg[] argArray0 = field0.getArgs("[]");
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
      assertEquals(0, argArray0.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setResource(false);
      arg0.setKey("fa$)&L/6m;o,4");
      Field field0 = new Field();
      arg0.setPosition(696);
      field0.addArg(arg0);
      assertEquals(696, arg0.getPosition());
      
      field0.getArg1("No ValidatorAction named ", 696);
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      field0.addArg(arg0);
      assertEquals(0, arg0.getPosition());
      
      field0.getArg1("var:", 0);
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setResource(false);
      arg0.setKey("fa$)&L/6m;o,4");
      Field field0 = new Field();
      arg0.setPosition(696);
      field0.addArg(arg0);
      assertEquals(696, arg0.getPosition());
      
      field0.getArg0(696);
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      field0.addArg(arg0);
      assertEquals(0, arg0.getPosition());
      
      field0.getArg0(0);
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Field field0 = new Field();
      // Undeclared exception!
      try { 
        field0.setDepends((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.position = 5002;
      arg0.setKey("[]");
      field0.addArg(arg0);
      field0.getArgs("&-<8K3$.__|");
      // Undeclared exception!
      field0.getArgs((String) null);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      field0.addArg(arg0);
      // Undeclared exception!
      try { 
        field0.getArgs((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Field field0 = new Field();
      field0.args = null;
      // Undeclared exception!
      try { 
        field0.getArg1("[]", 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      Field field0 = new Field();
      // Undeclared exception!
      try { 
        field0.getArg1("[]", (-2372));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      Field field0 = new Field();
      field0.args = null;
      // Undeclared exception!
      try { 
        field0.getArg0((-13));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Field field0 = new Field();
      // Undeclared exception!
      try { 
        field0.getArg0((-2372));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      Field field0 = new Field();
      boolean boolean0 = field0.isIndexed();
      assertFalse(boolean0);
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      Map<String, Arg>[] mapArray0 = (Map<String, Arg>[]) Array.newInstance(Map.class, 4);
      HashMap<String, Arg> hashMap0 = new HashMap<String, Arg>();
      mapArray0[0] = (Map<String, Arg>) hashMap0;
      field0.args = mapArray0;
      hashMap0.put("|V7pg0A*((2+", arg0);
      Arg arg1 = field0.getArg1("|V7pg0A*((2+", 0);
      assertNotNull(arg1);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      Field field0 = new Field();
      Map<String, Arg>[] mapArray0 = (Map<String, Arg>[]) Array.newInstance(Map.class, 4);
      HashMap<String, Arg> hashMap0 = new HashMap<String, Arg>();
      mapArray0[0] = (Map<String, Arg>) hashMap0;
      field0.args = mapArray0;
      field0.getArg1("", 0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      Field field0 = new Field();
      Map<String, Arg>[] mapArray0 = (Map<String, Arg>[]) Array.newInstance(Map.class, 4);
      field0.args = mapArray0;
      field0.getArg1(")Rb&=~=K}t", 0);
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      Field field0 = new Field();
      field0.getArg0(0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      Field field0 = new Field();
      field0.setDepends("[]");
      boolean boolean0 = field0.isDependency("[]");
      assertTrue(boolean0);
      assertEquals("[]", field0.getDepends());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      Field field0 = new Field();
      boolean boolean0 = field0.isDependency("$S<4ijpBQ");
      assertFalse(boolean0);
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedListProperty("[]");
      boolean boolean0 = field0.isIndexed();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      Field field0 = new Field();
      field0.setIndexedListProperty("");
      boolean boolean0 = field0.isIndexed();
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      Field field0 = new Field();
      String string0 = field0.getKey();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      Field field0 = new Field();
      field0.key = "";
      String string0 = field0.getKey();
      assertEquals("", string0);
      assertNotNull(string0);
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      Field field0 = new Field();
      field0.getArg1("", 0);
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      field0.addArg(arg0);
      arg0.setName("[]");
      arg0.setPosition((-20));
      field0.addArg(arg0);
      assertEquals(1, arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      arg0.position = 5195;
      field0.addArg(arg0);
      arg0.setPosition((-606));
      field0.addArg(arg0);
      assertEquals(5196, arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      arg0.setName("[]");
      field0.addArg(arg0);
      arg0.setPosition((-1));
      field0.addArg(arg0);
      assertEquals(1, arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      field0.args = null;
      arg0.setKey("0U>KQl!");
      // Undeclared exception!
      try { 
        field0.addArg(arg0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.validator.Field", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.name = "[]";
      arg0.setKey("rw.apacefcommons.vLliator.ValidaorE8cepOin");
      field0.addArg(arg0);
      assertEquals(0, arg0.getPosition());
      
      field0.getArg1("org.apache.commons.validator.Field.DEFAULT", 0);
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("[]");
      field0.addArg(arg0);
      field0.addArg(arg0);
      assertEquals(0, arg0.getPosition());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      arg0.setKey("");
      field0.addArg(arg0);
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertEquals((-1), arg0.getPosition());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      Field field0 = new Field();
      Arg arg0 = new Arg();
      field0.addArg(arg0);
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      Field field0 = new Field();
      field0.addArg((Arg) null);
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      Field field0 = new Field();
      field0.setDepends("\n");
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertEquals("\n", field0.getDepends());
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      Field field0 = new Field();
      String string0 = field0.getProperty();
      assertNull(string0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      Field field0 = new Field();
      field0.setKey(".");
      String string0 = field0.getKey();
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
      assertEquals(".", string0);
      assertNotNull(string0);
      assertTrue(field0.isClientValidation());
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Field field0 = new Field();
      int int0 = field0.getFieldOrder();
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      Field field0 = new Field();
      int int0 = field0.getPage();
      assertEquals(0, int0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      Field field0 = new Field();
      String string0 = field0.getDepends();
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      Field field0 = new Field();
      String string0 = field0.getIndexedListProperty();
      assertNull(string0);
      assertEquals(0, field0.getFieldOrder());
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      Field field0 = new Field();
      String string0 = field0.getIndexedProperty();
      assertNull(string0);
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      Field field0 = new Field();
      boolean boolean0 = field0.isClientValidation();
      assertEquals(0, field0.getFieldOrder());
      assertEquals(0, field0.getPage());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      Field field0 = new Field();
      field0.getDependencyList();
      assertTrue(field0.isClientValidation());
      assertEquals(0, field0.getPage());
      assertEquals(0, field0.getFieldOrder());
  }
}
