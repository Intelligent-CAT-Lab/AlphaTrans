
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
import me.lemire.integercompression.NewPFDS16;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class NewPFDS16_ESTest extends NewPFDS16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(2);
      int[] intArray1 = new int[7];
      newPFDS16_0.uncompress0(intArray0, intWrapper0, 17, intArray1, intWrapper0);
      assertEquals((short)3, intWrapper0.shortValue());
      assertEquals(3L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper((-4527));
      int[] intArray1 = new int[4];
      // Undeclared exception!
      try { 
        newPFDS16_0.uncompress0(intArray0, intWrapper0, (-3949), intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -4527 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[3];
      // Undeclared exception!
      try { 
        newPFDS16_0.compress0(intArray0, intWrapper0, 668, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[133];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(2);
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress(intArray0, intWrapper0, (-2081), intArray0, intWrapper1, 514);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 162
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[3];
      intArray0[1] = 668;
      intArray0[2] = 11;
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        newPFDS16_0.uncompress0(intArray0, intWrapper0, (-155), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[8];
      intArray0[0] = 131071;
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress(intArray0, intWrapper0, 131071, (int[]) null, intWrapper0, 131071);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 255 out of bounds for length 17
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[32];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[5];
      intArray1[0] = 1028;
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress(intArray1, intWrapper0, 3116, intArray0, intWrapper0, 1028);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[1];
      intArray0[0] = (-1222);
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress(intArray0, intWrapper0, 320, intArray0, intWrapper0, 320);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(1686);
      newPFDS16_0.headlessUncompress(intArray0, intWrapper0, (-3830), intArray0, intWrapper0, (-730));
      assertEquals(1686L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessCompress((int[]) null, intWrapper0, Integer.MAX_VALUE, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper((-4));
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessCompress(intArray0, intWrapper0, 137, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -4 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(14);
      IntWrapper intWrapper1 = new IntWrapper(0);
      newPFDS16_0.uncompress0(intArray0, intWrapper1, (-1222), intArray0, intWrapper0);
      assertEquals(1.0F, intWrapper1.floatValue(), 0.01F);
      assertEquals(14, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress((int[]) null, intWrapper0, Integer.MAX_VALUE, (int[]) null, intWrapper0, Integer.MAX_VALUE);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper1 = new IntWrapper(2147483618);
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessUncompress(intArray0, intWrapper0, 1660, intArray0, intWrapper1, 2147483618);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483618) > toIndex(-2147483646)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(131071);
      // Undeclared exception!
      try { 
        newPFDS16_0.compress0((int[]) null, intWrapper0, 993, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(14);
      newPFDS16_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals("14", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper((-845));
      // Undeclared exception!
      try { 
        newPFDS16_0.uncompress0((int[]) null, intWrapper0, (-845), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(18);
      newPFDS16_0.compress0((int[]) null, intWrapper0, 0, (int[]) null, intWrapper0);
      assertEquals(18.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      newPFDS16_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[13];
      IntWrapper intWrapper0 = new IntWrapper(2147483646);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessCompress(intArray0, intWrapper0, 2147483646, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483522 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(14);
      IntWrapper intWrapper1 = new IntWrapper(0);
      newPFDS16_0.compress0(intArray0, intWrapper0, (-862), intArray0, intWrapper1);
      assertEquals((short)1, intWrapper1.shortValue());
      assertEquals(14, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[133];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      newPFDS16_0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      int[] intArray0 = new int[133];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        newPFDS16_0.headlessCompress(intArray0, intWrapper0, 509, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.NewPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      NewPFDS16 newPFDS16_0 = new NewPFDS16();
      String string0 = newPFDS16_0.toString();
      assertEquals("NewPFDS16", string0);
  }
}
