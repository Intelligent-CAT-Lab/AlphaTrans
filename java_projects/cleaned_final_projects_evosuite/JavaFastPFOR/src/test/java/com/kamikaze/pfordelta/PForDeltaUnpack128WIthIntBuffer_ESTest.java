
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


package com.kamikaze.pfordelta;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer;
import java.nio.BufferUnderflowException;
import java.nio.IntBuffer;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PForDeltaUnpack128WIthIntBuffer_ESTest extends PForDeltaUnpack128WIthIntBuffer_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[128];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      int int0 = 16;
      intBuffer0.put((-1986));
      intBuffer0.clear();
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, int0);
      assertEquals("java.nio.HeapIntBuffer[pos=64 lim=128 cap=128]", intBuffer0.toString());
      assertEquals(64, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[38];
      IntBuffer intBuffer0 = IntBuffer.allocate(1806);
      intBuffer0.put(1, 2491);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 38 out of bounds for length 38
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[96];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      intBuffer0.put(1, 1002);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 96 out of bounds for length 96
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[157];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      intBuffer0.put(7, 7);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 12);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 12);
      assertEquals(96, intBuffer0.position());
      assertEquals("java.nio.HeapIntBuffer[pos=96 lim=157 cap=157]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[1] = 1923;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[0] = 1649;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = 127;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int[] intArray0 = new int[136];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      int[] intArray1 = new int[8];
      intArray1[0] = (-4500);
      intBuffer0.mark();
      intBuffer0.put(intArray1);
      intBuffer0.reset();
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 8);
      assertEquals(32, intBuffer0.position());
      assertEquals(104, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[144];
      int[] intArray1 = new int[7];
      intArray1[1] = (-4477);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 7);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[144];
      int[] intArray1 = new int[7];
      intArray1[0] = 2645;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 7);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      int[] intArray0 = new int[5];
      int[] intArray1 = new int[8];
      intArray1[0] = (-2143);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 28;
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[131];
      int[] intArray1 = new int[5];
      intArray1[0] = (-21);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray1);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 3);
        fail("Expecting exception: BufferUnderflowException");
      
      } catch(BufferUnderflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[0] = (-3848);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[20];
      intArray0[0] = (-307);
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 20 out of bounds for length 20
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntBuffer intBuffer0 = IntBuffer.allocate(2);
      // Undeclared exception!
      try { 
        PForDeltaUnpack128WIthIntBuffer.unpack((int[]) null, intBuffer0, 2);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDeltaUnpack128WIthIntBuffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      int[] intArray0 = new int[128];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 63550);
      assertEquals(128, intBuffer0.limit());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[157];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 28);
      assertEquals(45, intBuffer0.remaining());
      assertEquals("java.nio.HeapIntBuffer[pos=112 lim=157 cap=157]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 27);
      assertEquals(129, intBuffer0.capacity());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[10];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 26);
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=10 cap=10]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      int[] intArray0 = new int[38];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 25);
      assertTrue(intBuffer0.hasRemaining());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[5];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 24);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 23);
      assertEquals(0, intBuffer0.arrayOffset());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[20];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 22);
      assertEquals(0, intBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      int[] intArray0 = new int[7];
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, (IntBuffer) null, 21);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 20);
      assertEquals(80, intBuffer0.position());
      assertEquals("java.nio.HeapIntBuffer[pos=80 lim=129 cap=129]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      int[] intArray0 = new int[15];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 19);
      assertTrue(intBuffer0.hasRemaining());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      int[] intArray0 = new int[4];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 18);
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=4 cap=4]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      int[] intArray0 = new int[38];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 17);
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=38 cap=38]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int[] intArray0 = new int[20];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 15);
      assertEquals(0, intBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      int[] intArray0 = new int[38];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 14);
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=38 cap=38]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 13);
      assertEquals(77, intBuffer0.remaining());
      assertEquals(52, intBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 11);
      assertEquals(44, intBuffer0.position());
      assertEquals("java.nio.HeapIntBuffer[pos=44 lim=129 cap=129]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 10);
      assertEquals("java.nio.HeapIntBuffer[pos=40 lim=129 cap=129]", intBuffer0.toString());
      assertEquals(89, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 9);
      assertEquals(93, intBuffer0.remaining());
      assertEquals("java.nio.HeapIntBuffer[pos=36 lim=129 cap=129]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 6);
      assertEquals(24, intBuffer0.position());
      assertEquals(105, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 5);
      assertEquals(20, intBuffer0.position());
      assertEquals(109, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 4);
      assertEquals("java.nio.HeapIntBuffer[pos=16 lim=129 cap=129]", intBuffer0.toString());
      assertEquals(113, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      int[] intArray0 = new int[131];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 3);
      assertEquals(119, intBuffer0.remaining());
      assertEquals("java.nio.HeapIntBuffer[pos=12 lim=131 cap=131]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 2);
      assertEquals(8, intBuffer0.position());
      assertEquals("java.nio.HeapIntBuffer[pos=8 lim=129 cap=129]", intBuffer0.toString());
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 1);
      assertEquals("java.nio.HeapIntBuffer[pos=4 lim=129 cap=129]", intBuffer0.toString());
      assertEquals(4, intBuffer0.position());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      int[] intArray0 = new int[144];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 7);
      assertEquals("java.nio.HeapIntBuffer[pos=28 lim=144 cap=144]", intBuffer0.toString());
      assertEquals(116, intBuffer0.remaining());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      PForDeltaUnpack128WIthIntBuffer pForDeltaUnpack128WIthIntBuffer0 = new PForDeltaUnpack128WIthIntBuffer();
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      int[] intArray0 = new int[130];
      IntBuffer intBuffer0 = IntBuffer.wrap(intArray0);
      PForDeltaUnpack128WIthIntBuffer.unpack(intArray0, intBuffer0, 0);
      assertEquals(130, intBuffer0.remaining());
      assertEquals("java.nio.HeapIntBuffer[pos=0 lim=130 cap=130]", intBuffer0.toString());
  }
}
