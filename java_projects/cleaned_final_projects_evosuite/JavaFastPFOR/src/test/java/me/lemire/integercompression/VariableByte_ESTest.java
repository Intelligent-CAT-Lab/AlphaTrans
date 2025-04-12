
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
import java.nio.ByteBuffer;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.VariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class VariableByte_ESTest extends VariableByte_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[7];
      intArray0[2] = (-3509);
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        variableByte0.headlessUncompress(intArray0, intWrapper0, (-1746), intArray0, intWrapper0, 3552);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[13];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[5];
      byteArray0[2] = (byte)1;
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, intWrapper0, (byte)60, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[13];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[4];
      variableByte0.uncompress1(byteArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((byte)0, intWrapper0.byteValue());
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray1 = new int[9];
      intArray1[2] = (int) (byte) (-128);
      // Undeclared exception!
      try { 
        variableByte0.uncompress0(intArray1, intWrapper0, 4412, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[5];
      IntWrapper intWrapper0 = new IntWrapper(2177);
      variableByte0.uncompress0(intArray0, intWrapper0, (-1300), intArray0, intWrapper0);
      assertEquals(877.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals("877", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper1 = new IntWrapper(1);
      variableByte0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper1);
      byte[] byteArray0 = new byte[7];
      variableByte0.compress1(intArray0, intWrapper0, 1, byteArray0, intWrapper0);
      assertEquals((byte)4, intWrapper0.byteValue());
      assertEquals(4.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-492));
      variableByte0.compress1((int[]) null, intWrapper0, (-492), (byte[]) null, intWrapper0);
      assertEquals((-984.0), intWrapper0.doubleValue(), 0.01);
      assertEquals("-984", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      variableByte0.compress0(intArray0, intWrapper1, 1, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        variableByte0.compress0(intArray0, intWrapper0, 2297, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper((-1));
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, (-2147337599), intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      ByteBuffer byteBuffer0 = variableByte0.makeBuffer(2538);
      assertEquals(2538, byteBuffer0.limit());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[4];
      intArray0[0] = (-547);
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[8];
      variableByte0.compress1(intArray0, intWrapper0, 1, byteArray0, intWrapper0);
      assertEquals((short)6, intWrapper0.shortValue());
      assertArrayEquals(new byte[] {(byte)93, (byte)123, (byte)127, (byte)127, (byte) (-113), (byte)0, (byte)0, (byte)0}, byteArray0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[7];
      intArray0[2] = (-3509);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        variableByte0.compress1(intArray0, intWrapper0, 552, byteArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      byte[] byteArray0 = new byte[0];
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, (IntWrapper) null, (-2130706431), intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      // Undeclared exception!
      try { 
        variableByte0.uncompress0((int[]) null, (IntWrapper) null, 1643, (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      // Undeclared exception!
      try { 
        variableByte0.makeBuffer((-1855));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-1855 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        variableByte0.headlessUncompress((int[]) null, intWrapper0, 2069, (int[]) null, intWrapper0, 2069);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-492));
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress((int[]) null, intWrapper0, 7, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper((-1835));
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper1);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-183));
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress((int[]) null, intWrapper0, (-183), (int[]) null, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-1464 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        variableByte0.compress0((int[]) null, intWrapper0, 7, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[1];
      intArray0[0] = (-24);
      // Undeclared exception!
      try { 
        variableByte0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
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
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      VariableByte variableByte0 = new VariableByte();
      // Undeclared exception!
      try { 
        variableByte0.compress0(intArray0, intWrapper0, (-2036), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-16288 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      intArray0[2] = 33835;
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, 33835, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[8];
      intArray0[0] = 3552;
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, 3552, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      variableByte0.headlessCompress(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      assertEquals((byte)2, intWrapper0.byteValue());
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      variableByte0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0, 0, 0}, intArray0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[2];
      intArray0[0] = 138;
      variableByte0.headlessUncompress(intArray0, intWrapper0, 1, intArray0, intWrapper0, 1);
      assertEquals("1", intWrapper0.toString());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-492));
      variableByte0.headlessUncompress((int[]) null, intWrapper0, (-492), (int[]) null, intWrapper0, (-492));
      assertEquals("-492", intWrapper0.toString());
      assertEquals((short) (-492), intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[13];
      IntWrapper intWrapper0 = new IntWrapper(0);
      byte[] byteArray0 = new byte[5];
      byteArray0[3] = (byte) (-69);
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, intWrapper0, (byte)60, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      byte[] byteArray0 = new byte[3];
      byteArray0[1] = (byte) (-77);
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, intWrapper0, (byte)7, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte) (-42);
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, intWrapper0, 86, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      byte[] byteArray0 = new byte[3];
      int[] intArray0 = new int[6];
      variableByte0.uncompress1(byteArray0, intWrapper0, (byte) (-114), intArray0, intWrapper0);
      assertEquals(0, intWrapper0.intValue());
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[1];
      intArray0[0] = (-24);
      // Undeclared exception!
      try { 
        variableByte0.compress1(intArray0, intWrapper0, 1, (byte[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[2];
      intArray0[0] = 134;
      IntWrapper intWrapper1 = new IntWrapper(1);
      variableByte0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper1);
      byte[] byteArray0 = new byte[19];
      variableByte0.compress1(intArray0, intWrapper0, 1, byteArray0, intWrapper1);
      // Undeclared exception!
      try { 
        variableByte0.uncompress1(byteArray0, intWrapper0, 134, intArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      variableByte0.compress1(intArray0, intWrapper0, 0, (byte[]) null, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[8];
      intArray0[0] = 3552;
      intArray0[1] = 3552;
      variableByte0.uncompress0(intArray0, intWrapper1, 2, intArray0, intWrapper1);
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, 3552, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      VariableByte variableByte0 = new VariableByte();
      int[] intArray0 = new int[8];
      intArray0[3] = 1840700269;
      // Undeclared exception!
      try { 
        variableByte0.headlessCompress(intArray0, intWrapper0, 3552, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.VariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      String string0 = variableByte0.toString();
      assertEquals("VariableByte", string0);
  }
}
