package org.joda.money;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;

import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;
import org.joda.money.IntegrationUtils;
import java.io.Serializable;
import java.io.InvalidObjectException;
import java.io.ObjectInputStream;
import java.util.Iterator;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.Arrays;
import java.util.regex.Pattern;
import org.joda.convert.FromString;
import org.joda.convert.ToString;
public final class BigMoney {
    private static final Pattern PARSE_REGEX = Pattern.compile("[+-]?[0-9]*[.]?[0-9]*");
    private static final long serialVersionUID = 1L;
    private static Value clz = ContextInitializer.getPythonClass("/BigMoney.py", "BigMoney");
    private Value obj;
    public BigMoney(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// return new StringBuilder()
// .append(currency.getCode())
// .append(' ')
// .append(amount.toPlainString())
// .toString();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("toString").as(String.class);
}
    public int hashCode() {
// 
// return currency.hashCode() ^ amount.hashCode();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("hashCode").as(int.class);
}
    public boolean equals(Object other) {
// 
// if (this == other) {
// return true;
// }
// if (other instanceof BigMoney) {
// BigMoney otherMoney = (BigMoney) other;
// return currency.equals(otherMoney.getCurrencyUnit())
// && amount.equals(otherMoney.amount);
// }
// return false;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("equals", other).as(boolean.class);
}
    public int compareTo(BigMoneyProvider other) {
// 
// BigMoney otherMoney = of2(other);
// if (currency.equals(otherMoney.currency) == false) {
// throw new CurrencyMismatchException(getCurrencyUnit(), otherMoney.getCurrencyUnit());
// }
// return amount.compareTo(otherMoney.amount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("compareTo", other).as(int.class);
}
    public BigMoney toBigMoney() {
// 
// return this;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("toBigMoney").as(BigMoney.class);
}
    public BigMoney(int constructorId, BigDecimal amount, CurrencyUnit currency) {
// 
// if (constructorId == 0) {
// 
// assert currency != null : "Joda-Money bug: Currency must not be null";
// assert amount != null : "Joda-Money bug: Amount must not be null";
// this.currency = currency;
// this.amount = (amount.scale() < 0 ? amount.setScale(0) : amount);
// } else {
// 
// this.currency = null;
// this.amount = null;
// }
// 

this.obj = clz.invokeMember("__init__", constructorId, amount, currency);
}
    public static BigMoney parse(String moneyStr) {
// 
// MoneyUtils.checkNotNull(moneyStr, "Money must not be null");
// if (moneyStr.length() < 4) {
// throw new IllegalArgumentException("Money '" + moneyStr + "' cannot be parsed");
// }
// String currStr = moneyStr.substring(0, 3);
// int amountStart = 3;
// while (amountStart < moneyStr.length() && moneyStr.charAt(amountStart) == ' ') {
// amountStart++;
// }
// String amountStr = moneyStr.substring(amountStart);
// if (PARSE_REGEX.matcher(amountStr).matches() == false) {
// throw new IllegalArgumentException("Money amount '" + moneyStr + "' cannot be parsed");
// }
// return BigMoney.of0(CurrencyUnit.of1(currStr), new BigDecimal(amountStr));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("parse", moneyStr).as(BigMoney.class);
}
    public boolean isLessThanOrEqual(BigMoneyProvider other) {
// 
// return compareTo(other) <= 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isLessThanOrEqual", other).as(boolean.class);
}
    public boolean isLessThan(BigMoneyProvider other) {
// 
// return compareTo(other) < 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isLessThan", other).as(boolean.class);
}
    public boolean isGreaterThanOrEqual(BigMoneyProvider other) {
// 
// return compareTo(other) >= 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isGreaterThanOrEqual", other).as(boolean.class);
}
    public boolean isGreaterThan(BigMoneyProvider other) {
// 
// return compareTo(other) > 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isGreaterThan", other).as(boolean.class);
}
    public boolean isEqual(BigMoneyProvider other) {
// 
// return compareTo(other) == 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isEqual", other).as(boolean.class);
}
    public boolean isSameCurrency(BigMoneyProvider money) {
// 
// return (currency.equals(of2(money).getCurrencyUnit()));
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isSameCurrency", money).as(boolean.class);
}
    public Money toMoney1(RoundingMode roundingMode) {
// 
// return Money.of5(this, roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("toMoney1", roundingMode).as(Money.class);
}
    public Money toMoney0() {
// 
// return Money.of4(this);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("toMoney0").as(Money.class);
}
    public BigMoney convertRetainScale(
            CurrencyUnit currency, BigDecimal conversionMultipler, RoundingMode roundingMode) {
// 
// return convertedTo(currency, conversionMultipler).withScale1(getScale(), roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("convertRetainScale", currency, conversionMultipler, roundingMode).as(BigMoney.class);
}
    public BigMoney convertedTo(CurrencyUnit currency, BigDecimal conversionMultipler) {
// 
// MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
// MoneyUtils.checkNotNull(conversionMultipler, "Multiplier must not be null");
// if (this.currency == currency) {
// if (conversionMultipler.compareTo(BigDecimal.ONE) == 0) {
// return this;
// }
// throw new IllegalArgumentException("Cannot convert to the same currency");
// }
// if (conversionMultipler.compareTo(BigDecimal.ZERO) < 0) {
// throw new IllegalArgumentException(
// "Cannot convert using a negative conversion multiplier");
// }
// BigDecimal newAmount = amount.multiply(conversionMultipler);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("convertedTo", currency, conversionMultipler).as(BigMoney.class);
}
    public BigMoney rounded(int scale, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// if (scale >= getScale()) {
// return this;
// }
// int currentScale = amount.scale();
// BigDecimal newAmount = amount.setScale(scale, roundingMode).setScale(currentScale);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("rounded", scale, roundingMode).as(BigMoney.class);
}
    public BigMoney abs() {
// 
// return (isNegative() ? negated() : this);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("abs").as(BigMoney.class);
}
    public BigMoney negated() {
// 
// if (isZero()) {
// return this;
// }
// return BigMoney.of0(currency, amount.negate());
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("negated").as(BigMoney.class);
}
    public BigMoney dividedBy2(long valueToDivideBy, RoundingMode roundingMode) {
// 
// if (valueToDivideBy == 1) {
// return this;
// }
// BigDecimal newAmount = amount.divide(BigDecimal.valueOf(valueToDivideBy), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("dividedBy2", valueToDivideBy, roundingMode).as(BigMoney.class);
}
    public BigMoney dividedBy1(double valueToDivideBy, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// if (valueToDivideBy == 1) {
// return this;
// }
// BigDecimal newAmount = amount.divide(BigDecimal.valueOf(valueToDivideBy), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("dividedBy1", valueToDivideBy, roundingMode).as(BigMoney.class);
}
    public BigMoney dividedBy0(BigDecimal valueToDivideBy, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(valueToDivideBy, "Divisor must not be null");
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// if (valueToDivideBy.compareTo(BigDecimal.ONE) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.divide(valueToDivideBy, roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("dividedBy0", valueToDivideBy, roundingMode).as(BigMoney.class);
}
    public BigMoney multiplyRetainScale1(double valueToMultiplyBy, RoundingMode roundingMode) {
// 
// return multiplyRetainScale0(BigDecimal.valueOf(valueToMultiplyBy), roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("multiplyRetainScale1", valueToMultiplyBy, roundingMode).as(BigMoney.class);
}
    public BigMoney multiplyRetainScale0(BigDecimal valueToMultiplyBy, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(valueToMultiplyBy, "Multiplier must not be null");
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// if (valueToMultiplyBy.compareTo(BigDecimal.ONE) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.multiply(valueToMultiplyBy);
// newAmount = newAmount.setScale(getScale(), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("multiplyRetainScale0", valueToMultiplyBy, roundingMode).as(BigMoney.class);
}
    public BigMoney multipliedBy2(long valueToMultiplyBy) {
// 
// if (valueToMultiplyBy == 1) {
// return this;
// }
// BigDecimal newAmount = amount.multiply(BigDecimal.valueOf(valueToMultiplyBy));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("multipliedBy2", valueToMultiplyBy).as(BigMoney.class);
}
    public BigMoney multipliedBy1(double valueToMultiplyBy) {
// 
// if (valueToMultiplyBy == 1) {
// return this;
// }
// BigDecimal newAmount = amount.multiply(BigDecimal.valueOf(valueToMultiplyBy));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("multipliedBy1", valueToMultiplyBy).as(BigMoney.class);
}
    public BigMoney multipliedBy0(BigDecimal valueToMultiplyBy) {
// 
// MoneyUtils.checkNotNull(valueToMultiplyBy, "Multiplier must not be null");
// if (valueToMultiplyBy.compareTo(BigDecimal.ONE) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.multiply(valueToMultiplyBy);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("multipliedBy0", valueToMultiplyBy).as(BigMoney.class);
}
    public BigMoney minusRetainScale2(double amountToSubtract, RoundingMode roundingMode) {
// 
// if (amountToSubtract == 0) {
// return this;
// }
// BigDecimal newAmount = amount.subtract(BigDecimal.valueOf(amountToSubtract));
// newAmount = newAmount.setScale(getScale(), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minusRetainScale2", amountToSubtract, roundingMode).as(BigMoney.class);
}
    public BigMoney minusRetainScale1(BigDecimal amountToSubtract, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(amountToSubtract, "Amount must not be null");
// if (amountToSubtract.compareTo(BigDecimal.ZERO) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.subtract(amountToSubtract);
// newAmount = newAmount.setScale(getScale(), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minusRetainScale1", amountToSubtract, roundingMode).as(BigMoney.class);
}
    public BigMoney minusRetainScale0(BigMoneyProvider moneyToSubtract, RoundingMode roundingMode) {
// 
// BigMoney toSubtract = checkCurrencyEqual(moneyToSubtract);
// return minusRetainScale1(toSubtract.getAmount(), roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minusRetainScale0", moneyToSubtract, roundingMode).as(BigMoney.class);
}
    public BigMoney minusMinor(long amountToSubtract) {
// 
// if (amountToSubtract == 0) {
// return this;
// }
// BigDecimal newAmount =
// amount.subtract(BigDecimal.valueOf(amountToSubtract, currency.getDecimalPlaces()));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minusMinor", amountToSubtract).as(BigMoney.class);
}
    public BigMoney minusMajor(long amountToSubtract) {
// 
// if (amountToSubtract == 0) {
// return this;
// }
// BigDecimal newAmount = amount.subtract(BigDecimal.valueOf(amountToSubtract));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minusMajor", amountToSubtract).as(BigMoney.class);
}
    public BigMoney minus3(double amountToSubtract) {
// 
// if (amountToSubtract == 0) {
// return this;
// }
// BigDecimal newAmount = amount.subtract(BigDecimal.valueOf(amountToSubtract));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minus3", amountToSubtract).as(BigMoney.class);
}
    public BigMoney minus2(BigDecimal amountToSubtract) {
// 
// MoneyUtils.checkNotNull(amountToSubtract, "Amount must not be null");
// if (amountToSubtract.compareTo(BigDecimal.ZERO) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.subtract(amountToSubtract);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minus2", amountToSubtract).as(BigMoney.class);
}
    public BigMoney minus1(BigMoneyProvider moneyToSubtract) {
// 
// BigMoney toSubtract = checkCurrencyEqual(moneyToSubtract);
// return minus2(toSubtract.getAmount());
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minus1", moneyToSubtract).as(BigMoney.class);
}
    public BigMoney minus0(Iterable<? extends BigMoneyProvider> moniesToSubtract) {
// 
// BigDecimal total = amount;
// for (BigMoneyProvider moneyProvider : moniesToSubtract) {
// BigMoney money = checkCurrencyEqual(moneyProvider);
// total = total.subtract(money.amount);
// }
// return with(total);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("minus0", moniesToSubtract).as(BigMoney.class);
}
    public BigMoney plusRetainScale2(double amountToAdd, RoundingMode roundingMode) {
// 
// if (amountToAdd == 0) {
// return this;
// }
// BigDecimal newAmount = amount.add(BigDecimal.valueOf(amountToAdd));
// newAmount = newAmount.setScale(getScale(), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plusRetainScale2", amountToAdd, roundingMode).as(BigMoney.class);
}
    public BigMoney plusRetainScale1(BigDecimal amountToAdd, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(amountToAdd, "Amount must not be null");
// if (amountToAdd.compareTo(BigDecimal.ZERO) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.add(amountToAdd);
// newAmount = newAmount.setScale(getScale(), roundingMode);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plusRetainScale1", amountToAdd, roundingMode).as(BigMoney.class);
}
    public BigMoney plusRetainScale0(BigMoneyProvider moneyToAdd, RoundingMode roundingMode) {
// 
// BigMoney toAdd = checkCurrencyEqual(moneyToAdd);
// return plusRetainScale1(toAdd.getAmount(), roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plusRetainScale0", moneyToAdd, roundingMode).as(BigMoney.class);
}
    public BigMoney plusMinor(long amountToAdd) {
// 
// if (amountToAdd == 0) {
// return this;
// }
// BigDecimal newAmount =
// amount.add(BigDecimal.valueOf(amountToAdd, currency.getDecimalPlaces()));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plusMinor", amountToAdd).as(BigMoney.class);
}
    public BigMoney plusMajor(long amountToAdd) {
// 
// if (amountToAdd == 0) {
// return this;
// }
// BigDecimal newAmount = amount.add(BigDecimal.valueOf(amountToAdd));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plusMajor", amountToAdd).as(BigMoney.class);
}
    public BigMoney plus3(double amountToAdd) {
// 
// if (amountToAdd == 0) {
// return this;
// }
// BigDecimal newAmount = amount.add(BigDecimal.valueOf(amountToAdd));
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plus3", amountToAdd).as(BigMoney.class);
}
    public BigMoney plus2(BigDecimal amountToAdd) {
// 
// MoneyUtils.checkNotNull(amountToAdd, "Amount must not be null");
// if (amountToAdd.compareTo(BigDecimal.ZERO) == 0) {
// return this;
// }
// BigDecimal newAmount = amount.add(amountToAdd);
// return BigMoney.of0(currency, newAmount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plus2", amountToAdd).as(BigMoney.class);
}
    public BigMoney plus1(BigMoneyProvider moneyToAdd) {
// 
// BigMoney toAdd = checkCurrencyEqual(moneyToAdd);
// return plus2(toAdd.getAmount());
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plus1", moneyToAdd).as(BigMoney.class);
}
    public BigMoney plus0(Iterable<? extends BigMoneyProvider> moniesToAdd) {
// 
// BigDecimal total = amount;
// for (BigMoneyProvider moneyProvider : moniesToAdd) {
// BigMoney money = checkCurrencyEqual(moneyProvider);
// total = total.add(money.amount);
// }
// return with(total);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("plus0", moniesToAdd).as(BigMoney.class);
}
    public BigMoney withAmount1(double amount) {
// 
// return withAmount0(BigDecimal.valueOf(amount));
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withAmount1", amount).as(BigMoney.class);
}
    public BigMoney withAmount0(BigDecimal amount) {
// 
// MoneyUtils.checkNotNull(amount, "Amount must not be null");
// if (this.amount.equals(amount)) {
// return this;
// }
// return BigMoney.of0(currency, amount);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withAmount0", amount).as(BigMoney.class);
}
    public boolean isNegativeOrZero() {
// 
// return amount.compareTo(BigDecimal.ZERO) <= 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isNegativeOrZero").as(boolean.class);
}
    public boolean isNegative() {
// 
// return amount.compareTo(BigDecimal.ZERO) < 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isNegative").as(boolean.class);
}
    public boolean isPositiveOrZero() {
// 
// return amount.compareTo(BigDecimal.ZERO) >= 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isPositiveOrZero").as(boolean.class);
}
    public boolean isPositive() {
// 
// return amount.compareTo(BigDecimal.ZERO) > 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isPositive").as(boolean.class);
}
    public boolean isZero() {
// 
// return amount.compareTo(BigDecimal.ZERO) == 0;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isZero").as(boolean.class);
}
    public int getMinorPart() {
// 
// int cdp = getCurrencyUnit().getDecimalPlaces();
// return amount.setScale(cdp, RoundingMode.DOWN)
// .remainder(BigDecimal.ONE)
// .movePointRight(cdp)
// .intValueExact();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getMinorPart").as(int.class);
}
    public int getAmountMinorInt() {
// 
// return getAmountMinor().intValueExact();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMinorInt").as(int.class);
}
    public long getAmountMinorLong() {
// 
// return getAmountMinor().longValueExact();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMinorLong").as(long.class);
}
    public BigDecimal getAmountMinor() {
// 
// int cdp = getCurrencyUnit().getDecimalPlaces();
// return amount.setScale(cdp, RoundingMode.DOWN).movePointRight(cdp);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMinor").as(BigDecimal.class);
}
    public int getAmountMajorInt() {
// 
// return getAmountMajor().intValueExact();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMajorInt").as(int.class);
}
    public long getAmountMajorLong() {
// 
// return getAmountMajor().longValueExact();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMajorLong").as(long.class);
}
    public BigDecimal getAmountMajor() {
// 
// return amount.setScale(0, RoundingMode.DOWN);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmountMajor").as(BigDecimal.class);
}
    public BigDecimal getAmount() {
// 
// return amount;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getAmount").as(BigDecimal.class);
}
    public BigMoney withCurrencyScale1(RoundingMode roundingMode) {
// 
// return withScale1(currency.getDecimalPlaces(), roundingMode);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withCurrencyScale1", roundingMode).as(BigMoney.class);
}
    public BigMoney withCurrencyScale0() {
// 
// return withScale1(currency.getDecimalPlaces(), RoundingMode.UNNECESSARY);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withCurrencyScale0").as(BigMoney.class);
}
    public BigMoney withScale1(int scale, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// if (scale == amount.scale()) {
// return this;
// }
// return BigMoney.of0(currency, amount.setScale(scale, roundingMode));
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withScale1", scale, roundingMode).as(BigMoney.class);
}
    public BigMoney withScale0(int scale) {
// 
// return withScale1(scale, RoundingMode.UNNECESSARY);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withScale0", scale).as(BigMoney.class);
}
    public boolean isCurrencyScale() {
// 
// return amount.scale() == currency.getDecimalPlaces();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("isCurrencyScale").as(boolean.class);
}
    public int getScale() {
// 
// return amount.scale();
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getScale").as(int.class);
}
    public BigMoney withCurrencyUnit(CurrencyUnit currency) {
// 
// MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
// if (this.currency == currency) {
// return this;
// }
// return new BigMoney(0, amount, currency);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("withCurrencyUnit", currency).as(BigMoney.class);
}
    public CurrencyUnit getCurrencyUnit() {
// 
// return currency;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("getCurrencyUnit").as(CurrencyUnit.class);
}
    public static BigMoney total3(
            CurrencyUnit currency, Iterable<? extends BigMoneyProvider> monies) {
// 
// return BigMoney.zero0(currency).plus0(monies);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("total3", currency, monies).as(BigMoney.class);
}
    public static BigMoney total2(CurrencyUnit currency, BigMoneyProvider... monies) {
// 
// return BigMoney.zero0(currency).plus0(Arrays.asList(monies));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("total2", currency, monies).as(BigMoney.class);
}
    public static BigMoney total1(Iterable<? extends BigMoneyProvider> monies) {
// 
// MoneyUtils.checkNotNull(monies, "Money iterator must not be null");
// Iterator<? extends BigMoneyProvider> it = monies.iterator();
// if (it.hasNext() == false) {
// throw new IllegalArgumentException("Money iterator must not be empty");
// }
// BigMoney total = of2(it.next());
// MoneyUtils.checkNotNull(total, "Money iterator must not contain null entries");
// while (it.hasNext()) {
// total = total.plus1(it.next());
// }
// return total;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("total1", monies).as(BigMoney.class);
}
    public static BigMoney total0(BigMoneyProvider... monies) {
// 
// MoneyUtils.checkNotNull(monies, "Money array must not be null");
// if (monies.length == 0) {
// throw new IllegalArgumentException("Money array must not be empty");
// }
// BigMoney total = of2(monies[0]);
// MoneyUtils.checkNotNull(total, "Money array must not contain null entries");
// for (int i = 1; i < monies.length; i++) {
// total = total.plus1(of2(monies[i]));
// }
// return total;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("total0", monies).as(BigMoney.class);
}
    public static BigMoney of2(BigMoneyProvider moneyProvider) {
// 
// MoneyUtils.checkNotNull(moneyProvider, "BigMoneyProvider must not be null");
// BigMoney money = moneyProvider.toBigMoney();
// MoneyUtils.checkNotNull(money, "BigMoneyProvider must not return null");
// return money;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("of2", moneyProvider).as(BigMoney.class);
}
    public static BigMoney zero1(CurrencyUnit currency, int scale) {
// 
// return BigMoney.of0(currency, BigDecimal.valueOf(0, scale));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("zero1", currency, scale).as(BigMoney.class);
}
    public static BigMoney zero0(CurrencyUnit currency) {
// 
// return BigMoney.of0(currency, BigDecimal.ZERO);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("zero0", currency).as(BigMoney.class);
}
    public static BigMoney ofMinor(CurrencyUnit currency, long amountMinor) {
// 
// MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
// return BigMoney.of0(currency, BigDecimal.valueOf(amountMinor, currency.getDecimalPlaces()));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ofMinor", currency, amountMinor).as(BigMoney.class);
}
    public static BigMoney ofMajor(CurrencyUnit currency, long amountMajor) {
// 
// MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
// return BigMoney.of0(currency, BigDecimal.valueOf(amountMajor));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ofMajor", currency, amountMajor).as(BigMoney.class);
}
    public static BigMoney ofScale2(CurrencyUnit currency, long unscaledAmount, int scale) {
// 
// MoneyUtils.checkNotNull(currency, "Currency must not be null");
// return BigMoney.of0(currency, BigDecimal.valueOf(unscaledAmount, scale));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ofScale2", currency, unscaledAmount, scale).as(BigMoney.class);
}
    public static BigMoney ofScale1(
            CurrencyUnit currency, BigDecimal amount, int scale, RoundingMode roundingMode) {
// 
// MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
// MoneyUtils.checkNotNull(amount, "Amount must not be null");
// MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
// BigDecimal scaledAmount = amount.setScale(scale, roundingMode);
// return BigMoney.of0(currency, scaledAmount);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ofScale1", currency, amount, scale, roundingMode).as(BigMoney.class);
}
    public static BigMoney ofScale0(CurrencyUnit currency, BigDecimal amount, int scale) {
// 
// return BigMoney.ofScale1(currency, amount, scale, RoundingMode.UNNECESSARY);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ofScale0", currency, amount, scale).as(BigMoney.class);
}
    public static BigMoney of1(CurrencyUnit currency, double amount) {
// 
// MoneyUtils.checkNotNull(currency, "Currency must not be null");
// if (amount == 0d) {
// return zero0(currency);
// }
// return BigMoney.of0(currency, BigDecimal.valueOf(amount).stripTrailingZeros());
// 


// TODO: Check the type mapping below!
return clz.invokeMember("of1", currency, amount).as(BigMoney.class);
}
    public static BigMoney of0(CurrencyUnit currency, BigDecimal amount) {
// 
// MoneyUtils.checkNotNull(currency, "Currency must not be null");
// MoneyUtils.checkNotNull(amount, "Amount must not be null");
// BigDecimal checkedAmount = amount;
// if (amount.getClass() != BigDecimal.class) {
// BigInteger value = amount.unscaledValue();
// if (value == null) {
// throw new IllegalArgumentException("Illegal BigDecimal subclass");
// }
// if (value.getClass() != BigInteger.class) {
// value = new BigInteger(value.toString());
// }
// checkedAmount = new BigDecimal(value, amount.scale());
// }
// return new BigMoney(0, checkedAmount, currency);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("of0", currency, amount).as(BigMoney.class);
}
    private BigMoney checkCurrencyEqual(BigMoneyProvider moneyProvider) {
// 
// BigMoney money = of2(moneyProvider);
// if (isSameCurrency(money) == false) {
// throw new CurrencyMismatchException(getCurrencyUnit(), money.getCurrencyUnit());
// }
// return money;
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("checkCurrencyEqual", moneyProvider).as(BigMoney.class);
}
    private BigMoney with(BigDecimal newAmount) {
// 
// if (newAmount == amount) {
// return this;
// }
// return new BigMoney(0, newAmount, currency);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("with", newAmount).as(BigMoney.class);
}
    private Object writeReplace() {
// 
// return new Ser(0, this, Ser.BIG_MONEY);
// 


// TODO: Check the type mapping below!
return this.obj.invokeMember("writeReplace").as(Object.class);
}
    private void readObject(ObjectInputStream ois) throws InvalidObjectException {
try {
// 
// throw new InvalidObjectException("Serialization delegate required");
// 

this.obj.invokeMember("readObject", ois);
} catch (PolyglotException e) {
    // TODO: Handle InvalidObjectException
    throw (InvalidObjectException) ExceptionHandler.handle(e, "BigMoney.readObject");
}
}
}
