
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
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class LongJustCopy_ESTest extends LongJustCopy_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[5];
      IntWrapper intWrapper0 = new IntWrapper(1);
      IntWrapper intWrapper1 = new IntWrapper((-333));
      // Undeclared exception!
      try { 
        longJustCopy0.compress0(longArray0, intWrapper0, 0, longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[5];
      IntWrapper intWrapper1 = new IntWrapper(0);
      longJustCopy0.headlessUncompress(longArray0, intWrapper0, (-1821), longArray0, intWrapper1, 0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(0.0, intWrapper1.doubleValue(), 0.01);
      assertEquals(0L, intWrapper1.longValue());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[0];
      long[] longArray1 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(2175);
      IntWrapper intWrapper1 = new IntWrapper((-5957));
      // Undeclared exception!
      try { 
        longJustCopy0.uncompress1(longArray1, intWrapper0, 2175, longArray0, intWrapper1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      IntWrapper intWrapper0 = new IntWrapper(0);
      long[] longArray0 = new long[5];
      IntWrapper intWrapper1 = new IntWrapper(0);
      longJustCopy0.headlessCompress(longArray0, intWrapper1, 0, longArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[9];
      IntWrapper intWrapper0 = new IntWrapper((-1186));
      long[] longArray1 = new long[9];
      // Undeclared exception!
      try { 
        longJustCopy0.compress0(longArray0, intWrapper0, (-657), longArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[7];
      IntWrapper intWrapper0 = new IntWrapper(0);
      longJustCopy0.uncompress1(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
      assertEquals("0", intWrapper0.toString());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(0);
      longJustCopy0.compress0(longArray0, intWrapper0, 0, longArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[2];
      IntWrapper intWrapper0 = new IntWrapper(453);
      // Undeclared exception!
      try { 
        longJustCopy0.headlessUncompress(longArray0, intWrapper0, 453, longArray0, intWrapper0, 453);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[0];
      IntWrapper intWrapper0 = new IntWrapper((-1512));
      // Undeclared exception!
      try { 
        longJustCopy0.headlessCompress(longArray0, intWrapper0, (-1512), longArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        longJustCopy0.compress0((long[]) null, intWrapper0, 0, (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      IntWrapper intWrapper0 = new IntWrapper((-2298));
      // Undeclared exception!
      try { 
        longJustCopy0.headlessUncompress((long[]) null, intWrapper0, (-2298), (long[]) null, intWrapper0, (-2298));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      long[] longArray0 = new long[0];
      // Undeclared exception!
      try { 
        longJustCopy0.uncompress1(longArray0, (IntWrapper) null, 0, longArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.longcompression.LongJustCopy", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      String string0 = longJustCopy0.toString();
      assertEquals("LongJustCopy", string0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      LongJustCopy longJustCopy0 = new LongJustCopy();
      IntWrapper intWrapper0 = new IntWrapper((-4));
      // Undeclared exception!
      try { 
        longJustCopy0.headlessCompress((long[]) null, intWrapper0, (-4), (long[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }
}
