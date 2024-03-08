package org.apache.commons.validator.util;

import java.io.Serializable;
import org.apache.commons.validator.ContextInitializer;
import org.graalvm.polyglot.Value;

public class Flags implements Serializable, Cloneable {
  private long flags = 0;
  private static final long serialVersionUID = 8481587558770237995L;
  private static Value clz = ContextInitializer.getPythonClass("/util/Flags.py", "Flags");
  private Value obj;

  public Flags(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // StringBuilder bin = new StringBuilder(Long.toBinaryString(this.flags));
    // for (int i = 64 - bin.length(); i > 0; i--) { // CHECKSTYLE IGNORE MagicNumber
    // bin.insert(0, "0");
    // }
    // return bin.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return (int) this.flags;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(Object obj) {
    //
    // if (!(obj instanceof Flags)) {
    // return false;
    // }
    //
    // if (obj == this) {
    // return true;
    // }
    //
    // Flags f = (Flags) obj;
    //
    // return this.flags == f.flags;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public Object clone() {
    //
    // try {
    // return super.clone();
    // } catch (CloneNotSupportedException e) {
    // throw new RuntimeException("Couldn't clone Flags object.");
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("clone").as(Object.class);
  }

  public void turnOnAll() {
    //
    // this.flags = 0xFFFFFFFFFFFFFFFFl;
    //

    obj.invokeMember("turnOnAll");
  }

  public void clear() {
    //
    // this.flags = 0;
    //

    obj.invokeMember("clear");
  }

  public void turnOffAll() {
    //
    // this.flags = 0;
    //

    obj.invokeMember("turnOffAll");
  }

  public void turnOff(long flag) {
    //
    // this.flags &= ~flag;
    //

    obj.invokeMember("turnOff", flag);
  }

  public void turnOn(long flag) {
    //
    // this.flags |= flag;
    //

    obj.invokeMember("turnOn", flag);
  }

  public boolean isOff(long flag) {
    //
    // return (this.flags & flag) == 0;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOff", flag).as(boolean.class);
  }

  public boolean isOn(long flag) {
    //
    // return (this.flags & flag) == flag;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isOn", flag).as(boolean.class);
  }

  public long getFlags() {
    //
    // return this.flags;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getFlags").as(long.class);
  }

  public Flags(int constructorId, long flags) {
    //
    // super();
    // if (constructorId == 1) {
    // this.flags = flags;
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, flags);
  }
}
