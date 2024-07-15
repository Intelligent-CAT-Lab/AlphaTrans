
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


package org.joda.money;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.DefaultCurrencyUnitDataProvider;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CurrencyUnitDataProvider_ESTest extends CurrencyUnitDataProvider_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      defaultCurrencyUnitDataProvider0.registerCurrency("CHF", 3, 3);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      defaultCurrencyUnitDataProvider0.registerCountry("USD", "USD");
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      // Undeclared exception!
      try { 
        defaultCurrencyUnitDataProvider0.registerCurrency("{(Zp?2", (-369), 1512);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Invalid string code, must be length 3
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      // Undeclared exception!
      try { 
        defaultCurrencyUnitDataProvider0.registerCountry("CHF", "Currency code must not be null");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency 'Currency code must not be null'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      // Undeclared exception!
      try { 
        defaultCurrencyUnitDataProvider0.registerCountry((String) null, "CAD");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.concurrent.ConcurrentSkipListMap", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      // Undeclared exception!
      try { 
        defaultCurrencyUnitDataProvider0.registerCountry((String) null, (String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      DefaultCurrencyUnitDataProvider defaultCurrencyUnitDataProvider0 = new DefaultCurrencyUnitDataProvider();
      // Undeclared exception!
      try { 
        defaultCurrencyUnitDataProvider0.registerCurrency((String) null, 1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency code must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }
}
