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
package org.apache.commons.fileupload.portlet;

import org.apache.commons.fileupload.FileUploadBase;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.Arrays;
import java.util.Collections;
import java.util.Enumeration;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Locale;
import java.util.Map;

/**
 * Mock class for tests. Implements an {@link ActionRequest}.
 *
 * @see PortletFileUploadTest
 * @since 1.4
 */
@SuppressWarnings("rawtypes") // because of the portlet ActionRequest API does not use generics
public class MockPortletActionRequest {

    private final Hashtable<String, Object> attributes = new Hashtable<String, Object>();

    private final Map<String, String> parameters = new HashMap<String, String>();

    private String characterEncoding;
    private final int length;
    private final String contentType;
    private final InputStream requestData;

    public MockPortletActionRequest(
            int requestLength, ByteArrayInputStream byteArrayInputStream, String contentType) {
        this.requestData = byteArrayInputStream;
        length = requestLength;
        this.contentType = contentType;
        attributes.put(FileUploadBase.CONTENT_TYPE, contentType);
    }

    public static MockPortletActionRequest MockPortletActionRequest1(
            final byte[] requestData, final String contentType) {
        return new MockPortletActionRequest(
                requestData.length, new ByteArrayInputStream(requestData), contentType);
    }

    public Object getAttribute(String key) {
        return attributes.get(key);
    }

    public Enumeration getAttributeNames() {
        return attributes.keys();
    }

    public String getAuthType() {
        return null;
    }

    public String getContextPath() {
        return null;
    }

    public Locale getLocale() {
        return Locale.getDefault();
    }

    public Enumeration getLocales() {
        return Collections.enumeration(Arrays.asList(Locale.getAvailableLocales()));
    }

    public String getParameter(String key) {
        return parameters.get(key);
    }

    public Map getParameterMap() {
        return Collections.unmodifiableMap(parameters);
    }

    public Enumeration getParameterNames() {
        return Collections.enumeration(parameters.keySet());
    }

    public String[] getParameterValues(String arg0) {
        return null;
    }

    public Enumeration getProperties(String arg0) {
        return null;
    }

    public String getProperty(String arg0) {
        return null;
    }

    public Enumeration getPropertyNames() {
        return null;
    }

    public String getRemoteUser() {
        return null;
    }

    public String getRequestedSessionId() {
        return null;
    }

    public String getResponseContentType() {
        return null;
    }

    public Enumeration getResponseContentTypes() {
        return null;
    }

    public String getScheme() {
        return null;
    }

    public String getServerName() {
        return null;
    }

    public int getServerPort() {
        return 0;
    }

    public boolean isRequestedSessionIdValid() {
        return false;
    }

    public boolean isSecure() {
        return false;
    }

    public boolean isUserInRole(String arg0) {
        return false;
    }

    public void removeAttribute(String key) {
        attributes.remove(key);
    }

    public void setAttribute(String key, Object value) {
        attributes.put(key, value);
    }

    public String getCharacterEncoding() {
        return characterEncoding;
    }

    public int getContentLength() {
        return length;
    }

    public String getContentType() {
        return contentType;
    }

    public InputStream getPortletInputStream() throws IOException {
        return requestData;
    }

    public BufferedReader getReader() throws UnsupportedEncodingException, IOException {
        return null;
    }

    public void setCharacterEncoding(String characterEncoding) throws UnsupportedEncodingException {
        this.characterEncoding = characterEncoding;
    }
}
