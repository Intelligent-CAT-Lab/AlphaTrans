
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
import me.lemire.integercompression.benchmarktools.PerformanceLogger;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PerformanceLogger_ESTest extends PerformanceLogger_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addOriginalSize((-1543L));
      PerformanceLogger.Timer performanceLogger_Timer0 = performanceLogger0.compressionTimer;
      performanceLogger_Timer0.end();
      assertEquals(1392409281320000L, performanceLogger_Timer0.getDuration());
      
      double double0 = performanceLogger0.getCompressSpeed();
      assertEquals((-1.1081511885192552E-9), double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      PerformanceLogger.Timer performanceLogger_Timer0 = performanceLogger0.compressionTimer;
      performanceLogger_Timer0.start();
      long long0 = performanceLogger_Timer0.end();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addOriginalSize(2234L);
      long long0 = performanceLogger0.getOriginalSize();
      assertEquals(2234L, long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addOriginalSize((-1543L));
      long long0 = performanceLogger0.getOriginalSize();
      assertEquals((-1543L), long0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      PerformanceLogger.Timer performanceLogger_Timer0 = performanceLogger0.decompressionTimer;
      performanceLogger_Timer0.end();
      assertEquals(1392409281320000L, performanceLogger_Timer0.getDuration());
      
      double double0 = performanceLogger0.getDecompressSpeed();
      assertEquals(0.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addOriginalSize(1392409281320000L);
      assertEquals(1392409281320000L, long0);
      
      double double0 = performanceLogger0.getDecompressSpeed();
      assertEquals(Double.POSITIVE_INFINITY, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addOriginalSize((-1543L));
      assertEquals((-1543L), long0);
      
      double double0 = performanceLogger0.getDecompressSpeed();
      assertEquals(Double.NEGATIVE_INFINITY, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addCompressedSize(1L);
      long long0 = performanceLogger0.getCompressedSize();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      PerformanceLogger.Timer performanceLogger_Timer0 = performanceLogger0.compressionTimer;
      performanceLogger_Timer0.end();
      assertEquals(1392409281320000L, performanceLogger_Timer0.getDuration());
      
      double double0 = performanceLogger0.getCompressSpeed();
      assertEquals(0.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addOriginalSize(5002L);
      assertEquals(5002L, long0);
      
      double double0 = performanceLogger0.getBitPerInt();
      assertEquals(0.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addCompressedSize((-1529L));
      assertEquals((-1529L), long0);
      
      double double0 = performanceLogger0.getBitPerInt();
      assertEquals(Double.NEGATIVE_INFINITY, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addOriginalSize(1392409281320000L);
      assertEquals(1392409281320000L, long0);
      
      double double0 = performanceLogger0.getCompressSpeed();
      assertEquals(Double.POSITIVE_INFINITY, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addOriginalSize((-1543L));
      performanceLogger0.addCompressedSize((-1543L));
      double double0 = performanceLogger0.getBitPerInt();
      assertEquals(32.0, double0, 0.01);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      performanceLogger0.addCompressedSize((-1543L));
      long long0 = performanceLogger0.getCompressedSize();
      assertEquals((-1543L), long0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      PerformanceLogger.Timer performanceLogger_Timer0 = new PerformanceLogger.Timer();
      long long0 = performanceLogger_Timer0.getDuration();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.getCompressedSize();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.getOriginalSize();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addOriginalSize(0L);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      PerformanceLogger performanceLogger0 = new PerformanceLogger();
      long long0 = performanceLogger0.addCompressedSize(0L);
      assertEquals(0L, long0);
  }
}
