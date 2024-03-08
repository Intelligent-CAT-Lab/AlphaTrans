package org.apache.commons.pool;

import org.graalvm.polyglot.PolyglotException;

public interface PooledObjectFactory<T> {
  boolean validateObject(PooledObject<T> p);

  void passivateObject(PooledObject<T> p) throws Exception;

  PooledObject<T> makeObject() throws Exception;

  void destroyObject0(PooledObject<T> p) throws Exception;

  void activateObject(PooledObject<T> p) throws Exception;

  default void destroyObject1(final PooledObject<T> p, final DestroyMode destroyMode)
      throws Exception {
    try {
      //
      // destroyObject0(p);
      //

      obj.invokeMember("destroyObject1");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "PooledObjectFactory.destroyObject1");
    }
  }
}
