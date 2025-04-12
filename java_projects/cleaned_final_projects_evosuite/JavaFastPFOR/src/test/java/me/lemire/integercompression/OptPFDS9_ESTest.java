
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
import me.lemire.integercompression.OptPFDS9;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptPFDS9_ESTest extends OptPFDS9_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      int[] intArray0 = new int[46];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray1 = new int[7];
      intArray1[0] = 2;
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessUncompress(intArray1, intWrapper0, Integer.MIN_VALUE, intArray0, intWrapper0, 1191);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 46 out of bounds for length 46
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[5];
      intArray0[0] = 524296;
      intArray0[1] = 524296;
      // Undeclared exception!
      try { 
        optPFDS9_0.uncompress0(intArray0, intWrapper0, 524296, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[6];
      intArray0[0] = 898;
      intArray0[1] = (-2837);
      // Undeclared exception!
      try { 
        optPFDS9_0.uncompress0(intArray0, intWrapper0, (-43), intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFDS9_0.headlessUncompress(intArray0, intWrapper0, 31, intArray0, intWrapper0, (-674));
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessCompress(intArray0, intWrapper0, 212, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      optPFDS9_0.compress0(intArray0, intWrapper0, (-1584), intArray0, intWrapper0);
      assertEquals(1, intWrapper0.get());
      assertArrayEquals(new int[] {(-1536), 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[4];
      intArray0[0] = 1632;
      intArray0[1] = 1632;
      intArray0[2] = (-236);
      // Undeclared exception!
      try { 
        optPFDS9_0.uncompress0(intArray0, intWrapper0, (-236), intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        optPFDS9_0.uncompress0(intArray0, (IntWrapper) null, 67108863, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 2952;
      intArray0[1] = (-2837);
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessUncompress(intArray0, intWrapper0, (-2837), intArray0, intWrapper0, 2952);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessUncompress((int[]) null, intWrapper0, 4194303, (int[]) null, intWrapper0, 4194303);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessCompress((int[]) null, (IntWrapper) null, 1603, (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      int[] intArray0 = new int[18];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      // Undeclared exception!
      try { 
        optPFDS9_0.headlessCompress(intArray0, intWrapper0, 3792, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS9_0.compress0((int[]) null, intWrapper0, (-2026), (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFDS9_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFDS9_0.uncompress0(intArray0, intWrapper0, (-2427), intArray0, intWrapper0);
      assertEquals(1.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[4];
      optPFDS9_0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFDS9_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals((byte)0, intWrapper0.byteValue());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      optPFDS9_0.headlessUncompress(intArray0, intWrapper0, 245, intArray0, intWrapper0, 245);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      int[] intArray0 = new int[46];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      optPFDS9_0.headlessCompress(intArray0, intWrapper0, (-1357), intArray0, intWrapper0);
      assertEquals(46, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      IntWrapper intWrapper1 = new IntWrapper(98);
      // Undeclared exception!
      try { 
        optPFDS9_0.compress0(intArray0, intWrapper0, 2617, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 129 out of bounds for length 129
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(906);
      optPFDS9_0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((byte) (-118), intWrapper0.byteValue());
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      int[] intArray0 = new int[129];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      // Undeclared exception!
      try { 
        optPFDS9_0.compress0(intArray0, intWrapper0, 2617, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 129 out of bounds for length 129
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      OptPFDS9 optPFDS9_0 = new OptPFDS9();
      String string0 = optPFDS9_0.toString();
      assertEquals("OptPFDS9", string0);
  }
}
