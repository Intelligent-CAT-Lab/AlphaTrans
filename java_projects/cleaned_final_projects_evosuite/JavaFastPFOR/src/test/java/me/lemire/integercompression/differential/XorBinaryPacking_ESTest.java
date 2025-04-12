
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


package me.lemire.integercompression.differential;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.differential.XorBinaryPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class XorBinaryPacking_ESTest extends XorBinaryPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[70];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[8];
      xorBinaryPacking0.uncompress0(intArray1, intWrapper0, (-412), intArray1, intWrapper0);
      intArray1[1] = 1436;
      intArray1[2] = 401;
      intArray1[3] = (-881);
      // Undeclared exception!
      try { 
        xorBinaryPacking0.uncompress0(intArray1, intWrapper0, (-881), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 70 out of bounds for length 70
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[3];
      intArray0[1] = (-1268);
      intArray0[2] = 785;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        xorBinaryPacking0.compress0(intArray0, intWrapper0, 3023, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[90];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[4];
      intArray1[0] = 12;
      intArray1[1] = 1048575;
      // Undeclared exception!
      try { 
        xorBinaryPacking0.uncompress0(intArray1, intWrapper0, 1386, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[7];
      intArray0[0] = 302;
      IntWrapper intWrapper0 = new IntWrapper(302);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        xorBinaryPacking0.uncompress0(intArray0, intWrapper1, (-2789), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 302 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[9];
      intArray0[1] = (-4088);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      xorBinaryPacking0.compress0(intArray0, intWrapper0, (-1128), intArray0, intWrapper0);
      xorBinaryPacking0.uncompress0(intArray0, intWrapper0, 1779, intArray0, intWrapper0);
      assertEquals("2", intWrapper0.toString());
      assertArrayEquals(new int[] {(-1024), (-4088), 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        xorBinaryPacking0.uncompress0(intArray0, (IntWrapper) null, (-1283), intArray0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[71];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        xorBinaryPacking0.compress0(intArray0, intWrapper1, 128, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 71 out of bounds for length 71
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[72];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[11];
      // Undeclared exception!
      try { 
        xorBinaryPacking0.compress0(intArray0, intWrapper0, 2688, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 72 out of bounds for length 72
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 2863;
      intArray0[1] = (-3574);
      // Undeclared exception!
      try { 
        xorBinaryPacking0.uncompress0(intArray0, intWrapper0, (-3574), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      IntWrapper intWrapper0 = new IntWrapper((-654));
      // Undeclared exception!
      try { 
        xorBinaryPacking0.compress0((int[]) null, intWrapper0, (-654), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[42];
      IntWrapper intWrapper0 = new IntWrapper(0);
      xorBinaryPacking0.uncompress0(intArray0, intWrapper0, (-1680), intArray0, intWrapper0);
      xorBinaryPacking0.compress0(intArray0, intWrapper0, (-187), intArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        xorBinaryPacking0.compress0(intArray0, intWrapper1, 1881, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 42 out of bounds for length 42
         //
         verifyException("me.lemire.integercompression.differential.XorBinaryPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      int[] intArray0 = new int[42];
      IntWrapper intWrapper0 = new IntWrapper(3117);
      xorBinaryPacking0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(42, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[5];
      xorBinaryPacking0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      XorBinaryPacking xorBinaryPacking0 = new XorBinaryPacking();
      String string0 = xorBinaryPacking0.toString();
      assertEquals("XorBinaryPacking", string0);
  }
}
