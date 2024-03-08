package org.apache.commons.pool;

import org.apache.commons.pool2.PooledObject;
import org.graalvm.polyglot.Value;

public class DefaultPooledObjectInfo implements DefaultPooledObjectInfoMBean {
  private static final String PATTERN = "yyyy-MM-dd HH:mm:ss Z";
  private static Value clz =
      ContextInitializer.getPythonClass("/DefaultPooledObjectInfo.py", "DefaultPooledObjectInfo");
  private Value obj;

  public DefaultPooledObjectInfo(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("DefaultPooledObjectInfo [pooledObject=");
    // builder.append(pooledObject);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public String getPooledObjectType() {
    //
    // return pooledObject.getObject().getClass().getName();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPooledObjectType").as(String.class);
  }

  public String getPooledObjectToString() {
    //
    // return pooledObject.getObject().toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPooledObjectToString").as(String.class);
  }

  public String getLastReturnTimeFormatted() {
    //
    // return getTimeFormatted(getLastReturnTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastReturnTimeFormatted").as(String.class);
  }

  public long getLastReturnTime() {
    //
    // return pooledObject.getLastReturnInstant().toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastReturnTime").as(long.class);
  }

  public String getLastBorrowTrace() {
    //
    // final StringWriter sw = new StringWriter();
    // pooledObject.printStackTrace(new PrintWriter(sw));
    // return sw.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowTrace").as(String.class);
  }

  public String getLastBorrowTimeFormatted() {
    //
    // return getTimeFormatted(getLastBorrowTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowTimeFormatted").as(String.class);
  }

  public long getLastBorrowTime() {
    //
    // return pooledObject.getLastBorrowInstant().toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowTime").as(long.class);
  }

  public String getCreateTimeFormatted() {
    //
    // return getTimeFormatted(getCreateTime());
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreateTimeFormatted").as(String.class);
  }

  public long getCreateTime() {
    //
    // return pooledObject.getCreateInstant().toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreateTime").as(long.class);
  }

  public long getBorrowedCount() {
    //
    // return pooledObject.getBorrowedCount();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBorrowedCount").as(long.class);
  }

  public DefaultPooledObjectInfo(final PooledObject<?> pooledObject) {
    //
    // this.pooledObject = pooledObject;
    //

    this.obj = clz.invokeMember("__init__", pooledObject);
  }

  private String getTimeFormatted(final long millis) {
    //
    // return new SimpleDateFormat(PATTERN).format(Long.valueOf(millis));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getTimeFormatted", millis).as(String.class);
  }
}
