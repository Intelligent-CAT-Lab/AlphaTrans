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

package org.apache.commons.cli;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.io.File;
import java.io.FileInputStream;
import java.net.URL;

public class TypeHandlerTest {

    public static class Instantiable {}

    public static final class NotInstantiable {
        private NotInstantiable() {}
    }

    @Test
    public void testCreateValueClass_test0_decomposed() throws Exception {
        final Object clazz =
                TypeHandler.createValue0(
                        Instantiable.class.getName(), PatternOptionBuilder.CLASS_VALUE);
    }

    @Test
    public void testCreateValueClass_test1_decomposed() throws Exception {
        final Object clazz =
                TypeHandler.createValue0(
                        Instantiable.class.getName(), PatternOptionBuilder.CLASS_VALUE);
        assertEquals(Instantiable.class, clazz);
    }

    @Test(expected = ParseException.class)
    public void testCreateValueClass_notFound_test0_decomposed() throws Exception {
        TypeHandler.createValue0("what ever", PatternOptionBuilder.CLASS_VALUE);
    }

    @Test(expected = UnsupportedOperationException.class)
    public void testCreateValueDate_test0_decomposed() throws Exception {
        TypeHandler.createValue0("what ever", PatternOptionBuilder.DATE_VALUE);
    }

    @Test
    public void testCreateValueExistingFile_test0_decomposed() throws Exception {
        try (FileInputStream result =
                TypeHandler.createValue0(
                        "src/test/resources/org/apache/commons/cli/existing-readable.file",
                        PatternOptionBuilder.EXISTING_FILE_VALUE)) {
            assertNotNull(result);
        }
    }

    @Test(expected = ParseException.class)
    public void testCreateValueExistingFile_nonExistingFile_test0_decomposed() throws Exception {
        TypeHandler.createValue0("non-existing.file", PatternOptionBuilder.EXISTING_FILE_VALUE);
    }

    @Test
    public void testCreateValueFile_test0_decomposed() throws Exception {
        final File result =
                TypeHandler.createValue0("some-file.txt", PatternOptionBuilder.FILE_VALUE);
    }

    @Test
    public void testCreateValueFile_test1_decomposed() throws Exception {
        final File result =
                TypeHandler.createValue0("some-file.txt", PatternOptionBuilder.FILE_VALUE);
        assertEquals("some-file.txt", result.getName());
    }

    @Test(expected = UnsupportedOperationException.class)
    public void testCreateValueFiles_test0_decomposed() throws Exception {
        TypeHandler.createValue0("some.files", PatternOptionBuilder.FILES_VALUE);
    }

    @Test(expected = ParseException.class)
    public void testCreateValueInteger_failure_test0_decomposed() throws Exception {
        TypeHandler.createValue0("just-a-string", Integer.class);
    }

    @Test
    public void testCreateValueNumber_Double_test0_decomposed() throws Exception {
        assertEquals(1.5d, TypeHandler.createValue0("1.5", PatternOptionBuilder.NUMBER_VALUE));
    }

    @Test
    public void testCreateValueNumber_Long_test0_decomposed() throws Exception {
        assertEquals(
                Long.valueOf(15),
                TypeHandler.createValue0("15", PatternOptionBuilder.NUMBER_VALUE));
    }

    @Test(expected = ParseException.class)
    public void testCreateValueNumber_noNumber_test0_decomposed() throws Exception {
        TypeHandler.createValue0("not a number", PatternOptionBuilder.NUMBER_VALUE);
    }

    @Test
    public void testCreateValueObject_InstantiableClass_test0_decomposed() throws Exception {
        final Object result =
                TypeHandler.createValue0(
                        Instantiable.class.getName(), PatternOptionBuilder.OBJECT_VALUE);
    }

    @Test
    public void testCreateValueObject_InstantiableClass_test1_decomposed() throws Exception {
        final Object result =
                TypeHandler.createValue0(
                        Instantiable.class.getName(), PatternOptionBuilder.OBJECT_VALUE);
        assertTrue(result instanceof Instantiable);
    }

    @Test(expected = ParseException.class)
    public void testCreateValueObject_notInstantiableClass_test0_decomposed() throws Exception {
        TypeHandler.createValue0(
                NotInstantiable.class.getName(), PatternOptionBuilder.OBJECT_VALUE);
    }

    @Test(expected = ParseException.class)
    public void testCreateValueObject_unknownClass_test0_decomposed() throws Exception {
        TypeHandler.createValue0("unknown", PatternOptionBuilder.OBJECT_VALUE);
    }

    @Test
    public void testCreateValueString_test0_decomposed() throws Exception {
        assertEquals(
                "String", TypeHandler.createValue0("String", PatternOptionBuilder.STRING_VALUE));
    }

    @Test
    public void testCreateValueURL_test0_decomposed() throws Exception {
        final String urlString = "https://commons.apache.org";
        final URL result = TypeHandler.createValue0(urlString, PatternOptionBuilder.URL_VALUE);
    }

    @Test
    public void testCreateValueURL_test1_decomposed() throws Exception {
        final String urlString = "https://commons.apache.org";
        final URL result = TypeHandler.createValue0(urlString, PatternOptionBuilder.URL_VALUE);
        assertEquals(urlString, result.toString());
    }

    @Test(expected = ParseException.class)
    public void testCreateValueURL_malformed_test0_decomposed() throws Exception {
        TypeHandler.createValue0("malformed-url", PatternOptionBuilder.URL_VALUE);
    }
}