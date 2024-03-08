package org.apache.commons.pool;

import org.apache.commons.pool2.UsageTracking;
import org.graalvm.polyglot.Value;

public class JdkProxySource<T> implements ProxySource<T> {
  private static Value clz =
      ContextInitializer.getPythonClass("/JdkProxySource.py", "JdkProxySource");
  private Value obj;

  public JdkProxySource(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("JdkProxySource [classLoader=");
    // builder.append(classLoader);
    // builder.append(", interfaces=");
    // builder.append(Arrays.toString(interfaces));
    // builder.append("]");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public T resolveProxy(final T proxy) {
    //
    // return ((JdkProxyHandler<T>) Proxy.getInvocationHandler(proxy)).disableProxy();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("resolveProxy", proxy).as(T.class);
  }

  public T createProxy(final T pooledObject, final UsageTracking<T> usageTracking) {
    //
    // return (T)
    // Proxy.newProxyInstance(
    // classLoader,
    // interfaces,
    // new JdkProxyHandler<>(pooledObject, usageTracking));
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("createProxy", pooledObject, usageTracking).as(T.class);
  }

  public JdkProxySource(final ClassLoader classLoader, final Class<?>[] interfaces) {
    //
    // this.classLoader = classLoader;
    // this.interfaces = new Class<?>[interfaces.length];
    // System.arraycopy(interfaces, 0, this.interfaces, 0, interfaces.length);
    //

    this.obj = clz.invokeMember("__init__", classLoader, interfaces);
  }
}
