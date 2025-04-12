
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
import me.lemire.integercompression.OptPFD;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptPFD_ESTest extends OptPFD_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[8];
      intArray0[0] = 1507;
      intArray0[1] = (-578);
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        optPFD0.uncompress0(intArray0, intWrapper0, (-578), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[6];
      intArray0[0] = 131053;
      // Undeclared exception!
      try { 
        optPFD0.headlessUncompress(intArray0, intWrapper0, 131053, intArray0, intWrapper0, 379);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 237 out of bounds for length 17
         //
         verifyException("me.lemire.integercompression.OptPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper((-2037));
      optPFD0.headlessUncompress(intArray0, intWrapper0, 3941, intArray0, intWrapper0, (-2037));
      assertEquals((-2037.0F), intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFD0.uncompress0(intArray0, intWrapper0, (-578), intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(12);
      // Undeclared exception!
      try { 
        optPFD0.headlessCompress(intArray0, intWrapper0, 210, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper1 = new IntWrapper(Integer.MAX_VALUE);
      // Undeclared exception!
      try { 
        optPFD0.compress0(intArray0, intWrapper1, (-1099), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2147483521 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[5];
      OptPFD optPFD0 = new OptPFD();
      // Undeclared exception!
      try { 
        optPFD0.uncompress0(intArray0, (IntWrapper) null, 3079, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      // Undeclared exception!
      try { 
        optPFD0.headlessUncompress((int[]) null, intWrapper0, 67111079, (int[]) null, intWrapper0, 67111079);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper1 = new IntWrapper(2147483635);
      // Undeclared exception!
      try { 
        optPFD0.headlessUncompress(intArray0, intWrapper0, 2147483635, intArray0, intWrapper1, 2147483635);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483635) > toIndex(-2147483629)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(1414);
      // Undeclared exception!
      try { 
        optPFD0.headlessCompress(intArray0, (IntWrapper) null, 1414, intArray0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      // Undeclared exception!
      try { 
        optPFD0.compress0((int[]) null, intWrapper0, 1117, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFD", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(128);
      OptPFD optPFD0 = new OptPFD();
      optPFD0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(128, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(2948);
      optPFD0.compress0(intArray0, intWrapper0, 11, intArray0, intWrapper0);
      assertEquals(4, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[141];
      // Undeclared exception!
      try { 
        optPFD0.headlessUncompress(intArray0, intWrapper0, 5268, intArray0, intWrapper0, 5268);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 160
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[6];
      optPFD0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(4);
      optPFD0.compress0((int[]) null, intWrapper0, (-1398), intArray0, intWrapper0);
      assertEquals((byte)5, intWrapper0.byteValue());
      assertArrayEquals(new int[] {0, 0, 0, 0, (-1280), 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[141];
      IntWrapper intWrapper1 = new IntWrapper(32);
      // Undeclared exception!
      try { 
        optPFD0.compress0(intArray0, intWrapper0, 1023, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 141 out of bounds for length 141
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(2948);
      optPFD0.headlessCompress(intArray0, intWrapper0, 24, intArray0, intWrapper0);
      assertEquals(2948.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      OptPFD optPFD0 = new OptPFD();
      String string0 = optPFD0.toString();
      assertEquals("OptPFD", string0);
  }
}
