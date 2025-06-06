
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


package me.lemire.integercompression;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.NewPFD;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class NewPFD_ESTest extends NewPFD_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[9];
      intArray0[0] = 262016;
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        newPFD0.headlessUncompress(intArray0, intWrapper0, 2727, intArray0, intWrapper0, 262016);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 128 out of bounds for length 17
         //
         verifyException("me.lemire.integercompression.NewPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[9];
      intArray0[0] = 512;
      intArray0[1] = (-3968);
      // Undeclared exception!
      try { 
        newPFD0.uncompress0(intArray0, intWrapper0, (-2366), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFD0.compress0(intArray0, intWrapper0, 128, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(2147483607);
      NewPFD.getBestBFromData(intArray0, 2147483607, intWrapper0, intWrapper0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(1);
      newPFD0.uncompress0(intArray0, intWrapper0, 31, intArray0, intWrapper0);
      assertEquals(2, intWrapper0.get());
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper0 = new IntWrapper(1792);
      // Undeclared exception!
      try { 
        newPFD0.uncompress0((int[]) null, intWrapper0, 1792, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFD0.headlessUncompress((int[]) null, intWrapper0, 1126, (int[]) null, intWrapper0, 1126);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFD0.headlessUncompress(intArray0, intWrapper0, Integer.MAX_VALUE, intArray0, intWrapper1, Integer.MAX_VALUE);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483647) > toIndex(-2147483617)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[2];
      NewPFD newPFD0 = new NewPFD();
      // Undeclared exception!
      try { 
        newPFD0.headlessCompress(intArray0, (IntWrapper) null, 2705, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      // Undeclared exception!
      try { 
        NewPFD.getBestBFromData((int[]) null, Integer.MIN_VALUE, (IntWrapper) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        NewPFD.getBestBFromData(intArray0, (-2074), intWrapper0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2074 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        newPFD0.compress0(intArray0, (IntWrapper) null, 1836, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFD0.compress0(intArray0, intWrapper0, 3053, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      newPFD0.uncompress0(intArray0, (IntWrapper) null, 0, intArray0, intWrapper0);
      assertEquals(2.14748365E9F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[3];
      newPFD0.compress0(intArray0, intWrapper0, (-5), intArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals(0, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      newPFD0.headlessUncompress(intArray0, intWrapper0, (-1571), intArray0, intWrapper0, (-1571));
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[8];
      newPFD0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[32];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFD0.headlessUncompress(intArray0, intWrapper0, 2793, intArray0, intWrapper0, 2793);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 64
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(2147483607);
      int[] intArray0 = new int[20];
      NewPFD newPFD0 = new NewPFD();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFD0.headlessCompress(intArray0, intWrapper0, 2152, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483561 out of bounds for length 20
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      newPFD0.compress0(intArray0, intWrapper0, (-3313), intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertArrayEquals(new int[] {(-3200), 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      newPFD0.headlessCompress(intArray0, intWrapper0, 19, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      String string0 = newPFD0.toString();
      assertEquals("NewPFD", string0);
  }
}
