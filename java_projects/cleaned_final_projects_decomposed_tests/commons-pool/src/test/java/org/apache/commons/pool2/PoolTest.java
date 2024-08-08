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

import org.junit.jupiter.api.Disabled;

@Disabled
public class PoolTest {
    private static class Foo {}

    private static class PooledFooFactory {
        private static final long VALIDATION_WAIT_IN_MILLIS = 1000;

        public void activateObject(final PooledObject<Foo> pooledObject) throws Exception {}

        public void destroyObject(final PooledObject<Foo> pooledObject) throws Exception {}

        public void passivateObject(final PooledObject<Foo> pooledObject) throws Exception {}

        public boolean validateObject(final PooledObject<Foo> pooledObject) {
            try {
                Thread.sleep(VALIDATION_WAIT_IN_MILLIS);
            } catch (final InterruptedException e) {
                Thread.interrupted();
            }
            return false;
        }
    }

    private static final CharSequence COMMONS_POOL_EVICTIONS_TIMER_THREAD_NAME =
            "commons-pool-EvictionTimer";

    private static final long EVICTION_PERIOD_IN_MILLIS = 100;

    
}
