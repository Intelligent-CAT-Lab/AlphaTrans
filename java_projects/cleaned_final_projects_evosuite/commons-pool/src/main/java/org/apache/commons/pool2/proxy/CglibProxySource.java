
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */

package org.apache.commons.pool2.proxy;

/**
 * Provides proxy objects using CGLib.
 *
 * @param <T> type of the pooled object to be proxied
 * @since 2.0
 */
public class CglibProxySource<T> {

    private final Class<? extends T> superclass;

    /**
     * Constructs a new proxy source for the given class.
     *
     * @param superclass The class to proxy
     */
    public CglibProxySource(final Class<? extends T> superclass) {
        this.superclass = superclass;
    }

    /**
     * @since 2.4.3
     */
    public String toString() {
        final StringBuilder builder = new StringBuilder();
        builder.append("CglibProxySource [superclass=");
        builder.append(superclass);
        builder.append("]");
        return builder.toString();
    }
}
