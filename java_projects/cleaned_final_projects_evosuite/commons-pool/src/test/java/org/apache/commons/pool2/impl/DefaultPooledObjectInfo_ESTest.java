


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




package org.apache.commons.pool2.impl;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.time.Duration;
import java.time.Instant;
import java.time.temporal.TemporalAmount;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.impl.DefaultPooledObjectInfo;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.time.MockInstant;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DefaultPooledObjectInfo_ESTest extends DefaultPooledObjectInfo_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Object object0 = new Object();
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(object0).when(pooledObject0).getObject();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getPooledObjectType();
      assertEquals("java.lang.Object", string0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Object object0 = new Object();
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(object0).when(pooledObject0).getObject();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getPooledObjectToString();
      assertNotNull(string0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Instant instant0 = MockInstant.now();
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastReturnInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getLastReturnTimeFormatted();
      assertEquals("2014-02-14 20:21:21 +0000", string0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(0L, 730L);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastReturnInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastReturnTime();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochMilli(730L);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastReturnInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastReturnTime();
      assertEquals(730L, long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(0L);
      Instant instant1 = MockInstant.plusSeconds(instant0, (-802L));
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant1).when(pooledObject0).getLastReturnInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastReturnTime();
      assertEquals((-802000L), long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getLastBorrowTrace();
      assertEquals("", string0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(0L, 730L);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastBorrowInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastBorrowTime();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond((-4824L), (-1673L));
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastBorrowInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastBorrowTime();
      assertEquals((-4824001L), long0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(1L, 1L);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getCreateInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getCreateTimeFormatted();
      assertEquals("1970-01-01 00:00:01 +0000", string0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(0L);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getCreateInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getCreateTime();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochSecond(0L);
      Duration duration0 = Duration.ofMinutes((-1L));
      Instant instant1 = MockInstant.minus(instant0, (TemporalAmount) duration0);
      PooledObject<Object> pooledObject0 = (PooledObject<Object>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant1).when(pooledObject0).getCreateInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getCreateTime();
      assertEquals(60000L, long0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Instant instant0 = MockInstant.ofEpochMilli((-1192L));
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getCreateInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getCreateTime();
      assertEquals((-1192L), long0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(0L).when(pooledObject0).getBorrowedCount();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getBorrowedCount();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(2922L).when(pooledObject0).getBorrowedCount();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getBorrowedCount();
      assertEquals(2922L, long0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn((-1L)).when(pooledObject0).getBorrowedCount();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getBorrowedCount();
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getLastBorrowTime();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      Instant instant0 = MockInstant.now();
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastBorrowInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      long long0 = defaultPooledObjectInfo0.getLastBorrowTime();
      assertEquals(1392409281320L, long0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getPooledObjectType();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getCreateTimeFormatted();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getLastBorrowTrace();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getLastReturnTimeFormatted();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      Instant instant0 = MockInstant.now();
      PooledObject<Integer> pooledObject0 = (PooledObject<Integer>) mock(PooledObject.class, new ViolatedAssumptionAnswer());
      doReturn(instant0).when(pooledObject0).getLastBorrowInstant();
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo(pooledObject0);
      String string0 = defaultPooledObjectInfo0.getLastBorrowTimeFormatted();
      assertEquals("2014-02-14 20:21:21 +0000", string0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getCreateTime();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getBorrowedCount();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getPooledObjectToString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getLastReturnTime();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      String string0 = defaultPooledObjectInfo0.toString();
      assertEquals("DefaultPooledObjectInfo [pooledObject=null]", string0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      DefaultPooledObjectInfo defaultPooledObjectInfo0 = new DefaultPooledObjectInfo((PooledObject<?>) null);
      // Undeclared exception!
      try { 
        defaultPooledObjectInfo0.getLastBorrowTimeFormatted();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.pool2.impl.DefaultPooledObjectInfo", e);
      }
  }
}
