package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public class GenericObjectPoolConfig<T> extends BaseObjectPoolConfig<T> {
  public static final int DEFAULT_MIN_IDLE = 0;
  public static final int DEFAULT_MAX_IDLE = 8;
  public static final int DEFAULT_MAX_TOTAL = 8;
  private int minIdle = DEFAULT_MIN_IDLE;
  private int maxIdle = DEFAULT_MAX_IDLE;
  private int maxTotal = DEFAULT_MAX_TOTAL;
  private static Value clz =
      ContextInitializer.getPythonClass("/GenericObjectPoolConfig.py", "GenericObjectPoolConfig");
  private Value obj;

  public GenericObjectPoolConfig(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void toStringAppendFields(final StringBuilder builder) {
    //
    // super.toStringAppendFields(builder);
    // builder.append(", maxTotal=");
    // builder.append(maxTotal);
    // builder.append(", maxIdle=");
    // builder.append(maxIdle);
    // builder.append(", minIdle=");
    // builder.append(minIdle);
    //

    obj.invokeMember("toStringAppendFields", builder);
  }

  public GenericObjectPoolConfig<T> clone() {
    //
    // try {
    // return (GenericObjectPoolConfig<T>) super.clone();
    // } catch (final CloneNotSupportedException e) {
    // throw new AssertionError(); // Can't happen
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("clone").as(GenericObjectPoolConfig.class);
  }

  public void setMinIdle(final int minIdle) {
    //
    // this.minIdle = minIdle;
    //

    obj.invokeMember("setMinIdle", minIdle);
  }

  public void setMaxTotal(final int maxTotal) {
    //
    // this.maxTotal = maxTotal;
    //

    obj.invokeMember("setMaxTotal", maxTotal);
  }

  public void setMaxIdle(final int maxIdle) {
    //
    // this.maxIdle = maxIdle;
    //

    obj.invokeMember("setMaxIdle", maxIdle);
  }

  public int getMinIdle() {
    //
    // return minIdle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinIdle").as(int.class);
  }

  public int getMaxTotal() {
    //
    // return maxTotal;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxTotal").as(int.class);
  }

  public int getMaxIdle() {
    //
    // return maxIdle;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxIdle").as(int.class);
  }
}
