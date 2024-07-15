
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
import java.math.RoundingMode;
import java.util.Comparator;
import java.util.Currency;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Locale;
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
public class BigMoney_ESTest extends BigMoney_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test000()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.ofMinor(currencyUnit0, (-2270L));
      LinkedHashSet<Money> linkedHashSet0 = new LinkedHashSet<Money>();
      boolean boolean0 = linkedHashSet0.add(money0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test001()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.plus3(1.0);
      boolean boolean0 = bigMoney0.isLessThanOrEqual(bigMoney1);
      assertTrue(boolean0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test002()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 16);
      BigMoney bigMoney1 = bigMoney0.plusMajor((-3334L));
      boolean boolean0 = bigMoney0.isLessThan(bigMoney1);
      assertNotSame(bigMoney1, bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test003()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1625L);
      BigMoney bigMoney1 = bigMoney0.multipliedBy2(841L);
      boolean boolean0 = bigMoney1.isGreaterThanOrEqual(bigMoney0);
      assertNotSame(bigMoney1, bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test004()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigMoney bigMoney1 = BigMoney.zero1(currencyUnit0, (-845));
      boolean boolean0 = bigMoney0.isGreaterThan(bigMoney1);
      assertFalse(bigMoney1.equals((Object)bigMoney0));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test005()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigMoney bigMoney1 = bigMoney0.minusMinor(3630L);
      boolean boolean0 = bigMoney0.isEqual(bigMoney1);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test006()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        bigMoney0.convertRetainScale(currencyUnit0, bigDecimal0, roundingMode0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot convert to the same currency
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test007()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney1 = bigMoney0.rounded(0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test008()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigMoney bigMoney1 = bigMoney0.dividedBy1(927.7288717742318, roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test009()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.multipliedBy2((-4680L));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test010()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigMoney bigMoney1 = bigMoney0.multipliedBy1(7L);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test011()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney1 = bigMoney0.multipliedBy0(bigDecimal0);
      assertNotSame(bigMoney1, bigMoney0);
      assertFalse(bigMoney1.equals((Object)bigMoney0));
  }

  @Test(timeout = 4000)
  public void test012()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = new BigDecimal((-1822L));
      BigMoney bigMoney1 = bigMoney0.minus2(bigDecimal0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test013()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale2((-2270.0), roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test014()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = new BigDecimal((-1837L));
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test015()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      BigMoney bigMoney2 = bigMoney0.plusRetainScale0(bigMoney1, roundingMode0);
      assertSame(bigMoney2, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test016()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-638), 48);
      BigMoney bigMoney1 = bigMoney0.plusMinor(1L);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test017()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 0.0);
      BigMoney bigMoney1 = bigMoney0.plus3((-1834.54034602969));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test018()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = bigMoney0.isNegativeOrZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test019()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney1 = bigMoney0.plus3(2231.84);
      boolean boolean0 = bigMoney1.isPositiveOrZero();
      assertNotSame(bigMoney1, bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test020()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      boolean boolean0 = bigMoney0.isPositive();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test021()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      BigMoney bigMoney1 = bigMoney0.minus3(2228.66566665);
      boolean boolean0 = bigMoney1.isCurrencyScale();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test022()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney1 = bigMoney0.dividedBy2((-1586L), roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test023()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney1 = bigMoney0.dividedBy1((-2328.95), roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test024()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 44);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney1 = bigMoney0.withCurrencyScale1(roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test025()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      Money money0 = bigMoney0.toMoney0();
      assertNotNull(money0);
  }

  @Test(timeout = 4000)
  public void test026()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.ofScale0(currencyUnit0, bigDecimal0, 1126);
      assertNotNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test027()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(1.0);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      CurrencyUnit currencyUnit1 = new CurrencyUnit("{u!CT60@GBk6", (short) (-6), (short) (-6));
      BigMoney bigMoney1 = bigMoney0.convertRetainScale(currencyUnit1, bigDecimal0, roundingMode0);
      boolean boolean0 = bigMoney1.isSameCurrency(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test028()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1290.7206734967915));
      int int0 = bigMoney0.getScale();
      assertEquals(13, int0);
  }

  @Test(timeout = 4000)
  public void test029()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigMoney bigMoney1 = bigMoney0.minusMinor(3630L);
      int int0 = bigMoney1.getMinorPart();
      assertEquals((-30), int0);
  }

  @Test(timeout = 4000)
  public void test030()  throws Throwable  {
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short) (-1697), (short)48);
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, (short)48);
      CurrencyUnit currencyUnit1 = bigMoney0.getCurrencyUnit();
      assertEquals("", currencyUnit1.toString());
  }

  @Test(timeout = 4000)
  public void test031()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1625L);
      CurrencyUnit currencyUnit1 = bigMoney0.getCurrencyUnit();
      assertSame(currencyUnit1, currencyUnit0);
  }

  @Test(timeout = 4000)
  public void test032()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      long long0 = bigMoney0.getAmountMinorLong();
      assertEquals(1000L, long0);
  }

  @Test(timeout = 4000)
  public void test033()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      long long0 = bigMoney0.getAmountMinorLong();
      assertEquals((-128900L), long0);
  }

  @Test(timeout = 4000)
  public void test034()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(1.0);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      int int0 = bigMoney0.getAmountMinorInt();
      assertEquals(100, int0);
  }

  @Test(timeout = 4000)
  public void test035()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigMoney bigMoney1 = bigMoney0.minusMinor(3630L);
      int int0 = bigMoney1.getAmountMinorInt();
      assertEquals((-3630), int0);
  }

  @Test(timeout = 4000)
  public void test036()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = bigMoney0.getAmountMinor();
      assertEquals((byte)0, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test037()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0);
      Money money1 = Money.total3(currencyUnit0, list0);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[1];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) money1;
      BigMoney bigMoney0 = BigMoney.total0(bigMoneyProviderArray0);
      BigDecimal bigDecimal0 = bigMoney0.getAmountMinor();
      assertEquals((short)700, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test038()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0);
      long long0 = bigMoney0.getAmountMajorLong();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test039()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-3148L), 0);
      long long0 = bigMoney0.getAmountMajorLong();
      assertEquals((-3148L), long0);
  }

  @Test(timeout = 4000)
  public void test040()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale2(52.4458, roundingMode0);
      BigMoney bigMoney2 = bigMoney1.abs();
      BigMoney bigMoney3 = bigMoney2.minus1(bigMoney0);
      int int0 = bigMoney3.getAmountMajorInt();
      assertSame(bigMoney3, bigMoney2);
      assertEquals(53, int0);
  }

  @Test(timeout = 4000)
  public void test041()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      int int0 = bigMoney0.getAmountMajorInt();
      assertEquals((-1289), int0);
  }

  @Test(timeout = 4000)
  public void test042()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, 0);
      BigMoney bigMoney1 = bigMoney0.plusMajor(1L);
      BigDecimal bigDecimal0 = bigMoney1.getAmountMajor();
      assertEquals((short)1, bigDecimal0.shortValue());
  }

  @Test(timeout = 4000)
  public void test043()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = bigMoney0.getAmountMajor();
      assertEquals((byte) (-9), bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test044()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      BigMoney bigMoney0 = BigMoney.of2(money0);
      BigDecimal bigDecimal0 = bigMoney0.getAmount();
      assertEquals((byte)1, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test045()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      boolean boolean0 = bigMoney0.equals(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test046()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 841L);
      BigMoney bigMoney1 = bigMoney0.plusMajor(814L);
      int int0 = bigMoney1.compareTo((BigMoneyProvider) bigMoney0);
      assertEquals(1, int0);
  }

  @Test(timeout = 4000)
  public void test047()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.zero1((CurrencyUnit) null, 407);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test048()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.zero0((CurrencyUnit) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test049()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney(2, bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      // Undeclared exception!
      try { 
        bigMoney0.withScale1(0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test050()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal(477L);
      BigMoney bigMoney0 = new BigMoney((-1723), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.withScale0((-1723));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test051()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigInteger bigInteger0 = BigInteger.ONE;
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      // Undeclared exception!
      try { 
        bigMoney0.withScale0((-614));
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test052()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney0 = new BigMoney(627, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.withCurrencyScale1(roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test053()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 714.1664);
      // Undeclared exception!
      try { 
        bigMoney0.withCurrencyScale1(roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test054()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-2379L), 39);
      // Undeclared exception!
      try { 
        bigMoney0.withCurrencyScale0();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test055()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney(44, bigDecimal0, (CurrencyUnit) null);
      // Undeclared exception!
      try { 
        bigMoney0.withAmount0(bigDecimal0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test056()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, 0);
      // Undeclared exception!
      try { 
        bigMoney0.withAmount0((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test057()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      // Undeclared exception!
      try { 
        BigMoney.total3(currencyUnit0, (Iterable<? extends BigMoneyProvider>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test058()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.total3((CurrencyUnit) null, (Iterable<? extends BigMoneyProvider>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test059()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      Locale locale0 = Locale.SIMPLIFIED_CHINESE;
      Currency currency0 = Currency.getInstance(locale0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.of0(currency0);
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit1);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[8];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) bigMoney0;
      // Undeclared exception!
      try { 
        BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: USD/CNY
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test060()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      // Undeclared exception!
      try { 
        BigMoney.total2(currencyUnit0, (BigMoneyProvider[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("java.util.Objects", e);
      }
  }

  @Test(timeout = 4000)
  public void test061()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.total1((Iterable<? extends BigMoneyProvider>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Money iterator must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test062()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[5];
      Money money0 = Money.zero(currencyUnit0);
      bigMoneyProviderArray0[0] = (BigMoneyProvider) money0;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 2512L);
      bigMoneyProviderArray0[1] = (BigMoneyProvider) bigMoney0;
      bigMoneyProviderArray0[2] = (BigMoneyProvider) bigMoney0;
      bigMoneyProviderArray0[3] = (BigMoneyProvider) bigMoney0;
      BigMoney bigMoney1 = new BigMoney(1140, bigDecimal0, currencyUnit0);
      bigMoneyProviderArray0[4] = (BigMoneyProvider) bigMoney1;
      // Undeclared exception!
      try { 
        BigMoney.total0(bigMoneyProviderArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: USD/null
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test063()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 33);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = new BigMoney(33, bigDecimal0, currencyUnit0);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[4];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) bigMoney1;
      bigMoneyProviderArray0[1] = (BigMoneyProvider) bigMoney0;
      // Undeclared exception!
      try { 
        BigMoney.total0(bigMoneyProviderArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test064()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney((-8), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.toString();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test065()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.minus3((-1828.1825955349));
      // Undeclared exception!
      try { 
        bigMoney1.toMoney0();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test066()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      BigMoney bigMoney0 = new BigMoney((-1527), bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        bigMoney0.rounded((-1527), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test067()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale2(2488.8807, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test068()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = new BigDecimal((long) 7);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney0 = new BigMoney(7, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test069()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      RoundingMode roundingMode0 = RoundingMode.UP;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale1((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test070()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = new CurrencyUnit("3p", (short)3692, (short)3692);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      BigMoney bigMoney1 = BigMoney.zero1(currencyUnit1, (short)3692);
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale0(bigMoney1, roundingMode0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: USD/3p
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test071()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney((-13), bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale0(money0, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test072()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      // Undeclared exception!
      try { 
        bigMoney0.plusRetainScale0((BigMoneyProvider) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test073()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = new BigMoney(47, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.plusMajor((-1968L));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test074()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.plus2((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test075()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      CurrencyUnit currencyUnit1 = new CurrencyUnit((String) null, (short)2, (short) (-2543));
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      BigDecimal bigDecimal0 = new BigDecimal((long) (short)2);
      BigMoney bigMoney1 = bigMoney0.convertRetainScale(currencyUnit1, bigDecimal0, roundingMode0);
      Money money0 = Money.of1(currencyUnit0, bigDecimal0, roundingMode0);
      // Undeclared exception!
      try { 
        bigMoney1.plus1(money0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
      }
  }

  @Test(timeout = 4000)
  public void test076()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit1, 350L);
      // Undeclared exception!
      try { 
        bigMoney0.plus0(list0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: EUR/CHF
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test077()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal((-456.0));
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-971), roundingMode0);
      // Undeclared exception!
      try { 
        bigMoney0.plus0((Iterable<? extends BigMoneyProvider>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test078()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.parse("uCs5");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Unknown currency 'uCs'
         //
         verifyException("org.joda.money.CurrencyUnit", e);
      }
  }

  @Test(timeout = 4000)
  public void test079()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.parse((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Money must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test080()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.ofScale2((CurrencyUnit) null, 4335L, 5);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test081()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      // Undeclared exception!
      try { 
        BigMoney.ofScale2(currencyUnit0, (-725L), (-2146934699));
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // BigInteger would overflow supported range
         //
         verifyException("java.math.BigInteger", e);
      }
  }

  @Test(timeout = 4000)
  public void test082()  throws Throwable  {
      BigInteger bigInteger0 = BigInteger.TEN;
      BigDecimal bigDecimal0 = new BigDecimal(bigInteger0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        BigMoney.ofScale1((CurrencyUnit) null, bigDecimal0, 540, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test083()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.valueOf((-165L));
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-1840), roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test084()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      // Undeclared exception!
      try { 
        BigMoney.ofScale0(currencyUnit0, (BigDecimal) null, 2026);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test085()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.ofMinor((CurrencyUnit) null, (-742L));
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
      // Undeclared exception!
      try { 
        BigMoney.ofMajor((CurrencyUnit) null, (-1314L));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test087()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.of2((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test088()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.of1((CurrencyUnit) null, 650.71982050396);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Currency must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test089()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      // Undeclared exception!
      try { 
        BigMoney.of0(currencyUnit0, (BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test090()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney(32, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.negated();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test091()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = new BigMoney(338, bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        bigMoney0.multiplyRetainScale1((-1345.5), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test092()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1.0));
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        bigMoney0.multiplyRetainScale1(113.236137, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test093()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-3201L));
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        bigMoney0.multiplyRetainScale0((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Multiplier must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test094()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = new BigDecimal((-1957.443));
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        bigMoney0.multiplyRetainScale0(bigDecimal0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test095()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal(1553.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = new BigMoney((-1724), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.multipliedBy2(841L);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test096()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney((-2940), bigDecimal0, currencyUnit0);
      BigDecimal bigDecimal1 = new BigDecimal(0L);
      // Undeclared exception!
      try { 
        bigMoney0.multipliedBy0(bigDecimal1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test097()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 3715L, (-6));
      // Undeclared exception!
      try { 
        bigMoney0.multipliedBy0((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Multiplier must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test098()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = new BigMoney(4, bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      // Undeclared exception!
      try { 
        bigMoney0.minusRetainScale2((-423.792), roundingMode0);
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
      CurrencyUnit currencyUnit0 = new CurrencyUnit("", (short) (-1254), (short) (-1254));
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      // Undeclared exception!
      try { 
        bigMoney0.minusRetainScale1((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test100()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = new BigDecimal((long) 1092);
      BigMoney bigMoney0 = new BigMoney(1092, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.minusMinor(1092);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test101()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = new BigDecimal((-4680));
      BigMoney bigMoney0 = new BigMoney(3, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.minusMajor((-4680));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test102()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney(3, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.minus3(3);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test103()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney((-347), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.minus2(bigDecimal0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test104()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      // Undeclared exception!
      try { 
        bigMoney0.minus2((BigDecimal) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Amount must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test105()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-360), roundingMode0);
      Comparator<Object> comparator0 = (Comparator<Object>) mock(Comparator.class, new ViolatedAssumptionAnswer());
      doReturn(0).when(comparator0).compare(any() , any());
      TreeSet<Money> treeSet0 = new TreeSet<Money>(comparator0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.USD;
      Money money0 = Money.of1(currencyUnit1, bigDecimal0, roundingMode0);
      treeSet0.add(money0);
      // Undeclared exception!
      try { 
        bigMoney0.minus0(treeSet0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: GBP/USD
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test106()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.minus0((Iterable<? extends BigMoneyProvider>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test107()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney1 = new BigMoney(32, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney1.isSameCurrency(bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test108()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal(1553.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = new BigMoney((-1724), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.isPositive();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test109()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      BigMoney bigMoney0 = BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
      CurrencyUnit currencyUnit1 = CurrencyUnit.GBP;
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      Money money0 = Money.of3(currencyUnit1, (-1762.110832), roundingMode0);
      // Undeclared exception!
      try { 
        bigMoney0.isLessThanOrEqual(money0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: JPY/GBP
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test110()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      // Undeclared exception!
      try { 
        bigMoney0.isEqual((BigMoneyProvider) null);
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
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigDecimal bigDecimal0 = new BigDecimal((-456.0));
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, (-971), roundingMode0);
      // Undeclared exception!
      try { 
        bigMoney0.getAmountMinorLong();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Overflow
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test112()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = new BigMoney(66, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.getAmountMinor();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test113()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 530L, (-2398));
      // Undeclared exception!
      try { 
        bigMoney0.getAmountMajorLong();
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Overflow
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test114()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = new BigMoney(1129, bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy2(1591L, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test115()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = new BigMoney((-2797), bigDecimal0, currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy1((-2797), roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test116()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy0((BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Divisor must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test117()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal((double) 0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy0(bigDecimal0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test118()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal(1553.0);
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = new BigMoney((-1724), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.convertedTo(currencyUnit0, bigDecimal0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test119()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = new BigDecimal(1495L);
      // Undeclared exception!
      try { 
        bigMoney0.convertedTo((CurrencyUnit) null, bigDecimal0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // CurrencyUnit must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test120()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 4);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = new BigMoney(4, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney1.compareTo((BigMoneyProvider) bigMoney0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test121()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.compareTo((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test122()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = new BigMoney(762, bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.abs();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test123()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      int int0 = bigMoney0.compareTo((BigMoneyProvider) bigMoney0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test124()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 0.0);
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      CurrencyUnit currencyUnit1 = CurrencyUnit.EUR;
      BigMoney bigMoney1 = bigMoney0.convertedTo(currencyUnit1, bigDecimal0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test125()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigMoney bigMoney1 = bigMoney0.negated();
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test126()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 77);
      BigMoney bigMoney1 = bigMoney0.multiplyRetainScale0(bigDecimal0, roundingMode0);
      assertTrue(bigMoney1.equals((Object)bigMoney0));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test127()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test128()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal((long) 0);
      BigMoney bigMoney1 = bigMoney0.minus2(bigDecimal0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test129()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0);
      BigMoney bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test130()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney1 = bigMoney0.plus2(bigDecimal0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test131()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      boolean boolean0 = bigMoney0.isNegative();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test132()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 4);
      boolean boolean0 = bigMoney0.isNegative();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test133()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      boolean boolean0 = bigMoney0.isZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test134()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.plus3(1.0);
      boolean boolean0 = bigMoney1.isZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test135()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 775L);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      // Undeclared exception!
      try { 
        bigMoney0.withScale1((-1692), roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test136()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, (-2379L), 39);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigMoney bigMoney1 = bigMoney0.withScale1(39, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test137()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney(0, bigDecimal0, currencyUnit0);
  }

  @Test(timeout = 4000)
  public void test138()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = bigMoney0.isSameCurrency(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test139()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = bigMoney0.getAmountMajor();
      assertEquals((byte)0, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test140()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = new BigMoney(66, bigDecimal0, currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.toBigMoney();
      assertSame(bigMoney0, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test141()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      int int0 = bigMoney0.getScale();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test142()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      Money money0 = Money.zero(currencyUnit0);
      Money money1 = money0.withAmount1(bigDecimal0, roundingMode0);
      assertSame(money1, money0);
  }

  @Test(timeout = 4000)
  public void test143()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.equals(currencyUnit0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test144()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      boolean boolean0 = bigMoney0.isLessThanOrEqual(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test145()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      List<Money> list0 = List.of(money0, money0, money0, money0, money0, money0, money0);
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.plus0(list0);
      boolean boolean0 = bigMoney1.isLessThanOrEqual(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test146()  throws Throwable  {
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[1];
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1290.7206734967915));
      bigMoneyProviderArray0[0] = (BigMoneyProvider) bigMoney0;
      BigMoney bigMoney1 = bigMoney0.plus1(bigMoneyProviderArray0[0]);
      boolean boolean0 = bigMoney1.isLessThan(bigMoneyProviderArray0[0]);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test147()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 16);
      boolean boolean0 = bigMoney0.isLessThan(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test148()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.isGreaterThanOrEqual(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test149()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0);
      boolean boolean0 = bigMoney1.isGreaterThanOrEqual(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test150()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-1L));
      BigDecimal bigDecimal0 = new BigDecimal(67);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale1(bigDecimal0, roundingMode0);
      boolean boolean0 = bigMoney1.isGreaterThan(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test151()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, 0);
      boolean boolean0 = bigMoney0.isGreaterThan(bigMoney0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test152()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.isEqual(bigMoney0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test153()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.isEqual(money0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test154()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, (-5437));
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = new BigMoney((-5437), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.compareTo((BigMoneyProvider) bigMoney1);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: USD/null
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test155()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      CurrencyUnit currencyUnit1 = new CurrencyUnit("3p", (short)3692, (short)3692);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      BigMoney bigMoney1 = bigMoney0.convertRetainScale(currencyUnit1, bigDecimal0, roundingMode0);
      // Undeclared exception!
      try { 
        bigMoney1.plus1(bigMoney0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Currencies differ: 3p/USD
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test156()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      BigDecimal bigDecimal0 = bigMoney0.getAmountMinor();
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        bigMoney0.convertRetainScale(currencyUnit0, bigDecimal0, roundingMode0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot convert to the same currency
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test157()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney1 = bigMoney0.convertedTo(currencyUnit0, bigDecimal0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test158()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal((double) (-1079));
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = new BigMoney((-1079), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.convertedTo(currencyUnit0, bigDecimal0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot convert using a negative conversion multiplier
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test159()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney1 = bigMoney0.rounded(10, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test160()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      BigMoney bigMoney1 = bigMoney0.rounded((-7), roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
      assertTrue(bigMoney1.equals((Object)bigMoney0));
  }

  @Test(timeout = 4000)
  public void test161()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      RoundingMode roundingMode0 = RoundingMode.UNNECESSARY;
      BigMoney bigMoney1 = bigMoney0.dividedBy2(1L, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test162()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy2(0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test163()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      BigMoney bigMoney0 = BigMoney.of2(money0);
      RoundingMode roundingMode0 = RoundingMode.CEILING;
      BigMoney bigMoney1 = bigMoney0.dividedBy1(1.0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test164()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      // Undeclared exception!
      try { 
        bigMoney0.dividedBy1(0, roundingMode0);
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // / by zero
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test165()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = bigMoney0.dividedBy0(bigDecimal0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test166()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      BigMoney bigMoney1 = bigMoney0.dividedBy0(bigDecimal0, roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
      assertTrue(bigMoney1.equals((Object)bigMoney0));
  }

  @Test(timeout = 4000)
  public void test167()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney0 = BigMoney.ofScale1(currencyUnit0, bigDecimal0, 77, roundingMode0);
      BigDecimal bigDecimal1 = BigDecimal.ONE;
      BigMoney bigMoney1 = bigMoney0.multiplyRetainScale0(bigDecimal1, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test168()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.multipliedBy2(1L);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test169()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.multipliedBy1(1.0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test170()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.multipliedBy1(0.0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test171()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney1 = bigMoney0.multipliedBy0(bigDecimal0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test172()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      RoundingMode roundingMode0 = RoundingMode.UP;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale2(0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test173()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofMajor(currencyUnit0, 1877L);
      RoundingMode roundingMode0 = RoundingMode.HALF_DOWN;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale2(1.0, roundingMode0);
      int int0 = bigMoney1.compareTo((BigMoneyProvider) bigMoney0);
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test174()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = new BigDecimal((-3295L));
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale1(bigDecimal0, roundingMode0);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test175()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      BigMoney bigMoney1 = bigMoney0.minusMinor(0L);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test176()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.minusMinor((-981L));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test177()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.minusMajor(0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test178()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.minusMajor(1601L);
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test179()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.minus3(0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test180()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      HashSet<Money> hashSet0 = new HashSet<Money>();
      Money money0 = Money.total3(currencyUnit0, hashSet0);
      List<Money> list0 = List.of(money0);
      BigMoney bigMoney1 = bigMoney0.minus0(list0);
      assertNotSame(bigMoney1, bigMoney0);
      assertFalse(bigMoney1.equals((Object)bigMoney0));
  }

  @Test(timeout = 4000)
  public void test181()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_EVEN;
      BigMoney bigMoney1 = bigMoney0.plusRetainScale2(0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test182()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigMoney bigMoney1 = bigMoney0.plusMinor(0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test183()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.plusMinor((-1431655764L));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test184()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigMoney bigMoney1 = bigMoney0.plusMajor(0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test185()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.plus3(0.0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test186()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney1 = bigMoney0.plus2(bigDecimal0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test187()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      BigDecimal bigDecimal0 = BigDecimal.ZERO;
      BigMoney bigMoney1 = bigMoney0.withAmount0(bigDecimal0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test188()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      boolean boolean0 = bigMoney0.isNegativeOrZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test189()  throws Throwable  {
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      boolean boolean0 = bigMoney0.isNegativeOrZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test190()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.abs();
      assertSame(bigMoney0, bigMoney1);
  }

  @Test(timeout = 4000)
  public void test191()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.isPositiveOrZero();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test192()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      Money money0 = Money.of2(currencyUnit0, 1.0);
      BigMoney bigMoney0 = BigMoney.of2(money0);
      boolean boolean0 = bigMoney0.isPositive();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test193()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      boolean boolean0 = bigMoney0.isPositive();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test194()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.negated();
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test195()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, (-1L));
      BigMoney bigMoney1 = bigMoney0.withCurrencyScale0();
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test196()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.JPY;
      BigMoney bigMoney0 = BigMoney.ofScale2(currencyUnit0, 0L, 0);
      boolean boolean0 = bigMoney0.isCurrencyScale();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test197()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      boolean boolean0 = bigMoney0.isCurrencyScale();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test198()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.withCurrencyUnit(currencyUnit0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test199()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = new BigMoney((-2807), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.withCurrencyUnit(currencyUnit0);
        fail("Expecting exception: AssertionError");
      
      } catch(AssertionError e) {
         //
         // Joda-Money bug: Amount must not be null
         //
      }
  }

  @Test(timeout = 4000)
  public void test200()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = null;
      try {
        bigMoney0 = new BigMoney(0, (BigDecimal) null, currencyUnit0);
        fail("Expecting exception: AssertionError");
      
      } catch(AssertionError e) {
         //
         // Joda-Money bug: Amount must not be null
         //
      }
  }

  @Test(timeout = 4000)
  public void test201()  throws Throwable  {
      BigMoney bigMoney0 = BigMoney.parse("EUR 0");
      assertNotNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test202()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.parse("C1}");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money 'C1}' cannot be parsed
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test203()  throws Throwable  {
      // Undeclared exception!
      try { 
        BigMoney.parse(" is greater than the scale of the currency ");
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money amount ' is greater than the scale of the currency ' cannot be parsed
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test204()  throws Throwable  {
      Vector<Money> vector0 = new Vector<Money>();
      // Undeclared exception!
      try { 
        BigMoney.total1(vector0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money iterator must not be empty
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test205()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.ofMinor(currencyUnit0, 841L);
      List<BigMoney> list0 = List.of(bigMoney0, bigMoney0, bigMoney0, bigMoney0, bigMoney0);
      BigMoney bigMoney1 = BigMoney.total1(list0);
      assertFalse(list0.contains(bigMoney1));
  }

  @Test(timeout = 4000)
  public void test206()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[2];
      bigMoneyProviderArray0[0] = (BigMoneyProvider) bigMoney0;
      // Undeclared exception!
      try { 
        BigMoney.total0(bigMoneyProviderArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test207()  throws Throwable  {
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[0];
      // Undeclared exception!
      try { 
        BigMoney.total0(bigMoneyProviderArray0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Money array must not be empty
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test208()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, 0.0);
      BigDecimal bigDecimal0 = new BigDecimal(0L);
      // Undeclared exception!
      try { 
        bigMoney0.convertedTo(currencyUnit0, bigDecimal0);
        fail("Expecting exception: IllegalArgumentException");
      
      } catch(IllegalArgumentException e) {
         //
         // Cannot convert to the same currency
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test209()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.of1(currencyUnit0, (-1289.0));
      boolean boolean0 = bigMoney0.isPositiveOrZero();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test210()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      Money money0 = bigMoney0.toMoney1(roundingMode0);
      assertNotNull(money0);
  }

  @Test(timeout = 4000)
  public void test211()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      Money money0 = Money.ofMajor(currencyUnit0, 0L);
      RoundingMode roundingMode0 = RoundingMode.DOWN;
      BigMoney bigMoney1 = bigMoney0.minusRetainScale0(money0, roundingMode0);
      assertSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test212()  throws Throwable  {
      BigDecimal bigDecimal0 = new BigDecimal((-7));
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = new BigMoney((-7), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.withCurrencyScale0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test213()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = new BigDecimal(7);
      BigMoney bigMoney0 = new BigMoney((-1785), bigDecimal0, currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.toMoney0();
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.joda.money.BigMoney", e);
      }
  }

  @Test(timeout = 4000)
  public void test214()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.withScale0(17);
      assertFalse(bigMoney1.equals((Object)bigMoney0));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test215()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CHF;
      BigDecimal bigDecimal0 = BigDecimal.ONE;
      BigMoney bigMoney0 = BigMoney.of0(currencyUnit0, bigDecimal0);
      long long0 = bigMoney0.getAmountMajorLong();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test216()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      long long0 = bigMoney0.getAmountMinorLong();
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test217()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      int int0 = bigMoney0.getAmountMinorInt();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test218()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero1(currencyUnit0, 0);
      bigMoney0.hashCode();
  }

  @Test(timeout = 4000)
  public void test219()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      Vector<Money> vector0 = new Vector<Money>();
      BigMoney bigMoney0 = BigMoney.total3(currencyUnit0, vector0);
      assertNotNull(bigMoney0);
  }

  @Test(timeout = 4000)
  public void test220()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.HALF_UP;
      // Undeclared exception!
      try { 
        bigMoney0.convertRetainScale(currencyUnit0, (BigDecimal) null, roundingMode0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // Multiplier must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test221()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigMoney bigMoney1 = bigMoney0.withAmount1((-2041.5577429803));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test222()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.CAD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      // Undeclared exception!
      try { 
        bigMoney0.plus1((BigMoneyProvider) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }

  @Test(timeout = 4000)
  public void test223()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.GBP;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      int int0 = bigMoney0.getMinorPart();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test224()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigDecimal bigDecimal0 = BigDecimal.TEN;
      // Undeclared exception!
      try { 
        BigMoney.ofScale0(currencyUnit0, bigDecimal0, (-4579));
        fail("Expecting exception: ArithmeticException");
      
      } catch(ArithmeticException e) {
         //
         // Rounding necessary
         //
         verifyException("java.math.BigDecimal", e);
      }
  }

  @Test(timeout = 4000)
  public void test225()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      BigDecimal bigDecimal0 = bigMoney0.getAmount();
      assertEquals((byte)0, bigDecimal0.byteValue());
  }

  @Test(timeout = 4000)
  public void test226()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.EUR;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      String string0 = bigMoney0.toString();
      assertEquals("EUR 0", string0);
  }

  @Test(timeout = 4000)
  public void test227()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      RoundingMode roundingMode0 = RoundingMode.FLOOR;
      BigMoney bigMoney1 = bigMoney0.multiplyRetainScale1((-3109.98526811487), roundingMode0);
      assertTrue(bigMoney1.equals((Object)bigMoney0));
      assertNotSame(bigMoney1, bigMoney0);
  }

  @Test(timeout = 4000)
  public void test228()  throws Throwable  {
      CurrencyUnit currencyUnit0 = CurrencyUnit.AUD;
      BigMoney bigMoney0 = BigMoney.zero0(currencyUnit0);
      int int0 = bigMoney0.getAmountMajorInt();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test229()  throws Throwable  {
      BigMoneyProvider[] bigMoneyProviderArray0 = new BigMoneyProvider[1];
      CurrencyUnit currencyUnit0 = CurrencyUnit.USD;
      // Undeclared exception!
      try { 
        BigMoney.total2(currencyUnit0, bigMoneyProviderArray0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // BigMoneyProvider must not be null
         //
         verifyException("org.joda.money.MoneyUtils", e);
      }
  }
}
