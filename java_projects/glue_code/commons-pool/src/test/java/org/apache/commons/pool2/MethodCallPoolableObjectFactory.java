package org.apache.commons.pool;

import java.util.ArrayList;
import java.util.List;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class MethodCallPoolableObjectFactory {
  private boolean valid = true;
  private final List<MethodCall> methodCalls = new ArrayList<>();
  private static Value clz =
      ContextInitializer.getPythonClass(
          "/MethodCallPoolableObjectFactory.py", "MethodCallPoolableObjectFactory");
  private Value obj;

  public MethodCallPoolableObjectFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean validateObject(final PooledObject<Object> obj) {
    //
    // final MethodCall call = MethodCall.MethodCall1("validateObject", obj.getObject());
    // methodCalls.add(call);
    // if (validateObjectFail) {
    // throw new PrivateException("validateObject");
    // }
    // final boolean r = valid;
    // call.returned(Boolean.valueOf(r));
    // return r;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject", obj).as(boolean.class);
  }

  public void setValidateObjectFail(final boolean validateObjectFail) {
    //
    // this.validateObjectFail = validateObjectFail;
    //

    obj.invokeMember("setValidateObjectFail", validateObjectFail);
  }

  public void setValid(final boolean valid) {
    //
    // this.valid = valid;
    //

    obj.invokeMember("setValid", valid);
  }

  public void setPassivateObjectFail(final boolean passivateObjectFail) {
    //
    // this.passivateObjectFail = passivateObjectFail;
    //

    obj.invokeMember("setPassivateObjectFail", passivateObjectFail);
  }

  public void setMakeObjectFail(final boolean makeObjectFail) {
    //
    // this.makeObjectFail = makeObjectFail;
    //

    obj.invokeMember("setMakeObjectFail", makeObjectFail);
  }

  public void setDestroyObjectFail(final boolean destroyObjectFail) {
    //
    // this.destroyObjectFail = destroyObjectFail;
    //

    obj.invokeMember("setDestroyObjectFail", destroyObjectFail);
  }

  public void setCurrentCount(final int count) {
    //
    // this.count = count;
    //

    obj.invokeMember("setCurrentCount", count);
  }

  public void setActivateObjectFail(final boolean activateObjectFail) {
    //
    // this.activateObjectFail = activateObjectFail;
    //

    obj.invokeMember("setActivateObjectFail", activateObjectFail);
  }

  public void reset() {
    //
    // count = 0;
    // getMethodCalls().clear();
    // setMakeObjectFail(false);
    // setActivateObjectFail(false);
    // setValid(true);
    // setValidateObjectFail(false);
    // setPassivateObjectFail(false);
    // setDestroyObjectFail(false);
    //

    obj.invokeMember("reset");
  }

  public void passivateObject(final PooledObject<Object> obj) throws Exception {
    try {
      //
      // methodCalls.add(MethodCall.MethodCall1("passivateObject", obj.getObject()));
      // if (passivateObjectFail) {
      // throw new PrivateException("passivateObject");
      // }
      //

      obj.invokeMember("passivateObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception)
          ExceptionHandler.handle(e, "MethodCallPoolableObjectFactory.passivateObject");
    }
  }

  public boolean isValidateObjectFail() {
    //
    // return validateObjectFail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValidateObjectFail").as(boolean.class);
  }

  public boolean isValid() {
    //
    // return valid;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid").as(boolean.class);
  }

  public boolean isPassivateObjectFail() {
    //
    // return passivateObjectFail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isPassivateObjectFail").as(boolean.class);
  }

  public boolean isMakeObjectFail() {
    //
    // return makeObjectFail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isMakeObjectFail").as(boolean.class);
  }

  public boolean isDestroyObjectFail() {
    //
    // return destroyObjectFail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isDestroyObjectFail").as(boolean.class);
  }

  public boolean isActivateObjectFail() {
    //
    // return activateObjectFail;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isActivateObjectFail").as(boolean.class);
  }

  public List<MethodCall> getMethodCalls() {
    //
    // return methodCalls;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMethodCalls").as(List.class);
  }

  public int getCurrentCount() {
    //
    // return count;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCurrentCount").as(int.class);
  }

  public void destroyObject(final PooledObject<Object> obj) throws Exception {
    try {
      //
      // methodCalls.add(MethodCall.MethodCall1("destroyObject", obj.getObject()));
      // if (destroyObjectFail) {
      // throw new PrivateException("destroyObject");
      // }
      //

      obj.invokeMember("destroyObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "MethodCallPoolableObjectFactory.destroyObject");
    }
  }

  public void activateObject(final PooledObject<Object> obj) throws Exception {
    try {
      //
      // methodCalls.add(MethodCall.MethodCall1("activateObject", obj.getObject()));
      // if (activateObjectFail) {
      // throw new PrivateException("activateObject");
      // }
      //

      obj.invokeMember("activateObject", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception)
          ExceptionHandler.handle(e, "MethodCallPoolableObjectFactory.activateObject");
    }
  }
}
