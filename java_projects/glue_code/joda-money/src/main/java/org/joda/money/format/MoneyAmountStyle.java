package org.joda.money.format;

import java.io.Serializable;
import java.util.Locale;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import org.graalvm.polyglot.Value;
import org.joda.money.ContextInitializer;

public final class MoneyAmountStyle implements Serializable {
  public static final MoneyAmountStyle LOCALIZED_NO_GROUPING =
      new MoneyAmountStyle(-1, -1, -1, -1, GroupingStyle.NONE, -1, -1, -1, false, false);
  public static final MoneyAmountStyle LOCALIZED_GROUPING =
      new MoneyAmountStyle(-1, -1, -1, -1, GroupingStyle.FULL, -1, -1, -1, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_COMMA_NO_GROUPING =
      new MoneyAmountStyle('0', '+', '-', ',', GroupingStyle.NONE, '.', 3, 0, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_COMMA_GROUP3_SPACE =
      new MoneyAmountStyle('0', '+', '-', ',', GroupingStyle.FULL, ' ', 3, 0, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_COMMA_GROUP3_DOT =
      new MoneyAmountStyle('0', '+', '-', ',', GroupingStyle.FULL, '.', 3, 0, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_POINT_NO_GROUPING =
      new MoneyAmountStyle('0', '+', '-', '.', GroupingStyle.NONE, ',', 3, 0, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_POINT_GROUP3_SPACE =
      new MoneyAmountStyle('0', '+', '-', '.', GroupingStyle.FULL, ' ', 3, 0, false, false);
  public static final MoneyAmountStyle ASCII_DECIMAL_POINT_GROUP3_COMMA =
      new MoneyAmountStyle('0', '+', '-', '.', GroupingStyle.FULL, ',', 3, 0, false, false);
  private static final long serialVersionUID = 1L;
  private static final ConcurrentMap<Locale, MoneyAmountStyle> LOCALIZED_CACHE =
      new ConcurrentHashMap<Locale, MoneyAmountStyle>();
  private static Value clz =
      ContextInitializer.getPythonClass("/format/MoneyAmountStyle.py", "MoneyAmountStyle");
  private Value obj;

  public MoneyAmountStyle(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return "MoneyAmountStyle['"
    // + getZeroCharacter()
    // + "','"
    // + getPositiveSignCharacter()
    // + "','"
    // + getNegativeSignCharacter()
    // + "','"
    // + getDecimalPointCharacter()
    // + "','"
    // + getGroupingStyle()
    // + ","
    // + getGroupingCharacter()
    // + "','"
    // + getGroupingSize()
    // + "',"
    // + isForcedDecimalPoint()
    // + "',"
    // + isAbsValue()
    // + "]";
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // int hash = 13;
    // hash += zeroCharacter * 17;
    // hash += positiveCharacter * 17;
    // hash += negativeCharacter * 17;
    // hash += decimalPointCharacter * 17;
    // hash += groupingStyle.hashCode() * 17;
    // hash += groupingCharacter * 17;
    // hash += groupingSize * 17;
    // hash += (forceDecimalPoint ? 2 : 4);
    // hash += (absValue ? 3 : 9);
    // return hash;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object other) {
    //
    // if (other == this) {
    // return true;
    // }
    // if (other instanceof MoneyAmountStyle == false) {
    // return false;
    // }
    // MoneyAmountStyle otherStyle = (MoneyAmountStyle) other;
    // return (zeroCharacter == otherStyle.zeroCharacter)
    // && (positiveCharacter == otherStyle.positiveCharacter)
    // && (negativeCharacter == otherStyle.negativeCharacter)
    // && (decimalPointCharacter == otherStyle.decimalPointCharacter)
    // && (groupingStyle == otherStyle.groupingStyle)
    // && (groupingCharacter == otherStyle.groupingCharacter)
    // && (groupingSize == otherStyle.groupingSize)
    // && (forceDecimalPoint == otherStyle.forceDecimalPoint)
    // && (absValue == otherStyle.absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("equals", other).as(boolean.class);
  }

  public MoneyAmountStyle withAbsValue(boolean absValue) {
    //
    // if (this.absValue == absValue) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withAbsValue", absValue).as(MoneyAmountStyle.class);
  }

  public boolean isAbsValue() {
    //
    // return absValue;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isAbsValue").as(boolean.class);
  }

  public MoneyAmountStyle withForcedDecimalPoint(boolean forceDecimalPoint) {
    //
    // if (this.forceDecimalPoint == forceDecimalPoint) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withForcedDecimalPoint", forceDecimalPoint)
        .as(MoneyAmountStyle.class);
  }

  public boolean isForcedDecimalPoint() {
    //
    // return forceDecimalPoint;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("isForcedDecimalPoint").as(boolean.class);
  }

  public MoneyAmountStyle withGroupingStyle(GroupingStyle groupingStyle) {
    //
    // MoneyFormatter.checkNotNull(groupingStyle, "groupingStyle");
    // if (this.groupingStyle == groupingStyle) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withGroupingStyle", groupingStyle).as(MoneyAmountStyle.class);
  }

  public GroupingStyle getGroupingStyle() {
    //
    // return groupingStyle;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getGroupingStyle").as(GroupingStyle.class);
  }

  public MoneyAmountStyle withExtendedGroupingSize(Integer extendedGroupingSize) {
    //
    // int sizeVal = (extendedGroupingSize == null ? -1 : extendedGroupingSize);
    // if (extendedGroupingSize != null && sizeVal < 0) {
    // throw new IllegalArgumentException("Extended grouping size must not be negative");
    // }
    // if (sizeVal == this.extendedGroupingSize) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // sizeVal,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withExtendedGroupingSize", extendedGroupingSize)
        .as(MoneyAmountStyle.class);
  }

  public Integer getExtendedGroupingSize() {
    //
    // return extendedGroupingSize < 0 ? null : extendedGroupingSize;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getExtendedGroupingSize").as(Integer.class);
  }

  public MoneyAmountStyle withGroupingSize(Integer groupingSize) {
    //
    // int sizeVal = (groupingSize == null ? -1 : groupingSize);
    // if (groupingSize != null && sizeVal <= 0) {
    // throw new IllegalArgumentException("Grouping size must be greater than zero");
    // }
    // if (sizeVal == this.groupingSize) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // sizeVal,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withGroupingSize", groupingSize).as(MoneyAmountStyle.class);
  }

  public Integer getGroupingSize() {
    //
    // return groupingSize < 0 ? null : groupingSize;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getGroupingSize").as(Integer.class);
  }

  public MoneyAmountStyle withGroupingCharacter(Character groupingCharacter) {
    //
    // int groupingVal = (groupingCharacter == null ? -1 : groupingCharacter);
    // if (groupingVal == this.groupingCharacter) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingVal,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withGroupingCharacter", groupingCharacter)
        .as(MoneyAmountStyle.class);
  }

  public Character getGroupingCharacter() {
    //
    // return groupingCharacter < 0 ? null : (char) groupingCharacter;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getGroupingCharacter").as(Character.class);
  }

  public MoneyAmountStyle withDecimalPointCharacter(Character decimalPointCharacter) {
    //
    // int dpVal = (decimalPointCharacter == null ? -1 : decimalPointCharacter);
    // if (dpVal == this.decimalPointCharacter) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeCharacter,
    // dpVal,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withDecimalPointCharacter", decimalPointCharacter)
        .as(MoneyAmountStyle.class);
  }

  public Character getDecimalPointCharacter() {
    //
    // return decimalPointCharacter < 0 ? null : (char) decimalPointCharacter;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getDecimalPointCharacter").as(Character.class);
  }

  public MoneyAmountStyle withNegativeSignCharacter(Character negativeCharacter) {
    //
    // int negativeVal = (negativeCharacter == null ? -1 : negativeCharacter);
    // if (negativeVal == this.negativeCharacter) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveCharacter,
    // negativeVal,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withNegativeSignCharacter", negativeCharacter)
        .as(MoneyAmountStyle.class);
  }

  public Character getNegativeSignCharacter() {
    //
    // return negativeCharacter < 0 ? null : (char) negativeCharacter;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getNegativeSignCharacter").as(Character.class);
  }

  public MoneyAmountStyle withPositiveSignCharacter(Character positiveCharacter) {
    //
    // int positiveVal = (positiveCharacter == null ? -1 : positiveCharacter);
    // if (positiveVal == this.positiveCharacter) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroCharacter,
    // positiveVal,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj
        .invokeMember("withPositiveSignCharacter", positiveCharacter)
        .as(MoneyAmountStyle.class);
  }

  public Character getPositiveSignCharacter() {
    //
    // return positiveCharacter < 0 ? null : (char) positiveCharacter;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getPositiveSignCharacter").as(Character.class);
  }

  public MoneyAmountStyle withZeroCharacter(Character zeroCharacter) {
    //
    // int zeroVal = (zeroCharacter == null ? -1 : zeroCharacter);
    // if (zeroVal == this.zeroCharacter) {
    // return this;
    // }
    // return new MoneyAmountStyle(
    // zeroVal,
    // positiveCharacter,
    // negativeCharacter,
    // decimalPointCharacter,
    // groupingStyle,
    // groupingCharacter,
    // groupingSize,
    // extendedGroupingSize,
    // forceDecimalPoint,
    // absValue);
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("withZeroCharacter", zeroCharacter).as(MoneyAmountStyle.class);
  }

  public Character getZeroCharacter() {
    //
    // return zeroCharacter < 0 ? null : (char) zeroCharacter;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("getZeroCharacter").as(Character.class);
  }

  public MoneyAmountStyle localize(Locale locale) {
    //
    // MoneyFormatter.checkNotNull(locale, "Locale must not be null");
    // MoneyAmountStyle result = this;
    // MoneyAmountStyle protoStyle = null;
    // if (zeroCharacter < 0) {
    // protoStyle = getLocalizedStyle(locale);
    // result = result.withZeroCharacter(protoStyle.getZeroCharacter());
    // }
    // if (positiveCharacter < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withPositiveSignCharacter(protoStyle.getPositiveSignCharacter());
    // }
    // if (negativeCharacter < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withNegativeSignCharacter(protoStyle.getNegativeSignCharacter());
    // }
    // if (decimalPointCharacter < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withDecimalPointCharacter(protoStyle.getDecimalPointCharacter());
    // }
    // if (groupingCharacter < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withGroupingCharacter(protoStyle.getGroupingCharacter());
    // }
    // if (groupingSize < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withGroupingSize(protoStyle.getGroupingSize());
    // }
    // if (extendedGroupingSize < 0) {
    // protoStyle = (protoStyle == null ? getLocalizedStyle(locale) : protoStyle);
    // result = result.withExtendedGroupingSize(protoStyle.getExtendedGroupingSize());
    // }
    // return result;
    //

    // TODO: Check the type mapping below!
    return this.obj.invokeMember("localize", locale).as(MoneyAmountStyle.class);
  }

  public static MoneyAmountStyle of(Locale locale) {
    //
    // return getLocalizedStyle(locale);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("of", locale).as(MoneyAmountStyle.class);
  }

  private static MoneyAmountStyle getLocalizedStyle(Locale locale) {
    //
    // MoneyAmountStyle protoStyle = LOCALIZED_CACHE.get(locale);
    // if (protoStyle == null) {
    // DecimalFormatSymbols symbols = DecimalFormatSymbols.getInstance(locale);
    // NumberFormat format = NumberFormat.getCurrencyInstance(locale);
    // int size =
    // (format instanceof DecimalFormat
    // ? ((DecimalFormat) format).getGroupingSize()
    // : 3);
    // size = size <= 0 ? 3 : size;
    // protoStyle =
    // new MoneyAmountStyle(
    // symbols.getZeroDigit(),
    // '+',
    // symbols.getMinusSign(),
    // symbols.getMonetaryDecimalSeparator(),
    // GroupingStyle.FULL,
    // symbols.getGroupingSeparator(),
    // size,
    // 0,
    // false,
    // false);
    // LOCALIZED_CACHE.putIfAbsent(locale, protoStyle);
    // }
    // return protoStyle;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getLocalizedStyle", locale).as(MoneyAmountStyle.class);
  }

  private MoneyAmountStyle(
      int zeroCharacter,
      int positiveCharacter,
      int negativeCharacter,
      int decimalPointCharacter,
      GroupingStyle groupingStyle,
      int groupingCharacter,
      int groupingSize,
      int extendedGroupingSize,
      boolean forceDecimalPoint,
      boolean absValue) {
    //
    //
    // this.zeroCharacter = zeroCharacter;
    // this.positiveCharacter = positiveCharacter;
    // this.negativeCharacter = negativeCharacter;
    // this.decimalPointCharacter = decimalPointCharacter;
    // this.groupingStyle = groupingStyle;
    // this.groupingCharacter = groupingCharacter;
    // this.groupingSize = groupingSize;
    // this.extendedGroupingSize = extendedGroupingSize;
    // this.forceDecimalPoint = forceDecimalPoint;
    // this.absValue = absValue;
    //

    this.obj =
        clz.invokeMember(
            "__init__",
            zeroCharacter,
            positiveCharacter,
            negativeCharacter,
            decimalPointCharacter,
            groupingStyle,
            groupingCharacter,
            groupingSize,
            extendedGroupingSize,
            forceDecimalPoint,
            absValue);
  }
}
