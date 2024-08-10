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
package org.apache.commons.pool2.impl;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.time.Duration;

/** Tests for {@link EvictionConfig}. */
public class TestEvictionConfig {

    @Test
    public void testConstructor1s_test0_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
    }

    @Test
    public void testConstructor1s_test1_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
    }

    @Test
    public void testConstructor1s_test2_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
    }

    @Test
    public void testConstructor1s_test3_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
        assertEquals(1, config.getIdleEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructor1s_test4_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
        assertEquals(1, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictDuration().toMillis());
    }

    @Test
    public void testConstructor1s_test5_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
        assertEquals(1, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictTime());
    }

    @Test
    public void testConstructor1s_test6_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
        assertEquals(1, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictTime());
        assertEquals(1, config.getIdleSoftEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructor1s_test7_decomposed()  {
        final EvictionConfig config =
                new EvictionConfig(Duration.ofMillis(1), Duration.ofMillis(1), 1);
        assertEquals(1, config.getIdleEvictDuration().toMillis());
        assertEquals(1, config.getIdleEvictTime());
        assertEquals(1, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(1, config.getIdleSoftEvictTime());
        assertEquals(1, config.getIdleSoftEvictTimeDuration().toMillis());
        assertEquals(1, config.getMinIdle());
    }

    @Test
    public void testConstructorZerosDurations_test0_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
    }

    @Test
    public void testConstructorZerosDurations_test1_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
    }

    @Test
    public void testConstructorZerosDurations_test2_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
    }

    @Test
    public void testConstructorZerosDurations_test3_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructorZerosDurations_test4_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
    }

    @Test
    public void testConstructorZerosDurations_test5_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
    }

    @Test
    public void testConstructorZerosDurations_test6_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructorZerosDurations_test7_decomposed()  {
        final EvictionConfig config = new EvictionConfig(Duration.ZERO, Duration.ZERO, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTimeDuration().toMillis());
        assertEquals(0, config.getMinIdle());
    }

    @Test
    public void testConstructorZerosMillis_test0_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
    }

    @Test
    public void testConstructorZerosMillis_test1_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
    }

    @Test
    public void testConstructorZerosMillis_test2_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
    }

    @Test
    public void testConstructorZerosMillis_test3_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructorZerosMillis_test4_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
    }

    @Test
    public void testConstructorZerosMillis_test5_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
    }

    @Test
    public void testConstructorZerosMillis_test6_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTimeDuration().toMillis());
    }

    @Test
    public void testConstructorZerosMillis_test7_decomposed()  {
        @SuppressWarnings("deprecation")
        final EvictionConfig config = EvictionConfig.EvictionConfig0(0, 0, 0);
        assertEquals(Long.MAX_VALUE, config.getIdleEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleEvictTimeDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictDuration().toMillis());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTime());
        assertEquals(Long.MAX_VALUE, config.getIdleSoftEvictTimeDuration().toMillis());
        assertEquals(0, config.getMinIdle());
    }
}