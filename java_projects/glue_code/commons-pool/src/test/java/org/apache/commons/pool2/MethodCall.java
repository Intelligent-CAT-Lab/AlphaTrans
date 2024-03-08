package org.apache.commons.pool;

import java.util.List;
import org.graalvm.polyglot.Value;

public class MethodCall {
  private static Value clz = ContextInitializer.getPythonClass("/MethodCall.py", "MethodCall");
  private Value obj;

  public MethodCall(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder sb = new StringBuilder();
    // sb.append("MethodCall");
    // sb.append("{name='").append(name).append('\'');
    // if (!params.isEmpty()) {
    // sb.append(", params=").append(params);
    // }
    // if (returned != null) {
    // sb.append(", returned=").append(returned);
    // }
    // sb.append('}');
    // return sb.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // int result;
    // result = name != null ? name.hashCode() : 0;
    // result = 29 * result + (params != null ? params.hashCode() : 0);
    // result = 29 * result + (returned != null ? returned.hashCode() : 0);
    // return result;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(final Object o) {
    //
    // if (this == o) {
    // return true;
    // }
    // if (o == null || getClass() != o.getClass()) {
    // return false;
    // }
    //
    // final MethodCall that = (MethodCall) o;
    //
    // if (!Objects.equals(name, that.name)) {
    // return false;
    // }
    // if (!Objects.equals(params, that.params)) {
    // return false;
    // }
    // return Objects.equals(returned, that.returned);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", o).as(boolean.class);
  }

  public void setReturned(final Object returned) {
    //
    // this.returned = returned;
    //

    obj.invokeMember("setReturned", returned);
  }

  public MethodCall returned(final Object obj) {
    //
    // setReturned(obj);
    // return this;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("returned", obj).as(MethodCall.class);
  }

  public Object getReturned() {
    //
    // return returned;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getReturned").as(Object.class);
  }

  public List<Object> getParams() {
    //
    // return params;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getParams").as(List.class);
  }

  public String getName() {
    //
    // return name;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getName").as(String.class);
  }

  public static MethodCall MethodCall3(final String name) {
    //
    // return new MethodCall(2, null, null, null, name, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MethodCall3", name).as(MethodCall.class);
  }

  public static MethodCall MethodCall1(final String name, final Object param) {
    //
    // return new MethodCall(2, null, Collections.singletonList(param), null, name, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MethodCall1", name, param).as(MethodCall.class);
  }

  public static MethodCall MethodCall0(
      final String name, final Object param1, final Object param2) {
    //
    // return new MethodCall(2, null, Arrays.asList(param1, param2), null, name, null);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("MethodCall0", name, param1, param2).as(MethodCall.class);
  }

  public MethodCall(
      int constructorId,
      final Object param2,
      final List<Object> params,
      final Object param1,
      final String name,
      final Object param) {
    //
    // if (constructorId == 2) {
    //
    // if (name == null) {
    // throw new IllegalArgumentException("name must not be null.");
    // }
    // this.name = name;
    // if (params != null) {
    // this.params = params;
    // } else {
    // this.params = Collections.emptyList();
    // }
    // } else {
    //
    // if (name == null) {
    // throw new IllegalArgumentException("name must not be null.");
    // }
    // this.name = name;
    // if (params != null) {
    // this.params = params;
    // } else {
    // this.params = Collections.emptyList();
    // }
    // }
    //

    this.obj = clz.invokeMember("__init__", constructorId, param2, params, param1, name, param);
  }
}
