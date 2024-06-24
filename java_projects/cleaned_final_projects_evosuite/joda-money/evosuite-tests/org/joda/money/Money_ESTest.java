
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
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.math.RoundingMode;
import java.util.Collection;
import java.util.Comparator;
import java.util.Currency;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.PriorityQueue;
import java.util.ServiceLoader;
import java.util.TreeSet;
import java.util.Vector;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.joda.money.BigMoney;
import org.joda.money.BigMoneyProvider;
import org.joda.money.CurrencyUnit;
import org.joda.money.Money;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class Money_ESTest extends Money_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money1 = Money.of0(currencyUnit0, bigDecimal0);
      Money money2 = money0.minus1(money1);
      assertNotSame(money2, money0);
      assertFalse(money1.equals((Object)money0));
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 0.0);
      Money money0 = bigMoney0.toMoney0();
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money1 = money0.withCurrencyUnit1(currencyUnit0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.withAmount2((-1.0));
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money1 = money0.withAmount1(bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      BigMoney bigMoney0 = money0.toBigMoney();
      assertNotNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money1 = money0.rounded(1827, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.plusMinor((-2918L));
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 1.0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      Money money0 = Money.of4(bigMoney0);
      BigInteger bigInteger0 = BigInteger.ZERO;
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0, (-2559));
      Money money1 = money0.plus3(bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      Money money1 = money0.plus1(money0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("FJ(-/|N@o]HC4", (short)31, (short) (-1));
      BigDecimal bigDecimal0 = new BigDecimal((-106));
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      Class<Money> class0 = Money.class;
      ServiceLoader<Money> serviceLoader0 = ServiceLoader.load(class0, (ClassLoader) null);
      Money money1 = money0.plus0(serviceLoader0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      Money money0 = Money.parse("CHF 0.00");
      assertNotNull(money0);
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money1 = money0.multipliedBy0(bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.minusMajor((-645L));
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money1 = money0.minus5((-366.326589124059), roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.ofMajor(currencyUnit0, 0L);
      BigDecimal bigDecimal0 = new BigDecimal((-1L));
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money1 = money0.minus3(bigDecimal0, roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      Money money1 = money0.minus2(bigDecimal0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      boolean boolean0 = money0.isZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = new BigDecimal((-1819L));
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      boolean boolean0 = money0.isPositiveOrZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short) (-466), (short)42);
      Money money0 = Money.of2(currencyUnit0, (short) (-466));
      boolean boolean0 = money0.isPositive();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Country codes must not be null", (short)2599, (short)2599);
      Money money0 = Money.ofMajor(currencyUnit0, (short)2599);
      boolean boolean0 = money0.isNegativeOrZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      boolean boolean0 = money0.isNegative();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = money0.isLessThanOrEqual(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      Money money1 = money0.negated();
      boolean boolean0 = money1.isLessThanOrEqual(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 1L);
      boolean boolean0 = money0.isLessThan(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, (-783));
      boolean boolean0 = money0.isGreaterThanOrEqual(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      Money money1 = money0.minus4((-2984L));
      boolean boolean0 = money1.isGreaterThan(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)286, (short)1285);
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (short)286);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale0(bigMoney0, roundingMode0);
      Money money0 = bigMoney1.toMoney1(roundingMode0);
      boolean boolean0 = money0.isEqual(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      int int0 = money0.getScale();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      Money money1 = money0.negated();
      int int0 = money1.getMinorPart();
      assertEquals(84, int0);
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      int int0 = money0.getMinorPart();
      assertEquals((-84), int0);
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = money0.getCurrencyUnit();
      assertSame(currencyUnit0, currencyUnit1);
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMinor(currencyUnit0, 0L);
      long long0 = money0.getAmountMinorLong();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      long long0 = money0.getAmountMinorLong();
      assertEquals(100L, long0);
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMajor(currencyUnit0, (-1L));
      long long0 = money0.getAmountMinorLong();
      assertEquals((-100L), long0);
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      int int0 = money0.getAmountMinorInt();
      assertEquals((-2984), int0);
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = money0.getAmountMinor();
      assertEquals((short)0, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 1.0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale2((-3186.0), roundingMode0);
      BigMoney bigMoney2 = bigMoney1.withCurrencyScale1(roundingMode0);
      BigMoney bigMoney3 = bigMoney2.negated();
      Money money0 = Money.of4(bigMoney3);
      BigDecimal bigDecimal0 = money0.getAmountMinor();
      assertEquals((short) (-9180), bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      long long0 = money0.getAmountMajorLong();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      Money money0 = Money.of3(currencyUnit0, (-1.0), roundingMode0);
      long long0 = money0.getAmountMajorLong();
      assertEquals((-1L), long0);
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-3135L));
      int int0 = money0.getAmountMajorInt();
      assertEquals((-31), int0);
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = money0.getAmountMajor();
      assertEquals((short)0, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.ofMinor(currencyUnit0, (-1050L));
      BigDecimal bigDecimal0 = money0.getAmountMajor();
      assertEquals((byte) (-10), bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = money0.getAmount();
      assertEquals((short)0, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      BigDecimal bigDecimal1 = money0.getAmount();
      assertEquals((byte)1, bigDecimal1.byteValue());
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("Country codes must not be null", (short)18, (short)18);
      Money money0 = Money.of2(currencyUnit0, (-208.88629475));
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money1 = money0.dividedBy1((-208.88629475), roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      Money money1 = money0.dividedBy0(bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      Money money1 = money0.convertedTo(currencyUnit0, bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      int int0 = money0.compareTo((BigMoneyProvider) money0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMinor(currencyUnit0, 0L);
      BigDecimal bigDecimal0 = new BigDecimal((-1002));
      Money money1 = money0.plus2(bigDecimal0);
      int int0 = money0.compareTo((BigMoneyProvider) money1);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      Money money1 = Money.ofMinor(currencyUnit0, (-241L));
      int int0 = money1.compareTo((BigMoneyProvider) money0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.zero((CurrencyUnit) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[6];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[1] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[2] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[3] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[4] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[5] = (BigMoneyProvider) money0;
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money1 = new Money((-1481), bigMoney0);
      // Undeclared exception!
      try { 
        money1.withCurrencyUnit1(currencyUnit0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 14);
      Money money0 = new Money(14, bigMoney0);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      // Undeclared exception!
      try { 
        money0.withAmount3(14, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, (-3628));
      Money money0 = new Money((-3628), bigMoney0);
      // Undeclared exception!
      try { 
        money0.withAmount2((-3297.9804510482063));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      Money money0 = new Money(3095, (BigMoney) null);
      BigDecimal bigDecimal0 = new BigDecimal((double) 3095);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      // Undeclared exception!
      try { 
        money0.withAmount1(bigDecimal0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      Locale locale0 = Locale.PRC;
      CurrencyUnit currencyUnit0 = CurrencyUnit.of2(locale0);
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.withAmount0((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal((-4822.40255964));
      // Undeclared exception!
      try { 
        money0.withAmount0(bigDecimal0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money0 = Money.of5(bigMoney0, roundingMode0);
      Locale locale0 = Locale.GERMANY;
      Currency currency0 = Currency.getInstance(locale0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.of0(currency0);
      List<Money> list0 = List.of(money0);
      // Undeclared exception!
      try { 
        Money.total3(currencyUnit1, list0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: EUR/GBP
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      // Undeclared exception!
      try { 
        Money.total3(currencyUnit0, (Iterable<Money>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.total3((CurrencyUnit) null, (Iterable<Money>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      CurrencyUnit currencyUnit1 = CurrencyUnit.EUR;
      Money money0 = Money.ofMinor(currencyUnit1, 0L);
      Money[] moneyArray0 = new Money[8];
      moneyArray0[0] = money0;
      // Undeclared exception!
      try { 
        Money.total2(currencyUnit0, moneyArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: JPY/EUR
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      // Undeclared exception!
      try { 
        Money.total2(currencyUnit0, (Money[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money[] moneyArray0 = new Money[1];
      // Undeclared exception!
      try { 
        Money.total2(currencyUnit0, moneyArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.USD;
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money1 = Money.of3(currencyUnit1, (-19.7157), roundingMode0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money1, money0, money0, money0, money0);
      // Undeclared exception!
      try { 
        Money.total1(list0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: GBP/USD
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      Money money0 = new Money((-2115), bigMoney0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0, money0, money0);
      // Undeclared exception!
      try { 
        Money.total1(list0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.total1((Iterable<Money>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Money iterator must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money[] moneyArray0 = new Money[5];
      moneyArray0[0] = money0;
      moneyArray0[1] = money0;
      moneyArray0[2] = money0;
      moneyArray0[3] = money0;
      CurrencyUnit currencyUnit1 = CurrencyUnit.JPY;
      Money money1 = Money.zero(currencyUnit1);
      moneyArray0[4] = money1;
      // Undeclared exception!
      try { 
        Money.total0(moneyArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: EUR/JPY
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money[] moneyArray0 = new Money[2];
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      Money money0 = new Money(10, bigMoney0);
      moneyArray0[0] = money0;
      // Undeclared exception!
      try { 
        Money.total0(moneyArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Comparator<Money> comparator0 = (Comparator<Money>) mock(Comparator.class, new ViolatedAssumptionAnswer());
      PriorityQueue<Money> priorityQueue0 = new PriorityQueue<Money>(77, comparator0);
      BigMoney bigMoney0 = BigMoney.total3(currencyUnit0, priorityQueue0);
      Money money0 = new Money((-950), bigMoney0);
      // Undeclared exception!
      try { 
        money0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      Money money0 = new Money(4674, (BigMoney) null);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.rounded((-1457), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.plus4(1380.474300713);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      Money money0 = new Money(1344, (BigMoney) null);
      BigDecimal bigDecimal0 = new BigDecimal((long) 1344);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      // Undeclared exception!
      try { 
        money0.plus3(bigDecimal0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.plus2((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit1 = CurrencyUnit.CHF;
      Money money0 = Money.of0(currencyUnit1, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      Money money1 = Money.of1(currencyUnit0, bigDecimal0, roundingMode0);
      // Undeclared exception!
      try { 
        money0.plus1(money1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/JPY
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      Locale locale0 = Locale.CANADA;
      Currency currency0 = Currency.getInstance(locale0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.of0(currency0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      Money money1 = Money.of3(currencyUnit1, 1516.0, roundingMode0);
      hashSet0.add(money1);
      // Undeclared exception!
      try { 
        money0.plus0(hashSet0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/CAD
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.parse((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Money must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.parse("");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money '' cannot be parsed
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.ofMinor((CurrencyUnit) null, 0L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.ofMajor((CurrencyUnit) null, 1L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal((-642.011708682762));
      BigMoney bigMoney0 = new BigMoney(41, bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        Money.of5(bigMoney0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      RoundingMode roundingMode0 = RoundingMode.UP;
      // Undeclared exception!
      try { 
        Money.of5((BigMoneyProvider) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(0.0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-3576), roundingMode0);
      BigMoney bigMoney1 = bigMoney0.minus3(2234.132755916115);
      // Undeclared exception!
      try { 
        Money.of5(bigMoney1, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = new BigMoney((-596), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        Money.of4(bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.of4((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 4109.10315908);
      // Undeclared exception!
      try { 
        Money.of4(bigMoney0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        Money.of3((CurrencyUnit) null, (-1.0), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test086()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        Money.of3(currencyUnit0, (-3397.933944487), roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.of2((CurrencyUnit) null, (-4123.2));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      // Undeclared exception!
      try { 
        Money.of2(currencyUnit0, 3051.54465);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Scale of amount 3051.54465 is greater than the scale of the currency CHF
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.valueOf((-1580.97));
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        Money.of1(currencyUnit0, bigDecimal0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      // Undeclared exception!
      try { 
        Money.of0(currencyUnit0, (BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 0L);
      Money money0 = new Money(10, bigMoney0);
      // Undeclared exception!
      try { 
        money0.negated();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      Money money0 = new Money((-105), (BigMoney) null);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.multipliedBy1(2463.196, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      Money money0 = new Money((-893), (BigMoney) null);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      // Undeclared exception!
      try { 
        money0.multipliedBy0(bigDecimal0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      Money money0 = new Money(1773, bigMoney0);
      // Undeclared exception!
      try { 
        money0.minus5((-2063.71797904411), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.minus4(1170.9922759);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal(480.4741);
      // Undeclared exception!
      try { 
        money0.minus2(bigDecimal0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal(1L);
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 41);
      Money money0 = new Money(41, bigMoney0);
      // Undeclared exception!
      try { 
        money0.minus1(money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.minus0((Iterable<Money>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test099()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158L);
      Money money0 = bigMoney0.toMoney0();
      Money money1 = new Money(179, bigMoney0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money1, money1, money0);
      // Undeclared exception!
      try { 
        money0.minus0(list0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not return null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 48);
      Money money0 = new Money(48, bigMoney0);
      // Undeclared exception!
      try { 
        money0.isSameCurrency(bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.isSameCurrency((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      byte[] byteArray0 = new byte[4];
      BigInteger bigInteger0 = new BigInteger(byteArray0);
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      Money money0 = new Money((byte)59, bigMoney0);
      // Undeclared exception!
      try { 
        money0.isNegativeOrZero();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      CurrencyUnit currencyUnit1 = new CurrencyUnit("6OZbmjCl+", (short)1713, (short) (-1));
      Money money1 = Money.zero(currencyUnit1);
      // Undeclared exception!
      try { 
        money0.isLessThanOrEqual(money1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: JPY/6OZbmjCl+
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money[] moneyArray0 = new Money[6];
      BigDecimal bigDecimal0 = new BigDecimal((-1166));
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 9, roundingMode0);
      Money money0 = new Money((-1166), bigMoney0);
      // Undeclared exception!
      try { 
        money0.isLessThanOrEqual(moneyArray0[0]);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.ofMajor(currencyUnit0, (-764L));
      CurrencyUnit currencyUnit1 = CurrencyUnit.CHF;
      Money money1 = Money.ofMinor(currencyUnit1, (-764L));
      // Undeclared exception!
      try { 
        money1.isLessThan(money0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/EUR
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      Money money0 = new Money(39, (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.isLessThan((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      // Undeclared exception!
      try { 
        money0.isLessThan((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.JPY;
      Money money1 = Money.ofMajor(currencyUnit1, (-1L));
      // Undeclared exception!
      try { 
        money0.isGreaterThanOrEqual(money1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: CHF/JPY
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short)2052, (short)2052);
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.isGreaterThanOrEqual((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      // Undeclared exception!
      try { 
        money0.isEqual((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test111()  throws Throwable  {
      Money money0 = new Money((-1865), (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.getMinorPart();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      Money money0 = new Money(39, (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.getCurrencyUnit();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = new BigDecimal(30);
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 0);
      Money money0 = new Money(30, bigMoney0);
      // Undeclared exception!
      try { 
        money0.getAmountMinor();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      Money money0 = new Money(7, (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.getAmountMajorInt();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      Money money0 = new Money(109, (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.getAmountMajor();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal(1L);
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 41);
      Money money0 = new Money(41, bigMoney0);
      // Undeclared exception!
      try { 
        money0.getAmount();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal((long) 67);
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = new BigMoney(198, bigDecimal0, currencyUnit0);
      Money money0 = new Money(67, bigMoney0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        money0.dividedBy2(67, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        money0.dividedBy2(0L, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, (-1566));
      Money money0 = new Money(2, bigMoney0);
      // Undeclared exception!
      try { 
        money0.dividedBy1(2, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, (-88));
      Money money0 = new Money((-1238), bigMoney0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.dividedBy0((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        money0.dividedBy0(bigDecimal0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      // Undeclared exception!
      try { 
        money0.convertedTo(currencyUnit0, (BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Multiplier must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[2];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) money0;
      bigMoneyProviderArray0[1] = (BigMoneyProvider) money0;
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      Money money1 = new Money(0, bigMoney0);
      assertTrue(money1.equals((Object)money0));
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      // Undeclared exception!
      try { 
        money0.withCurrencyUnit1((CurrencyUnit) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      // Undeclared exception!
      try { 
        money0.withAmount1((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money1 = money0.plus5((-783.40558289), roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.plus1((Money) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      boolean boolean0 = money0.isNegative();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.minus5(1222.1105, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      // Undeclared exception!
      try { 
        Money.of1(currencyUnit0, (BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money1 = money0.withAmount3(0.0, roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.minus3((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.plus0((Iterable<Money>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        money0.plus3((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 0L);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      Money money1 = Money.of5(money0, roundingMode0);
      boolean boolean0 = money0.equals(money1);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = new BigDecimal((-1819L));
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      boolean boolean0 = money0.equals(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = money0.equals(currencyUnit0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.ofMajor(currencyUnit0, (-1L));
      Money money1 = money0.abs();
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.abs();
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      MathContext mathContext0 = MathContext.UNLIMITED;
      BigDecimal bigDecimal0 = new BigDecimal(0L, mathContext0);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      Money money0 = null;
      try {
        money0 = new Money(0, bigMoney0);
        fail("Expecting exception: AssertionError");
      
      } catch(AssertionError e) {
         //
         // Joda-Money bug: Only currency scale is valid for Money
         //
      }
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      Money money0 = null;
      try {
        money0 = new Money(0, (BigMoney) null);
        fail("Expecting exception: AssertionError");
      
      } catch(AssertionError e) {
         //
         // Joda-Money bug: BigMoney must not be null
         //
      }
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      TreeSet<Money> treeSet0 = new TreeSet<Money>();
      PriorityQueue<Money> priorityQueue0 = new PriorityQueue<Money>((Collection<? extends Money>) treeSet0);
      // Undeclared exception!
      try { 
        Money.total1(priorityQueue0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money iterator must not be empty
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test143()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0, money0, money0, money0);
      Money money1 = Money.total1(list0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test144()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money[] moneyArray0 = new Money[1];
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      moneyArray0[0] = money0;
      Money money1 = Money.total0(moneyArray0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test145()  throws Throwable  {
      Money[] moneyArray0 = new Money[0];
      // Undeclared exception!
      try { 
        Money.total0(moneyArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money array must not be empty
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test146()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigDecimal bigDecimal0 = new BigDecimal(2199.516458641819);
      // Undeclared exception!
      try { 
        Money.of0(currencyUnit0, bigDecimal0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Scale of amount 2199.51645864181909928447566926479339599609375 is greater than the scale of the currency JPY
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test147()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.ofMajor(currencyUnit0, (-764L));
      boolean boolean0 = money0.isLessThan(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test148()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-27L));
      int int0 = money0.getAmountMajorInt();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test149()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.ofMajor(currencyUnit0, 0L);
      boolean boolean0 = money0.isNegativeOrZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test150()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      long long0 = money0.getAmountMajorLong();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test151()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = money0.isZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test152()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      int int0 = money0.getMinorPart();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test153()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money[] moneyArray0 = new Money[0];
      Money money0 = Money.total2(currencyUnit0, moneyArray0);
      assertNotNull(money0);
  }

  @Test(timeout = 4000)
  public void test154()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Vector<Money> vector0 = new Vector<Money>();
      BigMoney bigMoney0 = BigMoney.total3(currencyUnit0, vector0);
      Money money0 = new Money(999, bigMoney0);
      // Undeclared exception!
      try { 
        money0.minusMajor(0L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test155()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 1.0);
      Money money0 = Money.of4(bigMoney0);
      boolean boolean0 = money0.isPositiveOrZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test156()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-27L));
      BigDecimal bigDecimal0 = money0.getAmountMinor();
      assertEquals((short) (-27), bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test157()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money1 = money0.dividedBy2((-1181L), roundingMode0);
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test158()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMinor(currencyUnit0, 0L);
      Money money1 = money0.withCurrencyUnit0(currencyUnit0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test159()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.ofMinor(currencyUnit0, 1071L);
      BigDecimal bigDecimal0 = money0.getAmountMajor();
      assertEquals((byte)10, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test160()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      // Undeclared exception!
      try { 
        money0.dividedBy1(0.0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test161()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 3529);
      Money money0 = new Money(3529, bigMoney0);
      // Undeclared exception!
      try { 
        money0.abs();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test162()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158L);
      Money money0 = bigMoney0.toMoney0();
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0, money0);
      Money money1 = money0.minus0(list0);
      assertFalse(list0.contains(money1));
  }

  @Test(timeout = 4000)
  public void test163()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.plusMajor((-476L));
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test164()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.multipliedBy2(2113L);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test165()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMajor(currencyUnit0, (-1803L));
      // Undeclared exception!
      try { 
        money0.withAmount2(1050.52909262545);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test166()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.plus4(0.0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test167()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 918L);
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      // Undeclared exception!
      try { 
        money0.rounded((-200), roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test168()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 48);
      Money money0 = new Money(48, bigMoney0);
      // Undeclared exception!
      try { 
        money0.getAmountMinorLong();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test169()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      boolean boolean0 = money0.isGreaterThan(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test170()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      Money money1 = money0.minus4((-2984L));
      int int0 = money1.getAmountMinorInt();
      assertEquals(295416, int0);
  }

  @Test(timeout = 4000)
  public void test171()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money[] moneyArray0 = new Money[2];
      Money money0 = Money.of2(currencyUnit0, 918L);
      moneyArray0[0] = money0;
      moneyArray0[1] = moneyArray0[0];
      boolean boolean0 = moneyArray0[1].isPositive();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test172()  throws Throwable  {
      // Undeclared exception!
      try { 
        Money.parse("o9H4");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency 'o9H'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test173()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMajor(currencyUnit0, (-1803L));
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = money0.isGreaterThanOrEqual(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test174()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        money0.dividedBy0((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Divisor must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test175()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("FJ(-/|N@o]HC4", (short)31, (short) (-1));
      BigDecimal bigDecimal0 = new BigDecimal((-106));
      Money money0 = Money.of0(currencyUnit0, bigDecimal0);
      BigDecimal bigDecimal1 = money0.getAmount();
      assertEquals((short) (-106), bigDecimal1.shortValue());
  }

  @Test(timeout = 4000)
  public void test176()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.ofMinor(currencyUnit0, 0L);
      CurrencyUnit currencyUnit1 = money0.getCurrencyUnit();
      assertEquals(2, currencyUnit1.getDecimalPlaces());
  }

  @Test(timeout = 4000)
  public void test177()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.minusMinor((-1223L));
      assertNotSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test178()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      Money money0 = Money.zero(currencyUnit0);
      int int0 = money0.getAmountMinorInt();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test179()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short) (-466), (short)42);
      Money money0 = Money.of2(currencyUnit0, (short) (-466));
      String string0 = money0.toString();
      assertEquals(" -466.000000000000000000000000000000000000000000", string0);
  }

  @Test(timeout = 4000)
  public void test180()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      Money money1 = money0.multipliedBy1((-1852.818531), roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test181()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-27L));
      int int0 = money0.getScale();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test182()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.zero(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        money0.multipliedBy0((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Multiplier must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test183()  throws Throwable  {
      Money money0 = new Money((-105), (BigMoney) null);
      // Undeclared exception!
      try { 
        money0.plusMinor((-105));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.Money", e);
      }
  }

  @Test(timeout = 4000)
  public void test184()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-27L));
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      Money money1 = money0.withAmount0(bigDecimal0);
      BigDecimal bigDecimal1 = money1.getAmountMinor();
      assertEquals((byte) (-24), bigDecimal1.byteValue());
  }

  @Test(timeout = 4000)
  public void test185()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 158L);
      Money money0 = bigMoney0.toMoney0();
      Money[] moneyArray0 = new Money[5];
      moneyArray0[0] = money0;
      // Undeclared exception!
      try { 
        Money.total0(moneyArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test186()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.zero(currencyUnit0);
      boolean boolean0 = money0.isEqual(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test187()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      // Undeclared exception!
      try { 
        money0.isLessThanOrEqual((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test188()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, (-27L));
      Money money0 = Money.ofMinor(currencyUnit0, (-27L));
      boolean boolean0 = money0.isSameCurrency(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test189()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      // Undeclared exception!
      try { 
        money0.convertedTo(currencyUnit0, bigDecimal0, roundingMode0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot convert to the same currency
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test190()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      Money money0 = Money.zero(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal(2407.165);
      // Undeclared exception!
      try { 
        money0.plus2(bigDecimal0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test191()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      // Undeclared exception!
      try { 
        money0.minus2((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test192()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.zero(currencyUnit0);
      money0.hashCode();
  }

  @Test(timeout = 4000)
  public void test193()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.ofMinor(currencyUnit0, (-2984L));
      Money money1 = money0.negated();
      int int0 = money1.getAmountMajorInt();
      assertEquals(29, int0);
  }
}
