
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


package org.apache.commons.cli;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.File;
import org.apache.commons.cli.TypeHandler;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class TypeHandler_ESTest extends TypeHandler_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      try { 
        TypeHandler.createObject("org.apache.commons.cli.Option");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // java.lang.InstantiationException; Unable to create an instance of: org.apache.commons.cli.Option
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile(".KsSb`k_VX_1N1jSin");
      byte[] byteArray0 = new byte[3];
      FileSystemHandling.appendDataToFile(evoSuiteFile0, byteArray0);
      File file0 = TypeHandler.createFile(".KsSb`k_VX_1N1jSin");
      assertEquals(0L, file0.getTotalSpace());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      File file0 = TypeHandler.createFile("/p.");
      assertTrue(file0.isAbsolute());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      File file0 = TypeHandler.createFile("");
      assertTrue(file0.canExecute());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Class<?> class0 = TypeHandler.createClass("org.apache.commons.cli.PatternOptionBuilder");
      assertFalse(class0.isPrimitive());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.openFile((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.mock.java.io.MockFileInputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createValue1(",y&2", ",y&2");
        fail("Expecting exception: ClassCastException");
      
      } catch(ClassCastException e) {
         //
         // class java.lang.String cannot be cast to class java.lang.Class (java.lang.String and java.lang.Class are in module java.base of loader 'bootstrap')
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Class<Object> class0 = Object.class;
      // Undeclared exception!
      try { 
        TypeHandler.createValue0((String) null, class0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      try { 
        TypeHandler.createObject("@;~YkT#_pRf");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to find the class: @;~YkT#_pRf
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createObject((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createNumber((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createFile((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.io.File", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      try { 
        TypeHandler.createClass("gNx");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to find the class: gNx
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createClass((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Class<Integer> class0 = Integer.class;
      try { 
        TypeHandler.createValue0("; Unable to create an instance of: ", class0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to handle the class: class java.lang.Integer
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      TypeHandler typeHandler0 = new TypeHandler();
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Class<Object> class0 = Object.class;
      Object object0 = TypeHandler.createValue0("org.apache.commons.cli.TypeHandler", class0);
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      try { 
        TypeHandler.createNumber("org.apache.commons.cli.Options");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // For input string: \"org.apache.commons.cli.Options\"
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Number number0 = TypeHandler.createNumber("5");
      assertEquals(5L, number0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createDate("}*o");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // Not yet implemented
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      try { 
        TypeHandler.createURL("]qlF%Fe^,Qb;");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to parse the URL: ]qlF%Fe^,Qb;
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Object object0 = TypeHandler.createObject("org.apache.commons.cli.TypeHandler");
      assertNotNull(object0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      try { 
        TypeHandler.createValue1((String) null, (Object) null);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to handle the class: null
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      // Undeclared exception!
      try { 
        TypeHandler.createFiles("org.apache.commons.cli.PatternOptionBuilder");
        fail("Expecting exception: UnsupportedOperationException");
      
      } catch(UnsupportedOperationException e) {
         //
         // Not yet implemented
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      try { 
        TypeHandler.openFile("");
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Unable to find file: 
         //
         verifyException("org.apache.commons.cli.TypeHandler", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Class<?> class0 = TypeHandler.createClass("[S");
      assertFalse(class0.isInterface());
  }
}
