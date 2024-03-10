package org.joda.money;

import java.io.InvalidObjectException;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.math.BigDecimal;
import java.math.RoundingMode;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public final class Money implements BigMoneyProvider, Comparable<BigMoneyProvider>, Serializable {
  private static final long serialVersionUID = 1L;
  private static Value clz = ContextInitializer.getPythonClass("/Money.py", "Money");
  private Value obj;

  public Money(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return money.toString();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return money.hashCode() + 3;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object other) {
    //
    // if (this == other) {
    // return true;
    // }
    // if (other instanceof Money) {
    // Money otherMoney = (Money) other;
    // return money.equals(otherMoney.money);
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("equals", other).as(boolean.class);
  }

  public int compareTo(BigMoneyProvider other) {
    //
    // return money.compareTo(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("compareTo", other).as(int.class);
  }

  public BigMoney toBigMoney() {
    //
    // return money;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toBigMoney").as(BigMoney.class);
  }

  public Money(int constructorId, BigMoney money) {
    //
    // if (constructorId == 0) {
    //
    // assert money != null : "Joda-Money bug: BigMoney must not be null";
    // assert money.isCurrencyScale()
    // : "Joda-Money bug: Only currency scale is valid for Money";
    // this.money = money;
    // } else {
    //
    // this.money = null;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, money);
  }

  public static Money parse(String moneyStr) {
    //
    // return Money.of4(BigMoney.parse(moneyStr));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("parse", moneyStr).as(Money.class);
  }

  public boolean isLessThanOrEqual(BigMoneyProvider other) {
    //
    // return money.isLessThanOrEqual(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isLessThanOrEqual", other).as(boolean.class);
  }

  public boolean isLessThan(BigMoneyProvider other) {
    //
    // return money.isLessThan(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isLessThan", other).as(boolean.class);
  }

  public boolean isGreaterThanOrEqual(BigMoneyProvider other) {
    //
    // return money.isGreaterThanOrEqual(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isGreaterThanOrEqual", other).as(boolean.class);
  }

  public boolean isGreaterThan(BigMoneyProvider other) {
    //
    // return money.isGreaterThan(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isGreaterThan", other).as(boolean.class);
  }

  public boolean isEqual(BigMoneyProvider other) {
    //
    // return money.isEqual(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isEqual", other).as(boolean.class);
  }

  public boolean isSameCurrency(BigMoneyProvider other) {
    //
    // return money.isSameCurrency(other);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isSameCurrency", other).as(boolean.class);
  }

  public Money convertedTo(
      CurrencyUnit currency, BigDecimal conversionMultipler, RoundingMode roundingMode) {
    //
    // return with(
    // money.convertedTo(currency, conversionMultipler).withCurrencyScale1(roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("convertedTo", currency, conversionMultipler, roundingMode)
        .as(Money.class);
  }

  public Money rounded(int scale, RoundingMode roundingMode) {
    //
    // return with(money.rounded(scale, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("rounded", scale, roundingMode).as(Money.class);
  }

  public Money abs() {
    //
    // return (isNegative() ? negated() : this);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("abs").as(Money.class);
  }

  public Money negated() {
    //
    // return with(money.negated());
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("negated").as(Money.class);
  }

  public Money dividedBy2(long valueToDivideBy, RoundingMode roundingMode) {
    //
    // return with(money.dividedBy2(valueToDivideBy, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("dividedBy2", valueToDivideBy, roundingMode).as(Money.class);
  }

  public Money dividedBy1(double valueToDivideBy, RoundingMode roundingMode) {
    //
    // return with(money.dividedBy1(valueToDivideBy, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("dividedBy1", valueToDivideBy, roundingMode).as(Money.class);
  }

  public Money dividedBy0(BigDecimal valueToDivideBy, RoundingMode roundingMode) {
    //
    // return with(money.dividedBy0(valueToDivideBy, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("dividedBy0", valueToDivideBy, roundingMode).as(Money.class);
  }

  public Money multipliedBy2(long valueToMultiplyBy) {
    //
    // return with(money.multipliedBy2(valueToMultiplyBy));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("multipliedBy2", valueToMultiplyBy).as(Money.class);
  }

  public Money multipliedBy1(double valueToMultiplyBy, RoundingMode roundingMode) {
    //
    // return with(money.multiplyRetainScale1(valueToMultiplyBy, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("multipliedBy1", valueToMultiplyBy, roundingMode).as(Money.class);
  }

  public Money multipliedBy0(BigDecimal valueToMultiplyBy, RoundingMode roundingMode) {
    //
    // return with(money.multiplyRetainScale0(valueToMultiplyBy, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("multipliedBy0", valueToMultiplyBy, roundingMode).as(Money.class);
  }

  public Money minusMinor(long amountToSubtract) {
    //
    // return with(money.minusMinor(amountToSubtract));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minusMinor", amountToSubtract).as(Money.class);
  }

  public Money minusMajor(long amountToSubtract) {
    //
    // return with(money.minusMajor(amountToSubtract));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minusMajor", amountToSubtract).as(Money.class);
  }

  public Money minus5(double amountToSubtract, RoundingMode roundingMode) {
    //
    // return with(money.minusRetainScale2(amountToSubtract, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus5", amountToSubtract, roundingMode).as(Money.class);
  }

  public Money minus4(double amountToSubtract) {
    //
    // return minus5(amountToSubtract, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus4", amountToSubtract).as(Money.class);
  }

  public Money minus3(BigDecimal amountToSubtract, RoundingMode roundingMode) {
    //
    // return with(money.minusRetainScale1(amountToSubtract, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus3", amountToSubtract, roundingMode).as(Money.class);
  }

  public Money minus2(BigDecimal amountToSubtract) {
    //
    // return minus3(amountToSubtract, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus2", amountToSubtract).as(Money.class);
  }

  public Money minus1(Money moneyToSubtract) {
    //
    // return with(money.minus1(moneyToSubtract));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus1", moneyToSubtract).as(Money.class);
  }

  public Money minus0(Iterable<Money> moniesToSubtract) {
    //
    // return with(money.minus0(moniesToSubtract));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("minus0", moniesToSubtract).as(Money.class);
  }

  public Money plusMinor(long amountToAdd) {
    //
    // return with(money.plusMinor(amountToAdd));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plusMinor", amountToAdd).as(Money.class);
  }

  public Money plusMajor(long amountToAdd) {
    //
    // return with(money.plusMajor(amountToAdd));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plusMajor", amountToAdd).as(Money.class);
  }

  public Money plus5(double amountToAdd, RoundingMode roundingMode) {
    //
    // return with(money.plusRetainScale2(amountToAdd, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus5", amountToAdd, roundingMode).as(Money.class);
  }

  public Money plus4(double amountToAdd) {
    //
    // return plus5(amountToAdd, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus4", amountToAdd).as(Money.class);
  }

  public Money plus3(BigDecimal amountToAdd, RoundingMode roundingMode) {
    //
    // return with(money.plusRetainScale1(amountToAdd, roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus3", amountToAdd, roundingMode).as(Money.class);
  }

  public Money plus2(BigDecimal amountToAdd) {
    //
    // return plus3(amountToAdd, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus2", amountToAdd).as(Money.class);
  }

  public Money plus1(Money moneyToAdd) {
    //
    // return with(money.plus1(moneyToAdd));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus1", moneyToAdd).as(Money.class);
  }

  public Money plus0(Iterable<Money> moniesToAdd) {
    //
    // return with(money.plus0(moniesToAdd));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("plus0", moniesToAdd).as(Money.class);
  }

  public Money withAmount3(double amount, RoundingMode roundingMode) {
    //
    // return with(money.withAmount1(amount).withCurrencyScale1(roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withAmount3", amount, roundingMode).as(Money.class);
  }

  public Money withAmount2(double amount) {
    //
    // return withAmount3(amount, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withAmount2", amount).as(Money.class);
  }

  public Money withAmount1(BigDecimal amount, RoundingMode roundingMode) {
    //
    // return with(money.withAmount0(amount).withCurrencyScale1(roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withAmount1", amount, roundingMode).as(Money.class);
  }

  public Money withAmount0(BigDecimal amount) {
    //
    // return withAmount1(amount, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withAmount0", amount).as(Money.class);
  }

  public boolean isNegativeOrZero() {
    //
    // return money.isNegativeOrZero();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isNegativeOrZero").as(boolean.class);
  }

  public boolean isNegative() {
    //
    // return money.isNegative();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isNegative").as(boolean.class);
  }

  public boolean isPositiveOrZero() {
    //
    // return money.isPositiveOrZero();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isPositiveOrZero").as(boolean.class);
  }

  public boolean isPositive() {
    //
    // return money.isPositive();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isPositive").as(boolean.class);
  }

  public boolean isZero() {
    //
    // return money.isZero();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isZero").as(boolean.class);
  }

  public int getMinorPart() {
    //
    // return money.getMinorPart();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getMinorPart").as(int.class);
  }

  public int getAmountMinorInt() {
    //
    // return money.getAmountMinorInt();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMinorInt").as(int.class);
  }

  public long getAmountMinorLong() {
    //
    // return money.getAmountMinorLong();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMinorLong").as(long.class);
  }

  public BigDecimal getAmountMinor() {
    //
    // return money.getAmountMinor();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMinor").as(BigDecimal.class);
  }

  public int getAmountMajorInt() {
    //
    // return money.getAmountMajorInt();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMajorInt").as(int.class);
  }

  public long getAmountMajorLong() {
    //
    // return money.getAmountMajorLong();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMajorLong").as(long.class);
  }

  public BigDecimal getAmountMajor() {
    //
    // return money.getAmountMajor();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmountMajor").as(BigDecimal.class);
  }

  public BigDecimal getAmount() {
    //
    // return money.getAmount();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmount").as(BigDecimal.class);
  }

  public int getScale() {
    //
    // return money.getScale();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getScale").as(int.class);
  }

  public Money withCurrencyUnit1(CurrencyUnit currency, RoundingMode roundingMode) {
    //
    // return with(money.withCurrencyUnit(currency).withCurrencyScale1(roundingMode));
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withCurrencyUnit1", currency, roundingMode).as(Money.class);
  }

  public Money withCurrencyUnit0(CurrencyUnit currency) {
    //
    // return withCurrencyUnit1(currency, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withCurrencyUnit0", currency).as(Money.class);
  }

  public CurrencyUnit getCurrencyUnit() {
    //
    // return money.getCurrencyUnit();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getCurrencyUnit").as(CurrencyUnit.class);
  }

  public static Money total3(CurrencyUnit currency, Iterable<Money> monies) {
    //
    // return Money.zero(currency).plus0(monies);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("total3", currency, monies).as(Money.class);
  }

  public static Money total2(CurrencyUnit currency, Money... monies) {
    //
    // return Money.zero(currency).plus0(Arrays.asList(monies));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("total2", currency, monies).as(Money.class);
  }

  public static Money total1(Iterable<Money> monies) {
    //
    // MoneyUtils.checkNotNull(monies, "Money iterator must not be null");
    // Iterator<Money> it = monies.iterator();
    // if (it.hasNext() == false) {
    // throw new IllegalArgumentException("Money iterator must not be empty");
    // }
    // Money total = it.next();
    // MoneyUtils.checkNotNull(total, "Money iterator must not contain null entries");
    // while (it.hasNext()) {
    // total = total.plus1(it.next());
    // }
    // return total;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("total1", monies).as(Money.class);
  }

  public static Money total0(Money... monies) {
    //
    // MoneyUtils.checkNotNull(monies, "Money array must not be null");
    // if (monies.length == 0) {
    // throw new IllegalArgumentException("Money array must not be empty");
    // }
    // Money total = monies[0];
    // MoneyUtils.checkNotNull(total, "Money arary must not contain null entries");
    // for (int i = 1; i < monies.length; i++) {
    // total = total.plus1(monies[i]);
    // }
    // return total;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("total0", monies).as(Money.class);
  }

  public static Money of5(BigMoneyProvider moneyProvider, RoundingMode roundingMode) {
    //
    // MoneyUtils.checkNotNull(moneyProvider, "BigMoneyProvider must not be null");
    // MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
    // return new Money(0, BigMoney.of2(moneyProvider).withCurrencyScale1(roundingMode));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of5", moneyProvider, roundingMode).as(Money.class);
  }

  public static Money of4(BigMoneyProvider moneyProvider) {
    //
    // return Money.of5(moneyProvider, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of4", moneyProvider).as(Money.class);
  }

  public static Money zero(CurrencyUnit currency) {
    //
    // MoneyUtils.checkNotNull(currency, "Currency must not be null");
    // BigDecimal bd = BigDecimal.valueOf(0, currency.getDecimalPlaces());
    // return new Money(0, BigMoney.of0(currency, bd));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("zero", currency).as(Money.class);
  }

  public static Money ofMinor(CurrencyUnit currency, long amountMinor) {
    //
    // return new Money(0, BigMoney.ofMinor(currency, amountMinor));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ofMinor", currency, amountMinor).as(Money.class);
  }

  public static Money ofMajor(CurrencyUnit currency, long amountMajor) {
    //
    // return Money.of1(currency, BigDecimal.valueOf(amountMajor), RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("ofMajor", currency, amountMajor).as(Money.class);
  }

  public static Money of3(CurrencyUnit currency, double amount, RoundingMode roundingMode) {
    //
    // return Money.of1(currency, BigDecimal.valueOf(amount), roundingMode);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of3", currency, amount, roundingMode).as(Money.class);
  }

  public static Money of2(CurrencyUnit currency, double amount) {
    //
    // return Money.of0(currency, BigDecimal.valueOf(amount));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of2", currency, amount).as(Money.class);
  }

  public static Money of1(CurrencyUnit currency, BigDecimal amount, RoundingMode roundingMode) {
    //
    // MoneyUtils.checkNotNull(currency, "CurrencyUnit must not be null");
    // MoneyUtils.checkNotNull(amount, "Amount must not be null");
    // MoneyUtils.checkNotNull(roundingMode, "RoundingMode must not be null");
    // BigDecimal scaledAmount = amount.setScale(currency.getDecimalPlaces(), roundingMode);
    // return new Money(0, BigMoney.of0(currency, scaledAmount));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of1", currency, amount, roundingMode).as(Money.class);
  }

  public static Money of0(CurrencyUnit currency, BigDecimal amount) {
    //
    // MoneyUtils.checkNotNull(currency, "Currency must not be null");
    // MoneyUtils.checkNotNull(amount, "Amount must not be null");
    // if (amount.scale() > currency.getDecimalPlaces()) {
    // throw new ArithmeticException(
    // "Scale of amount "
    // + amount
    // + " is greater than the scale of the currency "
    // + currency);
    // }
    // return Money.of1(currency, amount, RoundingMode.UNNECESSARY);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of0", currency, amount).as(Money.class);
  }

  private Money with(BigMoney newInstance) {
    //
    // if (money.equals(newInstance)) {
    // return this;
    // }
    // return new Money(0, newInstance);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("with", newInstance).as(Money.class);
  }

  private Object writeReplace() {
    //
    // return new Ser(0, this, Ser.MONEY);
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
      throw (InvalidObjectException) ExceptionHandler.handle(e, "Money.readObject");
    }
  }
}
