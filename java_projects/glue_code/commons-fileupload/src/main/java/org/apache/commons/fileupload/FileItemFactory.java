package org.apache.commons.fileupload;


public interface FileItemFactory {
  FileItem createItem(String fieldName, String contentType, boolean isFormField, String fileName);
}
