
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

package org.apache.commons.fileupload.portlet;

import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileUpload;

/**
 * High level API for processing file uploads.
 *
 * <p>This class handles multiple files per single HTML widget, sent using <code>multipart/mixed
 * </code> encoding type, as specified by <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC
 * 1867</a>. Use {@link org.apache.commons.fileupload.servlet.ServletFileUpload
 * #parseRequest(javax.servlet.http.HttpServletRequest)} to acquire a list of {@link
 * org.apache.commons.fileupload.FileItem FileItems} associated with a given HTML widget.
 *
 * <p>How the data for individual parts is stored is determined by the factory used to create them;
 * a given part may be in memory, on disk, or somewhere else.
 *
 * @since FileUpload 1.1
 */
public class PortletFileUpload extends FileUpload {

    /**
     * Utility method that determines whether the request contains multipart content.
     *
     * @param request The portlet request to be evaluated. Must be non-null.
     * @return <code>true</code> if the request is multipart; <code>false</code> otherwise.
     */

    /**
     * Constructs an uninitialised instance of this class. A factory must be configured, using
     * <code>setFileItemFactory()</code>, before attempting to parse requests.
     *
     * @see FileUpload#FileUpload(FileItemFactory)
     */
    public PortletFileUpload(FileItemFactory fileItemFactory) {
        super(0, fileItemFactory);
    }

    public static PortletFileUpload PortletFileUpload1() {
        return new PortletFileUpload(null);
    }

    /**
     * Constructs an instance of this class which uses the supplied factory to create <code>FileItem
     * </code> instances.
     *
     * @see FileUpload#FileUpload()
     * @param fileItemFactory The factory to use for creating file items.
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param request The portlet request to be parsed.
     * @return A list of <code>FileItem</code> instances parsed from the request, in the order that
     *     they were transmitted.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param request The portlet request to be parsed.
     * @return A map of <code>FileItem</code> instances parsed from the request.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     * @since 1.3
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param request The portlet request to be parsed.
     * @return An iterator to instances of <code>FileItemStream</code> parsed from the request, in
     *     the order that they were transmitted.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     * @throws IOException An I/O error occurred. This may be a network error while communicating
     *     with the client or a problem while storing the uploaded content.
     */
}
