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
package org.apache.commons.fileupload;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.junit.Test;

import java.util.Iterator;

/** Unit tests {@link FileItemHeaders} and {@link FileItemHeadersImpl}. */
public class FileItemHeadersTest {

    /**
     * @throws Exception
     */

    @Test
    public void testFileItemHeaders_test0_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
    }

    @Test
    public void testFileItemHeaders_test1_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
    }

    @Test
    public void testFileItemHeaders_test2_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
    }

    @Test
    public void testFileItemHeaders_test3_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
    }

    @Test
    public void testFileItemHeaders_test4_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test5_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
    }

    @Test
    public void testFileItemHeaders_test6_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
    }

    @Test
    public void testFileItemHeaders_test7_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test8_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
    }

    @Test
    public void testFileItemHeaders_test9_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test10_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
    }

    @Test
    public void testFileItemHeaders_test11_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test12_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
    }

    @Test
    public void testFileItemHeaders_test13_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test14_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
    }

    @Test
    public void testFileItemHeaders_test15_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test16_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
    }

    @Test
    public void testFileItemHeaders_test17_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test18_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
    }

    @Test
    public void testFileItemHeaders_test19_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test20_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
    }

    @Test
    public void testFileItemHeaders_test21_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
        assertTrue(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test22_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue4");
    }

    @Test
    public void testFileItemHeaders_test23_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue4");
        assertFalse(headerValueEnumeration.hasNext());
    }

    @Test
    public void testFileItemHeaders_test24_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue4");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader");
    }

    @Test
    public void testFileItemHeaders_test25_decomposed() throws Exception {
        FileItemHeadersImpl aMutableFileItemHeaders = new FileItemHeadersImpl();
        aMutableFileItemHeaders.addHeader(
                "Content-Disposition", "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        aMutableFileItemHeaders.addHeader("Content-Type", "text/plain");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue1");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue2");
        aMutableFileItemHeaders.addHeader("TestHeader", "headerValue3");
        aMutableFileItemHeaders.addHeader("testheader", "headerValue4");
        Iterator<String> headerNameEnumeration = aMutableFileItemHeaders.getHeaderNames();
        assertEquals("content-disposition", headerNameEnumeration.next());
        assertEquals("content-type", headerNameEnumeration.next());
        assertEquals("testheader", headerNameEnumeration.next());
        assertFalse(headerNameEnumeration.hasNext());
        assertEquals(
                aMutableFileItemHeaders.getHeader("Content-Disposition"),
                "form-data; name=\"FileItem\"; filename=\"file1.txt\"");
        assertEquals(aMutableFileItemHeaders.getHeader("Content-Type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("content-type"), "text/plain");
        assertEquals(aMutableFileItemHeaders.getHeader("TestHeader"), "headerValue1");
        assertNull(aMutableFileItemHeaders.getHeader("DummyHeader"));
        Iterator<String> headerValueEnumeration;
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("Content-Type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("content-type");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "text/plain");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("TestHeader");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue1");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue2");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue3");
        assertTrue(headerValueEnumeration.hasNext());
        assertEquals(headerValueEnumeration.next(), "headerValue4");
        assertFalse(headerValueEnumeration.hasNext());
        headerValueEnumeration = aMutableFileItemHeaders.getHeaders("DummyHeader");
        assertFalse(headerValueEnumeration.hasNext());
    }
}