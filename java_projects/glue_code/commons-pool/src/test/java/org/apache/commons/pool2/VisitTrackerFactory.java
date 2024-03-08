package org.apache.commons.pool;

import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class VisitTrackerFactory<K> {
  private static Value clz =
      ContextInitializer.getPythonClass("/VisitTrackerFactory.py", "VisitTrackerFactory");
  private Value obj;

  public VisitTrackerFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean validateObject1(final PooledObject<VisitTracker<K>> ref) {
    //
    // return ref.getObject().validate();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject1", ref).as(boolean.class);
  }

  public boolean validateObject0(final K key, final PooledObject<VisitTracker<K>> ref) {
    //
    // return ref.getObject().validate();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject0", key, ref).as(boolean.class);
  }

  public void resetId() {
    //
    // nextId = 0;
    //

    obj.invokeMember("resetId");
  }

  public void passivateObject1(final PooledObject<VisitTracker<K>> ref) throws Exception {
    try {
      //
      // ref.getObject().passivate();
      //

      obj.invokeMember("passivateObject1", ref);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "VisitTrackerFactory.passivateObject1");
    }
  }

  public void passivateObject0(final K key, final PooledObject<VisitTracker<K>> ref)
      throws Exception {
    try {
      //
      // ref.getObject().passivate();
      //

      obj.invokeMember("passivateObject0", key, ref);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "VisitTrackerFactory.passivateObject0");
    }
  }

  public void destroyObject1(final PooledObject<VisitTracker<K>> ref) {
    //
    // ref.getObject().destroy();
    //

    obj.invokeMember("destroyObject1", ref);
  }

  public void destroyObject0(final K key, final PooledObject<VisitTracker<K>> ref) {
    //
    // ref.getObject().destroy();
    //

    obj.invokeMember("destroyObject0", key, ref);
  }

  public void activateObject1(final PooledObject<VisitTracker<K>> ref) throws Exception {
    try {
      //
      // ref.getObject().activate();
      //

      obj.invokeMember("activateObject1", ref);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "VisitTrackerFactory.activateObject1");
    }
  }

  public void activateObject0(final K key, final PooledObject<VisitTracker<K>> ref)
      throws Exception {
    try {
      //
      // ref.getObject().activate();
      //

      obj.invokeMember("activateObject0", key, ref);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "VisitTrackerFactory.activateObject0");
    }
  }

  public VisitTrackerFactory() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
