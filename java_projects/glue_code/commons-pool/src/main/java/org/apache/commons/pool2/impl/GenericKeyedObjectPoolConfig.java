package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public class GenericKeyedObjectPoolConfig<T> extends BaseObjectPoolConfig<T> {
  public static final int DEFAULT_MAX_IDLE_PER_KEY = 8;
  public static final int DEFAULT_MIN_IDLE_PER_KEY = 0;
  public static final int DEFAULT_MAX_TOTAL = -1;
  public static final int DEFAULT_MAX_TOTAL_PER_KEY = 8;
  private int maxTotal = DEFAULT_MAX_TOTAL;
  private int maxTotalPerKey = DEFAULT_MAX_TOTAL_PER_KEY;
  private int maxIdlePerKey = DEFAULT_MAX_IDLE_PER_KEY;
  private int minIdlePerKey = DEFAULT_MIN_IDLE_PER_KEY;
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/GenericKeyedObjectPoolConfig.py", "GenericKeyedObjectPoolConfig");
  private Value obj;

  public GenericKeyedObjectPoolConfig(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  protected void toStringAppendFields(final StringBuilder builder) {
    //
    // super.toStringAppendFields(builder);
    // builder.append(", minIdlePerKey=");
    // builder.append(minIdlePerKey);
    // builder.append(", maxIdlePerKey=");
    // builder.append(maxIdlePerKey);
    // builder.append(", maxTotalPerKey=");
    // builder.append(maxTotalPerKey);
    // builder.append(", maxTotal=");
    // builder.append(maxTotal);
    //

    obj.invokeMember("toStringAppendFields", builder);
  }

  public GenericKeyedObjectPoolConfig<T> clone() {
    //
    // try {
    // return (GenericKeyedObjectPoolConfig<T>) super.clone();
    // } catch (final CloneNotSupportedException e) {
    // throw new AssertionError(); // Can't happen
    // }
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("clone").as(GenericKeyedObjectPoolConfig.class);
  }

  public void setMinIdlePerKey(final int minIdlePerKey) {
    //
    // this.minIdlePerKey = minIdlePerKey;
    //

    obj.invokeMember("setMinIdlePerKey", minIdlePerKey);
  }

  public void setMaxTotalPerKey(final int maxTotalPerKey) {
    //
    // this.maxTotalPerKey = maxTotalPerKey;
    //

    obj.invokeMember("setMaxTotalPerKey", maxTotalPerKey);
  }

  public void setMaxTotal(final int maxTotal) {
    //
    // this.maxTotal = maxTotal;
    //

    obj.invokeMember("setMaxTotal", maxTotal);
  }

  public void setMaxIdlePerKey(final int maxIdlePerKey) {
    //
    // this.maxIdlePerKey = maxIdlePerKey;
    //

    obj.invokeMember("setMaxIdlePerKey", maxIdlePerKey);
  }

  public int getMinIdlePerKey() {
    //
    // return minIdlePerKey;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMinIdlePerKey").as(int.class);
  }

  public int getMaxTotalPerKey() {
    //
    // return maxTotalPerKey;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxTotalPerKey").as(int.class);
  }

  public int getMaxTotal() {
    //
    // return maxTotal;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxTotal").as(int.class);
  }

  public int getMaxIdlePerKey() {
    //
    // return maxIdlePerKey;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxIdlePerKey").as(int.class);
  }

  public GenericKeyedObjectPoolConfig() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
