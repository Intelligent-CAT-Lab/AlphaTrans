package org.apache.commons.pool;

import java.lang.ref.SoftReference;
import org.graalvm.polyglot.Value;

public class PooledSoftReference<T> extends DefaultPooledObject<T> {
  private static Value clz =
      ContextInitializer.getPythonClass("/PooledSoftReference.py", "PooledSoftReference");
  private Value obj;

  public PooledSoftReference(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder result = new StringBuilder();
    // result.append("Referenced Object: ");
    // result.append(getObject().toString());
    // result.append(", State: ");
    // synchronized (this) {
    // result.append(getState().toString());
    // }
    // return result.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public T getObject() {
    //
    // return reference.get();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getObject").as(T.class);
  }

  public synchronized void setReference(final SoftReference<T> reference) {
    //
    // this.reference = reference;
    //

    obj.invokeMember("setReference", reference);
  }

  public synchronized SoftReference<T> getReference() {
    //
    // return reference;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getReference").as(SoftReference.class);
  }

  public PooledSoftReference(final SoftReference<T> reference) {
    //
    // super(null); // Null the hard reference in the parent
    // this.reference = reference;
    //

    this.obj = clz.invokeMember("__init__", reference);
  }
}
