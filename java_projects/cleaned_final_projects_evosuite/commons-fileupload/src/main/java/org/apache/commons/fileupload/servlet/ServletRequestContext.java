
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

package org.apache.commons.fileupload.servlet;

/**
 * Provides access to the request information needed for a request made to an HTTP servlet.
 *
 * @since FileUpload 1.1
 */
public class ServletRequestContext {

    /** The request for which the context is being provided. */

    /**
     * Construct a context for this request.
     *
     * @param request The request to which this context applies.
     */

    /**
     * Retrieve the character encoding for the request.
     *
     * @return The character encoding for the request.
     */

    /**
     * Retrieve the content type of the request.
     *
     * @return The content type of the request.
     */

    /**
     * Retrieve the content length of the request.
     *
     * @return The content length of the request.
     * @deprecated 1.3 Use {@link #contentLength()} instead
     */

    /**
     * Retrieve the content length of the request.
     *
     * @return The content length of the request.
     * @since 1.3
     */

    /**
     * Retrieve the input stream for the request.
     *
     * @return The input stream for the request.
     * @throws IOException if a problem occurs.
     */

    /**
     * Returns a string representation of this object.
     *
     * @return a string representation of this object.
     */
}
