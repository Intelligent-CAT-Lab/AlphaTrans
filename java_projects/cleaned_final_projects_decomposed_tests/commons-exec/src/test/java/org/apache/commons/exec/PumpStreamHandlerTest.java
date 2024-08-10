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

package org.apache.commons.exec;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.Duration;

import org.junit.jupiter.api.Test;

/**
 * Tests {@link PumpStreamHandler}.
 */
public class PumpStreamHandlerTest {

    @Test
    public void testSetStopTimeout_test0_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
    }

    @Test
    public void testSetStopTimeout_test1_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
    }

    @Test
    public void testSetStopTimeout_test2_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
    }

    @Test
    public void testSetStopTimeout_test3_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
    }

    @Test
    public void testSetStopTimeout_test4_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
    }

    @Test
    public void testSetStopTimeout_test5_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
    }

    @Test
    public void testSetStopTimeout_test6_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout1(60_001);
    }

    @Test
    public void testSetStopTimeout_test7_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout1(60_001);
        assertEquals(Duration.ofMillis(60_001), handler.getStopTimeout());
    }

    @Test
    public void testSetStopTimeout_test8_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout1(60_001);
        assertEquals(Duration.ofMillis(60_001), handler.getStopTimeout());
        handler.setStopTimeout0(null);
    }

    @Test
    public void testSetStopTimeout_test9_decomposed()  {
        final PumpStreamHandler handler = PumpStreamHandler.PumpStreamHandler0();
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout0(Duration.ofMinutes(1));
        assertEquals(Duration.ofMinutes(1), handler.getStopTimeout());
        handler.setStopTimeout1(0);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
        handler.setStopTimeout1(60_001);
        assertEquals(Duration.ofMillis(60_001), handler.getStopTimeout());
        handler.setStopTimeout0(null);
        assertEquals(Duration.ZERO, handler.getStopTimeout());
    }
}