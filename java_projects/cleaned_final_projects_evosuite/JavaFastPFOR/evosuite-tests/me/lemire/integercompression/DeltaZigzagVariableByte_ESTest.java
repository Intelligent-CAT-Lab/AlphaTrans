
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
import me.lemire.integercompression.DeltaZigzagVariableByte;
import me.lemire.integercompression.IntWrapper;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DeltaZigzagVariableByte_ESTest extends DeltaZigzagVariableByte_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(3124);
      deltaZigzagVariableByte0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(3124.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(3124.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper((-4262));
      deltaZigzagVariableByte0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper1);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals((-4262.0F), intWrapper1.floatValue(), 0.01F);
      assertEquals(0L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[24];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray1 = new int[7];
      deltaZigzagVariableByte0.uncompress0(intArray1, intWrapper0, 4, intArray0, intWrapper0);
      assertEquals(4, intWrapper0.get());
      assertEquals(4L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(0);
      deltaZigzagVariableByte0.uncompress0(intArray0, intWrapper0, (-1340), intArray0, intWrapper0);
      assertEquals((-1340), intWrapper0.get());
      assertEquals((byte) (-60), intWrapper0.byteValue());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 1, intArray0, intWrapper0);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.uncompress0(intArray0, intWrapper1, 1679, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, (-1686698240), intArray0, intWrapper0);
      assertEquals((-1.68669824E9F), intWrapper0.floatValue(), 0.01F);
      assertEquals((-1686698240), intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      ByteBuffer byteBuffer0 = deltaZigzagVariableByte0.makeBuffer(0);
      assertEquals(0, byteBuffer0.limit());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.uncompress0((int[]) null, (IntWrapper) null, (-1), (int[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.makeBuffer((-198));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-198 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 1, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, (-1787230848), intArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-346219645 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[3];
      intArray0[2] = (-4321);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 100713287, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[9];
      intArray0[0] = (-4321);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.uncompress0(intArray0, intWrapper0, 1679, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[24];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 1498, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 24 out of bounds for length 24
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[9];
      intArray0[4] = (-451);
      intArray0[5] = 155;
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 1427, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[6];
      intArray0[2] = 1379;
      intArray0[3] = (-1310);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 1379, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[9];
      intArray0[0] = (-4321);
      intArray0[1] = 6379;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      assertEquals(5.0, intWrapper0.doubleValue(), 0.01);
      assertArrayEquals(new int[] {(-1019117145), 417551744, 0, 0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      intArray0[1] = 3;
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 3, intArray0, intWrapper1);
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      assertEquals(5, intWrapper0.intValue());
      assertEquals(5, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      intArray0[1] = 4;
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 4, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 4, intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[6];
      intArray0[1] = 4;
      intWrapper0.increment();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 4, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 4, intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[5];
      intArray0[0] = 6381;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 6381, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      int[] intArray0 = new int[5];
      intArray0[1] = 6363;
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 3, intArray0, intWrapper0);
      // Undeclared exception!
      try { 
        deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 6363, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.DeltaZigzagVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      int[] intArray0 = new int[24];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      int[] intArray0 = new int[33];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper0, 6, intArray0, intWrapper0);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 6, intArray0, intWrapper0);
      assertEquals(11L, intWrapper0.longValue());
      
      deltaZigzagVariableByte0.compress0(intArray0, intWrapper1, 6, intArray0, intWrapper1);
      assertEquals(17, intWrapper1.get());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      String string0 = deltaZigzagVariableByte0.toString();
      assertEquals("DeltaZigzagVariableByte", string0);
  }
}
