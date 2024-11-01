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

import java.lang.reflect.Method;

/**
 * Parse the string format of OptionalLong from Java 8.
 *
 * <p>This is loaded by reflection only when using Java 8.
 */
final class OptionalLongStringConverter implements TypedStringConverter<Object> {

    private static final Class<?> TYPE;
    private static final Object EMPTY;
    private static final Method METHOD_OF;
    private static final Method METHOD_IS_PRESENT;
    private static final Method METHOD_GET;

    static {
        try {
            TYPE = Class.forName("java.util.OptionalLong");
            EMPTY = TYPE.getDeclaredMethod("empty").invoke(null);
            METHOD_OF = TYPE.getDeclaredMethod("of", long.class);
            METHOD_IS_PRESENT = TYPE.getDeclaredMethod("isPresent");
            METHOD_GET = TYPE.getDeclaredMethod("getAsLong");

        } catch (Exception ex) {
            throw new IllegalStateException(ex);
        }
    }

    OptionalLongStringConverter() {}

    @Override
    public String convertToString(Object object) {
        try {
            Object isPresent = METHOD_IS_PRESENT.invoke(object);
            return Boolean.TRUE.equals(isPresent) ? String.valueOf(METHOD_GET.invoke(object)) : "";
        } catch (Exception ex) {
            throw new IllegalArgumentException(ex);
        }
    }

    @Override
    public Object convertFromString(Class<? extends Object> cls, String str) {
        if ("".equals(str)) {
            return EMPTY;
        }
        long value = Long.parseLong(str);
        try {
            return METHOD_OF.invoke(null, value);
        } catch (Exception ex) {
            throw new IllegalArgumentException(ex);
        }
    }

    @Override
    public Class<?> getEffectiveType() {
        return TYPE;
    }
}
