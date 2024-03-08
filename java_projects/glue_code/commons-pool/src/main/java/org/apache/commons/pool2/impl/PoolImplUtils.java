package org.apache.commons.pool;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.time.Duration;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.concurrent.TimeUnit;
import org.apache.commons.pool2.PooledObjectFactory;
import org.graalvm.polyglot.Value;

class PoolImplUtils {
  private static Value clz =
      ContextInitializer.getPythonClass("/PoolImplUtils.py", "PoolImplUtils");
  private Value obj;

  public PoolImplUtils(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  static Class<?> getFactoryType(final Class<? extends PooledObjectFactory> factoryClass) {
    //
    // final Class<PooledObjectFactory> type = PooledObjectFactory.class;
    // final Object genericType = getGenericType(type, factoryClass);
    // if (genericType instanceof Integer) {
    // final ParameterizedType pi = getParameterizedType(type, factoryClass);
    // if (pi != null) {
    // final Type[] bounds =
    // ((TypeVariable)
    // pi.getActualTypeArguments()[
    // ((Integer) genericType).intValue()])
    // .getBounds();
    // if (bounds != null && bounds.length > 0) {
    // final Type bound0 = bounds[0];
    // if (bound0 instanceof Class) {
    // return (Class<?>) bound0;
    // }
    // }
    // }
    // return Object.class;
    // }
    // return (Class<?>) genericType;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getFactoryType", factoryClass).as(Class.class);
  }

  static Duration toDuration(final long amount, final TimeUnit timeUnit) {
    //
    // return Duration.of(amount, PoolImplUtils.toChronoUnit(timeUnit));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toDuration", amount, timeUnit).as(Duration.class);
  }

  static Duration nonNull(final Duration value, final Duration defaultValue) {
    //
    // return value != null ? value : Objects.requireNonNull(defaultValue, "defaultValue");
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("nonNull", value, defaultValue).as(Duration.class);
  }

  static ChronoUnit toChronoUnit(final TimeUnit timeUnit) {
    //
    // switch (Objects.requireNonNull(timeUnit)) {
    // case NANOSECONDS:
    // return ChronoUnit.NANOS;
    // case MICROSECONDS:
    // return ChronoUnit.MICROS;
    // case MILLISECONDS:
    // return ChronoUnit.MILLIS;
    // case SECONDS:
    // return ChronoUnit.SECONDS;
    // case MINUTES:
    // return ChronoUnit.MINUTES;
    // case HOURS:
    // return ChronoUnit.HOURS;
    // case DAYS:
    // return ChronoUnit.DAYS;
    // default:
    // throw new IllegalArgumentException(timeUnit.toString());
    // }
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("toChronoUnit", timeUnit).as(ChronoUnit.class);
  }

  static Instant min(final Instant a, final Instant b) {
    //
    // return a.compareTo(b) < 0 ? a : b;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("min", a, b).as(Instant.class);
  }

  static Instant max(final Instant a, final Instant b) {
    //
    // return a.compareTo(b) > 0 ? a : b;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("max", a, b).as(Instant.class);
  }

  static boolean isPositive(final Duration delay) {
    //
    // return delay != null && !delay.isNegative() && !delay.isZero();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("isPositive", delay).as(boolean.class);
  }

  private static Object getTypeParameter(final Class<?> clazz, final Type argType) {
    //
    // if (argType instanceof Class<?>) {
    // return argType;
    // }
    // final TypeVariable<?>[] tvs = clazz.getTypeParameters();
    // for (int i = 0; i < tvs.length; i++) {
    // if (tvs[i].equals(argType)) {
    // return Integer.valueOf(i);
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getTypeParameter", clazz, argType).as(Object.class);
  }

  private static <T> ParameterizedType getParameterizedType(
      final Class<T> type, final Class<? extends T> clazz) {
    //
    // for (final Type iface : clazz.getGenericInterfaces()) {
    // if (iface instanceof ParameterizedType) {
    // final ParameterizedType pi = (ParameterizedType) iface;
    // if (pi.getRawType() instanceof Class
    // && type.isAssignableFrom((Class<?>) pi.getRawType())) {
    // return pi;
    // }
    // }
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getParameterizedType", type, clazz).as(ParameterizedType.class);
  }

  private static <T> Object getGenericType(final Class<T> type, final Class<? extends T> clazz) {
    //
    // if (type == null || clazz == null) {
    // return null;
    // }
    //
    // final ParameterizedType pi = getParameterizedType(type, clazz);
    // if (pi != null) {
    // return getTypeParameter(clazz, pi.getActualTypeArguments()[0]);
    // }
    //
    // @SuppressWarnings("unchecked")
    // final Class<? extends T> superClass = (Class<? extends T>) clazz.getSuperclass();
    //
    // final Object result = getGenericType(type, superClass);
    // if (result instanceof Class<?>) {
    // return result;
    // }
    // if (result instanceof Integer) {
    // final ParameterizedType superClassType =
    // (ParameterizedType) clazz.getGenericSuperclass();
    // return getTypeParameter(
    // clazz, superClassType.getActualTypeArguments()[((Integer) result).intValue()]);
    // }
    // return null;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getGenericType", type, clazz).as(Object.class);
  }
}
