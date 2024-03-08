package org.apache.commons.pool;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import org.apache.commons.pool2.UsageTracking;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

class JdkProxyHandler<T> extends BaseProxyHandler<T> implements InvocationHandler {
  private static Value clz =
      ContextInitializer.getPythonClass("/JdkProxyHandler.py", "JdkProxyHandler");
  private Value obj;

  public JdkProxyHandler(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public Object invoke(final Object proxy, final Method method, final Object[] args)
      throws Throwable {
    try {
      //
      // return doInvoke(method, args);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("invoke", proxy, method, args).as(Object.class);
    } catch (PolyglotException e) {
      // TODO: Handle Throwable
      throw (Throwable) ExceptionHandler.handle(e, "JdkProxyHandler.invoke");
    }
  }

  JdkProxyHandler(final T pooledObject, final UsageTracking<T> usageTracking) {
    //
    // super(pooledObject, usageTracking);
    //

    this.obj = clz.invokeMember("__init__", pooledObject, usageTracking);
  }
}
