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
package org.apache.commons.fileupload.util;

import org.apache.commons.fileupload.FileItemHeaders;
import org.apache.commons.fileupload.ContextInitializer;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import org.graalvm.polyglot.Value;

/**
 * Default implementation of the {@link FileItemHeaders} interface.
 *
 * @since 1.2.1
 */
public class FileItemHeadersImpl implements FileItemHeaders, Serializable {

    /** Serial version UID, being used, if serialized. */
    private static final long serialVersionUID = -4455695752627032559L;

    /**
     * Contains a reference to the Python class.
     */
    private static Value clz = ContextInitializer.getPythonClass("util/file_item_headers_impl.py",
            "FileItemHeadersImpl");

    /**
     * Contains a reference to the Python exception.
     */
    private final Value obj;

    public FileItemHeadersImpl() {
        obj = clz.newInstance();
    }

    /** Map of <code>String</code> keys to a <code>List</code> of <code>String</code> instances. */
    // private final Map<String, List<String>> headerNameToValueListMap =
    //         new LinkedHashMap<String, List<String>>();

    /** {@inheritDoc} */
    @Override
    public String getHeader(String name) {
        // String nameLower = name.toLowerCase(Locale.ENGLISH);
        // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
        // if (null == headerValueList) {
        //     return null;
        // }
        // return headerValueList.get(0);
        return obj.invokeMember("getHeader", name).asString();
    }

    /** {@inheritDoc} */
    @Override
    public Iterator<String> getHeaderNames() {
        // return headerNameToValueListMap.keySet().iterator();
        return obj.invokeMember("getHeaderNames").as(List.class).iterator();
    }

    /** {@inheritDoc} */
    @Override
    public Iterator<String> getHeaders(String name) {
        // String nameLower = name.toLowerCase(Locale.ENGLISH);
        // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
        // if (null == headerValueList) {
        //     headerValueList = Collections.emptyList();
        // }
        // return headerValueList.iterator();
        return obj.invokeMember("getHeaders", name).as(List.class).iterator();
    }

    /**
     * Method to add header values to this instance.
     *
     * @param name name of this header
     * @param value value of this header
     */
    public synchronized void addHeader(String name, String value) {
        // String nameLower = name.toLowerCase(Locale.ENGLISH);
        // List<String> headerValueList = headerNameToValueListMap.get(nameLower);
        // if (null == headerValueList) {
        //     headerValueList = new ArrayList<String>();
        //     headerNameToValueListMap.put(nameLower, headerValueList);
        // }
        // headerValueList.add(value);
        obj.invokeMember("addHeader", name, value);
    }
}
