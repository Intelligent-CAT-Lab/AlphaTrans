package org.apache.commons.pool;

import org.graalvm.polyglot.PolyglotException;

public interface KeyedPooledObjectFactory<K, V> {
  boolean validateObject(K key, PooledObject<V> p);

  void passivateObject(K key, PooledObject<V> p) throws Exception;

  PooledObject<V> makeObject(K key) throws Exception;

  void destroyObject0(K key, PooledObject<V> p) throws Exception;

  void activateObject(K key, PooledObject<V> p) throws Exception;

  default void destroyObject1(final K key, final PooledObject<V> p, final DestroyMode destroyMode)
      throws Exception {
    try {
      //
      // destroyObject0(key, p);
      //

      obj.invokeMember("destroyObject1");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "KeyedPooledObjectFactory.destroyObject1");
    }
  }
}
