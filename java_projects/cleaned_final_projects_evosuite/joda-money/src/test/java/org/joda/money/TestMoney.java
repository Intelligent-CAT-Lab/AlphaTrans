
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

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertSame;
import static org.junit.Assert.fail;

import com.tngtech.java.junit.dataprovider.DataProvider;
import com.tngtech.java.junit.dataprovider.DataProviderRunner;
import com.tngtech.java.junit.dataprovider.UseDataProvider;

import org.junit.Test;
import org.junit.runner.RunWith;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Modifier;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.Collections;

/** Test Money. */
@RunWith(DataProviderRunner.class)
public class TestMoney {

    private static final CurrencyUnit GBP = CurrencyUnit.of1("GBP");
    private static final CurrencyUnit EUR = CurrencyUnit.of1("EUR");
    private static final CurrencyUnit USD = CurrencyUnit.of1("USD");
    private static final CurrencyUnit JPY = CurrencyUnit.of1("JPY");
    private static final BigDecimal BIGDEC_2_3 = new BigDecimal("2.3");
    private static final BigDecimal BIGDEC_2_34 = new BigDecimal("2.34");
    private static final BigDecimal BIGDEC_2_345 = new BigDecimal("2.345");
    private static final BigDecimal BIGDEC_M5_78 = new BigDecimal("-5.78");

    private static final Money GBP_0_00 = Money.parse("GBP 0.00");
    private static final Money GBP_1_23 = Money.parse("GBP 1.23");
    private static final Money GBP_2_33 = Money.parse("GBP 2.33");
    private static final Money GBP_2_34 = Money.parse("GBP 2.34");
    private static final Money GBP_2_35 = Money.parse("GBP 2.35");
    private static final Money GBP_2_36 = Money.parse("GBP 2.36");
    private static final Money GBP_5_78 = Money.parse("GBP 5.78");
    private static final Money GBP_M1_23 = Money.parse("GBP -1.23");
    private static final Money GBP_M5_78 = Money.parse("GBP -5.78");
    private static final Money GBP_INT_MAX_PLUS1 =
            Money.ofMinor(GBP, ((long) Integer.MAX_VALUE) + 1);
    private static final Money GBP_INT_MIN_MINUS1 =
            Money.ofMinor(GBP, ((long) Integer.MIN_VALUE) - 1);
    private static final Money GBP_INT_MAX_MAJOR_PLUS1 =
            Money.ofMinor(GBP, (((long) Integer.MAX_VALUE) + 1) * 100);
    private static final Money GBP_INT_MIN_MAJOR_MINUS1 =
            Money.ofMinor(GBP, (((long) Integer.MIN_VALUE) - 1) * 100);
    private static final Money GBP_LONG_MAX_PLUS1 =
            Money.of0(GBP, BigDecimal.valueOf(Long.MAX_VALUE).add(BigDecimal.ONE));
    private static final Money GBP_LONG_MIN_MINUS1 =
            Money.of0(GBP, BigDecimal.valueOf(Long.MIN_VALUE).subtract(BigDecimal.ONE));
    private static final Money GBP_LONG_MAX_MAJOR_PLUS1 =
            Money.of0(
                    GBP,
                    BigDecimal.valueOf(Long.MAX_VALUE)
                            .add(BigDecimal.ONE)
                            .multiply(BigDecimal.valueOf(100)));
    private static final Money GBP_LONG_MIN_MAJOR_MINUS1 =
            Money.of0(
                    GBP,
                    BigDecimal.valueOf(Long.MIN_VALUE)
                            .subtract(BigDecimal.ONE)
                            .multiply(BigDecimal.valueOf(100)));
    private static final Money JPY_423 = Money.parse("JPY 423");
    private static final Money USD_1_23 = Money.parse("USD 1.23");
    private static final Money USD_2_34 = Money.parse("USD 2.34");
    private static final Money USD_2_35 = Money.parse("USD 2.35");

    @Test
    public void test_factory_of_Currency_BigDecimal() {
        Money test = Money.of0(GBP, BIGDEC_2_34);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(234, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test
    public void test_factory_of_Currency_BigDecimal_correctScale() {
        Money test = Money.of0(GBP, BIGDEC_2_3);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(230, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_BigDecimal_invalidScaleGBP() {
        Money.of0(GBP, BIGDEC_2_345);
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_BigDecimal_invalidScaleJPY() {
        Money.of0(JPY, BIGDEC_2_3);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_BigDecimal_nullCurrency() {
        Money.of0((CurrencyUnit) null, BIGDEC_2_34);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_BigDecimal_nullBigDecimal() {
        Money.of0(GBP, (BigDecimal) null);
    }

    @Test
    public void test_factory_of_Currency_BigDecimal_GBP_RoundingMode_DOWN() {
        Money test = Money.of1(GBP, BIGDEC_2_34, RoundingMode.DOWN);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(234, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test
    public void test_factory_of_Currency_BigDecimal_JPY_RoundingMode_DOWN() {
        Money test = Money.of1(JPY, BIGDEC_2_34, RoundingMode.DOWN);
        assertEquals(JPY, test.getCurrencyUnit());
        assertEquals(2, test.getAmountMinorInt());
        assertEquals(0, test.getAmount().scale());
    }

    @Test
    public void test_factory_of_Currency_BigDecimal_JPY_RoundingMode_UP() {
        Money test = Money.of1(JPY, BIGDEC_2_34, RoundingMode.UP);
        assertEquals(JPY, test.getCurrencyUnit());
        assertEquals(3, test.getAmountMinorInt());
        assertEquals(0, test.getAmount().scale());
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_BigDecimal_RoundingMode_UNNECESSARY() {
        Money.of1(JPY, BIGDEC_2_34, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_BigDecimal_RoundingMode_nullCurrency() {
        Money.of1((CurrencyUnit) null, BIGDEC_2_34, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_BigDecimal_RoundingMode_nullBigDecimal() {
        Money.of1(GBP, (BigDecimal) null, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_BigDecimal_RoundingMode_nullRoundingMode() {
        Money.of1(GBP, BIGDEC_2_34, (RoundingMode) null);
    }

    @Test
    public void test_factory_of_Currency_double() {
        Money test = Money.of2(GBP, 2.34d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(234, test.getAmountMinorInt());
        assertEquals(2, test.getScale());
    }

    @Test
    public void test_factory_of_Currency_double_correctScale() {
        Money test = Money.of2(GBP, 2.3d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(230, test.getAmountMinorInt());
        assertEquals(2, test.getScale());
    }

    @Test
    public void test_factory_of_Currency_double_trailingZero1() {
        Money test = Money.of2(GBP, 1.230d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(BigDecimal.valueOf(123L, 2), test.getAmount());
        assertEquals(2, test.getScale());
    }

    @Test
    public void test_factory_of_Currency_double_trailingZero2() {
        Money test = Money.of2(GBP, 1.20d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(BigDecimal.valueOf(120L, 2), test.getAmount());
        assertEquals(2, test.getScale());
    }

    @Test
    public void test_factory_of_Currency_double_medium() {
        Money test = Money.of2(GBP, 2000d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(BigDecimal.valueOf(200000L, 2), test.getAmount());
        assertEquals(2, test.getScale());
    }

    @Test
    public void test_factory_of_Currency_double_big() {
        Money test = Money.of2(GBP, 200000000d);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(BigDecimal.valueOf(20000000000L, 2), test.getAmount());
        assertEquals(2, test.getScale());
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_double_invalidScaleGBP() {
        Money.of2(GBP, 2.345d);
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_double_invalidScaleJPY() {
        Money.of2(JPY, 2.3d);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_double_nullCurrency() {
        Money.of0((CurrencyUnit) null, BIGDEC_2_34);
    }

    @Test
    public void test_factory_of_Currency_double_GBP_RoundingMode_DOWN() {
        Money test = Money.of3(GBP, 2.34d, RoundingMode.DOWN);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(234, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test
    public void test_factory_of_Currency_double_JPY_RoundingMode_DOWN() {
        Money test = Money.of3(JPY, 2.34d, RoundingMode.DOWN);
        assertEquals(JPY, test.getCurrencyUnit());
        assertEquals(2, test.getAmountMinorInt());
        assertEquals(0, test.getAmount().scale());
    }

    @Test
    public void test_factory_of_Currency_double_JPY_RoundingMode_UP() {
        Money test = Money.of3(JPY, 2.34d, RoundingMode.UP);
        assertEquals(JPY, test.getCurrencyUnit());
        assertEquals(3, test.getAmountMinorInt());
        assertEquals(0, test.getAmount().scale());
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_of_Currency_double_RoundingMode_UNNECESSARY() {
        Money.of3(JPY, 2.34d, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_double_RoundingMode_nullCurrency() {
        Money.of3((CurrencyUnit) null, 2.34d, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_of_Currency_double_RoundingMode_nullRoundingMode() {
        Money.of3(GBP, 2.34d, (RoundingMode) null);
    }

    @Test
    public void test_factory_ofMajor_Currency_long() {
        Money test = Money.ofMajor(GBP, 234);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(23400, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_ofMajor_Currency_long_nullCurrency() {
        Money.ofMajor((CurrencyUnit) null, 234);
    }

    @Test
    public void test_factory_ofMinor_Currency_long() {
        Money test = Money.ofMinor(GBP, 234);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(234, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_ofMinor_Currency_long_nullCurrency() {
        Money.ofMinor((CurrencyUnit) null, 234);
    }

    @Test
    public void test_factory_zero_Currency() {
        Money test = Money.zero(GBP);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(0, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_zero_Currency_nullCurrency() {
        Money.zero((CurrencyUnit) null);
    }

    @Test
    public void test_factory_from_BigMoneyProvider() {
        Money test = Money.of4(BigMoney.parse("GBP 104.23"));
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(10423, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test
    public void test_factory_from_BigMoneyProvider_fixScale() {
        Money test = Money.of4(BigMoney.parse("GBP 104.2"));
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(10420, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = ArithmeticException.class)
    public void test_factory_from_BigMoneyProvider_invalidCurrencyScale() {
        Money.of4(BigMoney.parse("GBP 104.235"));
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_from_BigMoneyProvider_nullBigMoneyProvider() {
        Money.of4((BigMoneyProvider) null);
    }

    @Test
    public void test_factory_from_BigMoneyProvider_RoundingMode() {
        Money test = Money.of5(BigMoney.parse("GBP 104.235"), RoundingMode.HALF_EVEN);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(10424, test.getAmountMinorInt());
        assertEquals(2, test.getAmount().scale());
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_from_BigMoneyProvider_RoundingMode_nullBigMoneyProvider() {
        Money.of5((BigMoneyProvider) null, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_from_BigMoneyProvider_RoundingMode_nullRoundingMode() {
        Money.of5(BigMoney.parse("GBP 104.235"), (RoundingMode) null);
    }

    @Test
    public void test_factory_total_varargs_1() {
        Money test = Money.total0(GBP_1_23);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(123, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_array_1() {
        Money[] array = new Money[] {GBP_1_23};
        Money test = Money.total0(array);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(123, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_varargs_3() {
        Money test = Money.total0(GBP_1_23, GBP_2_33, GBP_2_36);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_array_3() {
        Money[] array = new Money[] {GBP_1_23, GBP_2_33, GBP_2_36};
        Money test = Money.total0(array);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_factory_total_varargs_empty() {
        Money.total0();
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_factory_total_array_empty() {
        Money[] array = new Money[0];
        Money.total0(array);
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_varargs_currenciesDiffer() {
        try {
            Money.total0(GBP_2_33, JPY_423);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_array_currenciesDiffer() {
        try {
            Money[] array = new Money[] {GBP_2_33, JPY_423};
            Money.total0(array);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_varargs_nullFirst() {
        Money.total0((Money) null, GBP_2_33, GBP_2_36);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_array_nullFirst() {
        Money[] array = new Money[] {null, GBP_2_33, GBP_2_36};
        Money.total0(array);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_varargs_nullNotFirst() {
        Money.total0(GBP_2_33, null, GBP_2_36);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_array_nullNotFirst() {
        Money[] array = new Money[] {GBP_2_33, null, GBP_2_36};
        Money.total0(array);
    }

    @Test
    public void test_factory_total_Iterable() {
        Iterable<Money> iterable = Arrays.asList(GBP_1_23, GBP_2_33, GBP_2_36);
        Money test = Money.total1(iterable);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_factory_total_Iterable_empty() {
        Iterable<Money> iterable = Collections.emptyList();
        Money.total1(iterable);
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_Iterable_currenciesDiffer() {
        try {
            Iterable<Money> iterable = Arrays.asList(GBP_2_33, JPY_423);
            Money.total1(iterable);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_Iterable_nullFirst() {
        Iterable<Money> iterable = Arrays.asList(null, GBP_2_33, GBP_2_36);
        Money.total1(iterable);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_Iterable_nullNotFirst() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, null, GBP_2_36);
        Money.total1(iterable);
    }

    @Test
    public void test_factory_total_CurrencyUnitVarargs_1() {
        Money test = Money.total2(GBP, GBP_1_23);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(123, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitArray_1() {
        Money[] array = new Money[] {GBP_1_23};
        Money test = Money.total2(GBP, array);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(123, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitVarargs_3() {
        Money test = Money.total2(GBP, GBP_1_23, GBP_2_33, GBP_2_36);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitArray_3() {
        Money[] array = new Money[] {GBP_1_23, GBP_2_33, GBP_2_36};
        Money test = Money.total2(GBP, array);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitVarargs_empty() {
        Money test = Money.total2(GBP);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(0, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitArray_empty() {
        Money[] array = new Money[0];
        Money test = Money.total2(GBP, array);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(0, test.getAmountMinorInt());
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitVarargs_currenciesDiffer() {
        try {
            Money.total2(GBP, JPY_423);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitArray_currenciesDiffer() {
        try {
            Money[] array = new Money[] {JPY_423};
            Money.total2(GBP, array);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitVarargs_currenciesDifferInArray() {
        try {
            Money.total2(GBP, GBP_2_33, JPY_423);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitArray_currenciesDifferInArray() {
        try {
            Money[] array = new Money[] {GBP_2_33, JPY_423};
            Money.total2(GBP, array);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitVarargs_nullFirst() {
        Money.total2(GBP, null, GBP_2_33, GBP_2_36);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitArray_nullFirst() {
        Money[] array = new Money[] {null, GBP_2_33, GBP_2_36};
        Money.total2(GBP, array);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitVarargs_nullNotFirst() {
        Money.total2(GBP, GBP_2_33, null, GBP_2_36);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitArray_nullNotFirst() {
        Money[] array = new Money[] {GBP_2_33, null, GBP_2_36};
        Money.total2(GBP, array);
    }

    @Test
    public void test_factory_total_CurrencyUnitIterable() {
        Iterable<Money> iterable = Arrays.asList(GBP_1_23, GBP_2_33, GBP_2_36);
        Money test = Money.total3(GBP, iterable);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(592, test.getAmountMinorInt());
    }

    @Test
    public void test_factory_total_CurrencyUnitIterable_empty() {
        Iterable<Money> iterable = Collections.emptyList();
        Money test = Money.total3(GBP, iterable);
        assertEquals(GBP, test.getCurrencyUnit());
        assertEquals(0, test.getAmountMinorInt());
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitIterable_currenciesDiffer() {
        try {
            Iterable<Money> iterable = Arrays.asList(JPY_423);
            Money.total3(GBP, iterable);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_factory_total_CurrencyUnitIterable_currenciesDifferInIterable() {
        try {
            Iterable<Money> iterable = Arrays.asList(GBP_2_33, JPY_423);
            Money.total3(GBP, iterable);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitIterable_nullFirst() {
        Iterable<Money> iterable = Arrays.asList(null, GBP_2_33, GBP_2_36);
        Money.total3(GBP, iterable);
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_total_CurrencyUnitIterable_nullNotFirst() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, null, GBP_2_36);
        Money.total3(GBP, iterable);
    }

    @DataProvider
    public static Object[][] data_parse() {
        return new Object[][] {
            {"GBP 2.43", GBP, 243},
            {"GBP +12.57", GBP, 1257},
            {"GBP -5.87", GBP, -587},
            {"GBP 0.99", GBP, 99},
            {"GBP .99", GBP, 99},
            {"GBP +.99", GBP, 99},
            {"GBP +0.99", GBP, 99},
            {"GBP -.99", GBP, -99},
            {"GBP -0.99", GBP, -99},
            {"GBP 0", GBP, 0},
            {"GBP 2", GBP, 200},
            {"GBP 123.", GBP, 12300},
            {"GBP3", GBP, 300},
            {"GBP3.10", GBP, 310},
            {"GBP  3.10", GBP, 310},
            {"GBP   3.10", GBP, 310},
            {"GBP                           3.10", GBP, 310},
        };
    }

    @Test
    @UseDataProvider("data_parse")
    public void test_factory_parse(String str, CurrencyUnit currency, int amount) {
        Money test = Money.parse(str);
        assertEquals(currency, test.getCurrencyUnit());
        assertEquals(amount, test.getAmountMinorInt());
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_factory_parse_String_tooShort() {
        Money.parse("GBP ");
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_factory_parse_String_badCurrency() {
        Money.parse("GBX 2.34");
    }

    @Test(expected = NullPointerException.class)
    public void test_factory_parse_String_nullString() {
        Money.parse((String) null);
    }

    @Test
    public void test_constructor_null1() throws Exception {
        Constructor<Money> con = Money.class.getDeclaredConstructor(int.class, BigMoney.class);
        assertEquals(true, Modifier.isPublic(con.getModifiers()));
        assertEquals(false, Modifier.isProtected(con.getModifiers()));
        try {
            con.setAccessible(true);
            con.newInstance(new Object[] {0, null});
            fail();
        } catch (InvocationTargetException ex) {
            assertEquals(AssertionError.class, ex.getCause().getClass());
        }
    }

    @Test
    public void test_constructor_scale() throws Exception {
        Constructor<Money> con = Money.class.getDeclaredConstructor(int.class, BigMoney.class);
        try {
            con.setAccessible(true);
            con.newInstance(new Object[] {0, BigMoney.of0(GBP, BIGDEC_2_3)});
            fail();
        } catch (InvocationTargetException ex) {
            assertEquals(AssertionError.class, ex.getCause().getClass());
        }
    }

    @Test
    public void test_getCurrencyUnit_GBP() {
        assertEquals(GBP, GBP_2_34.getCurrencyUnit());
    }

    @Test
    public void test_getCurrencyUnit_EUR() {
        assertEquals(EUR, Money.parse("EUR -5.78").getCurrencyUnit());
    }

    @Test
    public void test_withCurrencyUnit_Currency() {
        Money test = GBP_2_34.withCurrencyUnit0(USD);
        assertEquals("USD 2.34", test.toString());
    }

    @Test
    public void test_withCurrencyUnit_Currency_same() {
        Money test = GBP_2_34.withCurrencyUnit0(GBP);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withCurrencyUnit_Currency_scaleProblem() {
        GBP_2_34.withCurrencyUnit0(JPY);
    }

    @Test(expected = NullPointerException.class)
    public void test_withCurrencyUnit_Currency_nullCurrency() {
        GBP_2_34.withCurrencyUnit0((CurrencyUnit) null);
    }

    @Test
    public void test_withCurrencyUnit_CurrencyRoundingMode_DOWN() {
        Money test = GBP_2_34.withCurrencyUnit1(JPY, RoundingMode.DOWN);
        assertEquals("JPY 2", test.toString());
    }

    @Test
    public void test_withCurrencyUnit_CurrencyRoundingMode_UP() {
        Money test = GBP_2_34.withCurrencyUnit1(JPY, RoundingMode.UP);
        assertEquals("JPY 3", test.toString());
    }

    @Test
    public void test_withCurrencyUnit_CurrencyRoundingMode_same() {
        Money test = GBP_2_34.withCurrencyUnit1(GBP, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withCurrencyUnit_CurrencyRoundingMode_UNECESSARY() {
        GBP_2_34.withCurrencyUnit1(JPY, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_withCurrencyUnit_CurrencyRoundingMode_nullCurrency() {
        GBP_2_34.withCurrencyUnit1((CurrencyUnit) null, RoundingMode.UNNECESSARY);
    }

    @Test
    public void test_getScale_GBP() {
        assertEquals(2, GBP_2_34.getScale());
    }

    @Test
    public void test_getScale_JPY() {
        assertEquals(0, JPY_423.getScale());
    }

    @Test
    public void test_getAmount_positive() {
        assertEquals(BIGDEC_2_34, GBP_2_34.getAmount());
    }

    @Test
    public void test_getAmount_negative() {
        assertEquals(BIGDEC_M5_78, GBP_M5_78.getAmount());
    }

    @Test
    public void test_getAmountMajor_positive() {
        assertEquals(BigDecimal.valueOf(2), GBP_2_34.getAmountMajor());
    }

    @Test
    public void test_getAmountMajor_negative() {
        assertEquals(BigDecimal.valueOf(-5), GBP_M5_78.getAmountMajor());
    }

    @Test
    public void test_getAmountMajorLong_positive() {
        assertEquals(2L, GBP_2_34.getAmountMajorLong());
    }

    @Test
    public void test_getAmountMajorLong_negative() {
        assertEquals(-5L, GBP_M5_78.getAmountMajorLong());
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMajorLong_tooBigPositive() {
        GBP_LONG_MAX_MAJOR_PLUS1.getAmountMajorLong();
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMajorLong_tooBigNegative() {
        GBP_LONG_MIN_MAJOR_MINUS1.getAmountMajorLong();
    }

    @Test
    public void test_getAmountMajorInt_positive() {
        assertEquals(2, GBP_2_34.getAmountMajorInt());
    }

    @Test
    public void test_getAmountMajorInt_negative() {
        assertEquals(-5, GBP_M5_78.getAmountMajorInt());
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMajorInt_tooBigPositive() {
        GBP_INT_MAX_MAJOR_PLUS1.getAmountMajorInt();
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMajorInt_tooBigNegative() {
        GBP_INT_MIN_MAJOR_MINUS1.getAmountMajorInt();
    }

    @Test
    public void test_getAmountMinor_positive() {
        assertEquals(BigDecimal.valueOf(234), GBP_2_34.getAmountMinor());
    }

    @Test
    public void test_getAmountMinor_negative() {
        assertEquals(BigDecimal.valueOf(-578), GBP_M5_78.getAmountMinor());
    }

    @Test
    public void test_getAmountMinorLong_positive() {
        assertEquals(234L, GBP_2_34.getAmountMinorLong());
    }

    @Test
    public void test_getAmountMinorLong_negative() {
        assertEquals(-578L, GBP_M5_78.getAmountMinorLong());
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMinorLong_tooBigPositive() {
        GBP_LONG_MAX_PLUS1.getAmountMinorLong();
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMinorLong_tooBigNegative() {
        GBP_LONG_MIN_MINUS1.getAmountMinorLong();
    }

    @Test
    public void test_getAmountMinorInt_positive() {
        assertEquals(234, GBP_2_34.getAmountMinorInt());
    }

    @Test
    public void test_getAmountMinorInt_negative() {
        assertEquals(-578, GBP_M5_78.getAmountMinorInt());
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMinorInt_tooBigPositive() {
        GBP_INT_MAX_PLUS1.getAmountMinorInt();
    }

    @Test(expected = ArithmeticException.class)
    public void test_getAmountMinorInt_tooBigNegative() {
        GBP_INT_MIN_MINUS1.getAmountMinorInt();
    }

    @Test
    public void test_getMinorPart_positive() {
        assertEquals(34, GBP_2_34.getMinorPart());
    }

    @Test
    public void test_getMinorPart_negative() {
        assertEquals(-78, GBP_M5_78.getMinorPart());
    }

    @Test
    public void test_isZero() {
        assertEquals(true, GBP_0_00.isZero());
        assertEquals(false, GBP_2_34.isZero());
        assertEquals(false, GBP_M5_78.isZero());
    }

    @Test
    public void test_isPositive() {
        assertEquals(false, GBP_0_00.isPositive());
        assertEquals(true, GBP_2_34.isPositive());
        assertEquals(false, GBP_M5_78.isPositive());
    }

    @Test
    public void test_isPositiveOrZero() {
        assertEquals(true, GBP_0_00.isPositiveOrZero());
        assertEquals(true, GBP_2_34.isPositiveOrZero());
        assertEquals(false, GBP_M5_78.isPositiveOrZero());
    }

    @Test
    public void test_isNegative() {
        assertEquals(false, GBP_0_00.isNegative());
        assertEquals(false, GBP_2_34.isNegative());
        assertEquals(true, GBP_M5_78.isNegative());
    }

    @Test
    public void test_isNegativeOrZero() {
        assertEquals(true, GBP_0_00.isNegativeOrZero());
        assertEquals(false, GBP_2_34.isNegativeOrZero());
        assertEquals(true, GBP_M5_78.isNegativeOrZero());
    }

    @Test
    public void test_withAmount_BigDecimal() {
        Money test = GBP_2_34.withAmount0(BIGDEC_M5_78);
        assertEquals("GBP -5.78", test.toString());
    }

    @Test
    public void test_withAmount_BigDecimal_same() {
        Money test = GBP_2_34.withAmount0(BIGDEC_2_34);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withAmount_BigDecimal_invalidScale() {
        GBP_2_34.withAmount0(new BigDecimal("2.345"));
    }

    @Test(expected = NullPointerException.class)
    public void test_withAmount_BigDecimal_nullBigDecimal() {
        GBP_2_34.withAmount0((BigDecimal) null);
    }

    @Test
    public void test_withAmount_BigDecimalRoundingMode() {
        Money test = GBP_2_34.withAmount1(BIGDEC_M5_78, RoundingMode.UNNECESSARY);
        assertEquals("GBP -5.78", test.toString());
    }

    @Test
    public void test_withAmount_BigDecimalRoundingMode_same() {
        Money test = GBP_2_34.withAmount1(BIGDEC_2_34, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_withAmount_BigDecimalRoundingMode_roundDown() {
        Money test = GBP_2_34.withAmount1(new BigDecimal("2.355"), RoundingMode.DOWN);
        assertEquals(GBP_2_35, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withAmount_BigDecimalRoundingMode_roundUnecessary() {
        GBP_2_34.withAmount1(new BigDecimal("2.345"), RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_withAmount_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_2_34.withAmount1((BigDecimal) null, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_withAmount_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_2_34.withAmount1(BIGDEC_2_34, (RoundingMode) null);
    }

    @Test
    public void test_withAmount_double() {
        Money test = GBP_2_34.withAmount2(-5.78d);
        assertEquals("GBP -5.78", test.toString());
    }

    @Test
    public void test_withAmount_double_same() {
        Money test = GBP_2_34.withAmount2(2.34d);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withAmount_double_invalidScale() {
        GBP_2_34.withAmount2(2.345d);
    }

    @Test
    public void test_withAmount_doubleRoundingMode() {
        Money test = GBP_2_34.withAmount3(-5.78d, RoundingMode.UNNECESSARY);
        assertEquals("GBP -5.78", test.toString());
    }

    @Test
    public void test_withAmount_doubleRoundingMode_same() {
        Money test = GBP_2_34.withAmount3(2.34d, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_withAmount_doubleRoundingMode_roundDown() {
        Money test = GBP_2_34.withAmount3(2.355d, RoundingMode.DOWN);
        assertEquals(GBP_2_35, test);
    }

    @Test(expected = ArithmeticException.class)
    public void test_withAmount_doubleRoundingMode_roundUnecessary() {
        GBP_2_34.withAmount3(2.345d, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_withAmount_doubleRoundingMode_nullRoundingMode() {
        GBP_2_34.withAmount1(BIGDEC_2_34, (RoundingMode) null);
    }

    @Test
    public void test_plus_Iterable() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, GBP_1_23);
        Money test = GBP_2_34.plus0(iterable);
        assertEquals("GBP 5.90", test.toString());
    }

    @Test
    public void test_plus_Iterable_zero() {
        Iterable<Money> iterable = Arrays.asList(GBP_0_00);
        Money test = GBP_2_34.plus0(iterable);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_plus_Iterable_currencyMismatch() {
        try {
            Iterable<Money> iterable = Arrays.asList(GBP_2_33, JPY_423);
            GBP_M5_78.plus0(iterable);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_Iterable_nullEntry() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, null);
        GBP_M5_78.plus0(iterable);
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_Iterable_nullIterable() {
        GBP_M5_78.plus0((Iterable<Money>) null);
    }

    @Test
    public void test_plus_Money_zero() {
        Money test = GBP_2_34.plus1(GBP_0_00);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plus_Money_positive() {
        Money test = GBP_2_34.plus1(GBP_1_23);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plus_Money_negative() {
        Money test = GBP_2_34.plus1(GBP_M1_23);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_plus_Money_currencyMismatch() {
        try {
            GBP_M5_78.plus1(USD_1_23);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(USD, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_Money_nullMoney() {
        GBP_M5_78.plus1((Money) null);
    }

    @Test
    public void test_plus_BigDecimal_zero() {
        Money test = GBP_2_34.plus2(BigDecimal.ZERO);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plus_BigDecimal_positive() {
        Money test = GBP_2_34.plus2(new BigDecimal("1.23"));
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plus_BigDecimal_negative() {
        Money test = GBP_2_34.plus2(new BigDecimal("-1.23"));
        assertEquals("GBP 1.11", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_plus_BigDecimal_invalidScale() {
        GBP_2_34.plus2(new BigDecimal("1.235"));
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_BigDecimal_nullBigDecimal() {
        GBP_M5_78.plus2((BigDecimal) null);
    }

    @Test
    public void test_plus_BigDecimalRoundingMode_zero() {
        Money test = GBP_2_34.plus3(BigDecimal.ZERO, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plus_BigDecimalRoundingMode_positive() {
        Money test = GBP_2_34.plus3(new BigDecimal("1.23"), RoundingMode.UNNECESSARY);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plus_BigDecimalRoundingMode_negative() {
        Money test = GBP_2_34.plus3(new BigDecimal("-1.23"), RoundingMode.UNNECESSARY);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_plus_BigDecimalRoundingMode_roundDown() {
        Money test = GBP_2_34.plus3(new BigDecimal("1.235"), RoundingMode.DOWN);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_plus_BigDecimalRoundingMode_roundUnecessary() {
        GBP_2_34.plus3(new BigDecimal("1.235"), RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_M5_78.plus3((BigDecimal) null, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_M5_78.plus3(BIGDEC_2_34, (RoundingMode) null);
    }

    @Test
    public void test_plus_double_zero() {
        Money test = GBP_2_34.plus4(0d);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plus_double_positive() {
        Money test = GBP_2_34.plus4(1.23d);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plus_double_negative() {
        Money test = GBP_2_34.plus4(-1.23d);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_plus_double_invalidScale() {
        GBP_2_34.plus4(1.235d);
    }

    @Test
    public void test_plus_doubleRoundingMode_zero() {
        Money test = GBP_2_34.plus5(0d, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plus_doubleRoundingMode_positive() {
        Money test = GBP_2_34.plus5(1.23d, RoundingMode.UNNECESSARY);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plus_doubleRoundingMode_negative() {
        Money test = GBP_2_34.plus5(-1.23d, RoundingMode.UNNECESSARY);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_plus_doubleRoundingMode_roundDown() {
        Money test = GBP_2_34.plus5(1.235d, RoundingMode.DOWN);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_plus_doubleRoundingMode_roundUnecessary() {
        GBP_2_34.plus5(1.235d, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_plus_doubleRoundingMode_nullRoundingMode() {
        GBP_M5_78.plus5(2.34d, (RoundingMode) null);
    }

    @Test
    public void test_plusMajor_zero() {
        Money test = GBP_2_34.plusMajor(0);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plusMajor_positive() {
        Money test = GBP_2_34.plusMajor(123);
        assertEquals("GBP 125.34", test.toString());
    }

    @Test
    public void test_plusMajor_negative() {
        Money test = GBP_2_34.plusMajor(-123);
        assertEquals("GBP -120.66", test.toString());
    }

    @Test
    public void test_plusMinor_zero() {
        Money test = GBP_2_34.plusMinor(0);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_plusMinor_positive() {
        Money test = GBP_2_34.plusMinor(123);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_plusMinor_negative() {
        Money test = GBP_2_34.plusMinor(-123);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_Iterable() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, GBP_1_23);
        Money test = GBP_2_34.minus0(iterable);
        assertEquals("GBP -1.22", test.toString());
    }

    @Test
    public void test_minus_Iterable_zero() {
        Iterable<Money> iterable = Arrays.asList(GBP_0_00);
        Money test = GBP_2_34.minus0(iterable);
        assertSame(GBP_2_34, test);
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_minus_Iterable_currencyMismatch() {
        try {
            Iterable<Money> iterable = Arrays.asList(GBP_2_33, JPY_423);
            GBP_M5_78.minus0(iterable);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(JPY, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_Iterable_nullEntry() {
        Iterable<Money> iterable = Arrays.asList(GBP_2_33, null);
        GBP_M5_78.minus0(iterable);
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_Iterable_nullIterable() {
        GBP_M5_78.minus0((Iterable<Money>) null);
    }

    @Test
    public void test_minus_Money_zero() {
        Money test = GBP_2_34.minus1(GBP_0_00);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minus_Money_positive() {
        Money test = GBP_2_34.minus1(GBP_1_23);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_Money_negative() {
        Money test = GBP_2_34.minus1(GBP_M1_23);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_minus_Money_currencyMismatch() {
        try {
            GBP_M5_78.minus1(USD_1_23);
        } catch (CurrencyMismatchException ex) {
            assertEquals(GBP, ex.getFirstCurrency());
            assertEquals(USD, ex.getSecondCurrency());
            throw ex;
        }
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_Money_nullMoney() {
        GBP_M5_78.minus1((Money) null);
    }

    @Test
    public void test_minus_BigDecimal_zero() {
        Money test = GBP_2_34.minus2(BigDecimal.ZERO);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minus_BigDecimal_positive() {
        Money test = GBP_2_34.minus2(new BigDecimal("1.23"));
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_BigDecimal_negative() {
        Money test = GBP_2_34.minus2(new BigDecimal("-1.23"));
        assertEquals("GBP 3.57", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_minus_BigDecimal_invalidScale() {
        GBP_2_34.minus2(new BigDecimal("1.235"));
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_BigDecimal_nullBigDecimal() {
        GBP_M5_78.minus2((BigDecimal) null);
    }

    @Test
    public void test_minus_BigDecimalRoundingMode_zero() {
        Money test = GBP_2_34.minus3(BigDecimal.ZERO, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minus_BigDecimalRoundingMode_positive() {
        Money test = GBP_2_34.minus3(new BigDecimal("1.23"), RoundingMode.UNNECESSARY);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_BigDecimalRoundingMode_negative() {
        Money test = GBP_2_34.minus3(new BigDecimal("-1.23"), RoundingMode.UNNECESSARY);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_minus_BigDecimalRoundingMode_roundDown() {
        Money test = GBP_2_34.minus3(new BigDecimal("1.235"), RoundingMode.DOWN);
        assertEquals("GBP 1.10", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_minus_BigDecimalRoundingMode_roundUnecessary() {
        GBP_2_34.minus3(new BigDecimal("1.235"), RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_M5_78.minus3((BigDecimal) null, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_M5_78.minus3(BIGDEC_2_34, (RoundingMode) null);
    }

    @Test
    public void test_minus_double_zero() {
        Money test = GBP_2_34.minus4(0d);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minus_double_positive() {
        Money test = GBP_2_34.minus4(1.23d);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_double_negative() {
        Money test = GBP_2_34.minus4(-1.23d);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_minus_double_invalidScale() {
        GBP_2_34.minus4(1.235d);
    }

    @Test
    public void test_minus_doubleRoundingMode_zero() {
        Money test = GBP_2_34.minus5(0d, RoundingMode.UNNECESSARY);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minus_doubleRoundingMode_positive() {
        Money test = GBP_2_34.minus5(1.23d, RoundingMode.UNNECESSARY);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minus_doubleRoundingMode_negative() {
        Money test = GBP_2_34.minus5(-1.23d, RoundingMode.UNNECESSARY);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_minus_doubleRoundingMode_roundDown() {
        Money test = GBP_2_34.minus5(1.235d, RoundingMode.DOWN);
        assertEquals("GBP 1.10", test.toString());
    }

    @Test(expected = ArithmeticException.class)
    public void test_minus_doubleRoundingMode_roundUnecessary() {
        GBP_2_34.minus5(1.235d, RoundingMode.UNNECESSARY);
    }

    @Test(expected = NullPointerException.class)
    public void test_minus_doubleRoundingMode_nullRoundingMode() {
        GBP_M5_78.minus5(2.34d, (RoundingMode) null);
    }

    @Test
    public void test_minusMajor_zero() {
        Money test = GBP_2_34.minusMajor(0);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minusMajor_positive() {
        Money test = GBP_2_34.minusMajor(123);
        assertEquals("GBP -120.66", test.toString());
    }

    @Test
    public void test_minusMajor_negative() {
        Money test = GBP_2_34.minusMajor(-123);
        assertEquals("GBP 125.34", test.toString());
    }

    @Test
    public void test_minusMinor_zero() {
        Money test = GBP_2_34.minusMinor(0);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_minusMinor_positive() {
        Money test = GBP_2_34.minusMinor(123);
        assertEquals("GBP 1.11", test.toString());
    }

    @Test
    public void test_minusMinor_negative() {
        Money test = GBP_2_34.minusMinor(-123);
        assertEquals("GBP 3.57", test.toString());
    }

    @Test
    public void test_multipliedBy_BigDecimalRoundingMode_one() {
        Money test = GBP_2_34.multipliedBy0(BigDecimal.ONE, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_multipliedBy_BigDecimalRoundingMode_positive() {
        Money test = GBP_2_33.multipliedBy0(new BigDecimal("2.5"), RoundingMode.DOWN);
        assertEquals("GBP 5.82", test.toString());
    }

    @Test
    public void test_multipliedBy_BigDecimalRoundingMode_positive_halfUp() {
        Money test = GBP_2_33.multipliedBy0(new BigDecimal("2.5"), RoundingMode.HALF_UP);
        assertEquals("GBP 5.83", test.toString());
    }

    @Test
    public void test_multipliedBy_BigDecimalRoundingMode_negative() {
        Money test = GBP_2_33.multipliedBy0(new BigDecimal("-2.5"), RoundingMode.FLOOR);
        assertEquals("GBP -5.83", test.toString());
    }

    @Test(expected = NullPointerException.class)
    public void test_multipliedBy_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_5_78.multipliedBy0((BigDecimal) null, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_multipliedBy_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_5_78.multipliedBy0(new BigDecimal("2.5"), (RoundingMode) null);
    }

    @Test
    public void test_multipliedBy_doubleRoundingMode_one() {
        Money test = GBP_2_34.multipliedBy1(1d, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_multipliedBy_doubleRoundingMode_positive() {
        Money test = GBP_2_33.multipliedBy1(2.5d, RoundingMode.DOWN);
        assertEquals("GBP 5.82", test.toString());
    }

    @Test
    public void test_multipliedBy_doubleRoundingMode_positive_halfUp() {
        Money test = GBP_2_33.multipliedBy1(2.5d, RoundingMode.HALF_UP);
        assertEquals("GBP 5.83", test.toString());
    }

    @Test
    public void test_multipliedBy_doubleRoundingMode_negative() {
        Money test = GBP_2_33.multipliedBy1(-2.5d, RoundingMode.FLOOR);
        assertEquals("GBP -5.83", test.toString());
    }

    @Test(expected = NullPointerException.class)
    public void test_multipliedBy_doubleRoundingMode_nullRoundingMode() {
        GBP_5_78.multipliedBy1(2.5d, (RoundingMode) null);
    }

    @Test
    public void test_multipliedBy_long_one() {
        Money test = GBP_2_34.multipliedBy2(1);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_multipliedBy_long_positive() {
        Money test = GBP_2_34.multipliedBy2(3);
        assertEquals("GBP 7.02", test.toString());
    }

    @Test
    public void test_multipliedBy_long_negative() {
        Money test = GBP_2_34.multipliedBy2(-3);
        assertEquals("GBP -7.02", test.toString());
    }

    @Test
    public void test_dividedBy_BigDecimalRoundingMode_one() {
        Money test = GBP_2_34.dividedBy0(BigDecimal.ONE, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_dividedBy_BigDecimalRoundingMode_positive() {
        Money test = GBP_2_34.dividedBy0(new BigDecimal("2.5"), RoundingMode.DOWN);
        assertEquals("GBP 0.93", test.toString());
    }

    @Test
    public void test_dividedBy_BigDecimalRoundingMode_positive_halfUp() {
        Money test = GBP_2_34.dividedBy0(new BigDecimal("2.5"), RoundingMode.HALF_UP);
        assertEquals("GBP 0.94", test.toString());
    }

    @Test
    public void test_dividedBy_BigDecimalRoundingMode_negative() {
        Money test = GBP_2_34.dividedBy0(new BigDecimal("-2.5"), RoundingMode.FLOOR);
        assertEquals("GBP -0.94", test.toString());
    }

    @Test(expected = NullPointerException.class)
    public void test_dividedBy_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_5_78.dividedBy0((BigDecimal) null, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_dividedBy_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_5_78.dividedBy0(new BigDecimal("2.5"), (RoundingMode) null);
    }

    @Test
    public void test_dividedBy_doubleRoundingMode_one() {
        Money test = GBP_2_34.dividedBy1(1d, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_dividedBy_doubleRoundingMode_positive() {
        Money test = GBP_2_34.dividedBy1(2.5d, RoundingMode.DOWN);
        assertEquals("GBP 0.93", test.toString());
    }

    @Test
    public void test_dividedBy_doubleRoundingMode_positive_halfUp() {
        Money test = GBP_2_34.dividedBy1(2.5d, RoundingMode.HALF_UP);
        assertEquals("GBP 0.94", test.toString());
    }

    @Test
    public void test_dividedBy_doubleRoundingMode_negative() {
        Money test = GBP_2_34.dividedBy1(-2.5d, RoundingMode.FLOOR);
        assertEquals("GBP -0.94", test.toString());
    }

    @Test(expected = NullPointerException.class)
    public void test_dividedBy_doubleRoundingMode_nullRoundingMode() {
        GBP_5_78.dividedBy1(2.5d, (RoundingMode) null);
    }

    @Test
    public void test_dividedBy_long_one() {
        Money test = GBP_2_34.dividedBy2(1, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_dividedBy_long_positive() {
        Money test = GBP_2_34.dividedBy2(3, RoundingMode.DOWN);
        assertEquals("GBP 0.78", test.toString());
    }

    @Test
    public void test_dividedBy_long_positive_roundDown() {
        Money test = GBP_2_35.dividedBy2(3, RoundingMode.DOWN);
        assertEquals("GBP 0.78", test.toString());
    }

    @Test
    public void test_dividedBy_long_positive_roundUp() {
        Money test = GBP_2_35.dividedBy2(3, RoundingMode.UP);
        assertEquals("GBP 0.79", test.toString());
    }

    @Test
    public void test_dividedBy_long_negative() {
        Money test = GBP_2_34.dividedBy2(-3, RoundingMode.DOWN);
        assertEquals("GBP -0.78", test.toString());
    }

    @Test
    public void test_negated_positive() {
        Money test = GBP_2_34.negated();
        assertEquals("GBP -2.34", test.toString());
    }

    @Test
    public void test_negated_negative() {
        Money test = Money.parse("GBP -2.34").negated();
        assertEquals("GBP 2.34", test.toString());
    }

    @Test
    public void test_abs_positive() {
        Money test = GBP_2_34.abs();
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_abs_negative() {
        Money test = Money.parse("GBP -2.34").abs();
        assertEquals("GBP 2.34", test.toString());
    }

    @Test
    public void test_round_2down() {
        Money test = GBP_2_34.rounded(2, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_round_2up() {
        Money test = GBP_2_34.rounded(2, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_round_1down() {
        Money test = GBP_2_34.rounded(1, RoundingMode.DOWN);
        assertEquals("GBP 2.30", test.toString());
    }

    @Test
    public void test_round_1up() {
        Money test = GBP_2_34.rounded(1, RoundingMode.UP);
        assertEquals("GBP 2.40", test.toString());
    }

    @Test
    public void test_round_0down() {
        Money test = GBP_2_34.rounded(0, RoundingMode.DOWN);
        assertEquals("GBP 2.00", test.toString());
    }

    @Test
    public void test_round_0up() {
        Money test = GBP_2_34.rounded(0, RoundingMode.UP);
        assertEquals("GBP 3.00", test.toString());
    }

    @Test
    public void test_round_M1down() {
        Money test = Money.parse("GBP 432.34").rounded(-1, RoundingMode.DOWN);
        assertEquals("GBP 430.00", test.toString());
    }

    @Test
    public void test_round_M1up() {
        Money test = Money.parse("GBP 432.34").rounded(-1, RoundingMode.UP);
        assertEquals("GBP 440.00", test.toString());
    }

    @Test
    public void test_round_3() {
        Money test = GBP_2_34.rounded(3, RoundingMode.DOWN);
        assertSame(GBP_2_34, test);
    }

    @Test
    public void test_convertedTo_BigDecimalRoundingMode_positive() {
        Money test = GBP_2_33.convertedTo(EUR, new BigDecimal("2.5"), RoundingMode.DOWN);
        assertEquals("EUR 5.82", test.toString());
    }

    @Test
    public void test_convertedTo_BigDecimalRoundingMode_positive_halfUp() {
        Money test = GBP_2_33.convertedTo(EUR, new BigDecimal("2.5"), RoundingMode.HALF_UP);
        assertEquals("EUR 5.83", test.toString());
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_convertedTo_BigDecimalRoundingMode_negative() {
        GBP_2_33.convertedTo(EUR, new BigDecimal("-2.5"), RoundingMode.FLOOR);
    }

    @Test(expected = IllegalArgumentException.class)
    public void test_convertedTo_BigDecimalRoundingMode_sameCurrency() {
        GBP_2_33.convertedTo(GBP, new BigDecimal("2.5"), RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_convertedTo_BigDecimalRoundingMode_nullCurrency() {
        GBP_5_78.convertedTo((CurrencyUnit) null, new BigDecimal("2"), RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_convertedTo_BigDecimalRoundingMode_nullBigDecimal() {
        GBP_5_78.convertedTo(EUR, (BigDecimal) null, RoundingMode.DOWN);
    }

    @Test(expected = NullPointerException.class)
    public void test_convertedTo_BigDecimalRoundingMode_nullRoundingMode() {
        GBP_5_78.convertedTo(EUR, new BigDecimal("2.5"), (RoundingMode) null);
    }

    @Test
    public void test_toBigMoney() {
        assertEquals(BigMoney.ofMinor(GBP, 234), GBP_2_34.toBigMoney());
    }

    @Test
    public void test_isSameCurrency_Money_same() {
        assertEquals(true, GBP_2_34.isSameCurrency(GBP_2_35));
    }

    @Test
    public void test_isSameCurrency_Money_different() {
        assertEquals(false, GBP_2_34.isSameCurrency(USD_2_34));
    }

    @Test
    public void test_isSameCurrency_BigMoney_same() {
        assertEquals(true, GBP_2_34.isSameCurrency(BigMoney.parse("GBP 2")));
    }

    @Test
    public void test_isSameCurrency_BigMoney_different() {
        assertEquals(false, GBP_2_34.isSameCurrency(BigMoney.parse("USD 2")));
    }

    @Test(expected = NullPointerException.class)
    public void test_isSameCurrency_Money_nullMoney() {
        GBP_2_34.isSameCurrency((Money) null);
    }

    @Test
    public void test_compareTo_Money() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(0, a.compareTo(a));
        assertEquals(0, b.compareTo(b));
        assertEquals(0, c.compareTo(c));

        assertEquals(-1, a.compareTo(b));
        assertEquals(1, b.compareTo(a));

        assertEquals(-1, a.compareTo(c));
        assertEquals(1, c.compareTo(a));

        assertEquals(-1, b.compareTo(c));
        assertEquals(1, c.compareTo(b));
    }

    @Test
    public void test_compareTo_BigMoney() {
        Money t = GBP_2_35;
        BigMoney a = BigMoney.ofMinor(GBP, 234);
        BigMoney b = BigMoney.ofMinor(GBP, 235);
        BigMoney c = BigMoney.ofMinor(GBP, 236);
        assertEquals(1, t.compareTo(a));
        assertEquals(0, t.compareTo(b));
        assertEquals(-1, t.compareTo(c));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_compareTo_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.compareTo(b);
    }

    @Test(expected = ClassCastException.class)
    @SuppressWarnings({"unchecked", "rawtypes"})
    public void test_compareTo_wrongType() {
        Comparable a = GBP_2_34;
        a.compareTo("NotRightType");
    }

    @Test
    public void test_isEqual() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(true, a.isEqual(a));
        assertEquals(true, b.isEqual(b));
        assertEquals(true, c.isEqual(c));

        assertEquals(false, a.isEqual(b));
        assertEquals(false, b.isEqual(a));

        assertEquals(false, a.isEqual(c));
        assertEquals(false, c.isEqual(a));

        assertEquals(false, b.isEqual(c));
        assertEquals(false, c.isEqual(b));
    }

    @Test
    public void test_isEqual_Money() {
        Money a = GBP_2_34;
        BigMoney b = BigMoney.ofMinor(GBP, 234);
        assertEquals(true, a.isEqual(b));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_isEqual_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.isEqual(b);
    }

    @Test
    public void test_isGreaterThan() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(false, a.isGreaterThan(a));
        assertEquals(false, a.isGreaterThan(b));
        assertEquals(false, a.isGreaterThan(c));

        assertEquals(true, b.isGreaterThan(a));
        assertEquals(false, b.isGreaterThan(b));
        assertEquals(false, b.isGreaterThan(c));

        assertEquals(true, c.isGreaterThan(a));
        assertEquals(true, c.isGreaterThan(b));
        assertEquals(false, c.isGreaterThan(c));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_isGreaterThan_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.isGreaterThan(b);
    }

    @Test
    public void test_isGreaterThanOrEqual() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(true, a.isGreaterThanOrEqual(a));
        assertEquals(false, a.isGreaterThanOrEqual(b));
        assertEquals(false, a.isGreaterThanOrEqual(c));

        assertEquals(true, b.isGreaterThanOrEqual(a));
        assertEquals(true, b.isGreaterThanOrEqual(b));
        assertEquals(false, b.isGreaterThanOrEqual(c));

        assertEquals(true, c.isGreaterThanOrEqual(a));
        assertEquals(true, c.isGreaterThanOrEqual(b));
        assertEquals(true, c.isGreaterThanOrEqual(c));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_isGreaterThanOrEqual_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.isGreaterThanOrEqual(b);
    }

    @Test
    public void test_isLessThan() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(false, a.isLessThan(a));
        assertEquals(true, a.isLessThan(b));
        assertEquals(true, a.isLessThan(c));

        assertEquals(false, b.isLessThan(a));
        assertEquals(false, b.isLessThan(b));
        assertEquals(true, b.isLessThan(c));

        assertEquals(false, c.isLessThan(a));
        assertEquals(false, c.isLessThan(b));
        assertEquals(false, c.isLessThan(c));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_isLessThan_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.isLessThan(b);
    }

    @Test
    public void test_isLessThanOrEqual() {
        Money a = GBP_2_34;
        Money b = GBP_2_35;
        Money c = GBP_2_36;
        assertEquals(true, a.isLessThanOrEqual(a));
        assertEquals(true, a.isLessThanOrEqual(b));
        assertEquals(true, a.isLessThanOrEqual(c));

        assertEquals(false, b.isLessThanOrEqual(a));
        assertEquals(true, b.isLessThanOrEqual(b));
        assertEquals(true, b.isLessThanOrEqual(c));

        assertEquals(false, c.isLessThanOrEqual(a));
        assertEquals(false, c.isLessThanOrEqual(b));
        assertEquals(true, c.isLessThanOrEqual(c));
    }

    @Test(expected = CurrencyMismatchException.class)
    public void test_isLessThanOrEqual_currenciesDiffer() {
        Money a = GBP_2_34;
        Money b = USD_2_35;
        a.isLessThanOrEqual(b);
    }

    @Test
    public void test_equals_hashCode_positive() {
        Money a = GBP_2_34;
        Money b = GBP_2_34;
        Money c = GBP_2_35;
        assertEquals(true, a.equals(a));
        assertEquals(true, b.equals(b));
        assertEquals(true, c.equals(c));

        assertEquals(true, a.equals(b));
        assertEquals(true, b.equals(a));
        assertEquals(true, a.hashCode() == b.hashCode());

        assertEquals(false, a.equals(c));
        assertEquals(false, b.equals(c));
    }

    @Test
    public void test_equals_false() {
        Money a = GBP_2_34;
        assertEquals(false, a.equals(null));
        assertEquals(false, a.equals(new Object()));
    }

    @Test
    public void test_toString_positive() {
        Money test = Money.of0(GBP, BIGDEC_2_34);
        assertEquals("GBP 2.34", test.toString());
    }

    @Test
    public void test_toString_negative() {
        Money test = Money.of0(EUR, BIGDEC_M5_78);
        assertEquals("EUR -5.78", test.toString());
    }
}
