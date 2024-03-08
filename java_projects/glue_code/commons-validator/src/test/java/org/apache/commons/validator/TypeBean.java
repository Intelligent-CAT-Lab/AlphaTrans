package org.apache.commons.validator;

import org.graalvm.polyglot.Value;

public class TypeBean {
  private String sCreditCard = null;
  private String sDate = null;
  private String sDouble = null;
  private String sFloat = null;
  private String sLong = null;
  private String sInteger = null;
  private String sShort = null;
  private String sByte = null;
  private static Value clz = ContextInitializer.getPythonClass("/TypeBean.py", "TypeBean");
  private Value obj;

  public TypeBean(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void setCreditCard(String sCreditCard) {
    //
    // this.sCreditCard = sCreditCard;
    //

    obj.invokeMember("setCreditCard", sCreditCard);
  }

  public String getCreditCard() {
    //
    // return sCreditCard;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreditCard").as(String.class);
  }

  public void setDate(String sDate) {
    //
    // this.sDate = sDate;
    //

    obj.invokeMember("setDate", sDate);
  }

  public String getDate() {
    //
    // return sDate;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDate").as(String.class);
  }

  public void setDouble(String sDouble) {
    //
    // this.sDouble = sDouble;
    //

    obj.invokeMember("setDouble", sDouble);
  }

  public String getDouble() {
    //
    // return sDouble;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getDouble").as(String.class);
  }

  public void setFloat(String sFloat) {
    //
    // this.sFloat = sFloat;
    //

    obj.invokeMember("setFloat", sFloat);
  }

  public String getFloat() {
    //
    // return sFloat;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFloat").as(String.class);
  }

  public void setLong(String sLong) {
    //
    // this.sLong = sLong;
    //

    obj.invokeMember("setLong", sLong);
  }

  public String getLong() {
    //
    // return sLong;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLong").as(String.class);
  }

  public void setInteger(String sInteger) {
    //
    // this.sInteger = sInteger;
    //

    obj.invokeMember("setInteger", sInteger);
  }

  public String getInteger() {
    //
    // return sInteger;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getInteger").as(String.class);
  }

  public void setShort(String sShort) {
    //
    // this.sShort = sShort;
    //

    obj.invokeMember("setShort", sShort);
  }

  public String getShort() {
    //
    // return sShort;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getShort").as(String.class);
  }

  public void setByte(String sByte) {
    //
    // this.sByte = sByte;
    //

    obj.invokeMember("setByte", sByte);
  }

  public String getByte() {
    //
    // return sByte;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getByte").as(String.class);
  }
}
