
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


package me.lemire.integercompression.differential;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.differential.IntegratedBitPacking;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class IntegratedBitPacking_ESTest extends IntegratedBitPacking_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack9((-257), intArray0, 254, intArray0, 1259);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 254 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack5(3197, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack22(5740339, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack22(5740339, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[1] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack22(5740339, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 1, intArray0, (-28), 20);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -28 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      int[] intArray0 = new int[2];
      intArray0[0] = 2151;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[0] = 8388607;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack18(0, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(3382, intArray0, 0, intArray0, 0, 17);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack15((-1346), intArray0, 5, intArray0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack14((-2445), intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack12(326, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[4] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack9(1, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[1] = 1;
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack9((-318), intArray0, 1, intArray0, 1371);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1371 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack9(1, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack7((-867), intArray0, 0, intArray0, (-347));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -347 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      int[] intArray0 = new int[3];
      int[] intArray1 = new int[6];
      intArray1[4] = (-347);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack7((-347), intArray1, 4, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[6] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack6(1, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[7];
      intArray1[4] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack6(0, intArray1, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[1] = 965;
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack6((-591), intArray0, 1, intArray0, 965);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[3] = (-3142);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack4(0, intArray0, 1, intArray0, 1267);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      int[] intArray0 = new int[5];
      intArray0[3] = 1711;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(4, intArray0, 3, intArray0, (-3729), 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = 2;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack30(2, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[2] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack3(3550, intArray0, 0, intArray0, 30);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[2] = (-609);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack3(21, intArray0, 1, intArray0, (-1689));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack29(1, intArray0, 1, intArray0, 27);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 27 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = (-2840);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack27(0, intArray0, 0, (int[]) null, 511);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack26(53, intArray0, 4, intArray0, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(12, intArray0, 1, intArray0, 26, 26);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 26 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[4] = 1;
      intArray0[6] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack25(1, intArray0, 3, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 16777215;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack24(1, intArray0, 1, intArray0, 16777215);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16777215 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack23(2047, intArray0, 0, intArray0, 1073807232);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1073807232 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack22(39, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      int[] intArray0 = new int[5];
      int[] intArray1 = new int[3];
      intArray1[1] = (-594);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack22((-594), intArray1, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[5] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack2(3550, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[3] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack2(3550, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = 3550;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack2(3550, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = 1153;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack2(3213, intArray0, 0, intArray0, (-458));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack19(1, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[1] = (-1229);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack19(182, intArray0, 1, intArray0, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 28 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      int[] intArray0 = new int[4];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(3929, intArray0, 1, intArray0, 185, 18);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 185 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      int[] intArray0 = new int[2];
      int[] intArray1 = new int[6];
      intArray1[0] = 29;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack17((-558), intArray1, 0, intArray0, (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[7];
      intArray1[5] = (-821);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack16(0, intArray1, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      int[] intArray0 = new int[7];
      int[] intArray1 = new int[7];
      intArray1[3] = (-821);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack16(0, intArray1, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      int[] intArray0 = new int[6];
      intArray0[0] = 177;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack16(177, intArray0, 0, intArray0, 536870911);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 536870911 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[0] = 19;
      intArray0[2] = (-6);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack15((-1), intArray0, 0, intArray0, (-1178));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1178 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack14(10, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = 23;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack14(23, intArray0, 1, intArray0, 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[2] = (-1);
      intArray0[4] = (-1);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack13((-1), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      int[] intArray0 = new int[9];
      intArray0[2] = (-1035);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack13(1, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      int[] intArray0 = new int[8];
      intArray0[2] = (-4536);
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack12(1, intArray0, 1, intArray0, (-4536));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -4536 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[1] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack((-1039), intArray0, 1, intArray0, 214, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 214 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      int[] intArray0 = new int[7];
      intArray0[0] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack11(1, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      int[] intArray0 = new int[10];
      intArray0[3] = 1;
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(1, intArray0, 1, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      int[] intArray0 = new int[7];
      IntegratedBitPacking.integratedpack0(0, intArray0, 0, intArray0, 0);
      assertEquals(7, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack9(2, intArray0, 16, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack9(14, intArray0, 16, intArray0, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      int[] intArray0 = new int[9];
      int[] intArray1 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack7(0, intArray0, 0, intArray1, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack6(2, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack30(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 29);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack25((-3039), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack24(19, intArray0, 19, intArray0, 2500172);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 19 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(1, intArray0, 1, intArray0, 1, 21);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack15(1, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack14((-418), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack12(0, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack10(0, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      int[] intArray0 = new int[24];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 24 out of bounds for length 24
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(1, intArray0, 2, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack9((-1), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      int[] intArray0 = new int[37];
      IntegratedBitPacking.integratedpack6((-846), intArray0, 0, intArray0, 0);
      assertEquals(37, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(5, intArray0, 5, intArray0, 17, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack30(2, intArray0, 0, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      int[] intArray0 = new int[22];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack29(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 22 out of bounds for length 22
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack24((-3130), intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack17(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack14((-2184), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 18 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(3062, intArray0, 7, intArray0, 7, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      int[] intArray0 = new int[19];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack10(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 19 out of bounds for length 19
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack9((-406), (int[]) null, (-406), (int[]) null, (-406));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack8(1, (int[]) null, 1135, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack8((-867), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack7(144, (int[]) null, 144, (int[]) null, 144);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack6((-6), intArray0, 2, intArray0, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack5(950, (int[]) null, (-1479), (int[]) null, 255);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack4(9, (int[]) null, 229, (int[]) null, 9);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack4(255, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack32(10, (int[]) null, 2, (int[]) null, (-1598));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack32(4, intArray0, (-609), intArray0, (-609));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack31((-3280), (int[]) null, 16, (int[]) null, (-2128));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack31(127, intArray0, 19, intArray0, 19);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 19 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack30(556, intArray0, 0, (int[]) null, (-856));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      int[] intArray0 = new int[21];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack3(1, intArray0, 5, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 21 out of bounds for length 21
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack29(63, (int[]) null, 19, (int[]) null, 19);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack29(131071, intArray0, 640, intArray0, 131071);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 640 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack28(27, (int[]) null, 27, (int[]) null, (-1868));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack28(1, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack27((-1), (int[]) null, (-1632), (int[]) null, (-1632));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack27(2008, intArray0, (-22), intArray0, (-22));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -22 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack26(21, (int[]) null, 21, (int[]) null, (-137));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack26(1154, intArray0, 26, intArray0, 1154);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 26 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack25(134217727, (int[]) null, (-3765), (int[]) null, (-3765));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack24(29, (int[]) null, 422, (int[]) null, 1293);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack23(119, (int[]) null, 119, (int[]) null, (-4426));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack23(1, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack22(5, (int[]) null, 5, (int[]) null, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack21(19, (int[]) null, (-1), (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack21(4757, intArray0, 4757, intArray0, 4757);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4757 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack20(980, (int[]) null, 980, (int[]) null, 980);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack20(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack2((-3540), (int[]) null, (-3540), (int[]) null, 25);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack2(9, intArray0, 0, intArray0, (-2359));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2359 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack19((-545), (int[]) null, 2307, (int[]) null, 3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack19((-296), intArray0, (-296), intArray0, (-296));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -296 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack18(116, (int[]) null, 26, (int[]) null, (-1643));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack18((-1731), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack17(533, intArray0, 3, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack16(2801, (int[]) null, (-1101), (int[]) null, (-1101));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack16((-3373), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack15(452, (int[]) null, 452, (int[]) null, 28);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack14((-45), (int[]) null, 18, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack13(1, (int[]) null, (-3264), (int[]) null, 2192);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack13(2799, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack11(26, (int[]) null, 26, (int[]) null, 2781);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack11(5, intArray0, 5, intArray0, 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 6 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack10((-3463), (int[]) null, (-1), (int[]) null, (-3241));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      int[] intArray0 = new int[3];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack10(27, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3 out of bounds for length 3
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack1((-434), (int[]) null, (-434), (int[]) null, (-434));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack1(14, intArray0, (-1495), intArray0, 20);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1495 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack0(1, intArray0, 15, intArray0, Integer.MAX_VALUE);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // fromIndex(2147483647) > toIndex(-2147483617)
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack0(9, intArray0, 1830, intArray0, (-599));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: -599
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(47, (int[]) null, 1, (int[]) null, 8200, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack9((-897), (int[]) null, (-897), (int[]) null, 26);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack8(13, intArray0, 13, intArray0, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack7((-1923), (int[]) null, (-1075), (int[]) null, (-4791));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack6(1, (int[]) null, 716, (int[]) null, 12);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack5(14, (int[]) null, (-2926), (int[]) null, 14);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack5(15, intArray0, 0, intArray0, 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack4(21, (int[]) null, 2509, (int[]) null, 26);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      int[] intArray0 = new int[0];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack32(25, intArray0, 8, (int[]) null, 594);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
      }
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack32(1073741823, intArray0, 28, intArray0, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack31(3595, (int[]) null, 3595, (int[]) null, 3595);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test143()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack31((-1336), intArray0, (-1336), intArray0, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1336 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test144()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack30(851, (int[]) null, 851, (int[]) null, 29);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test145()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack3((-1), (int[]) null, (-2547), (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test146()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack29(12, intArray0, 0, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test147()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack28(3, (int[]) null, 3, (int[]) null, 16383);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test148()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack28(7, intArray0, 7, intArray0, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test149()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack27(2022, intArray0, 0, intArray0, 2022);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1 out of bounds for length 1
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test150()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack26(648, (int[]) null, 0, (int[]) null, (-665));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test151()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack26(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test152()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack25((-3073), (int[]) null, (-3073), (int[]) null, (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test153()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack25(0, intArray0, 1, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test154()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack24(1598, (int[]) null, 1598, (int[]) null, (-1034));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test155()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack23((-1289), (int[]) null, (-2820), (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test156()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack22((-1719), (int[]) null, (-1719), (int[]) null, 131071);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test157()  throws Throwable  {
      int[] intArray0 = new int[14];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack22(1211, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 14 out of bounds for length 14
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test158()  throws Throwable  {
      int[] intArray0 = new int[1];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack21(1623, (int[]) null, 1623, intArray0, 1108);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test159()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack21((-317), intArray0, 1, intArray0, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 14 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test160()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack20(2251, (int[]) null, 262143, (int[]) null, 262143);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test161()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack20(2251, intArray0, 20, (int[]) null, 20);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 20 out of bounds for length 2
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test162()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack19(0, intArray0, 0, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test163()  throws Throwable  {
      int[] intArray0 = new int[2];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack18(0, (int[]) null, 9, intArray0, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test164()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack18(1280, intArray0, 1, intArray0, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test165()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack17(12, (int[]) null, 1475, (int[]) null, 12);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test166()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack16(0, intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test167()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack15(7, (int[]) null, (-4449), (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test168()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack15((-4488), intArray0, 0, intArray0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test169()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack14(2097151, (int[]) null, 4492, (int[]) null, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test170()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack13(262143, (int[]) null, (-1749), (int[]) null, (-1749));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test171()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack11(1174, (int[]) null, 2808, (int[]) null, 1174);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test172()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack10(28, (int[]) null, 912, intArray0, 28);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test173()  throws Throwable  {
      int[] intArray0 = new int[4];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack10(3985, intArray0, 0, intArray0, 1642);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1642 out of bounds for length 4
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test174()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack1(0, (int[]) null, 0, (int[]) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test175()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack1(0, intArray0, 1073741823, intArray0, 1207);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 1073741823 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test176()  throws Throwable  {
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack((-618), (int[]) null, 2, (int[]) null, 2, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test177()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(536870911, intArray0, 536870911, intArray0, 536870911, 536870911);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test178()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(12, intArray0, 12, intArray0, 12, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test179()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack((-2926), intArray0, (-2926), intArray0, (-2926), (-2926));
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unsupported bit width.
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test180()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(14, intArray0, 9, intArray0, 14, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test181()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 0, intArray0, 0, 19);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test182()  throws Throwable  {
      int[] intArray0 = new int[9];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(9, intArray0, 9, intArray0, 9, 14);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test183()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(27, intArray0, 2, intArray0, 27, 27);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 27 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test184()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(12, intArray0, 6, intArray0, 6, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test185()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(3360, intArray0, 3360, intArray0, (-1155), 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 3360 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test186()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(6, intArray0, 6, intArray0, 6, 6);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test187()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(399, intArray0, 1, intArray0, 1, 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test188()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 18);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test189()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(26, intArray0, 965, intArray0, 965, 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 965 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test190()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack((-1), intArray0, (-4106), intArray0, 255, 32);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test191()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 3, intArray0, 0, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test192()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(15, intArray0, 15, intArray0, (-14), 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test193()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(312, intArray0, 312, intArray0, 3, 30);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 312 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test194()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(14, intArray0, 11, intArray0, 14, 11);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 11 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test195()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(8, intArray0, 8, intArray0, 13, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test196()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(12, intArray0, 17, intArray0, 17, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 17 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test197()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack((-1), intArray0, (-2205), intArray0, (-2613), 28);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2205 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test198()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(32, intArray0, 32, intArray0, 21, 21);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 32 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test199()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(10, intArray0, 0, intArray0, 0, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test200()  throws Throwable  {
      int[] intArray0 = new int[11];
      IntegratedBitPacking.integratedpack(1, intArray0, 1, intArray0, 1, 0);
      assertEquals(11, intArray0.length);
  }

  @Test(timeout = 4000)
  public void test201()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(3, intArray0, 3, intArray0, 3, 3);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 8 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test202()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(1, intArray0, (-784), intArray0, 29, 29);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -784 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test203()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(978, intArray0, 28, intArray0, 28, 7);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 28 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test204()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(5567, intArray0, 10, intArray0, 3, 10);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 10 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test205()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(4, intArray0, 3, intArray0, (-3729), 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3729 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test206()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(12, intArray0, 12, intArray0, 12, 25);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 12 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test207()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Array index out of range: 32
         //
         verifyException("java.util.Arrays", e);
      }
  }

  @Test(timeout = 4000)
  public void test208()  throws Throwable  {
      int[] intArray0 = new int[10];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(1, intArray0, 1, intArray0, 16386, 25);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16386 out of bounds for length 10
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test209()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(22, intArray0, 14, intArray0, 22, 22);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 14 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test210()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(4, intArray0, 4, intArray0, 4, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test211()  throws Throwable  {
      int[] intArray0 = new int[23];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 0, intArray0, 12, 20);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 23
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test212()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(399, intArray0, 1, intArray0, 1, 8);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test213()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(16, intArray0, 16, intArray0, 16, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test214()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(7, intArray0, 196, intArray0, 17, 17);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 196 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test215()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 0, intArray0, (-2393), 30);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2393 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test216()  throws Throwable  {
      int[] intArray0 = new int[18];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack((-2926), intArray0, (-2926), intArray0, (-2926), 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2926 out of bounds for length 18
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test217()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(13, intArray0, 0, intArray0, 13, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test218()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(3062, intArray0, (-4), intArray0, (-4), 11);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -4 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test219()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(18, intArray0, 18, intArray0, 18, 32);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test220()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack((-3189), intArray0, 8, intArray0, 21, 8);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 21 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test221()  throws Throwable  {
      int[] intArray0 = new int[11];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 7, intArray0, 412, 26);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 412 out of bounds for length 11
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test222()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(1, intArray0, 1, intArray0, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test223()  throws Throwable  {
      int[] intArray0 = new int[12];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(15, intArray0, 15, intArray0, 15, 15);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 15 out of bounds for length 12
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test224()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(23, intArray0, (-1), intArray0, 14, 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test225()  throws Throwable  {
      int[] intArray0 = new int[6];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, (-929), intArray0, (-929), 5);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -929 out of bounds for length 6
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test226()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack12((-294), (int[]) null, 0, intArray0, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test227()  throws Throwable  {
      IntegratedBitPacking integratedBitPacking0 = new IntegratedBitPacking();
  }

  @Test(timeout = 4000)
  public void test228()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(23, intArray0, 23, intArray0, 23, 23);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 23 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test229()  throws Throwable  {
      int[] intArray0 = new int[16];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 1, intArray0, 1, 16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 16 out of bounds for length 16
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test230()  throws Throwable  {
      int[] intArray0 = new int[8];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(9, intArray0, 9, intArray0, 9, 9);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 9 out of bounds for length 8
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test231()  throws Throwable  {
      int[] intArray0 = new int[34];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(700, intArray0, 6, intArray0, 19, 19);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 34 out of bounds for length 34
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test232()  throws Throwable  {
      int[] intArray0 = new int[39];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(5, intArray0, 12, intArray0, 12, 12);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 39 out of bounds for length 39
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test233()  throws Throwable  {
      int[] intArray0 = new int[13];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(0, intArray0, 0, intArray0, 0, 27);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 13 out of bounds for length 13
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test234()  throws Throwable  {
      int[] intArray0 = new int[5];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedunpack(0, intArray0, 0, intArray0, 0, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 5 out of bounds for length 5
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test235()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(31, intArray0, 0, intArray0, 3, 31);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }

  @Test(timeout = 4000)
  public void test236()  throws Throwable  {
      int[] intArray0 = new int[7];
      // Undeclared exception!
      try { 
        IntegratedBitPacking.integratedpack(4194303, intArray0, 31, intArray0, 2, 2);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 31 out of bounds for length 7
         //
         verifyException("me.lemire.integercompression.differential.IntegratedBitPacking", e);
      }
  }
}
