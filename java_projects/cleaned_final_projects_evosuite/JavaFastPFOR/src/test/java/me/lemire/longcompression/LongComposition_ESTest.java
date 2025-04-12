
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
import me.lemire.integercompression.FastPFOR;
import me.lemire.integercompression.IntWrapper;
import me.lemire.integercompression.OptPFDS16;
import me.lemire.longcompression.LongAs2IntsCodec;
import me.lemire.longcompression.LongCODEC;
import me.lemire.longcompression.LongComposition;
import me.lemire.longcompression.LongVariableByte;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongComposition_ESTest extends LongComposition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
      LongComposition longComposition1 = new LongComposition(longVariableByte0, longVariableByte0);
      longComposition1.F2 = (LongCODEC) longComposition0;
      String string0 = longComposition1.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      longComposition0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      longComposition0.uncompress1(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      assertEquals("2", intWrapper0.toString());
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      long[] longArray1 = new long[7];
      longComposition0.uncompress1(longArray0, intWrapper0, 1, longArray1, intWrapper0);
      assertEquals(1L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      LongComposition longComposition1 = new LongComposition(longComposition0, longAs2IntsCodec0);
      longComposition1.uncompress1(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      longComposition0.uncompress1(longArray0, intWrapper0, 1, longArray0, intWrapper1);
      assertEquals((byte)2, intWrapper0.byteValue());
      assertEquals(2.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      long[] longArray0 = new long[23];
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(1);
      long[] longArray1 = new long[3];
      longComposition0.compress0(longArray1, intWrapper0, Integer.MIN_VALUE, longArray0, intWrapper1);
      assertEquals((-2.14748365E9F), intWrapper0.floatValue(), 0.01F);
      assertEquals(Integer.MIN_VALUE, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      long[] longArray0 = new long[23];
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      long[] longArray1 = new long[3];
      longComposition0.compress0(longArray1, intWrapper0, Integer.MIN_VALUE, longArray0, intWrapper0);
      assertEquals((-2.14748365E9F), intWrapper0.floatValue(), 0.01F);
      assertEquals((short)0, intWrapper0.shortValue());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      LongComposition longComposition1 = new LongComposition(longComposition0, longAs2IntsCodec0);
      longComposition1.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
      assertEquals(2.0F, intWrapper0.floatValue(), 0.01F);
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      IntWrapper intWrapper0 = new IntWrapper(68);
      // Undeclared exception!
      try { 
        longComposition0.uncompress1((long[]) null, intWrapper0, 68, (long[]) null, intWrapper0);
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
      long[] longArray0 = new long[3];
      IntWrapper intWrapper0 = new IntWrapper(1);
      FastPFOR fastPFOR0 = new FastPFOR(1);
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(fastPFOR0, fastPFOR0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      // Undeclared exception!
      try { 
        longComposition0.uncompress1(longArray0, intWrapper0, (-76), longArray0, intWrapper0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1216
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LongComposition longComposition0 = new LongComposition((LongCODEC) null, (LongCODEC) null);
      // Undeclared exception!
      try { 
        longComposition0.toString();
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
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      IntWrapper intWrapper0 = new IntWrapper(35);
      // Undeclared exception!
      try { 
        longComposition0.compress0((long[]) null, intWrapper0, 35, (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longComposition0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -2
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      long[] longArray0 = new long[23];
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
      IntWrapper intWrapper1 = new IntWrapper(1);
      longComposition0.compress0(longArray0, intWrapper1, Integer.MIN_VALUE, longArray0, intWrapper1);
      // Undeclared exception!
      try { 
        longComposition0.compress0(longArray0, intWrapper0, Integer.MIN_VALUE, longArray0, intWrapper1);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      long[] longArray0 = new long[2];
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        longComposition0.compress0(longArray0, intWrapper0, 1, longArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-16 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      OptPFDS16 optPFDS16_0 = new OptPFDS16();
      LongAs2IntsCodec longAs2IntsCodec0 = new LongAs2IntsCodec(optPFDS16_0, optPFDS16_0);
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      IntWrapper intWrapper1 = new IntWrapper((-2));
      // Undeclared exception!
      try { 
        longComposition0.compress0(longArray0, intWrapper1, 1, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 8
         //
         verifyException("me.lemire.longcompression.LongAs2IntsCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      longComposition0.uncompress1(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals(1.0, intWrapper0.doubleValue(), 0.01);
  }

  // @Test(timeout = 4000)
  // public void test17()  throws Throwable  {
  //     long[] longArray0 = new long[23];
  //     LongVariableByte longVariableByte0 = new LongVariableByte();
  //     LongComposition longComposition0 = new LongComposition(longVariableByte0, longVariableByte0);
  //     IntWrapper intWrapper0 = IntWrapper.IntWrapper1();
  //     // Undeclared exception!
  //     try { 
  //       longComposition0.uncompress1(longArray0, intWrapper0, 447, longArray0, intWrapper0);
  //       fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
  //     } catch(ArrayIndexOutOfBoundsException e) {
  //        //
  //        // Index 23 out of bounds for length 23
  //        //
  //        verifyException("me.lemire.longcompression.LongVariableByte", e);
  //     }
  // }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      long[] longArray0 = new long[8];
      IntWrapper intWrapper0 = new IntWrapper(1);
      LongAs2IntsCodec longAs2IntsCodec0 = LongAs2IntsCodec.LongAs2IntsCodec1();
      LongComposition longComposition0 = new LongComposition(longAs2IntsCodec0, longAs2IntsCodec0);
      longComposition0.compress0(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals("1", intWrapper0.toString());
  }
}
