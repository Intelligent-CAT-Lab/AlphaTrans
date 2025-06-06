
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
import me.lemire.integercompression.NewPFDS9;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class NewPFDS9_ESTest extends NewPFDS9_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      int[] intArray0 = new int[1];
      newPFDS9_0.uncompress0(intArray0, intWrapper0, 2369, (int[]) null, intWrapper1);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(0L, intWrapper1.longValue());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(30);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[7];
      newPFDS9_0.compress0(intArray0, intWrapper0, (-2182), intArray1, intWrapper1);
      assertEquals((short)1, intWrapper1.shortValue());
      assertEquals(1, intWrapper1.intValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(30);
      int[] intArray1 = new int[7];
      // Undeclared exception!
      try { 
        newPFDS9_0.compress0(intArray0, intWrapper0, (-2182), intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 30 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[4];
      intArray0[0] = 3034;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[3];
      // Undeclared exception!
      try { 
        newPFDS9_0.uncompress0(intArray0, intWrapper0, (-1166), intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 33
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[4];
      intArray0[0] = 3034;
      intArray0[1] = 1683;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFDS9_0.uncompress0(intArray0, intWrapper0, (-1166), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 147 out of bounds for length 17
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[5];
      intArray0[1] = Integer.MIN_VALUE;
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessUncompress(intArray0, intWrapper0, 2, intArray0, intWrapper0, 137);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 33
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(30);
      newPFDS9_0.headlessUncompress(intArray0, intWrapper0, (-3922), intArray0, intWrapper0, (-2176));
      assertEquals(30, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[11];
      IntWrapper intWrapper0 = new IntWrapper(15);
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessCompress(intArray0, intWrapper0, 144, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[2];
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessCompress(intArray1, intWrapper0, 1842, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[6];
      intArray1[0] = 3510;
      intArray1[1] = 3510;
      intArray1[2] = (-187);
      // Undeclared exception!
      try { 
        newPFDS9_0.uncompress0(intArray1, intWrapper0, (-187), intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      // Undeclared exception!
      try { 
        newPFDS9_0.uncompress0((int[]) null, (IntWrapper) null, (-23), (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 445;
      intArray0[1] = (-1501);
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessUncompress(intArray0, intWrapper0, (-1501), intArray0, intWrapper0, 1034);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessUncompress((int[]) null, intWrapper0, Integer.MAX_VALUE, (int[]) null, intWrapper0, Integer.MAX_VALUE);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessUncompress(intArray0, intWrapper0, 1472, intArray0, intWrapper1, 418);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483647) > toIndex(-2147483617)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper((-2524));
      // Undeclared exception!
      try { 
        newPFDS9_0.compress0((int[]) null, intWrapper0, (-2524), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      int[] intArray0 = new int[9];
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS9_0.compress0(intArray0, intWrapper0, Integer.MAX_VALUE, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2147483647 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(0);
      newPFDS9_0.uncompress0((int[]) null, intWrapper0, 0, (int[]) null, intWrapper0);
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(34);
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      newPFDS9_0.compress0(intArray0, intWrapper0, 34, intArray0, intWrapper0);
      assertEquals(34, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[9];
      newPFDS9_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessCompress(intArray0, intWrapper1, Integer.MAX_VALUE, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483521 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      newPFDS9_0.headlessCompress(intArray0, intWrapper0, (-3471), intArray0, intWrapper0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      newPFDS9_0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS9_0.headlessCompress((int[]) null, intWrapper0, Integer.MAX_VALUE, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      String string0 = newPFDS9_0.toString();
      assertEquals("NewPFDS9", string0);
  }
}
