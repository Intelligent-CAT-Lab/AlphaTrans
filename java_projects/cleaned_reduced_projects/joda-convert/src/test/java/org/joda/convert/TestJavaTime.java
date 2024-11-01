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

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/** Test java.time.*. */
public class TestJavaTime {

    @Test
    public void test_basics() throws ClassNotFoundException {
        StringConvert test = StringConvert.INSTANCE;

        Class<?> zoneIdClass = Class.forName("java.time.ZoneId");
        assertEquals(
                "Europe/Paris", test.convertFromString(zoneIdClass, "Europe/Paris").toString());

        Class<?> zoneRegionClass = Class.forName("java.time.ZoneRegion");
        assertEquals(
                "Europe/Paris", test.convertFromString(zoneRegionClass, "Europe/Paris").toString());
    }
}
