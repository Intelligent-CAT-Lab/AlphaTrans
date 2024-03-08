package org.apache.commons.pool;

import org.apache.commons.pool2.PooledObject;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class SleepingObjectFactory {
  private static Value clz =
      ContextInitializer.getPythonClass("/SleepingObjectFactory.py", "SleepingObjectFactory");
  private Value obj;

  public SleepingObjectFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean validateObject(final PooledObject<Integer> obj) {
    //
    // debug("validateObject", obj);
    // Waiter.sleepQuietly(30);
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject", obj).as(boolean.class);
  }

  public void setDebug(final boolean b) {
    //
    // debug = b;
    //

    obj.invokeMember("setDebug", b);
  }

  public void passivateObject(final PooledObject<Integer> obj) throws Exception {
    try {
      //
      // debug("passivateObject", obj);
      // Waiter.sleepQuietly(10);
      //

      obj.invokeMember("passivateObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "SleepingObjectFactory.passivateObject");
    }
  }

  public boolean isDebug() {
    //
    // return debug;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDebug").as(boolean.class);
  }

  public void destroyObject(final PooledObject<Integer> obj) throws Exception {
    try {
      //
      // debug("destroyObject", obj);
      // Waiter.sleepQuietly(250);
      //

      obj.invokeMember("destroyObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "SleepingObjectFactory.destroyObject");
    }
  }

  public void activateObject(final PooledObject<Integer> obj) throws Exception {
    try {
      //
      // debug("activateObject", obj);
      // Waiter.sleepQuietly(10);
      //

      obj.invokeMember("activateObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "SleepingObjectFactory.activateObject");
    }
  }

  private void debug(final String method, final Object obj) {
    //
    // if (debug) {
    // final String thread = "thread" + Thread.currentThread().getName();
    // System.out.println(thread + ": " + method + " " + obj);
    // }
    //

    obj.invokeMember("debug", method, obj);
  }
}
