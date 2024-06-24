
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
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.CurrencyMismatchException;
import org.joda.money.CurrencyUnit;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CurrencyMismatchException_ESTest extends CurrencyMismatchException_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException((CurrencyUnit) null, (CurrencyUnit) null);
      CurrencyUnit currencyUnit0 = currencyMismatchException0.getSecondCurrency();
      assertNull(currencyUnit0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)0, (short)716);
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getSecondCurrency();
      assertFalse(currencyUnit1.isPseudoCurrency());
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getSecondCurrency();
      assertSame(currencyUnit0, currencyUnit1);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getFirstCurrency();
      assertFalse(currencyUnit1.isPseudoCurrency());
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)0, (short)716);
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getFirstCurrency();
      assertSame(currencyUnit1, currencyUnit0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException((CurrencyUnit) null, (CurrencyUnit) null);
      CurrencyUnit currencyUnit0 = currencyMismatchException0.getFirstCurrency();
      assertNull(currencyUnit0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Uk\tvgjlFlIk%}5W", (short) (-2117), (short) (-2117));
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getSecondCurrency();
      assertEquals("Uk\tvgjlFlIk%}5W", currencyUnit1.getCode());
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Uk\tvgjlFlIk%}5W", (short) (-2117), (short) (-2117));
      CurrencyMismatchException currencyMismatchException0 = new CurrencyMismatchException(currencyUnit0, currencyUnit0);
      CurrencyUnit currencyUnit1 = currencyMismatchException0.getFirstCurrency();
      assertSame(currencyUnit1, currencyUnit0);
  }
}
