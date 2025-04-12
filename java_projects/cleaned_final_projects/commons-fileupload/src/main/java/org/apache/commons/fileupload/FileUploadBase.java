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

import org.apache.commons.fileupload.util.FileItemHeadersImpl;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Locale;
import java.util.Map;

/**
 * High level API for processing file uploads.
 *
 * <p>This class handles multiple files per single HTML widget, sent using <code>multipart/mixed
 * </code> encoding type, as specified by <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC
 * 1867</a>. Use {@link #parseRequest(RequestContext)} to acquire a list of {@link
 * org.apache.commons.fileupload.FileItem}s associated with a given HTML widget.
 *
 * <p>How the data for individual parts is stored is determined by the factory used to create them;
 * a given part may be in memory, on disk, or somewhere else.
 */
public abstract class FileUploadBase {

    /**
     * Utility method that determines whether the request contains multipart content.
     *
     * <p><strong>NOTE:</strong>This method will be moved to the <code>ServletFileUpload</code>
     * class after the FileUpload 1.1 release. Unfortunately, since this method is static, it is not
     * possible to provide its replacement until this method is removed.
     *
     * @param ctx The request context to be evaluated. Must be non-null.
     * @return <code>true</code> if the request is multipart; <code>false</code> otherwise.
     */
    public static final boolean isMultipartContent(RequestContext ctx) {
        String contentType = ctx.getContentType();
        if (contentType == null) {
            return false;
        }
        if (contentType.toLowerCase(Locale.ENGLISH).startsWith(MULTIPART)) {
            return true;
        }
        return false;
    }

    /**
     * Utility method that determines whether the request contains multipart content.
     *
     * @param req The servlet request to be evaluated. Must be non-null.
     * @return <code>true</code> if the request is multipart; <code>false</code> otherwise.
     * @deprecated 1.1 Use the method on <code>ServletFileUpload</code> instead.
     */

    /** HTTP content type header name. */
    public static final String CONTENT_TYPE = "Content-type";

    /** HTTP content disposition header name. */
    public static final String CONTENT_DISPOSITION = "Content-disposition";

    /** HTTP content length header name. */
    public static final String CONTENT_LENGTH = "Content-length";

    /** Content-disposition value for form data. */
    public static final String FORM_DATA = "form-data";

    /** Content-disposition value for file attachment. */
    public static final String ATTACHMENT = "attachment";

    /** Part of HTTP content type header. */
    public static final String MULTIPART = "multipart/";

    /** HTTP content type header for multipart forms. */
    public static final String MULTIPART_FORM_DATA = "multipart/form-data";

    /** HTTP content type header for multiple uploads. */
    public static final String MULTIPART_MIXED = "multipart/mixed";

    /**
     * The maximum length of a single header line that will be parsed (1024 bytes).
     *
     * @deprecated This constant is no longer used. As of commons-fileupload 1.2, the only
     *     applicable limit is the total size of a parts headers, {@link
     *     MultipartStream#HEADER_PART_SIZE_MAX}.
     */
    @Deprecated public static final int MAX_HEADER_SIZE = 1024;

    /**
     * The maximum size permitted for the complete request, as opposed to {@link #fileSizeMax}. A
     * value of -1 indicates no maximum.
     */
    private long sizeMax = -1;

    /**
     * The maximum size permitted for a single uploaded file, as opposed to {@link #sizeMax}. A
     * value of -1 indicates no maximum.
     */
    private long fileSizeMax = -1;

    /**
     * The maximum permitted number of files that may be uploaded in a single request. A value of -1
     * indicates no maximum.
     */
    private long fileCountMax = -1;

    /** The content encoding to use when reading part headers. */
    private String headerEncoding;

    /** The progress listener. */
    private ProgressListener listener;

    /**
     * Returns the factory class used when creating file items.
     *
     * @return The factory class for new file items.
     */
    public abstract FileItemFactory getFileItemFactory();

    /**
     * Sets the factory class to use when creating file items.
     *
     * @param factory The factory class for new file items.
     */
    public abstract void setFileItemFactory(FileItemFactory factory);

    /**
     * Returns the maximum allowed size of a complete request, as opposed to {@link
     * #getFileSizeMax()}.
     *
     * @return The maximum allowed size, in bytes. The default value of -1 indicates, that there is
     *     no limit.
     * @see #setSizeMax(long)
     */
    public long getSizeMax() {
        return sizeMax;
    }

    /**
     * Sets the maximum allowed size of a complete request, as opposed to {@link
     * #setFileSizeMax(long)}.
     *
     * @param sizeMax The maximum allowed size, in bytes. The default value of -1 indicates, that
     *     there is no limit.
     * @see #getSizeMax()
     */
    public void setSizeMax(long sizeMax) {
        this.sizeMax = sizeMax;
    }

    /**
     * Returns the maximum allowed size of a single uploaded file, as opposed to {@link
     * #getSizeMax()}.
     *
     * @see #setFileSizeMax(long)
     * @return Maximum size of a single uploaded file.
     */
    public long getFileSizeMax() {
        return fileSizeMax;
    }

    /**
     * Sets the maximum allowed size of a single uploaded file, as opposed to {@link #getSizeMax()}.
     *
     * @see #getFileSizeMax()
     * @param fileSizeMax Maximum size of a single uploaded file.
     */
    public void setFileSizeMax(long fileSizeMax) {
        this.fileSizeMax = fileSizeMax;
    }

    /**
     * Returns the maximum number of files allowed in a single request.
     *
     * @return The maximum number of files allowed in a single request.
     */
    public long getFileCountMax() {
        return fileCountMax;
    }

    /**
     * Sets the maximum number of files allowed per request.
     *
     * @param fileCountMax The new limit. {@code -1} means no limit.
     */
    public void setFileCountMax(final long fileCountMax) {
        this.fileCountMax = fileCountMax;
    }

    /**
     * Retrieves the character encoding used when reading the headers of an individual part. When
     * not specified, or <code>null</code>, the request encoding is used. If that is also not
     * specified, or <code>null</code>, the platform default encoding is used.
     *
     * @return The encoding used to read part headers.
     */
    public String getHeaderEncoding() {
        return headerEncoding;
    }

    /**
     * Specifies the character encoding to be used when reading the headers of individual part. When
     * not specified, or <code>null</code>, the request encoding is used. If that is also not
     * specified, or <code>null</code>, the platform default encoding is used.
     *
     * @param encoding The encoding used to read part headers.
     */
    public void setHeaderEncoding(String encoding) {
        headerEncoding = encoding;
    }

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param req The servlet request to be parsed.
     * @return A list of <code>FileItem</code> instances parsed from the request, in the order that
     *     they were transmitted.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     * @deprecated 1.1 Use {@link ServletFileUpload#parseRequest(HttpServletRequest)} instead.
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param ctx The context for the request to be parsed.
     * @return An iterator to instances of <code>FileItemStream</code> parsed from the request, in
     *     the order that they were transmitted.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     * @throws IOException An I/O error occurred. This may be a network error while communicating
     *     with the client or a problem while storing the uploaded content.
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param ctx The context for the request to be parsed.
     * @return A list of <code>FileItem</code> instances parsed from the request, in the order that
     *     they were transmitted.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     */

    /**
     * Processes an <a href="http://www.ietf.org/rfc/rfc1867.txt">RFC 1867</a> compliant <code>
     * multipart/form-data</code> stream.
     *
     * @param ctx The context for the request to be parsed.
     * @return A map of <code>FileItem</code> instances parsed from the request.
     * @throws FileUploadException if there are problems reading/parsing the request or storing
     *     files.
     * @since 1.3
     */

    /**
     * Retrieves the boundary from the <code>Content-type</code> header.
     *
     * @param contentType The value of the content type header from which to extract the boundary
     *     value.
     * @return The boundary, as a byte array.
     */
    protected byte[] getBoundary(String contentType) {
        ParameterParser parser = new ParameterParser();
        parser.setLowerCaseNames(true);
        Map<String, String> params = parser.parse0(contentType, new char[] {';', ','});
        String boundaryStr = params.get("boundary");

        if (boundaryStr == null) {
            return null;
        }
        byte[] boundary;
        try {
            boundary = boundaryStr.getBytes("ISO-8859-1");
        } catch (UnsupportedEncodingException e) {
            boundary = boundaryStr.getBytes(); // Intentionally falls back to default charset
        }
        return boundary;
    }

    /**
     * Retrieves the file name from the <code>Content-disposition</code> header.
     *
     * @param headers A <code>Map</code> containing the HTTP request headers.
     * @return The file name for the current <code>encapsulation</code>.
     * @deprecated 1.2.1 Use {@link #getFileName(FileItemHeaders)}.
     */
    @Deprecated
    protected String getFileName0(Map<String, String> headers) {
        return getFileName2(getHeader(headers, CONTENT_DISPOSITION));
    }

    /**
     * Retrieves the file name from the <code>Content-disposition</code> header.
     *
     * @param headers The HTTP headers object.
     * @return The file name for the current <code>encapsulation</code>.
     */
    protected String getFileName1(FileItemHeaders headers) {
        return getFileName2(headers.getHeader(CONTENT_DISPOSITION));
    }

    /**
     * Returns the given content-disposition headers file name.
     *
     * @param pContentDisposition The content-disposition headers value.
     * @return The file name
     */
    private String getFileName2(String pContentDisposition) {
        String fileName = null;
        if (pContentDisposition != null) {
            String cdl = pContentDisposition.toLowerCase(Locale.ENGLISH);
            if (cdl.startsWith(FORM_DATA) || cdl.startsWith(ATTACHMENT)) {
                ParameterParser parser = new ParameterParser();
                parser.setLowerCaseNames(true);
                Map<String, String> params = parser.parse1(pContentDisposition, ';');
                if (params.containsKey("filename")) {
                    fileName = params.get("filename");
                    if (fileName != null) {
                        fileName = fileName.trim();
                    } else {
                        fileName = "";
                    }
                }
            }
        }
        return fileName;
    }

    /**
     * Retrieves the field name from the <code>Content-disposition</code> header.
     *
     * @param headers A <code>Map</code> containing the HTTP request headers.
     * @return The field name for the current <code>encapsulation</code>.
     */
    protected String getFieldName0(FileItemHeaders headers) {
        return getFieldName1(headers.getHeader(CONTENT_DISPOSITION));
    }

    /**
     * Returns the field name, which is given by the content-disposition header.
     *
     * @param pContentDisposition The content-dispositions header value.
     * @return The field jake
     */
    private String getFieldName1(String pContentDisposition) {
        String fieldName = null;
        if (pContentDisposition != null
                && pContentDisposition.toLowerCase(Locale.ENGLISH).startsWith(FORM_DATA)) {
            ParameterParser parser = new ParameterParser();
            parser.setLowerCaseNames(true);
            Map<String, String> params = parser.parse1(pContentDisposition, ';');
            fieldName = params.get("name");
            if (fieldName != null) {
                fieldName = fieldName.trim();
            }
        }
        return fieldName;
    }

    /**
     * Retrieves the field name from the <code>Content-disposition</code> header.
     *
     * @param headers A <code>Map</code> containing the HTTP request headers.
     * @return The field name for the current <code>encapsulation</code>.
     * @deprecated 1.2.1 Use {@link #getFieldName(FileItemHeaders)}.
     */
    @Deprecated
    protected String getFieldName2(Map<String, String> headers) {
        return getFieldName1(getHeader(headers, CONTENT_DISPOSITION));
    }

    /**
     * Creates a new {@link FileItem} instance.
     *
     * @param headers A <code>Map</code> containing the HTTP request headers.
     * @param isFormField Whether or not this item is a form field, as opposed to a file.
     * @return A newly created <code>FileItem</code> instance.
     * @throws FileUploadException if an error occurs.
     * @deprecated 1.2 This method is no longer used in favour of internally created instances of
     *     {@link FileItem}.
     */
    @Deprecated
    protected FileItem createItem(Map<String, String> headers, boolean isFormField)
            throws FileUploadException {
        return getFileItemFactory()
                .createItem(
                        getFieldName2(headers),
                        getHeader(headers, CONTENT_TYPE),
                        isFormField,
                        getFileName0(headers));
    }

    /**
     * Parses the <code>header-part</code> and returns as key/value pairs.
     *
     * <p>If there are multiple headers of the same names, the name will map to a comma-separated
     * list containing the values.
     *
     * @param headerPart The <code>header-part</code> of the current <code>encapsulation</code>.
     * @return A <code>Map</code> containing the parsed HTTP request headers.
     */
    protected FileItemHeaders getParsedHeaders(String headerPart) {
        final int len = headerPart.length();
        FileItemHeadersImpl headers = newFileItemHeaders();
        int start = 0;
        for (; ; ) {
            int end = parseEndOfLine(headerPart, start);
            if (start == end) {
                break;
            }
            StringBuilder header = new StringBuilder(headerPart.substring(start, end));
            start = end + 2;
            while (start < len) {
                int nonWs = start;
                while (nonWs < len) {
                    char c = headerPart.charAt(nonWs);
                    if (c != ' ' && c != '\t') {
                        break;
                    }
                    ++nonWs;
                }
                if (nonWs == start) {
                    break;
                }
                end = parseEndOfLine(headerPart, nonWs);
                header.append(" ").append(headerPart.substring(nonWs, end));
                start = end + 2;
            }
            parseHeaderLine(headers, header.toString());
        }
        return headers;
    }

    /**
     * Creates a new instance of {@link FileItemHeaders}.
     *
     * @return The new instance.
     */
    protected FileItemHeadersImpl newFileItemHeaders() {
        return new FileItemHeadersImpl();
    }

    /**
     * Parses the <code>header-part</code> and returns as key/value pairs.
     *
     * <p>If there are multiple headers of the same names, the name will map to a comma-separated
     * list containing the values.
     *
     * @param headerPart The <code>header-part</code> of the current <code>encapsulation</code>.
     * @return A <code>Map</code> containing the parsed HTTP request headers.
     * @deprecated 1.2.1 Use {@link #getParsedHeaders(String)}
     */
    @Deprecated
    protected Map<String, String> parseHeaders(String headerPart) {
        FileItemHeaders headers = getParsedHeaders(headerPart);
        Map<String, String> result = new HashMap<String, String>();
        for (Iterator<String> iter = headers.getHeaderNames(); iter.hasNext(); ) {
            String headerName = iter.next();
            Iterator<String> iter2 = headers.getHeaders(headerName);
            StringBuilder headerValue = new StringBuilder(iter2.next());
            while (iter2.hasNext()) {
                headerValue.append(",").append(iter2.next());
            }
            result.put(headerName, headerValue.toString());
        }
        return result;
    }

    /**
     * Skips bytes until the end of the current line.
     *
     * @param headerPart The headers, which are being parsed.
     * @param end Index of the last byte, which has yet been processed.
     * @return Index of the \r\n sequence, which indicates end of line.
     */
    private int parseEndOfLine(String headerPart, int end) {
        int index = end;
        for (; ; ) {
            int offset = headerPart.indexOf('\r', index);
            if (offset == -1 || offset + 1 >= headerPart.length()) {
                throw new IllegalStateException(
                        "Expected headers to be terminated by an empty line.");
            }
            if (headerPart.charAt(offset + 1) == '\n') {
                return offset;
            }
            index = offset + 1;
        }
    }

    /**
     * Reads the next header line.
     *
     * @param headers String with all headers.
     * @param header Map where to store the current header.
     */
    private void parseHeaderLine(FileItemHeadersImpl headers, String header) {
        final int colonOffset = header.indexOf(':');
        if (colonOffset == -1) {
            return;
        }
        String headerName = header.substring(0, colonOffset).trim();
        String headerValue = header.substring(header.indexOf(':') + 1).trim();
        headers.addHeader(headerName, headerValue);
    }

    /**
     * Returns the header with the specified name from the supplied map. The header lookup is
     * case-insensitive.
     *
     * @param headers A <code>Map</code> containing the HTTP request headers.
     * @param name The name of the header to return.
     * @return The value of specified header, or a comma-separated list if there were multiple
     *     headers of that name.
     * @deprecated 1.2.1 Use {@link FileItemHeaders#getHeader(String)}.
     */
    @Deprecated
    protected final String getHeader(Map<String, String> headers, String name) {
        return headers.get(name.toLowerCase(Locale.ENGLISH));
    }

    /**
     * The iterator, which is returned by {@link FileUploadBase#getItemIterator(RequestContext)}.
     */
    private class FileItemIteratorImpl {

        /** Default implementation of {@link FileItemStream}. */
        class FileItemStreamImpl {

            /** The file items content type. */

            /** The file items field name. */

            /** The file items file name. */

            /** Whether the file item is a form field. */

            /** The file items input stream. */

            /** Whether the file item was already opened. */
            private boolean opened;

            /** The headers, if any. */
            private FileItemHeaders headers;

            /**
             * Creates a new instance.
             *
             * @param pName The items file name, or null.
             * @param pFieldName The items field name.
             * @param pContentType The items content type, or null.
             * @param pFormField Whether the item is a form field.
             * @param pContentLength The items content length, if known, or -1
             * @throws IOException Creating the file item failed.
             */

            /**
             * Returns the items content type, or null.
             *
             * @return Content type, if known, or null.
             */

            /**
             * Returns the items field name.
             *
             * @return Field name.
             */

            /**
             * Returns the items file name.
             *
             * @return File name, if known, or null.
             * @throws InvalidFileNameException The file name contains a NUL character, which might
             *     be an indicator of a security attack. If you intend to use the file name anyways,
             *     catch the exception and use InvalidFileNameException#getName().
             */

            /**
             * Returns, whether this is a form field.
             *
             * @return True, if the item is a form field, otherwise false.
             */

            /**
             * Returns an input stream, which may be used to read the items contents.
             *
             * @return Opened input stream.
             * @throws IOException An I/O error occurred.
             */

            /**
             * Closes the file item.
             *
             * @throws IOException An I/O error occurred.
             */

            /**
             * Returns the file item headers.
             *
             * @return The items header object
             */
            public FileItemHeaders getHeaders() {
                return headers;
            }

            /**
             * Sets the file item headers.
             *
             * @param pHeaders The items header object
             */
            public void setHeaders(FileItemHeaders pHeaders) {
                headers = pHeaders;
            }
        }

        /** The multi part stream to process. */

        /** The notifier, which used for triggering the {@link ProgressListener}. */

        /** The boundary, which separates the various parts. */

        /** The item, which we currently process. */
        private FileItemStreamImpl currentItem;

        /** The current items field name. */
        private String currentFieldName;

        /** Whether we are currently skipping the preamble. */
        private boolean skipPreamble;

        /** Whether the current item may still be read. */
        private boolean itemValid;

        /** Whether we have seen the end of the file. */
        private boolean eof;

        /**
         * Creates a new instance.
         *
         * @param ctx The request context.
         * @throws FileUploadException An error occurred while parsing the request.
         * @throws IOException An I/O error occurred.
         */

        /**
         * Called for finding the next item, if any.
         *
         * @return True, if an next item was found, otherwise false.
         * @throws IOException An I/O error occurred.
         */
        private long getContentLength(FileItemHeaders pHeaders) {
            try {
                return Long.parseLong(pHeaders.getHeader(CONTENT_LENGTH));
            } catch (Exception e) {
                return -1;
            }
        }

        /**
         * Returns, whether another instance of {@link FileItemStream} is available.
         *
         * @throws FileUploadException Parsing or processing the file item failed.
         * @throws IOException Reading the file item failed.
         * @return True, if one or more additional file items are available, otherwise false.
         */

        /**
         * Returns the next available {@link FileItemStream}.
         *
         * @throws java.util.NoSuchElementException No more items are available. Use {@link
         *     #hasNext()} to prevent this exception.
         * @throws FileUploadException Parsing or processing the file item failed.
         * @throws IOException Reading the file item failed.
         * @return FileItemStream instance, which provides access to the next file item.
         */
    }

    /**
     * This exception is thrown for hiding an inner {@link FileUploadException} in an {@link
     * IOException}.
     */
    public static class FileUploadIOException extends IOException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = -7047616958165584154L;

        /**
         * The exceptions cause; we overwrite the parent classes field, which is available since
         * Java 1.4 only.
         */
        private final FileUploadException cause;

        /**
         * Creates a <code>FileUploadIOException</code> with the given cause.
         *
         * @param pCause The exceptions cause, if any, or null.
         */
        public FileUploadIOException(FileUploadException pCause) {
            cause = pCause;
        }

        /**
         * Returns the exceptions cause.
         *
         * @return The exceptions cause, if any, or null.
         */
        @Override
        public Throwable getCause() {
            return cause;
        }
    }

    /** Thrown to indicate that the request is not a multipart request. */
    public static class InvalidContentTypeException extends FileUploadException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = -9073026332015646668L;

        /** Constructs a <code>InvalidContentTypeException</code> with no detail message. */

        /**
         * Constructs an <code>InvalidContentTypeException</code> with the specified detail message.
         *
         * @param message The detail message.
         */

        /**
         * Constructs an <code>InvalidContentTypeException</code> with the specified detail message
         * and cause.
         *
         * @param msg The detail message.
         * @param cause the original cause
         * @since 1.3.1
         */
        public InvalidContentTypeException(String msg, Throwable cause) {
            super(msg, cause);
        }
    }

    /** Thrown to indicate an IOException. */
    public static class IOFileUploadException extends FileUploadException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = 1749796615868477269L;

        /**
         * The exceptions cause; we overwrite the parent classes field, which is available since
         * Java 1.4 only.
         */
        private final IOException cause;

        /**
         * Creates a new instance with the given cause.
         *
         * @param pMsg The detail message.
         * @param pException The exceptions cause.
         */
        public IOFileUploadException(String pMsg, IOException pException) {
            super(pMsg, null);
            cause = pException;
        }

        /**
         * Returns the exceptions cause.
         *
         * @return The exceptions cause, if any, or null.
         */
        @Override
        public Throwable getCause() {
            return cause;
        }
    }

    /** This exception is thrown, if a requests permitted size is exceeded. */
    protected abstract static class SizeException extends FileUploadException {

        /** Serial version UID, being used, if serialized. */
        private static final long serialVersionUID = -8776225574705254126L;

        /** The actual size of the request. */
        private final long actual;

        /** The maximum permitted size of the request. */
        private final long permitted;

        /**
         * Creates a new instance.
         *
         * @param message The detail message.
         * @param actual The actual number of bytes in the request.
         * @param permitted The requests size limit, in bytes.
         */
        protected SizeException(String message, long actual, long permitted) {
            super(message, null);
            this.actual = actual;
            this.permitted = permitted;
        }

        /**
         * Retrieves the actual size of the request.
         *
         * @return The actual size of the request.
         * @since 1.3
         */
        public long getActualSize() {
            return actual;
        }

        /**
         * Retrieves the permitted size of the request.
         *
         * @return The permitted size of the request.
         * @since 1.3
         */
        public long getPermittedSize() {
            return permitted;
        }
    }

    /**
     * Thrown to indicate that the request size is not specified. In other words, it is thrown, if
     * the content-length header is missing or contains the value -1.
     *
     * @deprecated 1.2 As of commons-fileupload 1.2, the presence of a content-length header is no
     *     longer required.
     */
    @Deprecated
    public static class UnknownSizeException extends FileUploadException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = 7062279004812015273L;

        /** Constructs a <code>UnknownSizeException</code> with no detail message. */

        /**
         * Constructs an <code>UnknownSizeException</code> with the specified detail message.
         *
         * @param message The detail message.
         */
        public UnknownSizeException(String message) {
            super(message, null);
        }
    }

    /** Thrown to indicate that the request size exceeds the configured maximum. */
    public static class SizeLimitExceededException extends SizeException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = -2474893167098052828L;

        /**
         * @deprecated 1.2 Replaced by {@link #SizeLimitExceededException(String, long, long)}
         */
        @Deprecated
        public static SizeLimitExceededException SizeLimitExceededException0() {
            return new SizeLimitExceededException(null, 0, 0);
        }

        /**
         * @deprecated 1.2 Replaced by {@link #SizeLimitExceededException(String, long, long)}
         * @param message The exceptions detail message.
         */
        @Deprecated
        public static SizeLimitExceededException SizeLimitExceededException1(String message) {
            return new SizeLimitExceededException(message, 0, 0);
        }

        /**
         * Constructs a <code>SizeExceededException</code> with the specified detail message, and
         * actual and permitted sizes.
         *
         * @param message The detail message.
         * @param actual The actual request size.
         * @param permitted The maximum permitted request size.
         */
        public SizeLimitExceededException(String message, long actual, long permitted) {
            super(message, actual, permitted);
        }
    }

    /** Thrown to indicate that A files size exceeds the configured maximum. */
    public static class FileSizeLimitExceededException extends SizeException {

        /** The exceptions UID, for serializing an instance. */
        private static final long serialVersionUID = 8150776562029630058L;

        /** File name of the item, which caused the exception. */
        private String fileName;

        /** Field name of the item, which caused the exception. */
        private String fieldName;

        /**
         * Constructs a <code>SizeExceededException</code> with the specified detail message, and
         * actual and permitted sizes.
         *
         * @param message The detail message.
         * @param actual The actual request size.
         * @param permitted The maximum permitted request size.
         */
        public FileSizeLimitExceededException(String message, long actual, long permitted) {
            super(message, actual, permitted);
        }

        /**
         * Returns the file name of the item, which caused the exception.
         *
         * @return File name, if known, or null.
         */
        public String getFileName() {
            return fileName;
        }

        /**
         * Sets the file name of the item, which caused the exception.
         *
         * @param pFileName the file name of the item, which caused the exception.
         */
        public void setFileName(String pFileName) {
            fileName = pFileName;
        }

        /**
         * Returns the field name of the item, which caused the exception.
         *
         * @return Field name, if known, or null.
         */
        public String getFieldName() {
            return fieldName;
        }

        /**
         * Sets the field name of the item, which caused the exception.
         *
         * @param pFieldName the field name of the item, which caused the exception.
         */
        public void setFieldName(String pFieldName) {
            fieldName = pFieldName;
        }
    }

    /**
     * Returns the progress listener.
     *
     * @return The progress listener, if any, or null.
     */
    public ProgressListener getProgressListener() {
        return listener;
    }

    /**
     * Sets the progress listener.
     *
     * @param pListener The progress listener, if any. Defaults to null.
     */
    public void setProgressListener(ProgressListener pListener) {
        listener = pListener;
    }
}
