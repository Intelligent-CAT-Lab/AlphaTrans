/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 *  contributor license agreements.  See the NOTICE file distributed with
 *  this work for additional information regarding copyright ownership.
 *  The ASF licenses this file to You under the Apache License, Version 2.0
 *  (the "License"); you may not use this file except in compliance with
 *  the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.apache.commons.exec.util;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.HashMap;
import java.util.Map;

import org.apache.commons.exec.environment.EnvironmentUtils;
import org.junit.jupiter.api.Test;

/**
 */
public class MapUtilTest {
    /**
     * Test copying of map
     */
    

    /**
     * Test merging of maps
     */
    

    /**
     * Test prefixing of map
     */

    @Test
    public void testCopyMap_test0_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
    }

    @Test
    public void testCopyMap_test1_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
        assertEquals(1, result.size());
        assertEquals(1, procEnvironment.size());
    }

    @Test
    public void testCopyMap_test2_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
        assertEquals(1, result.size());
        assertEquals(1, procEnvironment.size());
        assertEquals("/usr/opt/java", result.get("JAVA_HOME"));
    }

    @Test
    public void testCopyMap_test3_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
        assertEquals(1, result.size());
        assertEquals(1, procEnvironment.size());
        assertEquals("/usr/opt/java", result.get("JAVA_HOME"));
        result.remove("JAVA_HOME");
    }

    @Test
    public void testCopyMap_test4_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
        assertEquals(1, result.size());
        assertEquals(1, procEnvironment.size());
        assertEquals("/usr/opt/java", result.get("JAVA_HOME"));
        result.remove("JAVA_HOME");
        assertTrue(result.isEmpty());
    }

    @Test
    public void testCopyMap_test5_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.copy(procEnvironment);
        assertEquals(1, result.size());
        assertEquals(1, procEnvironment.size());
        assertEquals("/usr/opt/java", result.get("JAVA_HOME"));
        result.remove("JAVA_HOME");
        assertTrue(result.isEmpty());
        assertEquals(1, procEnvironment.size());
    }

    @Test
    public void testMergeMap_test0_decomposed() throws Exception {
        final Map<String, String> procEnvironment = EnvironmentUtils.getProcEnvironment();
    }

    @Test
    public void testMergeMap_test1_decomposed() throws Exception {
        final Map<String, String> procEnvironment = EnvironmentUtils.getProcEnvironment();
        final HashMap<String, String> applicationEnvironment = new HashMap<>();
        applicationEnvironment.put("appMainClass", "foo.bar.Main");
        final Map<String, String> result = MapUtils.merge(procEnvironment, applicationEnvironment);
    }

    @Test
    public void testMergeMap_test2_decomposed() throws Exception {
        final Map<String, String> procEnvironment = EnvironmentUtils.getProcEnvironment();
        final HashMap<String, String> applicationEnvironment = new HashMap<>();
        applicationEnvironment.put("appMainClass", "foo.bar.Main");
        final Map<String, String> result = MapUtils.merge(procEnvironment, applicationEnvironment);
        assertEquals(procEnvironment.size() + applicationEnvironment.size(), result.size());
    }

    @Test
    public void testMergeMap_test3_decomposed() throws Exception {
        final Map<String, String> procEnvironment = EnvironmentUtils.getProcEnvironment();
        final HashMap<String, String> applicationEnvironment = new HashMap<>();
        applicationEnvironment.put("appMainClass", "foo.bar.Main");
        final Map<String, String> result = MapUtils.merge(procEnvironment, applicationEnvironment);
        assertEquals(procEnvironment.size() + applicationEnvironment.size(), result.size());
        assertEquals("foo.bar.Main", result.get("appMainClass"));
    }

    @Test
    public void testPrefixMap_test0_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.prefix(procEnvironment, "env");
    }

    @Test
    public void testPrefixMap_test1_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.prefix(procEnvironment, "env");
        assertEquals(procEnvironment.size(), result.size());
    }

    @Test
    public void testPrefixMap_test2_decomposed() throws Exception {
        final HashMap<String, String> procEnvironment = new HashMap<>();
        procEnvironment.put("JAVA_HOME", "/usr/opt/java");
        final Map<String, String> result = MapUtils.prefix(procEnvironment, "env");
        assertEquals(procEnvironment.size(), result.size());
        assertEquals("/usr/opt/java", result.get("env.JAVA_HOME"));
    }
}