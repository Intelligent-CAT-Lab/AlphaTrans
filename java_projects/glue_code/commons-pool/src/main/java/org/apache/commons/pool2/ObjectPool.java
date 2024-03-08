package org.apache.commons.pool;

import java.io.Closeable;
import java.util.NoSuchElementException;
import org.graalvm.polyglot.PolyglotException;

public interface ObjectPool<T> extends Closeable {
  void returnObject(T obj) throws Exception;

  void invalidateObject0(T obj) throws Exception;

  int getNumIdle();

  int getNumActive();

  void close();

  void clear() throws Exception, UnsupportedOperationException;

  T borrowObject() throws Exception, NoSuchElementException, IllegalStateException;

  void addObject() throws Exception, IllegalStateException, UnsupportedOperationException;

  default void invalidateObject1(final T obj, final DestroyMode destroyMode) throws Exception {
    try {
      //
      // invalidateObject0(obj);
      //

      obj.invokeMember("invalidateObject1");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "ObjectPool.invalidateObject1");
    }
  }

  default void addObjects(final int count) throws Exception {
    try {
      //
      // for (int i = 0; i < count; i++) {
      // addObject();
      // }
      //

      obj.invokeMember("addObjects");
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "ObjectPool.addObjects");
    }
  }
}
