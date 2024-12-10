/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.pool2;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

/** Holds method names, parameters, and return values for tracing method calls. */
public class MethodCall {
    private final String name;
    private final List<Object> params;
    private Object returned;

    public MethodCall(
            int constructorId,
            final Object param2,
            final List<Object> params,
            final Object param1,
            final String name,
            final Object param) {
        if (constructorId == 2) {

            if (name == null) {
                throw new IllegalArgumentException("name must not be null.");
            }
            this.name = name;
            if (params != null) {
                this.params = params;
            } else {
                this.params = Collections.emptyList();
            }
        } else {

            if (name == null) {
                throw new IllegalArgumentException("name must not be null.");
            }
            this.name = name;
            if (params != null) {
                this.params = params;
            } else {
                this.params = Collections.emptyList();
            }
        }
    }

    public static MethodCall MethodCall0(
            final String name, final Object param1, final Object param2) {
        return new MethodCall(2, null, Arrays.asList(param1, param2), null, name, null);
    }

    public static MethodCall MethodCall1(final String name, final Object param) {
        return new MethodCall(2, null, Collections.singletonList(param), null, name, null);
    }

    public static MethodCall MethodCall3(final String name) {
        return new MethodCall(2, null, null, null, name, null);
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        final MethodCall that = (MethodCall) o;

        if (!Objects.equals(name, that.name)) {
            return false;
        }
        if (!Objects.equals(params, that.params)) {
            return false;
        }
        return Objects.equals(returned, that.returned);
    }

    public String getName() {
        return name;
    }

    public List<Object> getParams() {
        return params;
    }

    public Object getReturned() {
        return returned;
    }

    @Override
    public int hashCode() {
        int result;
        result = name != null ? name.hashCode() : 0;
        result = 29 * result + (params != null ? params.hashCode() : 0);
        result = 29 * result + (returned != null ? returned.hashCode() : 0);
        return result;
    }

    public MethodCall returned(final Object obj) {
        setReturned(obj);
        return this;
    }

    public void setReturned(final Object returned) {
        this.returned = returned;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("MethodCall");
        sb.append("{name='").append(name).append('\'');
        if (!params.isEmpty()) {
            sb.append(", params=").append(params);
        }
        if (returned != null) {
            sb.append(", returned=").append(returned);
        }
        sb.append('}');
        return sb.toString();
    }

    
}
