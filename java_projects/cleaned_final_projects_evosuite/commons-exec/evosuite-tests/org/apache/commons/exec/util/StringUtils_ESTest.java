
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


package org.apache.commons.exec.util;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.File;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.exec.util.StringUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class StringUtils_ESTest extends StringUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      HashMap<Object, File> hashMap0 = new HashMap<Object, File>();
      Object object0 = new Object();
      hashMap0.put(object0, (File) null);
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution("\u0003zN|2B&:Kk$HAbHaH", hashMap0, false);
      assertEquals("\u0003zN|2B&:Kk$HAbHaH", stringBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      String string0 = StringUtils.quoteArgument("\" ");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      String[] stringArray0 = StringUtils.split("", "");
      String string0 = StringUtils.toString(stringArray0, "");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      String string0 = StringUtils.fixFileSeparatorChar("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.toString((String[]) null, "4[f&Lq");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.split((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.StringTokenizer", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.quoteArgument((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.isQuoted((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.fixFileSeparatorChar((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      HashMap<Object, Object> hashMap0 = new HashMap<Object, Object>();
      Object object0 = new Object();
      hashMap0.put(object0, object0);
      // Undeclared exception!
      try { 
        StringUtils.stringSubstitution(":BVan5fKmu_Yy${t\"", hashMap0, true);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Delimiter not found for : t
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      HashMap<Object, File> hashMap0 = new HashMap<Object, File>();
      MockFile mockFile0 = new MockFile("", "");
      hashMap0.put("", mockFile0);
      // Undeclared exception!
      try { 
        StringUtils.stringSubstitution("${", hashMap0, false);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      HashMap<Object, Object> hashMap0 = new HashMap<Object, Object>();
      hashMap0.put("''P'LMw*Cuf${1>9}", "''P'LMw*Cuf${1>9}");
      // Undeclared exception!
      try { 
        StringUtils.stringSubstitution("''P'LMw*Cuf${1>9}", hashMap0, false);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // No value found for : 1
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      HashMap<Object, Object> hashMap0 = new HashMap<Object, Object>();
      Object object0 = new Object();
      hashMap0.put("$DZ7^", object0);
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution("IryWd$q}lO0LY8$>YZl", hashMap0, true);
      assertEquals("IryWd$q}lO0LY8$>YZl", stringBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution("No value found for : ", (Map<? super String, ?>) null, false);
      assertEquals("No value found for : ", stringBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution("", (Map<? super String, ?>) null, true);
      assertEquals(0, stringBuffer0.length());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      HashMap<Object, Object> hashMap0 = new HashMap<Object, Object>();
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution("IryWd$q}lO0LY8$>YZl", hashMap0, true);
      assertEquals(19, stringBuffer0.length());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      HashMap<Object, Object> hashMap0 = new HashMap<Object, Object>();
      StringBuffer stringBuffer0 = StringUtils.stringSubstitution((String) null, hashMap0, true);
      assertEquals("", stringBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      String[] stringArray0 = StringUtils.split("/home/ali/Documents/AlphaTrans/java_projects/cleaned_final_projects/commons-exec/\"", "IryWd$q}lO0LY8$>YZl");
      assertEquals(9, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      String string0 = StringUtils.quoteArgument("No value found for : ");
      assertEquals("\"No value found for :\"", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      String string0 = StringUtils.quoteArgument("Can't handle single and double quotes in same argument");
      assertEquals("\"Can't handle single and double quotes in same argument\"", string0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      // Undeclared exception!
      try { 
        StringUtils.quoteArgument("Can't handle single and double quotes in same argument\" \" \" \" \" \" \" \" ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Can't handle single and double quotes in same argument
         //
         verifyException("org.apache.commons.exec.util.StringUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      String string0 = StringUtils.quoteArgument("'*\"EQ#u;8Mc7sX'");
      assertEquals("'*\"EQ#u;8Mc7sX'", string0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      boolean boolean0 = StringUtils.isQuoted("\"Can't handle single and double quotes in same argument");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      boolean boolean0 = StringUtils.isQuoted("'No value found for : '");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      boolean boolean0 = StringUtils.isQuoted("'$`MEQ{3*Mf");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      boolean boolean0 = StringUtils.isQuoted("\"");
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      String[] stringArray0 = new String[5];
      String string0 = StringUtils.toString(stringArray0, "Can't handle single and double quotes in same argument");
      assertEquals("nullCan't handle single and double quotes in same argumentnullCan't handle single and double quotes in same argumentnullCan't handle single and double quotes in same argumentnullCan't handle single and double quotes in same argumentnull", string0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      String string0 = StringUtils.fixFileSeparatorChar("$DZ7^");
      assertEquals("$DZ7^", string0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      StringUtils stringUtils0 = new StringUtils();
  }
}
