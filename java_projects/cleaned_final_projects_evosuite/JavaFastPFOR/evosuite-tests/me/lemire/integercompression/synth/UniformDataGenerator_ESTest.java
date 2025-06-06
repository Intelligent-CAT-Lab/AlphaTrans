
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


package me.lemire.integercompression.synth;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.synth.UniformDataGenerator;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.util.MockRandom;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class UniformDataGenerator_ESTest extends UniformDataGenerator_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      MockRandom mockRandom0 = new MockRandom(1);
      mockRandom0.nextLong();
      int[] intArray0 = uniformDataGenerator0.generateUniform(1, 135);
      assertArrayEquals(new int[] {1}, intArray0);
      assertEquals(1, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = 1394;
      int[] intArray1 = UniformDataGenerator.negate(intArray0, 2142);
      assertEquals(2133, intArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(234, 234);
      // Undeclared exception!
      uniformDataGenerator0.generateUniformHash(2, 1850);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(0, 2);
      int[] intArray0 = uniformDataGenerator0.generateUniformHash(0, 0);
      assertEquals(0, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      int[] intArray0 = uniformDataGenerator0.generateUniformBitmap(1, 1);
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(0, 0);
      int[] intArray0 = uniformDataGenerator0.generateUniformBitmap(0, 0);
      assertEquals(0, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[1];
      UniformDataGenerator.negate(intArray0, 5329);
      // Undeclared exception!
      UniformDataGenerator.negate(intArray0, 5329);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      // Undeclared exception!
      try { 
        UniformDataGenerator.negate((int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        UniformDataGenerator.negate(intArray0, 0);
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -9
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      int[] intArray0 = new int[1];
      intArray0[0] = 344;
      // Undeclared exception!
      try { 
        UniformDataGenerator.negate(intArray0, 344);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 343 out of bounds for length 343
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      uniformDataGenerator0.rand = null;
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformHash(1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator((-8), (-8));
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformHash((-8), (-8));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -8
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(0, 0);
      // Undeclared exception!
      uniformDataGenerator0.generateUniformBitmap(158, 1456);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      uniformDataGenerator0.rand = null;
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformBitmap(1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator((-1967), (-1967));
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformBitmap((-1967), (-1967));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1967
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator((-4), (-4));
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniform((-4), (-9));
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // not possible
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator((-1410), (-1410));
      uniformDataGenerator0.rand = null;
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniform(980, 6571);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator((-1773), (-1773));
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniform((-1773), (-1773));
        fail("Expecting exception: NegativeArraySizeException");
      
      } catch(NegativeArraySizeException e) {
         //
         // -1773
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(0, 0);
      int[] intArray0 = uniformDataGenerator0.generateUniform(0, 0);
      int[] intArray1 = UniformDataGenerator.negate(intArray0, 0);
      assertEquals(0, intArray1.length);
      assertNotSame(intArray1, intArray0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(167, 167);
      // Undeclared exception!
      uniformDataGenerator0.generateUniform(167, 1813);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformBitmap(1644, 481);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // not possible
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      int[] intArray0 = uniformDataGenerator0.generateUniform(1, 1);
      assertArrayEquals(new int[] {0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      int[] intArray0 = uniformDataGenerator0.generateUniform(1644, 1645);
      assertEquals(1644, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(0, 0);
      // Undeclared exception!
      try { 
        uniformDataGenerator0.generateUniformHash(2615, 0);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // not possible
         //
         verifyException("me.lemire.integercompression.synth.UniformDataGenerator", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      UniformDataGenerator uniformDataGenerator0 = new UniformDataGenerator(1, 1);
      int[] intArray0 = uniformDataGenerator0.generateUniformHash(1, 1);
      assertEquals(1, intArray0.length);
  }
}
