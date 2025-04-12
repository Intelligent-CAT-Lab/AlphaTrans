
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
import me.lemire.integercompression.JustCopy;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class JustCopy_ESTest extends JustCopy_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      IntWrapper intWrapper0 = new IntWrapper(316);
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        justCopy0.compress0(intArray0, intWrapper0, 316, (int[]) null, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(0);
      justCopy0.headlessUncompress(intArray0, intWrapper0, (-6336), intArray0, intWrapper0, 0);
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
      assertEquals(0.0F, intWrapper0.floatValue(), 0.01F);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = new IntWrapper(0);
      justCopy0.headlessUncompress(intArray0, intWrapper1, 0, intArray0, intWrapper0, 0);
      assertEquals(0L, intWrapper0.longValue());
      assertEquals(0, intWrapper0.get());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[9];
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        justCopy0.headlessUncompress(intArray0, intWrapper0, 0, intArray0, intWrapper0, (-1510));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[8];
      IntWrapper intWrapper0 = new IntWrapper(1081);
      // Undeclared exception!
      try { 
        justCopy0.uncompress0(intArray0, intWrapper0, (-11), intArray0, (IntWrapper) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.JustCopy", e);
      }
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[3];
      IntWrapper intWrapper0 = new IntWrapper(5137);
      int[] intArray1 = new int[10];
      // Undeclared exception!
      try { 
        justCopy0.uncompress0(intArray0, intWrapper0, 0, intArray1, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      IntWrapper intWrapper1 = IntWrapper.IntWrapper1();
      justCopy0.compress0(intArray0, intWrapper1, 0, intArray0, intWrapper0);
      assertEquals(0L, intWrapper0.longValue());
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      IntWrapper intWrapper0 = new IntWrapper((-1));
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        justCopy0.headlessCompress((int[]) null, intWrapper0, (-1), intArray0, intWrapper0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      justCopy0.uncompress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0, intWrapper0.intValue());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      IntWrapper intWrapper0 = new IntWrapper(0);
      // Undeclared exception!
      try { 
        justCopy0.headlessUncompress((int[]) null, intWrapper0, 0, (int[]) null, intWrapper0, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[0];
      IntWrapper intWrapper0 = new IntWrapper(735);
      // Undeclared exception!
      try { 
        justCopy0.headlessCompress(intArray0, intWrapper0, 735, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper((-3356));
      // Undeclared exception!
      try { 
        justCopy0.compress0(intArray0, intWrapper0, 0, intArray0, intWrapper0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      int[] intArray0 = new int[1];
      IntWrapper intWrapper0 = new IntWrapper(0);
      justCopy0.headlessCompress(intArray0, intWrapper0, 0, intArray0, intWrapper0);
      assertEquals((short)0, intWrapper0.shortValue());
      assertEquals(0.0, intWrapper0.doubleValue(), 0.01);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      JustCopy justCopy0 = new JustCopy();
      String string0 = justCopy0.toString();
      assertEquals("JustCopy", string0);
  }
}
