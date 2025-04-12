
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
import me.lemire.integercompression.OptPFDS16;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class OptPFDS16_ESTest extends OptPFDS16_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[7];
      intArray0[0] = (-15);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.headlessUncompress(intArray0, intWrapper0, 447, intArray0, intWrapper0, 922);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.S16", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[2];
      IntWrapper intWrapper0 = new IntWrapper((-917));
      optPFDS16_0.headlessUncompress(intArray0, intWrapper0, 30, intArray0, intWrapper0, (-917));
      assertEquals((-917), intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      int[] intArray0 = new int[130];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      optPFDS16_0.compress0(intArray0, intWrapper0, 128, intArray0, intWrapper0);
      assertEquals((byte)2, intWrapper0.byteValue());
      assertEquals("2", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(0);
      optPFDS16_0.uncompress0(intArray0, intWrapper0, (-473), intArray0, intWrapper0);
      assertEquals("1", intWrapper0.toString());
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        optPFDS16_0.uncompress0(intArray0, intWrapper0, 14, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.OptPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.headlessUncompress((int[]) null, intWrapper0, 2618, (int[]) null, intWrapper0, 2618);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.headlessCompress(intArray0, intWrapper0, 701, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.compress0((int[]) null, intWrapper0, 1512, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.headlessCompress((int[]) null, intWrapper0, 384, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[6];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      optPFDS16_0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = new IntWrapper(457);
      // Undeclared exception!
      try { 
        optPFDS16_0.uncompress0((int[]) null, intWrapper0, 457, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.OptPFDS16", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      int[] intArray0 = new int[5];
      optPFDS16_0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[128];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      // Undeclared exception!
      try { 
        optPFDS16_0.headlessUncompress(intArray0, intWrapper0, 1319, intArray0, intWrapper0, 1319);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 160
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[5];
      optPFDS16_0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, 0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      int[] intArray0 = new int[133];
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      optPFDS16_0.compress0(intArray0, intWrapper0, (-5625), intArray0, intWrapper0);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      // Undeclared exception!
      try { 
        optPFDS16_0.compress0(intArray0, intWrapper1, 33554431, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 133 out of bounds for length 133
         //
         verifyException("me.lemire.integercompression.Util", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      int[] intArray0 = new int[5];
      optPFDS16_0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      String string0 = optPFDS16_0.toString();
      assertEquals("OptPFDS16", string0);
  }
}
