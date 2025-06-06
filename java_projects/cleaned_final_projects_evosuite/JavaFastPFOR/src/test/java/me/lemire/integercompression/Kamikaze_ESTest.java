
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
import me.lemire.integercompression.Kamikaze;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Kamikaze_ESTest extends Kamikaze_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1241));
      IntWrapper intWrapper1 = new IntWrapper(0);
      kamikaze0.uncompress0(intArray0, intWrapper1, 1594, intArray0, intWrapper0);
      assertEquals(1.0F, intWrapper1.floatValue(), 0.01F);
      assertEquals(1, intWrapper1.get());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray1 = new int[4];
      kamikaze0.uncompress0(intArray0, intWrapper0, (-1), intArray1, intWrapper0);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(2600);
      IntWrapper intWrapper1 = new IntWrapper(24);
      kamikaze0.headlessUncompress(intArray0, intWrapper0, (-627), intArray0, intWrapper1, 896);
      assertEquals((byte) (-104), intWrapper1.byteValue());
      assertEquals(2602, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(711);
      int[] intArray1 = new int[4];
      // Undeclared exception!
      try { 
        kamikaze0.headlessUncompress(intArray0, intWrapper0, 711, intArray1, intWrapper0, 2432);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1241));
      kamikaze0.headlessUncompress(intArray0, intWrapper0, (-1241), intArray0, intWrapper0, (-1241));
      assertEquals((-1241L), intWrapper0.longValue());
      assertEquals((-1241), intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(31);
      int[] intArray1 = new int[6];
      // Undeclared exception!
      try { 
        kamikaze0.headlessCompress(intArray0, intWrapper0, 1925, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1241));
      IntWrapper intWrapper1 = new IntWrapper(0);
      kamikaze0.compress0((int[]) null, intWrapper0, (-3722), intArray0, intWrapper1);
      assertEquals(1.0F, intWrapper1.floatValue(), 0.01F);
      assertArrayEquals(new int[] {(-3712), 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      IntWrapper intWrapper0 = new IntWrapper((-1));
      // Undeclared exception!
      try { 
        kamikaze0.uncompress0((int[]) null, intWrapper0, (-1), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Kamikaze", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntWrapper intWrapper0 = new IntWrapper(1870);
      Kamikaze kamikaze0 = new Kamikaze();
      // Undeclared exception!
      try { 
        kamikaze0.headlessUncompress((int[]) null, intWrapper0, 1870, (int[]) null, intWrapper0, 1870);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(2147483520);
      // Undeclared exception!
      try { 
        kamikaze0.headlessUncompress(intArray0, intWrapper0, 2147483520, intArray0, intWrapper0, 2147483520);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -256
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[2];
      intArray0[0] = 2147483528;
      // Undeclared exception!
      try { 
        kamikaze0.headlessCompress(intArray0, (IntWrapper) null, 2147483528, intArray0, (IntWrapper) null);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -256
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      Kamikaze kamikaze0 = new Kamikaze();
      // Undeclared exception!
      try { 
        kamikaze0.compress0((int[]) null, intWrapper0, 2602, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Kamikaze", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      IntWrapper intWrapper0 = new IntWrapper(0);
      kamikaze0.uncompress0((int[]) null, intWrapper0, 0, (int[]) null, intWrapper0);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1241));
      // Undeclared exception!
      try { 
        kamikaze0.uncompress0(intArray0, intWrapper0, 1594, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1241 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Kamikaze", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      Kamikaze kamikaze0 = new Kamikaze();
      kamikaze0.compress0((int[]) null, intWrapper0, 14, (int[]) null, intWrapper0);
      assertEquals(0, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper((-1241));
      // Undeclared exception!
      try { 
        kamikaze0.compress0((int[]) null, intWrapper0, (-3722), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1241 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.Kamikaze", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      IntWrapper intWrapper0 = new IntWrapper(1870);
      // Undeclared exception!
      try { 
        kamikaze0.headlessCompress((int[]) null, intWrapper0, 1870, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("com.kamikaze.pfordelta.PForDelta", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper(2600);
      kamikaze0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertArrayEquals(new int[] {0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      Kamikaze kamikaze0 = new Kamikaze();
      String string0 = kamikaze0.toString();
      assertEquals("Kamikaze's PForDelta", string0);
  }
}
