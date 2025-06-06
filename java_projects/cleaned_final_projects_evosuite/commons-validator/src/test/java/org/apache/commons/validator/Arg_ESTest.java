

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
import org.apache.commons.validator.Arg;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Arg_ESTest extends Arg_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setKey("Pn");
      String string0 = arg0.toString();
      assertEquals("Arg: name=null  key=Pn  position=-1  bundle=null  resource=true\n", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.bundle = "";
      String string0 = arg0.toString();
      assertEquals("Arg: name=null  key=null  position=-1  bundle=  resource=true\n", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.resource = false;
      arg0.setResource(true);
      assertTrue(arg0.isResource());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Arg arg0 = new Arg();
      assertTrue(arg0.isResource());
      
      arg0.resource = false;
      arg0.isResource();
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Arg arg0 = new Arg();
      assertEquals((-1), arg0.getPosition());
      
      arg0.position = 0;
      int int0 = arg0.getPosition();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.position = 1675;
      int int0 = arg0.getPosition();
      assertEquals(1675, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.name = "";
      String string0 = arg0.getName();
      assertNotNull(string0);
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.key = "";
      String string0 = arg0.getKey();
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.bundle = "Arg: name=null  key=null  position=-1  bundle=null  resource=true\n";
      String string0 = arg0.getBundle();
      assertEquals((-1), arg0.getPosition());
      assertTrue(arg0.isResource());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setBundle("");
      String string0 = arg0.getBundle();
      assertNotNull(string0);
      assertEquals((-1), arg0.getPosition());
      assertTrue(arg0.isResource());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Arg arg0 = new Arg();
      int int0 = arg0.getPosition();
      assertEquals((-1), int0);
      assertTrue(arg0.isResource());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setName("org.apache.commons.validator.Arg");
      String string0 = arg0.getName();
      assertNotNull(string0);
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.getBundle();
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setKey("{fr;");
      String string0 = arg0.getKey();
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.getName();
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Arg arg0 = new Arg();
      Arg arg1 = (Arg)arg0.clone();
      assertTrue(arg1.isResource());
      assertEquals((-1), arg1.getPosition());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Arg arg0 = new Arg();
      boolean boolean0 = arg0.isResource();
      assertTrue(boolean0);
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.getKey();
      assertTrue(arg0.isResource());
      assertEquals((-1), arg0.getPosition());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Arg arg0 = new Arg();
      arg0.setPosition(3166);
      assertEquals(3166, arg0.getPosition());
  }
}
