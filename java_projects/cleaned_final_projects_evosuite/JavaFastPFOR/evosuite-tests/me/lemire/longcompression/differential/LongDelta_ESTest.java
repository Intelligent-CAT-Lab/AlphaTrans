
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


package me.lemire.longcompression.differential;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.longcompression.differential.LongDelta;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongDelta_ESTest extends LongDelta_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      long[] longArray0 = new long[4];
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta1(longArray0, 0, 5, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      long[] longArray0 = new long[4];
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta1(longArray0, 0, 0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      long[] longArray0 = new long[9];
      longArray0[0] = 1L;
      LongDelta.fastinverseDelta0(longArray0);
      assertArrayEquals(new long[] {1L, 1L, 1L, 1L, 1L, 1L, 1L, 1L, 1L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      long[] longArray0 = new long[5];
      longArray0[0] = 503L;
      LongDelta.inverseDelta(longArray0);
      assertArrayEquals(new long[] {503L, 503L, 503L, 503L, 503L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      long[] longArray0 = new long[0];
      LongDelta.inverseDelta(longArray0);
      assertArrayEquals(new long[] {}, longArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      long[] longArray0 = new long[4];
      longArray0[2] = (-72L);
      long long0 = LongDelta.delta2(longArray0, 2, 2, 2, longArray0);
      assertEquals(0L, long0);
      assertArrayEquals(new long[] {(-74L), 72L, (-72L), 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      long[] longArray0 = new long[4];
      long[] longArray1 = new long[9];
      LongDelta.delta2(longArray0, 2, 2, 2, longArray1);
      assertArrayEquals(new long[] {(-2L), 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L}, longArray1);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      long[] longArray0 = new long[5];
      long long0 = LongDelta.delta2(longArray0, 1, 3, 10, longArray0);
      assertEquals(0L, long0);
      assertArrayEquals(new long[] {(-10L), 0L, 0L, 0L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      long[] longArray0 = new long[6];
      longArray0[0] = (-8L);
      LongDelta.fastinverseDelta0(longArray0);
      long long0 = LongDelta.delta1(longArray0, 1, 3, (-2490));
      assertArrayEquals(new long[] {(-8L), 2482L, 0L, 0L, (-8L), (-8L)}, longArray0);
      assertEquals((-8L), long0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      long[] longArray0 = new long[4];
      longArray0[0] = (-1916L);
      LongDelta.delta0(longArray0);
      assertArrayEquals(new long[] {(-1916L), 1916L, 0L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      long[] longArray0 = new long[0];
      LongDelta.delta0(longArray0);
      assertArrayEquals(new long[] {}, longArray0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      long[] longArray0 = new long[10];
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta1(longArray0, 1, 15, (-4));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      long[] longArray0 = new long[6];
      longArray0[1] = (-1L);
      long long0 = LongDelta.fastinverseDelta1(longArray0, 1, 1, 1);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      long[] longArray0 = new long[6];
      longArray0[0] = (-8L);
      LongDelta.fastinverseDelta0(longArray0);
      long long0 = LongDelta.fastinverseDelta1(longArray0, 1, 1, 3);
      assertArrayEquals(new long[] {(-8L), (-5L), (-8L), (-8L), (-8L), (-8L)}, longArray0);
      assertEquals((-5L), long0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      long[] longArray0 = new long[4];
      longArray0[3] = 2635L;
      long long0 = LongDelta.delta2(longArray0, 2, 2, 2, longArray0);
      assertEquals(2635L, long0);
      assertArrayEquals(new long[] {(-2L), 2635L, 0L, 2635L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      long[] longArray0 = new long[4];
      longArray0[3] = (-392L);
      long long0 = LongDelta.delta2(longArray0, 2, 2, 2, longArray0);
      assertEquals((-392L), long0);
      assertArrayEquals(new long[] {(-2L), (-392L), 0L, (-392L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      long[] longArray0 = new long[4];
      longArray0[3] = (long) 1;
      long long0 = LongDelta.delta1(longArray0, 1, 3, (-2490));
      assertArrayEquals(new long[] {0L, 2490L, 0L, 1L}, longArray0);
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta1((long[]) null, (-1), (-1), (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta0((long[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      // Undeclared exception!
      try { 
        LongDelta.delta2((long[]) null, (-28), (-28), (-28), (long[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      long[] longArray0 = new long[17];
      // Undeclared exception!
      try { 
        LongDelta.delta2(longArray0, (-984), (-984), (-984), longArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -984 out of bounds for length 17
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      // Undeclared exception!
      try { 
        LongDelta.delta1((long[]) null, (-1), (-1), (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      long[] longArray0 = new long[17];
      // Undeclared exception!
      try { 
        LongDelta.delta1(longArray0, (-1), (-1), (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3 out of bounds for length 17
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      long[] longArray0 = new long[17];
      long long0 = LongDelta.fastinverseDelta1(longArray0, 5, 5, 5);
      assertEquals(5L, long0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      long[] longArray0 = new long[0];
      // Undeclared exception!
      try { 
        LongDelta.fastinverseDelta0(longArray0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 0
         //
         verifyException("me.lemire.longcompression.differential.LongDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      long[] longArray0 = new long[26];
      long long0 = LongDelta.delta1(longArray0, 4, 4, 4);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      long[] longArray0 = new long[17];
      long long0 = LongDelta.delta1(longArray0, 3, (-1), 1175);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      LongDelta longDelta0 = new LongDelta();
  }
}
