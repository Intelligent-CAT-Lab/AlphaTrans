
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
import org.apache.commons.codec.digest.Blake3;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Blake3_ESTest extends Blake3_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      byte[] byteArray1 = Blake3.hash(byteArray0);
      Blake3 blake3_0 = Blake3.initKeyedHash(byteArray1);
      blake3_0.update1(byteArray1, (byte)0, 32);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      Blake3 blake3_0 = Blake3.initKeyDerivationFunction(byteArray0);
      blake3_0.doFinalize1(byteArray0, 2, 2);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      blake3_0.doFinalize2(0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      // Undeclared exception!
      try { 
        blake3_0.update1((byte[]) null, 2037, (-1964));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = blake3_0.doFinalize2(3437);
      Blake3.initKeyDerivationFunction(byteArray0);
      Blake3 blake3_1 = Blake3.initKeyDerivationFunction(byteArray0);
      // Undeclared exception!
      blake3_1.update0(byteArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      // Undeclared exception!
      try { 
        blake3_0.update0((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      // Undeclared exception!
      try { 
        Blake3.keyedHash((byte[]) null, (byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        Blake3.initKeyedHash((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      // Undeclared exception!
      try { 
        Blake3.initKeyDerivationFunction((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = blake3_0.doFinalize2(3434);
      blake3_0.doFinalize2(1715);
      Blake3.initKeyDerivationFunction(byteArray0);
      // Undeclared exception!
      Blake3.hash(byteArray0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      // Undeclared exception!
      try { 
        Blake3.hash((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      // Undeclared exception!
      try { 
        blake3_0.doFinalize1((byte[]) null, 2534, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      // Undeclared exception!
      try { 
        blake3_0.doFinalize0((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        blake3_0.doFinalize1(byteArray0, (-997), (-997));
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // Offset must be non-negative
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        Blake3.initKeyedHash(byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Blake3 keys must be 32 bytes
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = new byte[6];
      blake3_0.doFinalize0(byteArray0);
      //  // Unstable assertion: assertArrayEquals(new byte[] {(byte) (-11), (byte) (-113), (byte) (-56), (byte) (-48), (byte) (-94), (byte) (-79)}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = new byte[6];
      // Undeclared exception!
      try { 
        blake3_0.update1(byteArray0, 1359893119, (-2693));
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // Length must be non-negative
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = blake3_0.doFinalize2(3437);
      blake3_0.update0(byteArray0);
      assertEquals(3437, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      Blake3 blake3_0 = Blake3.initKeyDerivationFunction(byteArray0);
      // Undeclared exception!
      try { 
        blake3_0.doFinalize1(byteArray0, 891, 891);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // Offset 891 and length 891 out of bounds with buffer length 5
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      // Undeclared exception!
      try { 
        blake3_0.doFinalize2((-1411));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Requested bytes must be non-negative
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      byte[] byteArray0 = blake3_0.doFinalize2(1049);
      // Undeclared exception!
      try { 
        Blake3.keyedHash(byteArray0, byteArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Blake3 keys must be 32 bytes
         //
         verifyException("org.apache.commons.codec.digest.Blake3", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      Blake3 blake3_0 = Blake3.initHash();
      blake3_0.reset();
  }
}
