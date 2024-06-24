
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


package org.joda.money.format;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.Locale;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.format.MoneyPrintContext;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MoneyPrintContext_ESTest extends MoneyPrintContext_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Locale locale0 = Locale.JAPANESE;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      moneyPrintContext0.setLocale(locale0);
      assertEquals("ja", locale0.getLanguage());
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Locale locale0 = Locale.JAPANESE;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      // Undeclared exception!
      try { 
        moneyPrintContext0.setLocale((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Locale locale0 = Locale.CHINA;
      MoneyPrintContext moneyPrintContext0 = new MoneyPrintContext(locale0);
      Locale locale1 = moneyPrintContext0.getLocale();
      assertEquals("zho", locale1.getISO3Language());
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      MoneyPrintContext moneyPrintContext0 = null;
      try {
        moneyPrintContext0 = new MoneyPrintContext((Locale) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Locale must not be null
         //
         verifyException("org.joda.money.format.MoneyFormatter", e);
      }
  }
}
