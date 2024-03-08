package org.apache.commons.pool;

import java.lang.reflect.Method;
import org.apache.commons.pool2.UsageTracking;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

class BaseProxyHandler<T> {
  private static Value clz =
      ContextInitializer.getPythonClass("/BaseProxyHandler.py", "BaseProxyHandler");
  private Value obj;

  public BaseProxyHandler(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append(getClass().getName());
    // builder.append(" [pooledObject=");
    // builder.append(pooledObject);
    // builder.append(", usageTracking=");
    // builder.append(usageTracking);
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  void validateProxiedObject() {
    //
    // if (pooledObject == null) {
    // throw new IllegalStateException(
    // "This object may no longer be "
    // + "used as it has been returned to the Object Pool.");
    // }
    //

    obj.invokeMember("validateProxiedObject");
  }

  T getPooledObject() {
    //
    // return pooledObject;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPooledObject").as(T.class);
  }

  Object doInvoke(final Method method, final Object[] args) throws Throwable {
    try {
      //
      // validateProxiedObject();
      // final T object = getPooledObject();
      // if (usageTracking != null) {
      // usageTracking.use(object);
      // }
      // return method.invoke(object, args);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("doInvoke", method, args).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle Throwable
      throw (Throwable) ExceptionHandler.handle(e, "BaseProxyHandler.doInvoke");
    }
  }

  T disableProxy() {
    //
    // final T result = pooledObject;
    // pooledObject = null;
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("disableProxy").as(T.class);
  }

  BaseProxyHandler(final T pooledObject, final UsageTracking<T> usageTracking) {
    //
    // this.pooledObject = pooledObject;
    // this.usageTracking = usageTracking;
    //

    this.obj = clz.invokeMember("__init__", pooledObject, usageTracking);
  }
}
