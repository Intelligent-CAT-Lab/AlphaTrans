
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
import me.lemire.integercompression.Composition;
import me.lemire.integercompression.DeltaZigzagVariableByte;
import me.lemire.integercompression.FastPFOR;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.IntegerCODEC;
import me.lemire.integercompression.NewPFD;
import me.lemire.integercompression.NewPFDS9;
import me.lemire.integercompression.VariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Composition_ESTest extends Composition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      Composition composition1 = new Composition(composition0, newPFDS9_0);
      String string0 = composition1.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      composition0.uncompress0(intArray0, intWrapper1, (-484), intArray0, intWrapper0);
      assertEquals(2.0, intWrapper1.doubleValue(), 0.01);
      assertEquals(2, intWrapper1.get());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray1 = new int[8];
      composition0.uncompress0(intArray0, intWrapper0, 55, intArray1, intWrapper0);
      assertEquals((short)3, intWrapper0.shortValue());
      assertEquals(3, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      Composition composition1 = new Composition(composition0, newPFDS9_0);
      composition1.uncompress0(intArray0, intWrapper0, 55, intArray0, intWrapper0);
      assertEquals((byte)4, intWrapper0.byteValue());
      assertEquals(4.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[7];
      IntWrapper intWrapper0 = new IntWrapper(0);
      Composition composition1 = new Composition(composition0, newPFDS9_0);
      composition1.compress0(intArray0, intWrapper0, 78, intArray0, intWrapper0);
      assertEquals((byte)1, intWrapper0.byteValue());
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      int[] intArray1 = new int[8];
      composition0.compress0(intArray0, intWrapper0, 55, intArray1, intWrapper0);
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(2, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper(0);
      composition0.compress0(intArray0, intWrapper0, 55, intArray0, intWrapper1);
      assertEquals(1.0F, intWrapper1.floatValue(), 0.01F);
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      intArray0[1] = 524287;
      intArray0[2] = 554;
      intArray0[3] = (-6);
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        composition0.uncompress0(intArray0, intWrapper0, (-484), intArray0, intWrapper0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // shouldn't happen
         //
         verifyException("me.lemire.integercompression.S9", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      IntWrapper intWrapper0 = new IntWrapper(65536);
      Composition composition0 = new Composition(fastPFOR0, fastPFOR0);
      // Undeclared exception!
      try { 
        composition0.uncompress0((int[]) null, intWrapper0, 65536, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      NewPFDS9 newPFDS9_0 = new NewPFDS9();
      Composition composition0 = new Composition(newPFDS9_0, newPFDS9_0);
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper((-1764));
      // Undeclared exception!
      try { 
        composition0.uncompress0(intArray0, intWrapper1, 55, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1764 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.NewPFDS9", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Composition composition0 = new Composition((IntegerCODEC) null, (IntegerCODEC) null);
      // Undeclared exception!
      try { 
        composition0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      Composition composition0 = new Composition(fastPFOR0, fastPFOR0);
      IntWrapper intWrapper0 = new IntWrapper(256);
      // Undeclared exception!
      try { 
        composition0.compress0((int[]) null, intWrapper0, 256, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.FastPFOR", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      NewPFD newPFD0 = new NewPFD();
      DeltaZigzagVariableByte deltaZigzagVariableByte0 = new DeltaZigzagVariableByte();
      Composition composition0 = new Composition(deltaZigzagVariableByte0, newPFD0);
      IntWrapper intWrapper0 = new IntWrapper(4336);
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        composition0.compress0(intArray0, intWrapper0, Integer.MAX_VALUE, intArray0, intWrapper0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      VariableByte variableByte0 = new VariableByte();
      Composition composition0 = new Composition(variableByte0, variableByte0);
      IntWrapper intWrapper0 = new IntWrapper((-3032));
      // Undeclared exception!
      try { 
        composition0.compress0((int[]) null, intWrapper0, (-3032), (int[]) null, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-24256 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      Composition composition0 = new Composition(fastPFOR0, fastPFOR0);
      int[] intArray0 = new int[24];
      IntWrapper intWrapper0 = new IntWrapper(256);
      // Undeclared exception!
      try { 
        composition0.compress0(intArray0, intWrapper0, 44, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 256 out of bounds for length 24
         //
         verifyException("me.lemire.integercompression.Composition", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      Composition composition0 = new Composition(fastPFOR0, fastPFOR0);
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(256);
      composition0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertArrayEquals(new int[] {0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      FastPFOR fastPFOR0 = FastPFOR.FastPFOR1();
      Composition composition0 = new Composition(fastPFOR0, fastPFOR0);
      int[] intArray0 = new int[33];
      IntWrapper intWrapper0 = new IntWrapper(256);
      composition0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(33, intArray0.length);
  }
}
