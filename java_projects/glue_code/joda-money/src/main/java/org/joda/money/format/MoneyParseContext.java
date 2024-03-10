package org.joda.money.format;

import java.math.BigDecimal;
import java.text.ParsePosition;
import java.util.Locale;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.ContextInitializer;
import org.joda.money.CurrencyUnit;

public final class MoneyParseContext {
  private int textErrorIndex = -1;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MoneyParseContext.py", "MoneyParseContext");
  private Value obj;

  public MoneyParseContext(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public BigMoney toBigMoney() {
    //
    // if (currency == null) {
    // throw MoneyFormatException.MoneyFormatException1(
    // "Cannot convert to BigMoney as no currency found");
    // }
    // if (amount == null) {
    // throw MoneyFormatException.MoneyFormatException1(
    // "Cannot convert to BigMoney as no amount found");
    // }
    // return BigMoney.of0(currency, amount);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toBigMoney").as(BigMoney.class);
  }

  public ParsePosition toParsePosition() {
    //
    // ParsePosition pp = new ParsePosition(textIndex);
    // pp.setErrorIndex(textErrorIndex);
    // return pp;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toParsePosition").as(ParsePosition.class);
  }

  public boolean isComplete() {
    //
    // return currency != null && amount != null;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isComplete").as(boolean.class);
  }

  public boolean isFullyParsed() {
    //
    // return textIndex == getTextLength();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isFullyParsed").as(boolean.class);
  }

  public boolean isError() {
    //
    // return textErrorIndex >= 0;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isError").as(boolean.class);
  }

  public void setAmount(BigDecimal amount) {
    //
    // this.amount = amount;
    //

    this.obj.invokeMember("setAmount", amount);
  }

  public BigDecimal getAmount() {
    //
    // return amount;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getAmount").as(BigDecimal.class);
  }

  public void setCurrency(CurrencyUnit currency) {
    //
    // this.currency = currency;
    //

    this.obj.invokeMember("setCurrency", currency);
  }

  public CurrencyUnit getCurrency() {
    //
    // return currency;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getCurrency").as(CurrencyUnit.class);
  }

  public void setError() {
    //
    // this.textErrorIndex = textIndex;
    //

    this.obj.invokeMember("setError");
  }

  public void setErrorIndex(int index) {
    //
    // this.textErrorIndex = index;
    //

    this.obj.invokeMember("setErrorIndex", index);
  }

  public int getErrorIndex() {
    //
    // return textErrorIndex;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getErrorIndex").as(int.class);
  }

  public void setIndex(int index) {
    //
    // this.textIndex = index;
    //

    this.obj.invokeMember("setIndex", index);
  }

  public int getIndex() {
    //
    // return textIndex;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getIndex").as(int.class);
  }

  public String getTextSubstring(int start, int end) {
    //
    // return text.subSequence(start, end).toString();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getTextSubstring", start, end).as(String.class);
  }

  public int getTextLength() {
    //
    // return text.length();
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getTextLength").as(int.class);
  }

  public void setText(CharSequence text) {
    //
    // MoneyFormatter.checkNotNull(text, "Text must not be null");
    // this.text = text;
    //

    this.obj.invokeMember("setText", text);
  }

  public CharSequence getText() {
    //
    // return text;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getText").as(CharSequence.class);
  }

  public void setLocale(Locale locale) {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // this.locale = locale;
    //

    this.obj.invokeMember("setLocale", locale);
  }

  public Locale getLocale() {
    //
    // return locale;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getLocale").as(Locale.class);
  }

  public MoneyParseContext(
      int constructorId,
      CharSequence text,
      int index,
      Locale locale,
      BigDecimal amount,
      int errorIndex,
      CurrencyUnit currency) {
    //
    // if (constructorId == 0) {
    //
    // this.locale = locale;
    // this.text = text;
    // this.textIndex = index;
    // this.textErrorIndex = errorIndex;
    // this.currency = currency;
    // this.amount = amount;
    // } else {
    //
    // this.locale = locale;
    // this.text = text;
    // this.textIndex = index;
    // }
    //

    this.obj =
        clz.invokeMember(
            "__init__", constructorId, text, index, locale, amount, errorIndex, currency);
  }

  void mergeChild(MoneyParseContext child) {
    //
    // setLocale(child.getLocale());
    // setText(child.getText());
    // setIndex(child.getIndex());
    // setErrorIndex(child.getErrorIndex());
    // setCurrency(child.getCurrency());
    // setAmount(child.getAmount());
    //

    this.obj.invokeMember("mergeChild", child);
  }

  MoneyParseContext createChild() {
    //
    // return new MoneyParseContext(0, text, textIndex, locale, amount, textErrorIndex, currency);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("createChild").as(MoneyParseContext.class);
  }
}
