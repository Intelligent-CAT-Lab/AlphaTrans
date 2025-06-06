
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
import me.lemire.longcompression.LongJustCopy;
import me.lemire.longcompression.LongVariableByte;
import me.lemire.longcompression.SkippableLongCODEC;
import me.lemire.longcompression.SkippableLongComposition;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class SkippableLongComposition_ESTest extends SkippableLongComposition_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      LongJustCopy longJustCopy0 = new LongJustCopy();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longJustCopy0);
      String string0 = skippableLongComposition0.toString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = new IntWrapper(49);
      long[] longArray1 = new long[1];
      skippableLongComposition0.headlessUncompress(longArray1, intWrapper0, (-1), longArray0, intWrapper0, (-1));
      assertEquals((short)50, intWrapper0.shortValue());
      assertEquals(50L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[15];
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray1 = new long[6];
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessUncompress(longArray0, intWrapper0, 2, longArray1, intWrapper0, 42);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 15
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      long[] longArray0 = new long[5];
      IntWrapper intWrapper0 = new IntWrapper((-899));
      IntWrapper intWrapper1 = new IntWrapper((-1435));
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessUncompress(longArray0, intWrapper0, (-899), longArray0, intWrapper1, (-899));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -898 out of bounds for length 5
         //
         verifyException("me.lemire.longcompression.LongVariableByte", e);
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[15];
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray1 = new long[6];
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress(longArray0, intWrapper0, 0, longArray1, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-16 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longJustCopy0, longVariableByte0);
      long[] longArray0 = new long[4];
      IntWrapper intWrapper0 = new IntWrapper(1);
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress(longArray0, intWrapper0, 1, longArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-16 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition((SkippableLongCODEC) null, (SkippableLongCODEC) null);
      // Undeclared exception!
      try { 
        skippableLongComposition0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.System", e);
      }
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      IntWrapper intWrapper0 = new IntWrapper((-2611));
      LongJustCopy longJustCopy0 = new LongJustCopy();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longJustCopy0);
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessUncompress((long[]) null, intWrapper0, 2, (long[]) null, intWrapper0, (-2611));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[1];
      IntWrapper intWrapper0 = new IntWrapper((-50));
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress(longArray0, intWrapper0, 0, (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.SkippableLongComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      long[] longArray0 = new long[6];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper((-1263));
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress(longArray0, intWrapper0, 3, longArray0, intWrapper1);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = new IntWrapper(49);
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress((long[]) null, intWrapper0, 0, longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 49 out of bounds for length 7
         //
         verifyException("me.lemire.longcompression.SkippableLongComposition", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[15];
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      skippableLongComposition0.headlessUncompress(longArray0, intWrapper0, 0, longArray0, intWrapper0, (-3026));
      // Undeclared exception!
      try { 
        skippableLongComposition0.headlessCompress(longArray0, intWrapper0, 0, longArray0, intWrapper0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // capacity < 0: (-16 < 0)
         //
         verifyException("java.nio.Buffer", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      long[] longArray0 = new long[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      SkippableLongComposition skippableLongComposition1 = new SkippableLongComposition(skippableLongComposition0, skippableLongComposition0);
      skippableLongComposition1.headlessUncompress(longArray0, intWrapper0, 0, longArray0, intWrapper0, 0);
      assertEquals((byte)2, intWrapper0.byteValue());
      assertEquals(2L, intWrapper0.longValue());
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LongVariableByte longVariableByte0 = new LongVariableByte();
      long[] longArray0 = new long[15];
      SkippableLongComposition skippableLongComposition0 = new SkippableLongComposition(longVariableByte0, longVariableByte0);
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(2);
      SkippableLongComposition skippableLongComposition1 = new SkippableLongComposition(skippableLongComposition0, skippableLongComposition0);
      skippableLongComposition1.headlessCompress(longArray0, intWrapper0, 0, longArray0, intWrapper1);
      assertEquals(4.0, intWrapper1.doubleValue(), 0.01);
      assertEquals(4.0F, intWrapper1.floatValue(), 0.01F);
  }
}
