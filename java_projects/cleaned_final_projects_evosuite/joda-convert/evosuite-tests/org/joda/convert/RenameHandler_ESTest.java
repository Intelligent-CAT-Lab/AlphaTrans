
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
import java.net.Proxy;
import java.util.Map;
import java.util.Set;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.convert.RenameHandler;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class RenameHandler_ESTest extends RenameHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<?> class0 = renameHandler0.INSTANCE.lookupType("char");
      assertFalse(class0.isInterface());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<?> class0 = renameHandler0.lookupType("org.joda.convert.ReflectionStringConverter");
      assertFalse(class0.isPrimitive());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      renameHandler0.INSTANCE.getTypeRenames();
      Class<Proxy.Type> class0 = Proxy.Type.class;
      renameHandler0.renamedType("name must not be null", class0);
      Class<?> class1 = renameHandler0.lookupType("name must not be null");
      assertFalse(class1.isSynthetic());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      Proxy.Type proxy_Type0 = Proxy.Type.DIRECT;
      renameHandler0.renamedEnum(">=J-O#E", proxy_Type0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<Proxy.Type> class0 = Proxy.Type.class;
      Map<String, Enum<?>> map0 = renameHandler0.getEnumRenames(class0);
      assertTrue(map0.isEmpty());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      String string0 = "^xA:b{bC$1";
      Proxy.Type proxy_Type0 = Proxy.Type.DIRECT;
      renameHandler0.renamedEnum("^xA:b{bC$1", proxy_Type0);
      RenameHandler.create0();
      renameHandler0.getEnumTypesWithRenames();
      renameHandler0.lock();
      try { 
        renameHandler0.lookupType("^xA:b{bC$1");
        fail("Expecting exception: ClassNotFoundException");
      
      } catch(ClassNotFoundException e) {
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create1(false);
      Class<Proxy.Type> class0 = Proxy.Type.class;
      // Undeclared exception!
      try { 
        renameHandler0.lookupEnum(class0, (String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // name must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      // Undeclared exception!
      try { 
        renameHandler0.lookupEnum((Class<Proxy.Type>) null, "name must");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // type must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      // Undeclared exception!
      try { 
        renameHandler0.getEnumRenames((Class<?>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // type must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<Proxy.Type> class0 = Proxy.Type.class;
      // Undeclared exception!
      try { 
        renameHandler0.lookupEnum(class0, "$*_q");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No enum constant java.net.Proxy.Type.$*_q
         //
         verifyException("java.lang.Enum", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      // Undeclared exception!
      try { 
        renameHandler0.renamedEnum("org.joda.`", (Enum<?>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // currentValue must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Proxy.Type proxy_Type0 = Proxy.Type.SOCKS;
      // Undeclared exception!
      try { 
        renameHandler0.renamedEnum((String) null, proxy_Type0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // oldName must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Proxy.Type proxy_Type0 = Proxy.Type.SOCKS;
      renameHandler0.renamedEnum("getAsInt", proxy_Type0);
      Class<Proxy.Type> class0 = Proxy.Type.class;
      Proxy.Type proxy_Type1 = renameHandler0.lookupEnum(class0, "getAsInt");
      assertEquals(Proxy.Type.SOCKS, proxy_Type1);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create1(false);
      // Undeclared exception!
      try { 
        renameHandler0.lookupType((String) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // name must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      Class<Proxy.Type> class0 = Proxy.Type.class;
      // Undeclared exception!
      try { 
        renameHandler0.renamedType("org.joda.convert.RenameHandler", class0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // oldName must not be a java.*, javax.* or org.joda.* type
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<Object> class0 = Object.class;
      // Undeclared exception!
      try { 
        renameHandler0.renamedType("javax.org.joda.convert.AnnotationStringConverterFactory", class0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // oldName must not be a java.*, javax.* or org.joda.* type
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create1(true);
      Class<Object> class0 = Object.class;
      // Undeclared exception!
      try { 
        renameHandler0.renamedType("java.", class0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // oldName must not be a java.*, javax.* or org.joda.* type
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      // Undeclared exception!
      try { 
        renameHandler0.renamedType("!m", (Class<?>) null);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // currentValue must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create1(false);
      String string0 = renameHandler0.toString();
      assertEquals("RenamedTypes{},RenamedEnumConstants{}", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.INSTANCE;
      Set<Class<?>> set0 = renameHandler0.getEnumTypesWithRenames();
      assertEquals(0, set0.size());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      RenameHandler renameHandler0 = RenameHandler.create0();
      Class<Object> class0 = Object.class;
      // Undeclared exception!
      try { 
        renameHandler0.renamedType((String) null, class0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // oldName must not be null
         //
         verifyException("org.joda.convert.RenameHandler", e);
      }
  }
}
