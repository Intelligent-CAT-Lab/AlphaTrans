
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

package org.apache.commons.fileupload.disk;

import static java.lang.String.format;

import org.apache.commons.fileupload.FileItemHeaders;
import org.apache.commons.fileupload.ParameterParser;
import org.apache.commons.fileupload.util.Streams;

import java.io.File;
import java.util.Map;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * The default implementation of the {@link org.apache.commons.fileupload.FileItem FileItem}
 * interface.
 *
 * <p>After retrieving an instance of this class from a {@link DiskFileItemFactory} instance (see
 * {@link org.apache.commons.fileupload.servlet.ServletFileUpload
 * #parseRequest(javax.servlet.http.HttpServletRequest)}), you may either request all contents of
 * file at once using {@link #get()} or request an {@link java.io.InputStream InputStream} with
 * {@link #getInputStream()} and process the file without attempting to load it into memory, which
 * may come handy with large files.
 *
 * <p>Temporary files, which are created for file items, should be deleted later on. The best way to
 * do this is using a {@link org.apache.commons.io.FileCleaningTracker}, which you can set on the
 * {@link DiskFileItemFactory}. However, if you do use such a tracker, then you must consider the
 * following: Temporary files are automatically deleted as soon as they are no longer needed. (More
 * precisely, when the corresponding instance of {@link java.io.File} is garbage collected.) This is
 * done by the so-called reaper thread, which is started and stopped automatically by the {@link
 * org.apache.commons.io.FileCleaningTracker} when there are files to be tracked. It might make
 * sense to terminate that thread, for example, if your web application ends. See the section on
 * "Resource cleanup" in the users guide of commons-fileupload.
 *
 * @since FileUpload 1.1
 */
public class DiskFileItem {

    /**
     * Default content charset to be used when no explicit charset parameter is provided by the
     * sender. Media subtypes of the "text" type are defined to have a default charset value of
     * "ISO-8859-1" when received via HTTP.
     */
    public static final String DEFAULT_CHARSET = "ISO-8859-1";

    /** UID used in unique file name generation. */
    private static final String UID = UUID.randomUUID().toString().replace('-', '_');

    /** Counter used in unique identifier generation. */
    private static final AtomicInteger COUNTER = new AtomicInteger(0);

    /** The name of the form field as provided by the browser. */
    private String fieldName;

    /** The content type passed by the browser, or <code>null</code> if not defined. */
    private final String contentType;

    /** Whether or not this item is a simple form field. */
    private boolean isFormField;

    /** The original filename in the user's filesystem. */
    private final String fileName;

    /**
     * The size of the item, in bytes. This is used to cache the size when a file item is moved from
     * its original location.
     */
    private long size = -1;

    /** The threshold above which uploads will be stored on disk. */
    private final int sizeThreshold;

    /** The directory in which uploaded files will be stored, if stored on disk. */
    private final File repository;

    /** Cached contents of the file. */
    private byte[] cachedContent;

    /** Output stream for this item. */

    /** The temporary file to use. */
    private transient File tempFile;

    /** The file items headers. */
    private FileItemHeaders headers;

    /**
     * Default content charset to be used when no explicit charset parameter is provided by the
     * sender.
     */
    private String defaultCharset = DEFAULT_CHARSET;

    /**
     * Constructs a new <code>DiskFileItem</code> instance.
     *
     * @param fieldName The name of the form field.
     * @param contentType The content type passed by the browser or <code>null</code> if not
     *     specified.
     * @param isFormField Whether or not this item is a plain form field, as opposed to a file
     *     upload.
     * @param fileName The original filename in the user's filesystem, or <code>null</code> if not
     *     specified.
     * @param sizeThreshold The threshold, in bytes, below which items will be retained in memory
     *     and above which they will be stored as a file.
     * @param repository The data repository, which is the directory in which files will be created,
     *     should the item size exceed the threshold.
     */
    public DiskFileItem(
            String fieldName,
            String contentType,
            boolean isFormField,
            String fileName,
            int sizeThreshold,
            File repository) {
        this.fieldName = fieldName;
        this.contentType = contentType;
        this.isFormField = isFormField;
        this.fileName = fileName;
        this.sizeThreshold = sizeThreshold;
        this.repository = repository;
    }

    /**
     * Returns an {@link java.io.InputStream InputStream} that can be used to retrieve the contents
     * of the file.
     *
     * @return An {@link java.io.InputStream InputStream} that can be used to retrieve the contents
     *     of the file.
     * @throws IOException if an error occurs.
     */

    /**
     * Returns the content type passed by the agent or <code>null</code> if not defined.
     *
     * @return The content type passed by the agent or <code>null</code> if not defined.
     */
    public String getContentType() {
        return contentType;
    }

    /**
     * Returns the content charset passed by the agent or <code>null</code> if not defined.
     *
     * @return The content charset passed by the agent or <code>null</code> if not defined.
     */
    public String getCharSet() {
        ParameterParser parser = new ParameterParser();
        parser.setLowerCaseNames(true);
        Map<String, String> params = parser.parse1(getContentType(), ';');
        return params.get("charset");
    }

    /**
     * Returns the original filename in the client's filesystem.
     *
     * @return The original filename in the client's filesystem.
     * @throws org.apache.commons.fileupload.InvalidFileNameException The file name contains a NUL
     *     character, which might be an indicator of a security attack. If you intend to use the
     *     file name anyways, catch the exception and use {@link
     *     org.apache.commons.fileupload.InvalidFileNameException#getName()}.
     */
    public String getName() {
        return Streams.checkFileName(fileName);
    }

    /**
     * Provides a hint as to whether or not the file contents will be read from memory.
     *
     * @return <code>true</code> if the file contents will be read from memory; <code>false</code>
     *     otherwise.
     */

    /**
     * Returns the size of the file.
     *
     * @return The size of the file, in bytes.
     */

    /**
     * Returns the contents of the file as an array of bytes. If the contents of the file were not
     * yet cached in memory, they will be loaded from the disk storage and cached.
     *
     * @return The contents of the file as an array of bytes or {@code null} if the data cannot be
     *     read
     */

    /**
     * Returns the contents of the file as a String, using the specified encoding. This method uses
     * {@link #get()} to retrieve the contents of the file.
     *
     * @param charset The charset to use.
     * @return The contents of the file, as a string.
     * @throws UnsupportedEncodingException if the requested character encoding is not available.
     */

    /**
     * Returns the contents of the file as a String, using the default character encoding. This
     * method uses {@link #get()} to retrieve the contents of the file.
     *
     * <p><b>TODO</b> Consider making this method throw UnsupportedEncodingException.
     *
     * @return The contents of the file, as a string.
     */

    /**
     * A convenience method to write an uploaded item to disk. The client code is not concerned with
     * whether or not the item is stored in memory, or on disk in a temporary location. They just
     * want to write the uploaded item to a file.
     *
     * <p>This implementation first attempts to rename the uploaded item to the specified
     * destination file, if the item was originally written to disk. Otherwise, the data will be
     * copied to the specified file.
     *
     * <p>This method is only guaranteed to work <em>once</em>, the first time it is invoked for a
     * particular item. This is because, in the event that the method renames a temporary file, that
     * file will no longer be available to copy or rename again at a later time.
     *
     * @param file The <code>File</code> into which the uploaded item should be stored.
     * @throws Exception if an error occurs.
     */

    /**
     * Deletes the underlying storage for a file item, including deleting any associated temporary
     * disk file. Although this storage will be deleted automatically when the <code>FileItem</code>
     * instance is garbage collected, this method can be used to ensure that this is done at an
     * earlier time, thus preserving system resources.
     */

    /**
     * Returns the name of the field in the multipart form corresponding to this file item.
     *
     * @return The name of the form field.
     * @see #setFieldName(java.lang.String)
     */
    public String getFieldName() {
        return fieldName;
    }

    /**
     * Sets the field name used to reference this file item.
     *
     * @param fieldName The name of the form field.
     * @see #getFieldName()
     */
    public void setFieldName(String fieldName) {
        this.fieldName = fieldName;
    }

    /**
     * Determines whether or not a <code>FileItem</code> instance represents a simple form field.
     *
     * @return <code>true</code> if the instance represents a simple form field; <code>false</code>
     *     if it represents an uploaded file.
     * @see #setFormField(boolean)
     */
    public boolean isFormField() {
        return isFormField;
    }

    /**
     * Specifies whether or not a <code>FileItem</code> instance represents a simple form field.
     *
     * @param state <code>true</code> if the instance represents a simple form field; <code>false
     *     </code> if it represents an uploaded file.
     * @see #isFormField()
     */
    public void setFormField(boolean state) {
        isFormField = state;
    }

    /**
     * Returns an {@link java.io.OutputStream OutputStream} that can be used for storing the
     * contents of the file.
     *
     * @return An {@link java.io.OutputStream OutputStream} that can be used for storing the
     *     contents of the file.
     * @throws IOException if an error occurs.
     */

    /**
     * Returns the {@link java.io.File} object for the <code>FileItem</code>'s data's temporary
     * location on the disk. Note that for <code>FileItem</code>s that have their data stored in
     * memory, this method will return <code>null</code>. When handling large files, you can use
     * {@link java.io.File#renameTo(java.io.File)} to move the file to new location without copying
     * the data, if the source and destination locations reside within the same logical volume.
     *
     * @return The data file, or <code>null</code> if the data is stored in memory.
     */

    /** Removes the file contents from the temporary storage. */

    /**
     * Creates and returns a {@link java.io.File File} representing a uniquely named temporary file
     * in the configured repository path. The lifetime of the file is tied to the lifetime of the
     * <code>FileItem</code> instance; the file will be deleted when the instance is garbage
     * collected.
     *
     * <p><b>Note: Subclasses that override this method must ensure that they return the same File
     * each time.</b>
     *
     * @return The {@link java.io.File File} to be used for temporary storage.
     */
    protected File getTempFile() {
        if (tempFile == null) {
            File tempDir = repository;
            if (tempDir == null) {
                tempDir = new File(System.getProperty("java.io.tmpdir"));
            }

            String tempFileName = format("upload_%s_%s.tmp", UID, getUniqueId());

            tempFile = new File(tempDir, tempFileName);
        }
        return tempFile;
    }

    /**
     * Returns an identifier that is unique within the class loader used to load this class, but
     * does not have random-like appearance.
     *
     * @return A String with the non-random looking instance identifier.
     */
    private static String getUniqueId() {
        final int limit = 100000000;
        int current = COUNTER.getAndIncrement();
        String id = Integer.toString(current);

        if (current < limit) {
            id = ("00000000" + id).substring(id.length());
        }
        return id;
    }

    /**
     * Returns a string representation of this object.
     *
     * @return a string representation of this object.
     */

    /**
     * Returns the file item headers.
     *
     * @return The file items headers.
     */
    public FileItemHeaders getHeaders() {
        return headers;
    }

    /**
     * Sets the file item headers.
     *
     * @param pHeaders The file items headers.
     */
    public void setHeaders(FileItemHeaders pHeaders) {
        headers = pHeaders;
    }

    /**
     * Returns the default charset for use when no explicit charset parameter is provided by the
     * sender.
     *
     * @return the default charset
     */
    public String getDefaultCharset() {
        return defaultCharset;
    }

    /**
     * Sets the default charset for use when no explicit charset parameter is provided by the
     * sender.
     *
     * @param charset the default charset
     */
    public void setDefaultCharset(String charset) {
        defaultCharset = charset;
    }
}
