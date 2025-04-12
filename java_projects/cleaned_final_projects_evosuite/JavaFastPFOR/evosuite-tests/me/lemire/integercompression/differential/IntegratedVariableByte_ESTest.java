
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
import java.nio.BufferOverflowException;
import java.nio.ByteBuffer;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.differential.IntegratedVariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegratedVariableByte_ESTest extends IntegratedVariableByte_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(2794);
      IntWrapper intWrapper1 = new IntWrapper(1);
      int[] intArray0 = new int[7];
      intArray0[2] = (-2525);
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessUncompress(intArray0, intWrapper1, 7, intArray0, intWrapper0, 5, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2794 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(0);
      int[] intArray0 = new int[6];
      intArray0[0] = 997;
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessUncompress(intArray0, intWrapper0, 997, intArray0, intWrapper0, 997, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[16];
      intArray0[3] = (-257);
      intArray0[4] = (-129);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 16, intArray0, intWrapper0, intWrapper0);
      assertEquals("22", intWrapper0.toString());
      assertEquals(22, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[4];
      byteArray0[2] = (byte)116;
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, (byte)19, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[4];
      byteArray0[1] = (byte)66;
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, 1, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      byte[] byteArray0 = new byte[2];
      byteArray0[0] = (byte)4;
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, (byte)4, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[9];
      intArray0[7] = (-4555);
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress0(intArray0, intWrapper0, 1435, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(878);
      integratedVariableByte0.uncompress0(intArray0, intWrapper0, (-86), intArray0, intWrapper0);
      assertEquals(792.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals((short)792, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[9];
      byte[] byteArray0 = new byte[3];
      integratedVariableByte0.compress1(intArray0, intWrapper0, 1, byteArray0, intWrapper0);
      assertEquals(3L, intWrapper0.longValue());
      assertEquals(3, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[8];
      intArray0[3] = (-257);
      intArray0[4] = (-129);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper0, 31, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(0);
      integratedVariableByte0.compress0(intArray0, intWrapper0, (-2130836486), intArray0, intWrapper0);
      assertEquals((-2.13083648E9F), intWrapper0.floatValue(), 0.01F);
      assertEquals((short)1018, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      ByteBuffer byteBuffer0 = integratedVariableByte0.makeBuffer(4025);
      assertEquals(4025, byteBuffer0.capacity());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, 2, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress0(intArray0, (IntWrapper) null, 122, intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      // Undeclared exception!
      try { 
        integratedVariableByte0.makeBuffer((-1));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-1 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-1805));
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessUncompress((int[]) null, intWrapper0, (-1805), (int[]) null, intWrapper0, (-1805), intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessCompress((int[]) null, intWrapper0, 14, (int[]) null, intWrapper0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(79);
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 79, intArray0, intWrapper0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 157 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper0, 1073741824, intArray0, intWrapper0);
        fail("Expecting exception: BufferOverflowException");
      
      } catch(BufferOverflowException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(984);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0((int[]) null, intWrapper0, 984, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[5];
      IntWrapper intWrapper1 = new IntWrapper(1633);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper1);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper0, (-721), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-5768 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      intArray0[3] = (-279);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      integratedVariableByte0.headlessUncompress(intArray0, intWrapper0, (-279), intArray0, intWrapper0, 1, intWrapper0);
      assertEquals((short)4, intWrapper0.shortValue());
      assertEquals(4L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[8];
      integratedVariableByte0.headlessUncompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, 0, intWrapper0);
      assertEquals((short)1, intWrapper0.shortValue());
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[26];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper1 = new IntWrapper(12);
      integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 12, intArray0, intWrapper0, intWrapper1);
      integratedVariableByte0.headlessCompress(intArray0, intWrapper1, 12, intArray0, intWrapper0, intWrapper0);
      assertEquals(7.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(7, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[5];
      intArray0[1] = 3359;
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper(1);
      IntWrapper intWrapper2 = new IntWrapper(83);
      integratedVariableByte0.headlessCompress(intArray0, intWrapper1, 1, intArray0, intWrapper1, intWrapper2);
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper2, intWrapper2);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[4];
      byteArray0[3] = (byte) (-87);
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, (byte)19, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[4];
      byteArray0[2] = (byte) (-45);
      integratedVariableByte0.uncompress1(byteArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals((byte)4, intWrapper0.byteValue());
      assertEquals(4.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte) (-1);
      // Undeclared exception!
      try { 
        integratedVariableByte0.uncompress1(byteArray0, intWrapper0, (byte)4, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[20];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[2];
      byteArray0[0] = (byte) (-3);
      integratedVariableByte0.uncompress1(byteArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(2, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[9];
      byte[] byteArray0 = new byte[0];
      integratedVariableByte0.uncompress1(byteArray0, intWrapper0, (-5025), intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        integratedVariableByte0.headlessCompress(intArray0, intWrapper0, (-1), intArray0, intWrapper0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-8 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[44];
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      integratedVariableByte0.uncompress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      assertEquals(3.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(3, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray0 = new int[6];
      intArray0[2] = 2964;
      byte[] byteArray0 = new byte[12];
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress1(intArray0, intWrapper0, 2964, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[2];
      intArray0[1] = 3407;
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper(1);
      IntWrapper intWrapper2 = new IntWrapper(22);
      integratedVariableByte0.headlessCompress(intArray0, intWrapper1, 1, intArray0, intWrapper1, intWrapper2);
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress1(intArray0, intWrapper0, 2785, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      byte[] byteArray0 = new byte[9];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      integratedVariableByte0.compress1((int[]) null, intWrapper0, (-510), byteArray0, intWrapper0);
      assertEquals((short) (-510), intWrapper0.shortValue());
      assertEquals("-510", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[16];
      byte[] byteArray0 = new byte[9];
      integratedVariableByte0.compress1(intArray0, intWrapper0, (byte)0, byteArray0, intWrapper0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
      assertEquals((byte)0, intWrapper0.byteValue());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[4];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress1(intArray0, intWrapper0, 3241, (byte[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[24];
      IntWrapper intWrapper1 = new IntWrapper(1);
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      integratedVariableByte0.headlessCompress(intArray0, intWrapper1, 3, intArray0, intWrapper1, intWrapper0);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper0, 4258, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 24 out of bounds for length 24
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      int[] intArray0 = new int[4];
      intArray0[1] = 3241;
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper(1);
      IntWrapper intWrapper2 = new IntWrapper(24);
      integratedVariableByte0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, intWrapper2);
      // Undeclared exception!
      try { 
        integratedVariableByte0.compress0(intArray0, intWrapper1, 39185, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[8];
      integratedVariableByte0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(0, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      IntegratedVariableByte integratedVariableByte0 = new IntegratedVariableByte();
      String string0 = integratedVariableByte0.toString();
      assertEquals("IntegratedVariableByte", string0);
  }
}
