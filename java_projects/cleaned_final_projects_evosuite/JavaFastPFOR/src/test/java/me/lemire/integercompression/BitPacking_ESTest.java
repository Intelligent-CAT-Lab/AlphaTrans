
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
import me.lemire.integercompression.BitPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class BitPacking_ESTest extends BitPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[1] = (-3428);
      // Undeclared exception!
      try { 
        BitPacking.fastunpack9(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[0] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack8(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[9];
      intArray1[2] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack7(intArray1, 1, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[9];
      intArray1[1] = 2;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack7(intArray1, 1, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[7] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack30(intArray0, 5, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[6] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack30(intArray0, 5, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[4] = 4062;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = (-656);
      // Undeclared exception!
      try { 
        BitPacking.fastunpack29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 4062;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = 2;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack28(intArray0, 1, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[1] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack25(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack25(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = (-387);
      // Undeclared exception!
      try { 
        BitPacking.fastunpack24(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = 28;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack23(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = (-3104);
      // Undeclared exception!
      try { 
        BitPacking.fastunpack23(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 1950;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[0] = 1862;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[2];
      intArray1[1] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack2(intArray1, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[3] = (-1363);
      // Undeclared exception!
      try { 
        BitPacking.fastunpack14(intArray0, 3, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 0, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[3] = (-6);
      intArray0[4] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask9(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[2] = (-6);
      intArray0[3] = (-6);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask9(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = 1441;
      intArray0[2] = (-6);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask9(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[4] = 302;
      intArray0[5] = 302;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask7(intArray0, 1, intArray0, 2792);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2792 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask7(intArray0, 1, intArray0, 2792);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2792 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = 2792;
      intArray0[2] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask7(intArray0, 1, intArray0, 2792);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2792 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[6] = (-415);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6(intArray0, 1, intArray0, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = 1346;
      intArray0[5] = (-3170);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6(intArray0, 1, intArray0, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[3] = 1774;
      intArray0[4] = 1346;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6(intArray0, 1, intArray0, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[0] = (-656);
      intArray0[1] = 4062;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[6] = (-1);
      intArray0[7] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask5(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 3899;
      intArray0[5] = 2177;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask5(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 2420;
      intArray0[4] = 15;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask5(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[3] = 21;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask5(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 3899;
      intArray0[1] = 15;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask5(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[5] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask31(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask31(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = 994;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask31(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 994;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask31(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[1] = 2;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask30(intArray0, 0, intArray0, (-2393));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2393 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = (-1912);
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask29(intArray0, 0, intArray0, (-1782));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1782 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 28;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask26(intArray0, 2097152, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2097152 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = (-980);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 0, (int[]) null, 0, 26);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[1] = 13;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask24(intArray0, 0, intArray0, (-978));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -978 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = 63;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask22(intArray0, 0, intArray0, 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[5] = 17;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask21(intArray0, 5, intArray0, 5919);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5919 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = (-1);
      intArray0[2] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 0, intArray0, 9, 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      int[] intArray0 = new int[6];
      int[] intArray1 = new int[6];
      intArray1[2] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask15(intArray1, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = 31;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask11(intArray0, 0, intArray0, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 31 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[0] = (-3158);
      intArray0[2] = (-1279);
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask10(intArray0, 0, intArray0, 759);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = 1493;
      intArray0[1] = 63;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask10(intArray0, 0, intArray0, 2251);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      int[] intArray0 = new int[13];
      intArray0[10] = 255;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask1(intArray0, 0, intArray0, 372);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      int[] intArray0 = new int[13];
      intArray0[0] = 255;
      intArray0[1] = 2;
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask1(intArray0, 0, intArray0, 372);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[0] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack8(intArray0, 0, intArray0, 2072);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2072 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[1] = 2092;
      // Undeclared exception!
      try { 
        BitPacking.fastpack8(intArray0, 0, intArray0, 2092);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack7(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[2] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack7(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[5] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 0, intArray0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[4] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 0, intArray0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 0, intArray0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[3] = (-379);
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 0, intArray0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[2] = 1441;
      // Undeclared exception!
      try { 
        BitPacking.fastpack30(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = (-6);
      // Undeclared exception!
      try { 
        BitPacking.fastpack30(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpack3(intArray0, 1, intArray0, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = (-6743);
      // Undeclared exception!
      try { 
        BitPacking.fastpack29(intArray0, 0, intArray0, 135659520);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 135659520 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 28;
      // Undeclared exception!
      try { 
        BitPacking.fastpack28(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = (-391);
      // Undeclared exception!
      try { 
        BitPacking.fastpack27(intArray0, 0, intArray0, 40);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 40 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[2] = (-1364);
      // Undeclared exception!
      try { 
        BitPacking.fastpack26(intArray0, 1, intArray0, (-1531));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1531 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[2] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack25(intArray0, 1, intArray0, (-755));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -755 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[5] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[4] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[2] = 1;
      // Undeclared exception!
      try { 
        BitPacking.fastpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      int[] intArray0 = new int[3];
      intArray0[1] = 1084;
      // Undeclared exception!
      try { 
        BitPacking.fastpack20(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[7] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack2(intArray0, 1, intArray0, (-1750));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[5] = 1035;
      // Undeclared exception!
      try { 
        BitPacking.fastpack2(intArray0, 0, intArray0, 255);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[3] = (-45);
      // Undeclared exception!
      try { 
        BitPacking.fastpack2(intArray0, 0, intArray0, 255);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = (-6743);
      // Undeclared exception!
      try { 
        BitPacking.fastpack2(intArray0, 0, intArray0, 255);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[8] = 25;
      // Undeclared exception!
      try { 
        BitPacking.fastpack19(intArray0, 7, intArray0, (-2015));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2015 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[8];
      intArray1[2] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastpack15(intArray1, 0, intArray0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[8];
      intArray1[1] = 5;
      // Undeclared exception!
      try { 
        BitPacking.fastpack15(intArray1, 0, intArray0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[2] = (-1077);
      // Undeclared exception!
      try { 
        BitPacking.fastpack14(intArray0, 0, intArray0, (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[1] = (-6743);
      // Undeclared exception!
      try { 
        BitPacking.fastpack14(intArray0, 0, intArray0, (-3722));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3722 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[3] = 32;
      // Undeclared exception!
      try { 
        BitPacking.fastpack13(intArray0, 1, intArray0, (-2018));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2018 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[2] = (-3832);
      // Undeclared exception!
      try { 
        BitPacking.fastpack13(intArray0, 1, intArray0, (-2018));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2018 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      int[] intArray0 = new int[9];
      int[] intArray1 = new int[8];
      intArray1[7] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray1, 1, intArray0, 16777215);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      int[] intArray0 = new int[9];
      int[] intArray1 = new int[8];
      intArray1[6] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray1, 1, intArray0, 16777215);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      int[] intArray0 = new int[9];
      int[] intArray1 = new int[8];
      intArray1[5] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray1, 1, intArray0, 16777215);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[4] = (-1);
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray0, 1, intArray0, 86);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = (-1117);
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray0, 1, intArray0, 86);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = 7;
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      int[] intArray0 = new int[6];
      BitPacking.fastpackwithoutmask0(intArray0, (-45), intArray0, (-483));
      assertArrayEquals(new int[] {0, 0, 0, 0, 0, 0}, intArray0);
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      int[] intArray0 = new int[12];
      BitPacking.fastpack0(intArray0, 0, intArray0, 2158);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack9(intArray0, 2, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack6(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 5, intArray1, 5, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack30(intArray0, 0, intArray0, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack3(intArray0, 5, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack25(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack24(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack21(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack20(intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack2(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack18(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      int[] intArray0 = new int[8];
      int[] intArray1 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack16(intArray0, 0, intArray1, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      int[] intArray0 = new int[21];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack15(intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 21 out of bounds for length 21
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack14(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack13(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack10(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      int[] intArray0 = new int[19];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask7(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 19 out of bounds for length 19
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask27(intArray0, 0, intArray0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask26(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask22(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask21(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask16(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask12(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpack5(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      int[] intArray0 = new int[8];
      int[] intArray1 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpack26(intArray1, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack24(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpack23(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        BitPacking.fastpack17(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack9((int[]) null, 23, (int[]) null, 4);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack7((int[]) null, (-893), (int[]) null, (-893));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack7(intArray0, 2, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack5(intArray0, (-218), intArray0, (-218));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -218 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack4(intArray0, 2, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack32((int[]) null, 1373, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack32(intArray0, 31, intArray0, 32);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack31(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack30((int[]) null, (-2504), (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack3((int[]) null, 26, (int[]) null, 26);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack28((int[]) null, (-1), (int[]) null, 560);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack26(intArray0, 0, intArray0, (-307));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -307 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack25((int[]) null, (-1135), (int[]) null, 29);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack24((int[]) null, 2438, (int[]) null, (-76));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack21((int[]) null, 2775, (int[]) null, 4095);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack19(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack17(intArray0, (-330), intArray0, (-330));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -330 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack15((int[]) null, 21, (int[]) null, 27);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test143()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack13((int[]) null, 1, (int[]) null, (-330));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test144()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack12((int[]) null, 1, intArray0, 24);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test145()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack11(intArray0, 2158, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2158 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test146()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack1(intArray0, (-22), intArray0, (-22));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -22 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test147()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack0(intArray0, (-651), intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 33
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test148()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask6((int[]) null, 16338, (int[]) null, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test149()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask32(intArray0, 14, intArray0, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test150()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask29((int[]) null, (-590), (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test151()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask28(intArray0, 79, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 79 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test152()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask27((int[]) null, 25, intArray0, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test153()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask24((int[]) null, (-1909), (int[]) null, 25);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test154()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask23(intArray0, 1628, intArray0, 29);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1628 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test155()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask2(intArray0, 485, intArray0, 932);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 485 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test156()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask19(intArray0, 12, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test157()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask18((int[]) null, 1, (int[]) null, 1037);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test158()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask18(intArray0, 2092, intArray0, 2092);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2092 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test159()  throws Throwable  {
      int[] intArray0 = new int[22];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask16((int[]) null, (-3733), intArray0, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test160()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask15(intArray0, 2, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test161()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask13(intArray0, 44, intArray0, 44);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 44 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test162()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask12((int[]) null, (-1), (int[]) null, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test163()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask11((int[]) null, 30, intArray0, 30);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test164()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask1((int[]) null, 2423, (int[]) null, 2423);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test165()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        BitPacking.fastpack7((int[]) null, (-1), intArray0, 28);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test166()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack5((int[]) null, 27, (int[]) null, 25);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test167()  throws Throwable  {
      int[] intArray0 = new int[22];
      // Undeclared exception!
      try { 
        BitPacking.fastpack32(intArray0, 1, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test168()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpack25((int[]) null, 3, intArray0, 1302);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test169()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack24((int[]) null, (-410), (int[]) null, 1003);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test170()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpack22(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test171()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack21((int[]) null, 1, (int[]) null, (-3487));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test172()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack19((int[]) null, (-1180), (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test173()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack18((int[]) null, 2745, (int[]) null, 16383);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test174()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack14((int[]) null, 0, (int[]) null, (-1575));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test175()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpack13(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test176()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack11((int[]) null, (-1602), (int[]) null, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test177()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack1((int[]) null, 32767, (int[]) null, 20);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test178()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 18, intArray0, 0, 18);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test179()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, (-3370), intArray0, (-3370), (-3370));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test180()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 31, intArray0, 31, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 31 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test181()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 24, intArray0, 879, 27);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 24 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test182()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 4028, intArray0, 18, 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4028 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test183()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 4028, intArray0, (-173), 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4028 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test184()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 11, intArray0, (-755), 11);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -755 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test185()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-2484), intArray0, (-2484), (-2484));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test186()  throws Throwable  {
      int[] intArray0 = new int[12];
      BitPacking.fastpackwithoutmask(intArray0, 1, intArray0, 0, 0);
      assertEquals(12, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test187()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpack(intArray0, 0, intArray0, 1639, 1639);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test188()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 22, intArray0, 22, 21);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test189()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-530), intArray0, 0, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -530 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test190()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask14(intArray0, 524287, intArray0, 1700);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 524287 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test191()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask20(intArray0, 12, intArray0, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test192()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 1, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test193()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask2((int[]) null, (-17), (int[]) null, (-901));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test194()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        BitPacking.fastpack31(intArray0, 2183, intArray0, (-3392));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2183 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test195()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, (-652), intArray0, (-172), 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -652 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test196()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack10((int[]) null, 0, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test197()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-980), intArray0, 31, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -980 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test198()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack28(intArray0, intArray0[5], intArray0, intArray0[5]);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test199()  throws Throwable  {
      int[] intArray0 = new int[14];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 22, intArray0, 21, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 14
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test200()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack20((int[]) null, 26, (int[]) null, (-813));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test201()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack14(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test202()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack4(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test203()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        BitPacking.fastpack19(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test204()  throws Throwable  {
      BitPacking.fastpack((int[]) null, (-1630), (int[]) null, (-2504), 0);
  }

  @Test(timeout = 4000)
  public void test205()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask25(intArray0, 67108863, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 67108863 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test206()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 0, intArray0, 4194303, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4194303 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test207()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 19, intArray0, 21, 19);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 19 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test208()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 29, intArray0, 29, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 29 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test209()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask4(intArray0, 4123, intArray0, 548);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4123 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test210()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 3, (int[]) null, 3, 30);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test211()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-935), intArray0, 34, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -935 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test212()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack12(intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test213()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask9(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test214()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask17(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test215()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 18, intArray0, 18, 18);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test216()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack7(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test217()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 4164, intArray0, (-2347), 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4164 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test218()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack22((int[]) null, 1, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test219()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack8((int[]) null, (-654), (int[]) null, (-2108));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test220()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        BitPacking.fastpack2(intArray0, 0, intArray0, (-8));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test221()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack11((int[]) null, 1, intArray0, (-978));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test222()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask3(intArray0, (-2052), intArray0, 21);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2052 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test223()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack1(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test224()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 27, intArray0, 44, 27);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 27 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test225()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 17, intArray0, 3, 17);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test226()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack12(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test227()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 2573, intArray0, 17, 8);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2573 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test228()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 0, intArray0, (-5052), 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -5052 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test229()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 28, intArray0, 16, 20);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 28 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test230()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 4164, intArray0, (-2347), 26);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4164 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test231()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        BitPacking.fastpack21(intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test232()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        BitPacking.fastpack18(intArray0, 0, intArray0, 30);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 30 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test233()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 1, intArray0, 0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 32
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test234()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 1, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test235()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack27(intArray0, 0, intArray0, 2991);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2991 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test236()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack29((int[]) null, 1, (int[]) null, 4123);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test237()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack13((int[]) null, (-1796), (int[]) null, (-5497));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test238()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack22(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test239()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 32, intArray0, 6, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 32 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test240()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask8(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test241()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 32, intArray0, 10, 32);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test242()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack9(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test243()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, (-755), intArray0, (-1177), 19);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -755 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test244()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack11(intArray0, 0, intArray0, 406);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 406 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test245()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpack32(intArray0, (-1), intArray0, (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test246()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 16, intArray0, 25, 25);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test247()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpack26((int[]) null, (-893), (int[]) null, 33554431);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test248()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 24, intArray0, 879, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 24 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test249()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpack16(intArray0, (-124), intArray0, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -124 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test250()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 7, intArray0, 7, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test251()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask28((int[]) null, 0, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test252()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-989), intArray0, (-989), 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -989 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test253()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        BitPacking.fastpack6(intArray0, 3, intArray0, (-1360));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test254()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, 7, intArray0, 7, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test255()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 63, intArray0, (-4308), 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 63 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test256()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask29(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test257()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-980), intArray0, 24, 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -980 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test258()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        BitPacking.fastpack10(intArray0, (-1092), intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1092 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test259()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, (-749), intArray0, 27, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -749 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test260()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-530), intArray0, 5, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -530 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test261()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpackwithoutmask(intArray0, (-1), intArray0, (-808), 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test262()  throws Throwable  {
      BitPacking bitPacking0 = new BitPacking();
  }

  @Test(timeout = 4000)
  public void test263()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        BitPacking.fastpack4(intArray0, (-4480), intArray0, (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -4480 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test264()  throws Throwable  {
      // Undeclared exception!
      try { 
        BitPacking.fastunpack5((int[]) null, (-4556), (int[]) null, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test265()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 32, intArray0, (-1097), 32);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test266()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 18, intArray0, 18, 29);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test267()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack(intArray0, 30, intArray0, 14, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 30 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test268()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        BitPacking.fastpack15(intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test269()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        BitPacking.fastunpack23(intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.BitPacking", e);
      }
  }
}
