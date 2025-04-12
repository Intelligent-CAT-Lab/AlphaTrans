

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
import org.apache.commons.validator.Msg;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Msg_ESTest extends Msg_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.bundle = "i{lR:Wbi.h:V(-}";
      String string0 = msg0.toString();
      assertEquals("Msg: name=null  key=null  resource=true  bundle=i{lR:Wbi.h:V(-}\n", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.name = "";
      String string0 = msg0.toString();
      assertEquals("Msg: name=  key=null  resource=true  bundle=null\n", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.setName("s$oc0a<k6");
      String string0 = msg0.getName();
      assertTrue(msg0.isResource());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.name = "";
      String string0 = msg0.getName();
      assertTrue(msg0.isResource());
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.setKey(",dF*z{m");
      String string0 = msg0.getKey();
      assertNotNull(string0);
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.bundle = "  key=";
      String string0 = msg0.getBundle();
      assertNotNull(string0);
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.bundle = "";
      String string0 = msg0.getBundle();
      assertNotNull(string0);
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Msg msg0 = new Msg();
      Msg msg1 = (Msg)msg0.clone();
      assertTrue(msg1.isResource());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Msg msg0 = new Msg();
      boolean boolean0 = msg0.isResource();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.getKey();
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.getName();
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Msg msg0 = new Msg();
      assertTrue(msg0.isResource());
      
      msg0.setResource(false);
      boolean boolean0 = msg0.isResource();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.setKey("");
      String string0 = msg0.getKey();
      assertNotNull(string0);
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.getBundle();
      assertTrue(msg0.isResource());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Msg msg0 = new Msg();
      msg0.setBundle("  key=");
      assertTrue(msg0.isResource());
  }
}
