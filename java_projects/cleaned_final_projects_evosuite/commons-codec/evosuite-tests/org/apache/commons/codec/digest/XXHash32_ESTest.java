
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
import org.apache.commons.codec.digest.XXHash32;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class XXHash32_ESTest extends XXHash32_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      byte[] byteArray0 = new byte[8];
      byteArray0[0] = (byte) (-29);
      // Undeclared exception!
      try { 
        xXHash32_0.update1(byteArray0, (byte)0, 4311);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("org.apache.commons.codec.digest.XXHash32", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      byte[] byteArray0 = new byte[8];
      byteArray0[6] = (byte) (-29);
      // Undeclared exception!
      try { 
        xXHash32_0.update1(byteArray0, (byte)0, 4311);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("org.apache.commons.codec.digest.XXHash32", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      XXHash32 xXHash32_0 = new XXHash32(723);
      byte[] byteArray0 = new byte[9];
      byteArray0[1] = (byte)1;
      xXHash32_0.update1(byteArray0, (byte)0, 7);
      long long0 = xXHash32_0.getValue();
      assertEquals(686811741L, long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      XXHash32 xXHash32_0 = new XXHash32(0);
      xXHash32_0.update0(1);
      long long0 = xXHash32_0.getValue();
      assertEquals(949155633L, long0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      XXHash32 xXHash32_0 = new XXHash32(723);
      byte[] byteArray0 = new byte[9];
      xXHash32_0.update1(byteArray0, (byte)0, 7);
      xXHash32_0.update0((-2204));
      long long0 = xXHash32_0.getValue();
      assertEquals(2763811559L, long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[32];
      XXHash32 xXHash32_0 = new XXHash32((-668));
      xXHash32_0.update1(byteArray0, 16, 16);
      long long0 = xXHash32_0.getValue();
      assertEquals(1895327912L, long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      XXHash32 xXHash32_0 = new XXHash32(723);
      byte[] byteArray0 = new byte[9];
      xXHash32_0.update1(byteArray0, 1799, 0);
      assertEquals(2679648573L, xXHash32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      XXHash32 xXHash32_0 = new XXHash32(723);
      byte[] byteArray0 = new byte[9];
      xXHash32_0.update(byteArray0, (int) (byte)0, 2754);
      assertEquals(2679648573L, xXHash32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      // Undeclared exception!
      try { 
        xXHash32_0.update1((byte[]) null, 3191, 3191);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.XXHash32", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      byte[] byteArray0 = new byte[37];
      xXHash32_0.update1(byteArray0, 11, 11);
      long long0 = xXHash32_0.getValue();
      assertEquals(632180237L, long0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      byte[] byteArray0 = new byte[32];
      xXHash32_0.update0(0);
      // Undeclared exception!
      try { 
        xXHash32_0.update1(byteArray0, 16, 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      byte[] byteArray0 = new byte[7];
      xXHash32_0.update1(byteArray0, (byte)17, (byte) (-53));
      assertEquals(46947589L, xXHash32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      xXHash32_0.reset();
      assertEquals(46947589L, xXHash32_0.getValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      XXHash32 xXHash32_0 = XXHash32.XXHash321();
      xXHash32_0.update((-97));
      assertEquals(46947589L, xXHash32_0.getValue());
  }
}
