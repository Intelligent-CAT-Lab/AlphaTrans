
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


package org.fusesource.jansi.internal;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.fusesource.jansi.internal.OSInfo;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OSInfo_ESTest extends OSInfo_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      String string0 = OSInfo.translateArchNameToFolderName("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      String string0 = OSInfo.getHardwareName();
      assertEquals("unknown", string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      // Undeclared exception!
      try { 
        OSInfo.translateOSNameToFolderName((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.internal.OSInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      // Undeclared exception!
      try { 
        OSInfo.translateArchNameToFolderName((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.internal.OSInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      // Undeclared exception!
      try { 
        OSInfo.main((String[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.fusesource.jansi.internal.OSInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      String string0 = OSInfo.getArchName();
      assertEquals("x86_64", string0);
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      String string0 = OSInfo.getOSName();
      assertEquals("Linux", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      boolean boolean0 = OSInfo.isAndroid();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      String string0 = OSInfo.translateOSNameToFolderName("AIX");
      assertEquals("AIX", string0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String string0 = OSInfo.translateOSNameToFolderName("");
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      String string0 = OSInfo.translateOSNameToFolderName("Darwin");
      assertEquals("Mac", string0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      String string0 = OSInfo.translateOSNameToFolderName("Mac");
      assertEquals("Mac", string0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      String string0 = OSInfo.translateOSNameToFolderName("Windows");
      assertEquals("Windows", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      boolean boolean0 = OSInfo.isAlpine();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      String[] stringArray0 = new String[1];
      stringArray0[0] = "--arch";
      OSInfo.main(stringArray0);
      assertEquals(1, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[6];
      stringArray0[0] = "--os";
      OSInfo.main(stringArray0);
      assertEquals(6, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      String[] stringArray0 = new String[3];
      OSInfo.main(stringArray0);
      assertEquals(3, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      String[] stringArray0 = new String[0];
      OSInfo.main(stringArray0);
      assertEquals(0, stringArray0.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      String string0 = OSInfo.resolveArmArchType();
      assertEquals("arm", string0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      OSInfo oSInfo0 = new OSInfo();
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      String string0 = OSInfo.translateArchNameToFolderName("SU");
      assertEquals("SU", string0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      String string0 = OSInfo.getNativeLibFolderPathForCurrentOS();
      assertEquals("Linux/x86_64", string0);
  }
}
