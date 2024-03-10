package org.joda.money.format;

import java.io.IOException;
import java.io.Serializable;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;
import org.joda.money.BigMoney;
import org.joda.money.ContextInitializer;
import org.joda.money.ExceptionHandler;

final class AmountPrinterParser implements MoneyPrinter, MoneyParser, Serializable {
  private static final long serialVersionUID = 1L;
  private static Value clz =
      ContextInitializer.getPythonClass("/format/AmountPrinterParser.py", "AmountPrinterParser");
  private Value obj;

  public AmountPrinterParser(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return "${amount}";
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public void parse(MoneyParseContext context) {
    //
    // final int len = context.getTextLength();
    // final MoneyAmountStyle activeStyle = style.localize(context.getLocale());
    // char[] buf = new char[len - context.getIndex()];
    // int bufPos = 0;
    // boolean dpSeen = false;
    // int pos = context.getIndex();
    // if (pos < len) {
    // char ch = context.getText().charAt(pos++);
    // if (ch == activeStyle.getNegativeSignCharacter()) {
    // buf[bufPos++] = '-';
    // } else if (ch == activeStyle.getPositiveSignCharacter()) {
    // buf[bufPos++] = '+';
    // } else if (ch >= activeStyle.getZeroCharacter()
    // && ch < activeStyle.getZeroCharacter() + 10) {
    // buf[bufPos++] = (char) ('0' + ch - activeStyle.getZeroCharacter());
    // } else if (ch == activeStyle.getDecimalPointCharacter()) {
    // buf[bufPos++] = '.';
    // dpSeen = true;
    // } else {
    // context.setError();
    // return;
    // }
    // }
    // boolean lastWasGroup = false;
    // for (; pos < len; pos++) {
    // char ch = context.getText().charAt(pos);
    // if (ch >= activeStyle.getZeroCharacter() && ch < activeStyle.getZeroCharacter() + 10) {
    // buf[bufPos++] = (char) ('0' + ch - activeStyle.getZeroCharacter());
    // lastWasGroup = false;
    // } else if (ch == activeStyle.getDecimalPointCharacter() && dpSeen == false) {
    // buf[bufPos++] = '.';
    // dpSeen = true;
    // lastWasGroup = false;
    // } else if (ch == activeStyle.getGroupingCharacter() && lastWasGroup == false) {
    // lastWasGroup = true;
    // } else {
    // break;
    // }
    // }
    // if (lastWasGroup) {
    // pos--;
    // }
    // try {
    // context.setAmount(new BigDecimal(buf, 0, bufPos));
    // context.setIndex(pos);
    // } catch (NumberFormatException ex) {
    // context.setError();
    // }
    //

    this.obj.invokeMember("parse", context);
  }

  public void print(MoneyPrintContext context, Appendable appendable, BigMoney money)
      throws IOException {
    try {
      //
      // MoneyAmountStyle activeStyle = style.localize(context.getLocale());
      // String str;
      // if (money.isNegative()) {
      // if (!activeStyle.isAbsValue()) {
      // appendable.append(activeStyle.getNegativeSignCharacter());
      // }
      // str = money.negated().getAmount().toPlainString();
      // } else {
      // str = money.getAmount().toPlainString();
      // }
      // char zeroChar = activeStyle.getZeroCharacter();
      // if (zeroChar != '0') {
      // int diff = zeroChar - '0';
      // StringBuilder zeroConvert = new StringBuilder(str);
      // for (int i = 0; i < str.length(); i++) {
      // char ch = str.charAt(i);
      // if (ch >= '0' && ch <= '9') {
      // zeroConvert.setCharAt(i, (char) (ch + diff));
      // }
      // }
      // str = zeroConvert.toString();
      // }
      // final int decPoint = str.indexOf('.');
      // final int afterDecPoint = decPoint + 1;
      // if (activeStyle.getGroupingStyle() == GroupingStyle.NONE) {
      // if (decPoint < 0) {
      // appendable.append(str);
      // if (activeStyle.isForcedDecimalPoint()) {
      // appendable.append(activeStyle.getDecimalPointCharacter());
      // }
      // } else {
      // appendable
      // .append(str.subSequence(0, decPoint))
      // .append(activeStyle.getDecimalPointCharacter())
      // .append(str.substring(afterDecPoint));
      // }
      // } else {
      // int groupingSize = activeStyle.getGroupingSize();
      // int extendedGroupingSize = activeStyle.getExtendedGroupingSize();
      // extendedGroupingSize = extendedGroupingSize == 0 ? groupingSize : extendedGroupingSize;
      // char groupingChar = activeStyle.getGroupingCharacter();
      // int pre = (decPoint < 0 ? str.length() : decPoint);
      // int post = (decPoint < 0 ? 0 : str.length() - decPoint - 1);
      // appendable.append(str.charAt(0));
      // for (int i = 1; i < pre; i++) {
      // if (isPreGroupingPoint(pre - i, groupingSize, extendedGroupingSize)) {
      // appendable.append(groupingChar);
      // }
      // appendable.append(str.charAt(i));
      // }
      // if (decPoint >= 0 || activeStyle.isForcedDecimalPoint()) {
      // appendable.append(activeStyle.getDecimalPointCharacter());
      // }
      // if (activeStyle.getGroupingStyle() == GroupingStyle.BEFORE_DECIMAL_POINT) {
      // if (decPoint >= 0) {
      // appendable.append(str.substring(afterDecPoint));
      // }
      // } else {
      // for (int i = 0; i < post; i++) {
      // appendable.append(str.charAt(i + afterDecPoint));
      // if (isPostGroupingPoint(i, post, groupingSize, extendedGroupingSize)) {
      // appendable.append(groupingChar);
      // }
      // }
      // }
      // }
      //

      this.obj.invokeMember("print", context, appendable, money);
    } catch (PolyglotException e) {
      // TODO: Handle IOException
      throw (IOException) ExceptionHandler.handle(e, "AmountPrinterParser.print");
    }
  }

  private boolean isPostGroupingPoint(int i, int post, int groupingSize, int extendedGroupingSize) {
    //
    // boolean atEnd = (i + 1) >= post;
    // if (i > groupingSize) {
    // return (i - groupingSize) % extendedGroupingSize == (extendedGroupingSize - 1)
    // && !atEnd;
    // }
    // return i % groupingSize == (groupingSize - 1) && !atEnd;
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("isPostGroupingPoint", i, post, groupingSize, extendedGroupingSize)
        .as(boolean.class);
  }

  private boolean isPreGroupingPoint(int remaining, int groupingSize, int extendedGroupingSize) {
    //
    // if (remaining >= groupingSize + extendedGroupingSize) {
    // return (remaining - groupingSize) % extendedGroupingSize == 0;
    // }
    // return remaining % groupingSize == 0;
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("isPreGroupingPoint", remaining, groupingSize, extendedGroupingSize)
        .as(boolean.class);
  }

  AmountPrinterParser(MoneyAmountStyle style) {
    //
    // this.style = style;
    //

    this.obj = clz.invokeMember("__init__", style);
  }
}
