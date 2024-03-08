package org.apache.commons.pool;

import org.graalvm.polyglot.Value;

public class VisitTracker<K> {
  private static Value clz = ContextInitializer.getPythonClass("/VisitTracker.py", "VisitTracker");
  private Value obj;

  public VisitTracker(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // return "Key: " + key + " id: " + id;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public boolean validate() {
    //
    // if (destroyed) {
    // fail("attempted to validate a destroyed object");
    // }
    // validateCount++;
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validate").as(boolean.class);
  }

  public void reset() {
    //
    // validateCount = 0;
    // activateCount = 0;
    // passivateCount = 0;
    // destroyed = false;
    //

    obj.invokeMember("reset");
  }

  public void passivate() {
    //
    // if (destroyed) {
    // fail("attempted to passivate a destroyed object");
    // }
    // passivateCount++;
    //

    obj.invokeMember("passivate");
  }

  public boolean isDestroyed() {
    //
    // return destroyed;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDestroyed").as(boolean.class);
  }

  public int getValidateCount() {
    //
    // return validateCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValidateCount").as(int.class);
  }

  public int getPassivateCount() {
    //
    // return passivateCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPassivateCount").as(int.class);
  }

  public K getKey() {
    //
    // return key;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getKey").as(K.class);
  }

  public int getId() {
    //
    // return id;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getId").as(int.class);
  }

  public int getActivateCount() {
    //
    // return activateCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getActivateCount").as(int.class);
  }

  public void destroy() {
    //
    // destroyed = true;
    //

    obj.invokeMember("destroy");
  }

  public void activate() {
    //
    // if (destroyed) {
    // fail("attempted to activate a destroyed object");
    // }
    // activateCount++;
    //

    obj.invokeMember("activate");
  }

  public VisitTracker(int constructorId, final K key, final int id) {
    //
    // if (constructorId == 0) {
    //
    // this.id = id;
    // this.key = key;
    // reset();
    // } else if (constructorId == 1) {
    //
    // this.id = id;
    // reset();
    // } else {
    //
    // reset();
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, key, id);
  }

  private void fail(final String message) {
    //
    // throw new IllegalStateException(message);
    //

    obj.invokeMember("fail", message);
  }
}
