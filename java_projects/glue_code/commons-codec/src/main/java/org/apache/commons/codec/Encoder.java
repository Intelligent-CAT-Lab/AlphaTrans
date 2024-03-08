package org.apache.commons.codec;


public interface Encoder {
  Object encode(Object source) throws EncoderException;
}
