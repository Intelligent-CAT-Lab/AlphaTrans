
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


package org.fusesource.jansi.internal;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.Random;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.fusesource.jansi.internal.JansiLoader;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class JansiLoader_ESTest extends JansiLoader_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile("/tmp/jansi-2.4.2-1-libjansi.so.lck");
          boolean boolean0 = FileSystemHandling.createFolder(evoSuiteFile0);
          assertTrue(boolean0);
          
          int int0 = JansiLoader.getMinorVersion();
          assertEquals(4, int0);
          
          JansiLoader.cleanup();
          boolean boolean1 = JansiLoader.initialize();
          assertFalse(boolean1 == boolean0);
          assertFalse(boolean1);
          
          JansiLoader.cleanup();
          String string0 = JansiLoader.getNativeLibraryPath();
          assertNull(string0);
          
          String string1 = JansiLoader.getNativeLibraryPath();
          assertNull(string1);
          
          int int1 = JansiLoader.getMajorVersion();
          assertFalse(int1 == int0);
          assertEquals(2, int1);
          
          JansiLoader jansiLoader0 = new JansiLoader();
          assertNotNull(jansiLoader0);
          assertNull(jansiLoader0.getNativeLibraryPath());
          assertNull(jansiLoader0.getNativeLibrarySourceUrl());
          
          int int2 = JansiLoader.getMajorVersion();
          assertFalse(int2 == int0);
          assertEquals(2, int2);
          
          int int3 = JansiLoader.getMinorVersion();
          assertFalse(int3 == int1);
          assertFalse(int3 == int2);
          assertEquals(4, int3);
          
          boolean boolean2 = JansiLoader.initialize();
          assertFalse(boolean2 == boolean0);
          assertFalse(boolean2);
          
          int int4 = JansiLoader.getMinorVersion();
          assertFalse(int4 == int1);
          assertFalse(int4 == int2);
          assertEquals(4, int4);
          
          String string2 = JansiLoader.getNativeLibraryPath();
          assertNull(string2);
          
          String string3 = JansiLoader.getVersion();
          assertEquals("2.4.2", string3);
          assertNotNull(string3);
          
          String string4 = JansiLoader.getNativeLibraryPath();
          assertNull(string4);
          
          String string5 = JansiLoader.getVersion();
          assertTrue(string5.equals((Object)string3));
          assertEquals("2.4.2", string5);
          assertNotNull(string5);
          
          Random.setNextRandom(4);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          String string0 = JansiLoader.getNativeLibrarySourceUrl();
          assertNull(string0);
          
          String string1 = JansiLoader.getVersion();
          assertEquals("2.4.2", string1);
          assertNotNull(string1);
          
          String string2 = JansiLoader.getNativeLibraryPath();
          assertNull(string2);
          
          JansiLoader.cleanup();
          JansiLoader jansiLoader0 = new JansiLoader();
          assertNotNull(jansiLoader0);
          assertNull(jansiLoader0.getNativeLibraryPath());
          assertNull(jansiLoader0.getNativeLibrarySourceUrl());
          
          int int0 = JansiLoader.getMinorVersion();
          assertEquals(4, int0);
          
          int int1 = JansiLoader.getMajorVersion();
          assertFalse(int1 == int0);
          assertEquals(2, int1);
          
          boolean boolean0 = FileSystemHandling.shouldAllThrowIOExceptions();
          assertTrue(boolean0);
          
          JansiLoader.cleanup();
          int int2 = JansiLoader.getMajorVersion();
          assertFalse(int2 == int0);
          assertEquals(2, int2);
          
          int int3 = JansiLoader.getMinorVersion();
          assertFalse(int3 == int2);
          assertFalse(int3 == int1);
          assertEquals(4, int3);
          
          boolean boolean1 = JansiLoader.initialize();
          assertFalse(boolean1 == boolean0);
          assertFalse(boolean1);
          
          int int4 = JansiLoader.getMinorVersion();
          assertFalse(int4 == int1);
          assertFalse(int4 == int2);
          assertEquals(4, int4);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          String string0 = JansiLoader.getNativeLibrarySourceUrl();
          assertNull(string0);
          
          String string1 = JansiLoader.getVersion();
          assertEquals("2.4.2", string1);
          assertNotNull(string1);
          
          String string2 = JansiLoader.getNativeLibraryPath();
          assertNull(string2);
          
          JansiLoader.cleanup();
          JansiLoader jansiLoader0 = new JansiLoader();
          assertNotNull(jansiLoader0);
          assertNull(jansiLoader0.getNativeLibrarySourceUrl());
          assertNull(jansiLoader0.getNativeLibraryPath());
          
          JansiLoader.cleanup();
          int int0 = JansiLoader.getMinorVersion();
          assertEquals(4, int0);
          
          JansiLoader.cleanup();
          int int1 = JansiLoader.getMajorVersion();
          assertFalse(int1 == int0);
          assertEquals(2, int1);
          
          boolean boolean0 = FileSystemHandling.shouldAllThrowIOExceptions();
          assertTrue(boolean0);
          
          int int2 = JansiLoader.getMinorVersion();
          assertFalse(int2 == int1);
          assertEquals(4, int2);
          
          JansiLoader.cleanup();
          int int3 = JansiLoader.getMajorVersion();
          assertFalse(int3 == int0);
          assertFalse(int3 == int2);
          assertEquals(2, int3);
          
          boolean boolean1 = JansiLoader.initialize();
          assertFalse(boolean1 == boolean0);
          assertFalse(boolean1);
          
          JansiLoader.cleanup();
          int int4 = JansiLoader.getMinorVersion();
          assertFalse(int4 == int1);
          assertFalse(int4 == int3);
          assertEquals(4, int4);
          
          JansiLoader.cleanup();
          String string3 = JansiLoader.getVersion();
          assertTrue(string3.equals((Object)string1));
          assertEquals("2.4.2", string3);
          assertNotNull(string3);
          
          int int5 = JansiLoader.getMinorVersion();
          assertFalse(int5 == int3);
          assertFalse(int5 == int1);
          assertEquals(4, int5);
          
          String string4 = JansiLoader.getNativeLibraryPath();
          assertNull(string4);
          
          JansiLoader.cleanup();
          String string5 = JansiLoader.getVersion();
          assertTrue(string5.equals((Object)string3));
          assertTrue(string5.equals((Object)string1));
          assertEquals("2.4.2", string5);
          assertNotNull(string5);
          
          String string6 = JansiLoader.getNativeLibrarySourceUrl();
          assertNull(string6);
          
          String string7 = JansiLoader.getNativeLibraryPath();
          assertNull(string7);
          
          String string8 = JansiLoader.getNativeLibraryPath();
          assertNull(string8);
          
          JansiLoader.cleanup();
          int int6 = JansiLoader.getMinorVersion();
          assertFalse(int6 == int3);
          assertFalse(int6 == int1);
          assertEquals(4, int6);
          
          int int7 = JansiLoader.getMajorVersion();
          assertFalse(int7 == int0);
          assertFalse(int7 == int2);
          assertFalse(int7 == int6);
          assertFalse(int7 == int4);
          assertFalse(int7 == int5);
          assertEquals(2, int7);
          
          int int8 = JansiLoader.getMajorVersion();
          assertFalse(int8 == int0);
          assertFalse(int8 == int6);
          assertFalse(int8 == int2);
          assertFalse(int8 == int4);
          assertFalse(int8 == int5);
          assertEquals(2, int8);
          
          String string9 = JansiLoader.getNativeLibraryPath();
          assertNull(string9);
          
          String string10 = JansiLoader.getNativeLibrarySourceUrl();
          assertNull(string10);
          
          JansiLoader.cleanup();
          boolean boolean2 = JansiLoader.initialize();
          assertFalse(boolean2 == boolean0);
          assertFalse(boolean2);
          
          String string11 = JansiLoader.getNativeLibraryPath();
          assertNull(string11);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          boolean boolean0 = JansiLoader.initialize();
          assertFalse(boolean0);
          
          JansiLoader.cleanup();
          String string0 = JansiLoader.getNativeLibraryPath();
          assertNull(string0);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          JansiLoader.cleanup();
          String string0 = JansiLoader.getNativeLibraryPath();
          assertNull(string0);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      int int0 = JansiLoader.getMajorVersion();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          JansiLoader jansiLoader0 = new JansiLoader();
          JansiLoader.getMajorVersion();
          JansiLoader.getVersion();
          JansiLoader.initialize();
          JansiLoader.getNativeLibraryPath();
          JansiLoader.initialize();
          JansiLoader.getVersion();
          String string0 = JansiLoader.getNativeLibraryPath();
          assertNull(string0);
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      int int0 = JansiLoader.getMinorVersion();
      assertEquals(4, int0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
    Future<?> future = executor.submit(new Runnable(){ 
            @Override public void run() { 
          JansiLoader.getNativeLibraryPath();
          JansiLoader.cleanup();
          JansiLoader.getNativeLibraryPath();
          JansiLoader.getNativeLibraryPath();
          JansiLoader jansiLoader0 = new JansiLoader();
          JansiLoader.getVersion();
          JansiLoader.initialize();
          JansiLoader.initialize();
          JansiLoader.getVersion();
          JansiLoader.getMajorVersion();
          JansiLoader.getVersion();
          JansiLoader.getNativeLibraryPath();
          JansiLoader.getNativeLibrarySourceUrl();
          JansiLoader.getVersion();
          JansiLoader.getVersion();
          JansiLoader.cleanup();
          JansiLoader.getNativeLibraryPath();
          JansiLoader.cleanup();
          JansiLoader.getMinorVersion();
          JansiLoader.cleanup();
      } 
    });
    future.get(4000, TimeUnit.MILLISECONDS);
  }
}
