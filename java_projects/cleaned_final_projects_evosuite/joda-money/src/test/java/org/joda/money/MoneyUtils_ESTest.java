
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
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.List;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.CurrencyUnit;
import org.joda.money.Money;
import org.joda.money.MoneyUtils;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MoneyUtils_ESTest extends MoneyUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-1), roundingMode0);
      BigMoney bigMoney1 = bigMoney0.plus2(bigDecimal0);
      BigMoney bigMoney2 = MoneyUtils.subtract1(bigMoney0, bigMoney1);
      assertNotSame(bigMoney2, bigMoney0);
      assertFalse(bigMoney2.equals((Object)bigMoney0));
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 0);
      BigMoney bigMoney1 = MoneyUtils.subtract1(bigMoney0, (BigMoney) null);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-1), roundingMode0);
      BigMoney bigMoney1 = bigMoney0.plusMajor((-1));
      BigMoney bigMoney2 = bigMoney1.negated();
      BigMoney bigMoney3 = MoneyUtils.add1(bigMoney0, bigMoney2);
      assertTrue(bigMoney3.equals((Object)bigMoney2));
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = MoneyUtils.add1((BigMoney) null, bigMoney0);
      assertSame(bigMoney0, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-84L));
      BigMoney bigMoney1 = bigMoney0.multipliedBy2((-84L));
      BigMoney bigMoney2 = MoneyUtils.min1(bigMoney1, bigMoney0);
      assertNotSame(bigMoney2, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney2 = MoneyUtils.max1(bigMoney0, bigMoney1);
      assertSame(bigMoney2, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 0);
      BigMoney bigMoney1 = MoneyUtils.max1((BigMoney) null, bigMoney0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      Money money1 = MoneyUtils.subtract0(money0, (Money) null);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 1510L);
      Money money0 = bigMoney0.toMoney0();
      Money money1 = MoneyUtils.add0((Money) null, money0);
      assertSame(money0, money1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      Money money1 = Money.of3(currencyUnit0, (-1L), roundingMode0);
      Money money2 = MoneyUtils.min0(money0, money1);
      assertSame(money2, money1);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      Money money0 = Money.of3(currencyUnit0, 514.0, roundingMode0);
      Money money1 = money0.multipliedBy1((-1713.181969), roundingMode0);
      Money money2 = MoneyUtils.max0(money1, money0);
      assertSame(money2, money0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = MoneyUtils.max0((Money) null, money0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Object object0 = new Object();
      MoneyUtils.checkNotNull(object0, "");
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      BigMoney bigMoney0 = MoneyUtils.min1((BigMoney) null, (BigMoney) null);
      assertNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      Money money0 = MoneyUtils.min0((Money) null, (Money) null);
      assertNull(money0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = new BigMoney(1755, (BigDecimal) null, currencyUnit0);
      // Undeclared exception!
      try { 
        MoneyUtils.subtract1(bigMoney0, bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = new Money((-1), (BigMoney) null);
      // Undeclared exception!
      try { 
        MoneyUtils.subtract0(money0, money1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not return null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.CHF;
      BigMoney bigMoney1 = BigMoney.ofScale2(currencyUnit1, 59L, 0);
      // Undeclared exception!
      try { 
        MoneyUtils.min1(bigMoney1, bigMoney0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/USD
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal((-1));
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = new BigMoney((-1), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        MoneyUtils.min1(bigMoney0, bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.JPY;
      Money money1 = Money.ofMajor(currencyUnit1, (-340L));
      // Undeclared exception!
      try { 
        MoneyUtils.min0(money0, money1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/JPY
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      Money money0 = new Money(832, (BigMoney) null);
      // Undeclared exception!
      try { 
        MoneyUtils.min0(money0, money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-1139));
      CurrencyUnit currencyUnit1 = CurrencyUnit.EUR;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney1 = BigMoney.total2(currencyUnit1, bigMoneyProviderArray0);
      // Undeclared exception!
      try { 
        MoneyUtils.max1(bigMoney1, bigMoney0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: EUR/CHF
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = new BigMoney((-749), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        MoneyUtils.max1(bigMoney0, bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = new BigMoney((-66), bigDecimal0, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        MoneyUtils.isPositive(bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      Money money0 = new Money(100, (BigMoney) null);
      // Undeclared exception!
      try { 
        MoneyUtils.isNegative(money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      // Undeclared exception!
      try { 
        MoneyUtils.checkNotNull((Object) null, "yicM=6Mo4ibkj");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // yicM=6Mo4ibkj
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Invalid string code, must be ASCII upper-case letters", (short)1464, (short)1464);
      BigMoney bigMoney0 = new BigMoney(1, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        MoneyUtils.add1(bigMoney0, bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      Money money0 = new Money(832, (BigMoney) null);
      // Undeclared exception!
      try { 
        MoneyUtils.add0(money0, money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-208L));
      BigDecimal bigDecimal0 = new BigDecimal((-1962.0));
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 92);
      Money money1 = new Money(92, bigMoney0);
      // Undeclared exception!
      try { 
        MoneyUtils.add0(money0, money1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not return null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 1L, 0);
      BigMoney bigMoney1 = MoneyUtils.subtract1((BigMoney) null, bigMoney0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      BigMoney bigMoney0 = MoneyUtils.subtract1((BigMoney) null, (BigMoney) null);
      assertNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-84L));
      BigMoney bigMoney1 = MoneyUtils.add1(bigMoney0, (BigMoney) null);
      assertSame(bigMoney0, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      BigMoney bigMoney0 = MoneyUtils.add1((BigMoney) null, (BigMoney) null);
      assertNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney2 = MoneyUtils.min1(bigMoney0, bigMoney1);
      assertNotSame(bigMoney2, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 1L, 0);
      BigMoney bigMoney1 = MoneyUtils.min1(bigMoney0, (BigMoney) null);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-1139));
      BigMoney bigMoney1 = MoneyUtils.min1((BigMoney) null, bigMoney0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      BigMoney bigMoney1 = MoneyUtils.min1(bigMoney0, bigMoney0);
      assertSame(bigMoney0, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-498L));
      BigMoney bigMoney1 = MoneyUtils.subtract1(bigMoney0, bigMoney0);
      BigMoney bigMoney2 = MoneyUtils.max1(bigMoney1, bigMoney0);
      assertNotSame(bigMoney2, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = MoneyUtils.max1(bigMoney0, (BigMoney) null);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      BigMoney bigMoney0 = MoneyUtils.max1((BigMoney) null, (BigMoney) null);
      assertNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      BigMoney bigMoney1 = MoneyUtils.max1(bigMoney0, bigMoney0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      Money money0 = new Money((-1336), bigMoney0);
      // Undeclared exception!
      try { 
        MoneyUtils.subtract0(money0, money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      Money money0 = MoneyUtils.subtract0((Money) null, (Money) null);
      assertNull(money0);
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.of2(currencyUnit0, 0);
      Money money1 = MoneyUtils.subtract0((Money) null, money0);
      assertSame(money0, money1);
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = MoneyUtils.add0(money0, (Money) null);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      Money money0 = MoneyUtils.add0((Money) null, (Money) null);
      assertNull(money0);
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.ofMinor(currencyUnit0, (-1L));
      Money money1 = MoneyUtils.add0(money0, money0);
      Money money2 = MoneyUtils.min0(money1, money0);
      assertNotSame(money2, money0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-1139), (-1139));
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      Money money1 = MoneyUtils.min0(money0, money0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = MoneyUtils.min0(money0, (Money) null);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money0 = Money.of3(currencyUnit0, (-2687.757945337272), roundingMode0);
      Money money1 = MoneyUtils.min0((Money) null, money0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.ofMajor(currencyUnit0, (-1L));
      Money[] moneyArray0 = new Money[3];
      moneyArray0[0] = money0;
      moneyArray0[1] = money0;
      moneyArray0[2] = money0;
      Money money1 = Money.total2(currencyUnit0, moneyArray0);
      Money money2 = MoneyUtils.max0(money0, money1);
      assertNotSame(money2, money1);
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.ofMajor(currencyUnit0, (-1L));
      Money money1 = MoneyUtils.max0(money0, money0);
      assertSame(money0, money1);
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      Money money0 = MoneyUtils.max0((Money) null, (Money) null);
      assertNull(money0);
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      List<Money> list0 = List.of();
      Money money0 = Money.total3(currencyUnit0, list0);
      Money money1 = MoneyUtils.max0(money0, (Money) null);
      assertFalse(list0.contains(money1));
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal(1.0);
      BigMoney bigMoney1 = bigMoney0.withAmount0(bigDecimal0);
      Money money0 = Money.of4(bigMoney1);
      boolean boolean0 = MoneyUtils.isNegativeOrZero(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      boolean boolean0 = MoneyUtils.isNegativeOrZero(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      boolean boolean0 = MoneyUtils.isNegativeOrZero((BigMoneyProvider) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, (-1L));
      boolean boolean0 = MoneyUtils.isNegative(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-1139));
      boolean boolean0 = MoneyUtils.isNegative(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      boolean boolean0 = MoneyUtils.isNegative((BigMoneyProvider) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.ofMinor(currencyUnit0, (-1011L));
      boolean boolean0 = MoneyUtils.isPositiveOrZero(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.ofMinor(currencyUnit0, 0L);
      boolean boolean0 = MoneyUtils.isPositiveOrZero(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      boolean boolean0 = MoneyUtils.isPositiveOrZero((BigMoneyProvider) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = MoneyUtils.isPositive(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      boolean boolean0 = MoneyUtils.isPositive(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      boolean boolean0 = MoneyUtils.isPositive((BigMoneyProvider) null);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-1L));
      boolean boolean0 = MoneyUtils.isZero(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-1139));
      boolean boolean0 = MoneyUtils.isZero(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      boolean boolean0 = MoneyUtils.isZero((BigMoneyProvider) null);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-393L));
      Money money1 = new Money((-2428), bigMoney0);
      // Undeclared exception!
      try { 
        MoneyUtils.min0(money0, money1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not return null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }
}
