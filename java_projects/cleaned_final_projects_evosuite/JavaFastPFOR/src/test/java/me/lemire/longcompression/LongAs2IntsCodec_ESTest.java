
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


package me.lemire.longcompression;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.OptPFDS16;
import me.lemire.longcompression.LongAs2IntsCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongAs2IntsCodec_ESTest extends LongAs2IntsCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[14];
      IntWrapper intWrapper0 = new IntWrapper(1);
      longAs2IntsCodec0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(1);
      intWrapper1.increment();
      intWrapper1.increment();
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.uncompress1(longArray0, intWrapper1, (-3890), longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 14 out of bounds for length 14
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[14];
      IntWrapper intWrapper0 = new IntWrapper(1);
      longAs2IntsCodec0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(1);
      intWrapper1.increment();
      long[] longArray1 = new long[2];
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.uncompress1(longArray0, intWrapper1, (-3890), longArray1, intWrapper1);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -62240
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[10];
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray1 = new long[9];
      longAs2IntsCodec0.uncompress1(longArray0, intWrapper0, 67, longArray1, intWrapper0);
      assertEquals(1, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[14];
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray1 = new long[7];
      longArray1[1] = (-1560L);
      longAs2IntsCodec0.compress0(longArray1, intWrapper0, 5, longArray0, intWrapper0);
      assertEquals((byte)6, intWrapper0.byteValue());
      assertEquals(6.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[14];
      IntWrapper intWrapper0 = new IntWrapper(1);
      long[] longArray1 = new long[7];
      longAs2IntsCodec0.compress0(longArray1, intWrapper0, 5, longArray0, intWrapper0);
      assertEquals("5", intWrapper0.toString());
      assertEquals(5L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[4];
      IntWrapper intWrapper0 = new IntWrapper(2);
      IntWrapper intWrapper1 = new IntWrapper((-869));
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.compress0(longArray0, intWrapper0, 2, longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -869 out of bounds for length 4
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.uncompress1((long[]) null, (IntWrapper) null, 639, (long[]) null, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[10];
      IntWrapper intWrapper0 = new IntWrapper(1);
      longAs2IntsCodec0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      IntWrapper intWrapper1 = new IntWrapper(1);
      IntWrapper intWrapper2 = new IntWrapper(64);
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.uncompress1(longArray0, intWrapper1, 67, longArray0, intWrapper2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 64 out of bounds for length 10
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      IntWrapper intWrapper0 = new IntWrapper(2);
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.compress0((long[]) null, intWrapper0, 2, (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[0];
      // Undeclared exception!
      try { 
        longAs2IntsCodec0.compress0(longArray0, (IntWrapper) null, Integer.MIN_VALUE, longArray0, (IntWrapper) null);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2147483648
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[5];
      IntWrapper intWrapper0 = new IntWrapper(0);
      longAs2IntsCodec0.uncompress1(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertArrayEquals(new long[] {0L, 0L, 0L, 0L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      long[] longArray0 = new long[4];
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      IntWrapper intWrapper0 = new IntWrapper(2);
      longAs2IntsCodec0.compress0(longArray0, intWrapper0, 2, longArray0, intWrapper0);
      assertEquals((short)3, intWrapper0.shortValue());
      assertArrayEquals(new long[] {0L, 0L, 0L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      long[] longArray0 = new long[6];
      IntWrapper intWrapper0 = new IntWrapper(0);
      longAs2IntsCodec0.compress0(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertArrayEquals(new long[] {0L, 0L, 0L, 0L, 0L, 0L}, longArray0);
      assertEquals("0", intWrapper0.toString());
  }
}
