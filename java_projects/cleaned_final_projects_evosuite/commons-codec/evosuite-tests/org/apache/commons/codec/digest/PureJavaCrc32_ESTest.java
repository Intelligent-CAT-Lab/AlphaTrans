
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


package org.apache.commons.codec.digest;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.codec.digest.PureJavaCrc32;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PureJavaCrc32_ESTest extends PureJavaCrc32_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[8];
      byteArray0[4] = (byte) (-1);
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)0, 1172266101);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[6];
      byteArray0[3] = (byte)118;
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)0, (byte)14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[9];
      byteArray0[2] = (byte) (-1);
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)0, (byte)79);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[5];
      byteArray0[2] = (byte) (-60);
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)1, 3425);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[5];
      byteArray0[1] = (byte) (-57);
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)1, 3425);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[1];
      pureJavaCrc32_0.update(byteArray0, 0, (int) (byte)0);
      assertEquals(0L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[2];
      pureJavaCrc32_0.update0(byteArray0, (byte)0, (byte)0);
      assertEquals(0L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte) (-2), (byte) (-2));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[13];
      pureJavaCrc32_0.update0(byteArray0, 5, 5);
      assertEquals(3324180253L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[3];
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte) (-12), (byte) (-12));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -12 out of bounds for length 3
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)0, (-1381));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[11];
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (-2542), (-2542));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2542 out of bounds for length 11
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[7];
      pureJavaCrc32_0.update0(byteArray0, 1, 1);
      assertEquals(3523407757L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      byte[] byteArray0 = new byte[13];
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0(byteArray0, (byte)0, 3044);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      // Undeclared exception!
      try { 
        pureJavaCrc32_0.update0((byte[]) null, (-1), (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.PureJavaCrc32", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      pureJavaCrc32_0.update(3081);
      assertEquals(0L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      pureJavaCrc32_0.update1(1380);
      long long0 = pureJavaCrc32_0.getValue();
      assertEquals(2564639436L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      pureJavaCrc32_0.reset();
      assertEquals(0L, pureJavaCrc32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      PureJavaCrc32 pureJavaCrc32_0 = new PureJavaCrc32();
      long long0 = pureJavaCrc32_0.getValue();
      assertEquals(0L, long0);
  }
}
