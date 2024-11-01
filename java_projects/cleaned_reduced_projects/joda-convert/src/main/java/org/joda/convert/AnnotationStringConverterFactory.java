/*
 *  Copyright 2010-present Stephen Colebourne
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package org.joda.convert;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

/**
 * Factory for {@code StringConverter} looking up annotations.
 *
 * <p>This class is immutable and thread-safe.
 *
 * @since 1.5
 */
final class AnnotationStringConverterFactory implements StringConverterFactory {

    /** Singleton instance. */
    static final AnnotationStringConverterFactory INSTANCE = new AnnotationStringConverterFactory();

    /** Restricted constructor. */
    private AnnotationStringConverterFactory() {}

    /**
     * Finds a converter by type.
     *
     * @param cls the type to lookup, not null
     * @return the converter, null if not found
     * @throws RuntimeException (or subclass) if source code is invalid
     */
    @Override
    public StringConverter<?> findConverter(Class<?> cls) {
        return findAnnotatedConverter(cls); // capture generics
    }

    /**
     * Finds a converter searching annotated.
     *
     * @param <T> the type of the converter
     * @param cls the class to find a method for, not null
     * @return the converter, not null
     * @throws RuntimeException if none found
     */
    private <T> StringConverter<T> findAnnotatedConverter(Class<T> cls) {
        Method toString = findToStringMethod(cls); // checks superclasses
        if (toString == null) {
            return null;
        }
        TypedFromStringConverter<T> fromString = findAnnotatedFromStringConverter(cls);
        if (fromString == null) {
            throw new IllegalStateException(
                    "Class annotated with @ToString but not with @FromString: " + cls.getName());
        }
        return new ReflectionStringConverter<T>(cls, toString, fromString);
    }

    /**
     * Finds a from-string converter by type.
     *
     * @param <T> the type of the converter
     * @param cls the type to lookup, not null
     * @return the converter, null if not found
     * @throws RuntimeException (or subclass) if source code is invalid
     */
    <T> TypedFromStringConverter<T> findFromStringConverter(Class<T> cls) {
        return findAnnotatedFromStringConverter(cls); // capture generics
    }

    /**
     * Finds a from-string converter.
     *
     * @param <T> the type of the converter
     * @param cls the class to find a method for, not null
     * @return the converter, null if not found
     * @throws RuntimeException if none found
     */
    private <T> TypedFromStringConverter<T> findAnnotatedFromStringConverter(Class<T> cls) {
        TypedFromStringConverter<T> con = findFromStringConstructor(cls);
        TypedFromStringConverter<T> mth =
                findFromStringMethod(cls, con == null); // optionally checks superclasses
        if (con != null && mth != null) {
            throw new IllegalStateException(
                    "Both method and constructor are annotated with @FromString: " + cls.getName());
        }
        return (con != null ? con : mth);
    }

    /**
     * Finds the conversion method.
     *
     * @param cls the class to find a method for, not null
     * @return the method to call, null means use {@code toString}
     * @throws RuntimeException if invalid
     */
    private Method findToStringMethod(Class<?> cls) {
        Method matched = null;
        Class<?> loopCls = cls;
        while (loopCls != null && matched == null) {
            Method[] methods = loopCls.getDeclaredMethods();
            for (Method method : methods) {
                if (!method.isBridge() && !method.isSynthetic()) {
                    ToString toString = method.getAnnotation(ToString.class);
                    if (toString != null) {
                        if (matched != null) {
                            throw new IllegalStateException(
                                    "Two methods are annotated with @ToString: " + cls.getName());
                        }
                        matched = method;
                    }
                }
            }
            loopCls = loopCls.getSuperclass();
        }
        if (matched == null) {
            for (Class<?> loopIfc : eliminateEnumSubclass(cls).getInterfaces()) {
                Method[] methods = loopIfc.getDeclaredMethods();
                for (Method method : methods) {
                    if (!method.isBridge() && !method.isSynthetic()) {
                        ToString toString = method.getAnnotation(ToString.class);
                        if (toString != null) {
                            if (matched != null) {
                                throw new IllegalStateException(
                                        "Two methods are annotated with @ToString on interfaces: "
                                                + cls.getName());
                            }
                            matched = method;
                        }
                    }
                }
            }
        }
        return matched;
    }

    /**
     * Finds the conversion method.
     *
     * @param <T> the type of the converter
     * @param cls the class to find a method for, not null
     * @return the method to call, null means none found
     * @throws RuntimeException if invalid
     */
    private <T> TypedFromStringConverter<T> findFromStringConstructor(Class<T> cls) {
        Constructor<T> con;
        try {
            con = cls.getDeclaredConstructor(String.class);
        } catch (NoSuchMethodException ex) {
            try {
                con = cls.getDeclaredConstructor(CharSequence.class);
            } catch (NoSuchMethodException ex2) {
                return null;
            }
        }
        FromString fromString = con.getAnnotation(FromString.class);
        if (fromString == null) {
            return null;
        }
        return new ConstructorFromStringConverter<T>(cls, con);
    }

    /**
     * Finds the conversion method.
     *
     * @param cls the class to find a method for, not null
     * @param searchSuperclasses whether to search superclasses
     * @return the method to call, null means not found
     * @throws RuntimeException if invalid
     */
    private <T> TypedFromStringConverter<T> findFromStringMethod(
            Class<T> cls, boolean searchSuperclasses) {
        Class<?> loopCls = cls;
        while (loopCls != null) {
            Method fromString = findFromString(loopCls);
            if (fromString != null) {
                return new MethodFromStringConverter<T>(cls, fromString, loopCls);
            }
            if (searchSuperclasses == false) {
                break;
            }
            loopCls = loopCls.getSuperclass();
        }
        TypedFromStringConverter<T> matched = null;
        if (searchSuperclasses) {
            for (Class<?> loopIfc : eliminateEnumSubclass(cls).getInterfaces()) {
                Method fromString = findFromString(loopIfc);
                if (fromString != null) {
                    if (matched != null) {
                        throw new IllegalStateException(
                                "Two different interfaces are annotated with "
                                        + "@FromString or @FromStringFactory: "
                                        + cls.getName());
                    }
                    matched = new MethodFromStringConverter<T>(cls, fromString, loopIfc);
                }
            }
        }
        return matched;
    }

    /**
     * Finds the conversion method.
     *
     * @param cls the class to find a method for, not null
     * @param matched the matched method, may be null
     * @return the method to call, null means not found
     * @throws RuntimeException if invalid
     */
    private Method findFromString(Class<?> cls) {
        Method[] methods = cls.getDeclaredMethods();
        Method matched = null;
        for (Method method : methods) {
            if (!method.isBridge() && !method.isSynthetic()) {
                FromString fromString = method.getAnnotation(FromString.class);
                if (fromString != null) {
                    if (matched != null) {
                        throw new IllegalStateException(
                                "Two methods are annotated with @FromString: " + cls.getName());
                    }
                    matched = method;
                }
            }
        }
        FromStringFactory factory = cls.getAnnotation(FromStringFactory.class);
        if (factory != null) {
            if (matched != null) {
                throw new IllegalStateException(
                        "Class annotated with @FromString and @FromStringFactory: "
                                + cls.getName());
            }
            Method[] factoryMethods = factory.factory().getDeclaredMethods();
            for (Method method : factoryMethods) {
                if (!method.isBridge() && !method.isSynthetic()) {
                    if (cls.isAssignableFrom(method.getReturnType())) {
                        FromString fromString = method.getAnnotation(FromString.class);
                        if (fromString != null) {
                            if (matched != null) {
                                throw new IllegalStateException(
                                        "Two methods are annotated with @FromString on the factory:"
                                                + " "
                                                + factory.factory().getName());
                            }
                            matched = method;
                        }
                    }
                }
            }
        }
        return matched;
    }

    private Class<?> eliminateEnumSubclass(Class<?> cls) {
        Class<?> sup = cls.getSuperclass();
        if (sup != null && sup.getSuperclass() == Enum.class) {
            return sup;
        }
        return cls;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName();
    }
}
