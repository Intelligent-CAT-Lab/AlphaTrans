
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


package me.lemire.integercompression.benchmarktools;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.FileNotFoundException;
import me.lemire.integercompression.benchmarktools.Benchmark;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Benchmark_ESTest extends Benchmark_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      int[][] intArray0 = new int[0][8];
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze(intArray0, 2048, false);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      int[][] intArray0 = new int[3][4];
      int[] intArray1 = new int[0];
      intArray0[0] = intArray1;
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze(intArray0, 14, false);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // we have a bug (diff length)  expected 4 got 128
         //
         verifyException("me.lemire.integercompression.benchmarktools.Benchmark", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      int[][] intArray0 = new int[2][9];
      int[] intArray1 = new int[3];
      intArray0[1] = intArray1;
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze(intArray0, 3678, true);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // we have a bug (diff length)  expected 9 got 128
         //
         verifyException("me.lemire.integercompression.benchmarktools.Benchmark", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze((int[][]) null, 0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      int[][] intArray0 = new int[1][0];
      // Undeclared exception!
      Benchmark.testKamikaze(intArray0, 1048575, false);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      int[][] intArray0 = new int[1][2];
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze(intArray0, (-2479), true);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      int[][] intArray0 = new int[8][8];
      // Undeclared exception!
      try { 
        Benchmark.testKamikaze(intArray0, 4194303, true);
        fail("Expecting exception: RuntimeException");
      
      } catch(RuntimeException e) {
         //
         // we have a bug (diff length)  expected 8 got 128
         //
         verifyException("me.lemire.integercompression.benchmarktools.Benchmark", e);
      }
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      String[] stringArray0 = new String[0];
      // Undeclared exception!
      Benchmark.main(stringArray0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile("benchmark-20140214T202121.csv");
      FileSystemHandling.createFolder(evoSuiteFile0);
      String[] stringArray0 = new String[1];
      try { 
        Benchmark.main(stringArray0);
        fail("Expecting exception: FileNotFoundException");
      
      } catch(FileNotFoundException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.evosuite.runtime.mock.java.io.MockFileOutputStream", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      Benchmark benchmark0 = new Benchmark();
  }
}
